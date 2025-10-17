# AI-moduler för Neuroljus Neurohus
# Empati-motor för rekommendation, moderering och analys

import re
import json
import logging
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy
from textblob import TextBlob
import openai
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

# Konfiguration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ladda svensk språkmodell för NLP
try:
    nlp = spacy.load("sv_core_news_sm")
except OSError:
    logger.warning("Svensk språkmodell inte tillgänglig, använder engelsk som fallback")
    nlp = spacy.load("en_core_web_sm")

# Ladda sentimentanalys-modell
sentiment_analyzer = pipeline("sentiment-analysis", 
                            model="KBLab/sentence-bert-swedish-cased",
                            tokenizer="KBLab/sentence-bert-swedish-cased")

@dataclass
class AnvändarProfil:
    """Användarprofil för AI-rekommendationer"""
    användare_id: str
    roll: str  # familj, assistent, kommun, forskare
    kommun: str
    preferenser: Dict[str, Any]
    tidigare_interaktioner: List[Dict[str, Any]]
    diagnoser: List[str]
    åldersgrupp: str
    behov: List[str]

@dataclass
class VerksamhetsProfil:
    """Verksamhetsprofil för matchning"""
    verksamhet_id: str
    typ: str
    kommun: str
    diagnoser: List[str]
    tjänster: List[str]
    åldersgrupp: str
    kapacitet: int
    recensioner: List[Dict[str, Any]]
    kvalitetsindikatorer: Dict[str, float]

class EmpatiRekommendation:
    """AI-modul för empatiska rekommendationer"""
    
    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            max_features=1000,
            stop_words='english',  # Byt till svenska när tillgängligt
            ngram_range=(1, 2)
        )
        
    def beräkna_matchning(self, användar_profil: AnvändarProfil, 
                         verksamhets_profil: VerksamhetsProfil) -> float:
        """
        Beräknar empatisk matchning mellan användare och verksamhet
        Returnerar poäng 0-1 där 1 är perfekt matchning
        """
        try:
            # Grundläggande matchning baserat på kriterier
            grundpoäng = self._beräkna_grundmatchning(användar_profil, verksamhets_profil)
            
            # Empatisk analys av recensioner
            empati_poäng = self._analysera_empati_i_recensioner(verksamhets_profil.recensioner)
            
            # Kommunspecifik anpassning
            kommun_poäng = self._beräkna_kommunmatchning(användar_profil.kommun, 
                                                        verksamhets_profil.kommun)
            
            # Viktad summa av alla faktorer
            total_poäng = (
                grundpoäng * 0.4 +
                empati_poäng * 0.4 +
                kommun_poäng * 0.2
            )
            
            return min(1.0, max(0.0, total_poäng))
            
        except Exception as e:
            logger.error(f"Fel vid beräkning av matchning: {e}")
            return 0.0
    
    def _beräkna_grundmatchning(self, användar: AnvändarProfil, 
                               verksamhet: VerksamhetsProfil) -> float:
        """Beräknar grundläggande matchning baserat på kriterier"""
        poäng = 0.0
        total_kriterier = 0
        
        # Diagnosmatchning
        if användar.diagnoser and verksamhet.diagnoser:
            gemensamma_diagnoser = set(användar.diagnoser) & set(verksamhet.diagnoser)
            diagnos_poäng = len(gemensamma_diagnoser) / len(set(användar.diagnoser))
            poäng += diagnos_poäng
            total_kriterier += 1
        
        # Åldersgruppsmatchning
        if användar.åldersgrupp == verksamhet.åldersgrupp:
            poäng += 1.0
            total_kriterier += 1
        
        # Behov vs tjänster
        if användar.behov and verksamhet.tjänster:
            matchade_tjänster = set(användar.behov) & set(verksamhet.tjänster)
            tjänst_poäng = len(matchade_tjänster) / len(set(användar.behov))
            poäng += tjänst_poäng
            total_kriterier += 1
        
        return poäng / total_kriterier if total_kriterier > 0 else 0.0
    
    def _analysera_empati_i_recensioner(self, recensioner: List[Dict[str, Any]]) -> float:
        """Analyserar empati i recensioner med NLP"""
        if not recensioner:
            return 0.5  # Neutral poäng om inga recensioner
        
        empati_nyckelord = [
            'empati', 'förståelse', 'trygg', 'respekt', 'varm', 'omsorg',
            'professionell', 'kompetent', 'stödjande', 'inkluderande',
            'individuell', 'personcentrerad', 'värdig', 'värdighet'
        ]
        
        empati_poäng = []
        
        for recension in recensioner:
            text = recension.get('innehåll', '').lower()
            
            # Räkna empati-nyckelord
            empati_träffar = sum(1 for ord in empati_nyckelord if ord in text)
            
            # Sentimentanalys
            try:
                sentiment = sentiment_analyzer(text)
                sentiment_poäng = sentiment[0]['score'] if sentiment[0]['label'] == 'POSITIVE' else 1 - sentiment[0]['score']
            except:
                sentiment_poäng = 0.5
            
            # Kombinera empati-nyckelord och sentiment
            kombinerad_poäng = (empati_träffar / len(empati_nyckelord) * 0.6 + 
                              sentiment_poäng * 0.4)
            empati_poäng.append(kombinerad_poäng)
        
        return np.mean(empati_poäng) if empati_poäng else 0.5
    
    def _beräkna_kommunmatchning(self, användar_kommun: str, 
                                verksamhet_kommun: str) -> float:
        """Beräknar matchning baserat på kommun"""
        if användar_kommun == verksamhet_kommun:
            return 1.0
        else:
            # Ge lägre poäng för annan kommun, men inte noll
            return 0.3
    
    def rekommendera_verksamheter(self, användar_profil: AnvändarProfil,
                                 alla_verksamheter: List[VerksamhetsProfil],
                                 antal: int = 5) -> List[Tuple[str, float]]:
        """Rekommenderar verksamheter baserat på användarprofil"""
        rekommendationer = []
        
        for verksamhet in alla_verksamheter:
            matchning = self.beräkna_matchning(användar_profil, verksamhet)
            rekommendationer.append((verksamhet.verksamhet_id, matchning))
        
        # Sortera efter matchning och returnera topp-rekommendationer
        rekommendationer.sort(key=lambda x: x[1], reverse=True)
        return rekommendationer[:antal]

class EmpatiModerering:
    """AI-modul för empatisk moderering av innehåll"""
    
    def __init__(self):
        self.negativa_nyckelord = [
            'hat', 'diskriminering', 'kränkande', 'nedvärderande',
            'förnedrande', 'hot', 'mobbning', 'trakasseri'
        ]
        
        self.empatiska_nyckelord = [
            'respekt', 'förståelse', 'empati', 'stöd', 'hjälp',
            'tack', 'uppskattning', 'värdefull', 'viktig'
        ]
    
    def moderera_text(self, text: str, användare_roll: str) -> Dict[str, Any]:
        """
        Modererar text med fokus på empati och respekt
        Returnerar modereringsresultat med rekommendationer
        """
        try:
            # Grundläggande säkerhetskontroll
            säkerhets_resultat = self._kontrollera_säkerhet(text)
            
            # Empatisk analys
            empati_resultat = self._analysera_empati(text)
            
            # Rollspecifik moderering
            roll_resultat = self._moderera_för_roll(text, användare_roll)
            
            # Kombinera resultat
            total_poäng = (
                säkerhets_resultat['poäng'] * 0.4 +
                empati_resultat['poäng'] * 0.4 +
                roll_resultat['poäng'] * 0.2
            )
            
            godkänd = total_poäng >= 0.7 and säkerhets_resultat['säker']
            
            return {
                'godkänd': godkänd,
                'total_poäng': total_poäng,
                'säkerhets_resultat': säkerhets_resultat,
                'empati_resultat': empati_resultat,
                'roll_resultat': roll_resultat,
                'rekommendationer': self._generera_rekommendationer(text, total_poäng),
                'modererad_text': self._förbättra_text(text) if not godkänd else text
            }
            
        except Exception as e:
            logger.error(f"Fel vid moderering: {e}")
            return {
                'godkänd': False,
                'total_poäng': 0.0,
                'fel': str(e)
            }
    
    def _kontrollera_säkerhet(self, text: str) -> Dict[str, Any]:
        """Kontrollerar säkerhet och innehåll som kan vara skadligt"""
        text_lower = text.lower()
        
        # Kontrollera negativa nyckelord
        negativa_träffar = [ord for ord in self.negativa_nyckelord if ord in text_lower]
        
        # Kontrollera personuppgifter (enkel regex)
        personuppgifter = re.findall(r'\b\d{4}-\d{2}-\d{2}\b|\b\d{10,12}\b', text)
        
        säker = len(negativa_träffar) == 0 and len(personuppgifter) == 0
        
        return {
            'säker': säker,
            'poäng': 1.0 if säker else 0.0,
            'negativa_träffar': negativa_träffar,
            'personuppgifter': personuppgifter
        }
    
    def _analysera_empati(self, text: str) -> Dict[str, Any]:
        """Analyserar empati och respekt i texten"""
        text_lower = text.lower()
        
        # Räkna empatiska nyckelord
        empatiska_träffar = [ord for ord in self.empatiska_nyckelord if ord in text_lower]
        
        # Sentimentanalys
        try:
            sentiment = sentiment_analyzer(text)
            sentiment_poäng = sentiment[0]['score'] if sentiment[0]['label'] == 'POSITIVE' else 1 - sentiment[0]['score']
        except:
            sentiment_poäng = 0.5
        
        # Beräkna empati-poäng
        empati_poäng = min(1.0, len(empatiska_träffar) / 5 + sentiment_poäng * 0.5)
        
        return {
            'poäng': empati_poäng,
            'empatiska_träffar': empatiska_träffar,
            'sentiment_poäng': sentiment_poäng
        }
    
    def _moderera_för_roll(self, text: str, roll: str) -> Dict[str, Any]:
        """Rollspecifik moderering"""
        if roll == 'familj':
            # Familjer bör undvika specifika medicinska termer utan kontext
            medicinska_termer = ['diagnos', 'behandling', 'terapi']
            text_lower = text.lower()
            medicinska_träffar = [term for term in medicinska_termer if term in text_lower]
            
            poäng = 1.0 if len(medicinska_träffar) == 0 else 0.7
            
        elif roll == 'assistent':
            # Assistenter bör använda professionellt språk
            professionella_termer = ['brukare', 'omsorg', 'stöd', 'assistans']
            text_lower = text.lower()
            professionella_träffar = [term for term in professionella_termer if term in text_lower]
            
            poäng = min(1.0, len(professionella_träffar) / 3 + 0.5)
            
        else:
            poäng = 0.8  # Standard för andra roller
        
        return {
            'poäng': poäng,
            'roll': roll
        }
    
    def _generera_rekommendationer(self, text: str, poäng: float) -> List[str]:
        """Genererar förbättringsrekommendationer"""
        rekommendationer = []
        
        if poäng < 0.5:
            rekommendationer.append("Överväg att omformulera texten med mer empatiskt språk")
            rekommendationer.append("Undvik negativa eller kränkande uttryck")
        
        if poäng < 0.7:
            rekommendationer.append("Fokusera på respekt och förståelse i ditt meddelande")
            rekommendationer.append("Använd konstruktivt språk som bygger broar")
        
        return rekommendationer
    
    def _förbättra_text(self, text: str) -> str:
        """Förbättrar text med empatiska förslag"""
        # Enkel implementation - i verkligheten skulle detta vara mer sofistikerat
        förbättringar = {
            'inte bra': 'kan förbättras',
            'dålig': 'utvecklingspotential',
            'problem': 'utmaning',
            'fel': 'förbättringsområde'
        }
        
        förbättrad_text = text
        for gammalt, nytt in förbättringar.items():
            förbättrad_text = förbättrad_text.replace(gammalt, nytt)
        
        return förbättrad_text

class TrendAnalys:
    """AI-modul för trendanalys per kommun och kategori"""
    
    def __init__(self):
        self.vektoriserare = TfidfVectorizer(max_features=500, ngram_range=(1, 2))
    
    def analysera_trender(self, data: List[Dict[str, Any]], 
                        kommun: str = None, 
                        kategori: str = None) -> Dict[str, Any]:
        """
        Analyserar trender i data baserat på kommun och kategori
        """
        try:
            # Filtrera data baserat på parametrar
            filtrerad_data = self._filtrera_data(data, kommun, kategori)
            
            if not filtrerad_data:
                return {'fel': 'Ingen data att analysera'}
            
            # Analysera trender över tid
            tidsanalys = self._analysera_tids_trender(filtrerad_data)
            
            # Analysera sentiment-trender
            sentiment_trender = self._analysera_sentiment_trender(filtrerad_data)
            
            # Analysera teman och nyckelord
            tema_analys = self._analysera_teman(filtrerad_data)
            
            # Generera insikter
            insikter = self._generera_insikter(tidsanalys, sentiment_trender, tema_analys)
            
            return {
                'kommun': kommun,
                'kategori': kategori,
                'tidsanalys': tidsanalys,
                'sentiment_trender': sentiment_trender,
                'tema_analys': tema_analys,
                'insikter': insikter,
                'analys_datum': datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Fel vid trendanalys: {e}")
            return {'fel': str(e)}
    
    def _filtrera_data(self, data: List[Dict[str, Any]], 
                      kommun: str, kategori: str) -> List[Dict[str, Any]]:
        """Filtrerar data baserat på kommun och kategori"""
        filtrerad = data
        
        if kommun:
            filtrerad = [d for d in filtrerad if d.get('kommun') == kommun]
        
        if kategori:
            filtrerad = [d for d in filtrerad if d.get('kategori') == kategori]
        
        return filtrerad
    
    def _analysera_tids_trender(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyserar trender över tid"""
        # Gruppera data per månad
        månads_data = {}
        
        for post in data:
            datum = datetime.fromisoformat(post.get('skapad', datetime.now().isoformat()))
            månad_nyckel = f"{datum.year}-{datum.month:02d}"
            
            if månad_nyckel not in månads_data:
                månads_data[månad_nyckel] = []
            månads_data[månad_nyckel].append(post)
        
        # Beräkna trender
        trender = {}
        förra_månaden = None
        
        for månad in sorted(månads_data.keys()):
            antal_poster = len(månads_data[månad])
            
            if förra_månaden:
                förändring = antal_poster - månads_data[förra_månaden]
                trender[månad] = {
                    'antal_poster': antal_poster,
                    'förändring': förändring,
                    'förändring_procent': (förändring / månads_data[förra_månaden]) * 100 if månads_data[förra_månaden] > 0 else 0
                }
            else:
                trender[månad] = {
                    'antal_poster': antal_poster,
                    'förändring': 0,
                    'förändring_procent': 0
                }
            
            förra_månaden = månad
        
        return trender
    
    def _analysera_sentiment_trender(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyserar sentiment-trender"""
        sentiment_data = []
        
        for post in data:
            text = post.get('innehåll', '') or post.get('beskrivning', '')
            if text:
                try:
                    sentiment = sentiment_analyzer(text)
                    sentiment_data.append({
                        'datum': post.get('skapad'),
                        'sentiment': sentiment[0]['score'] if sentiment[0]['label'] == 'POSITIVE' else 1 - sentiment[0]['score']
                    })
                except:
                    continue
        
        if not sentiment_data:
            return {'genomsnittligt_sentiment': 0.5, 'trend': 'neutral'}
        
        genomsnittligt_sentiment = np.mean([d['sentiment'] for d in sentiment_data])
        
        # Beräkna trend (enkel linjär regression)
        if len(sentiment_data) > 1:
            x = np.arange(len(sentiment_data))
            y = [d['sentiment'] for d in sentiment_data]
            trend_koefficient = np.polyfit(x, y, 1)[0]
            
            if trend_koefficient > 0.01:
                trend = 'förbättring'
            elif trend_koefficient < -0.01:
                trend = 'försämring'
            else:
                trend = 'stabil'
        else:
            trend = 'neutral'
        
        return {
            'genomsnittligt_sentiment': genomsnittligt_sentiment,
            'trend': trend,
            'antal_analyserade': len(sentiment_data)
        }
    
    def _analysera_teman(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyserar teman och nyckelord"""
        texter = []
        
        for post in data:
            text = post.get('innehåll', '') or post.get('beskrivning', '')
            if text:
                texter.append(text)
        
        if not texter:
            return {'vanligaste_teman': [], 'nyckelord': []}
        
        try:
            # Använd TF-IDF för att hitta viktiga termer
            tfidf_matrix = self.vektoriserare.fit_transform(texter)
            feature_names = self.vektoriserare.get_feature_names_out()
            
            # Hitta de vanligaste termerna
            mean_scores = np.mean(tfidf_matrix.toarray(), axis=0)
            top_indices = np.argsort(mean_scores)[-10:][::-1]
            
            vanligaste_teman = [feature_names[i] for i in top_indices]
            
            return {
                'vanligaste_teman': vanligaste_teman,
                'nyckelord': vanligaste_teman[:5]  # Top 5 nyckelord
            }
            
        except Exception as e:
            logger.error(f"Fel vid tema-analys: {e}")
            return {'vanligaste_teman': [], 'nyckelord': []}
    
    def _generera_insikter(self, tidsanalys: Dict, sentiment_trender: Dict, 
                          tema_analys: Dict) -> List[str]:
        """Genererar AI-insikter baserat på analysen"""
        insikter = []
        
        # Tidsbaserade insikter
        if tidsanalys:
            senaste_månad = max(tidsanalys.keys()) if tidsanalys else None
            if senaste_månad and tidsanalys[senaste_månad]['förändring'] > 0:
                insikter.append(f"Aktivitet har ökat med {tidsanalys[senaste_månad]['förändring']} poster den senaste månaden")
        
        # Sentiment-insikter
        if sentiment_trender.get('trend') == 'förbättring':
            insikter.append("Positiv utveckling i sentiment och ton")
        elif sentiment_trender.get('trend') == 'försämring':
            insikter.append("Negativ trend i sentiment - överväg stödåtgärder")
        
        # Tema-insikter
        if tema_analys.get('nyckelord'):
            insikter.append(f"Vanligaste diskussionsämnen: {', '.join(tema_analys['nyckelord'][:3])}")
        
        return insikter

class AIInsights:
    """AI-modul för generering av insikter till dashboard"""
    
    def __init__(self):
        self.trend_analys = TrendAnalys()
    
    def generera_dashboard_insikter(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Genererar AI-insikter för dashboard
        """
        try:
            insikter = {
                'sammanfattning': self._generera_sammanfattning(data),
                'rekommendationer': self._generera_rekommendationer(data),
                'varningar': self._identifiera_varningar(data),
                'möjligheter': self._identifiera_möjligheter(data),
                'trender': self._analysera_globala_trender(data),
                'genererat_datum': datetime.now().isoformat()
            }
            
            return insikter
            
        except Exception as e:
            logger.error(f"Fel vid generering av insikter: {e}")
            return {'fel': str(e)}
    
    def _generera_sammanfattning(self, data: Dict[str, Any]) -> str:
        """Genererar sammanfattning av data"""
        antal_användare = data.get('antal_användare', 0)
        antal_verksamheter = data.get('antal_verksamheter', 0)
        antal_recensioner = data.get('antal_recensioner', 0)
        
        sammanfattning = f"Neuroljus Neurohus har {antal_användare} registrerade användare, "
        sammanfattning += f"{antal_verksamheter} verksamheter och {antal_recensioner} recensioner. "
        
        if antal_recensioner > 0:
            genomsnittligt_betyg = data.get('genomsnittligt_betyg', 0)
            sammanfattning += f"Genomsnittligt betyg är {genomsnittligt_betyg:.1f}/5.0."
        
        return sammanfattning
    
    def _generera_rekommendationer(self, data: Dict[str, Any]) -> List[str]:
        """Genererar rekommendationer baserat på data"""
        rekommendationer = []
        
        # Rekommendationer baserat på aktivitet
        antal_recensioner = data.get('antal_recensioner', 0)
        antal_verksamheter = data.get('antal_verksamheter', 0)
        
        if antal_recensioner < antal_verksamheter * 2:
            rekommendationer.append("Överväg att uppmuntra fler recensioner för att förbättra transparens")
        
        # Rekommendationer baserat på kvalitet
        genomsnittligt_betyg = data.get('genomsnittligt_betyg', 0)
        if genomsnittligt_betyg < 3.5:
            rekommendationer.append("Fokusera på kvalitetsförbättringar i verksamheter med låga betyg")
        
        # Rekommendationer baserat på geografisk spridning
        kommuner = data.get('kommuner', [])
        if len(kommuner) < 10:
            rekommendationer.append("Utöka verksamhetsnätverket till fler kommuner")
        
        return rekommendationer
    
    def _identifiera_varningar(self, data: Dict[str, Any]) -> List[str]:
        """Identifierar potentiella varningar"""
        varningar = []
        
        # Varningar baserat på låga betyg
        genomsnittligt_betyg = data.get('genomsnittligt_betyg', 0)
        if genomsnittligt_betyg < 2.5:
            varningar.append("Låga genomsnittliga betyg kräver omedelbar uppmärksamhet")
        
        # Varningar baserat på aktivitet
        antal_recensioner_senaste_månad = data.get('recensioner_senaste_månad', 0)
        if antal_recensioner_senaste_månad < 5:
            varningar.append("Låg aktivitet i recensioner den senaste månaden")
        
        return varningar
    
    def _identifiera_möjligheter(self, data: Dict[str, Any]) -> List[str]:
        """Identifierar möjligheter för förbättring"""
        möjligheter = []
        
        # Möjligheter baserat på höga betyg
        genomsnittligt_betyg = data.get('genomsnittligt_betyg', 0)
        if genomsnittligt_betyg > 4.0:
            möjligheter.append("Höga betyg visar på god kvalitet - dela framgångsrika metoder")
        
        # Möjligheter baserat på aktivitet
        antal_användare = data.get('antal_användare', 0)
        if antal_användare > 100:
            möjligheter.append("Stor användarbas - överväg att expandera tjänster")
        
        return möjligheter
    
    def _analysera_globala_trender(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyserar globala trender"""
        trender = {
            'användar_tillväxt': data.get('användar_tillväxt', 0),
            'verksamhets_tillväxt': data.get('verksamhets_tillväxt', 0),
            'kvalitets_trend': data.get('kvalitets_trend', 'stabil'),
            'geografisk_spridning': data.get('geografisk_spridning', [])
        }
        
        return trender

# Huvudklass för AI-moduler
class NeuroljusAI:
    """Huvudklass som sammanbinder alla AI-moduler"""
    
    def __init__(self):
        self.rekommendation = EmpatiRekommendation()
        self.moderering = EmpatiModerering()
        self.trend_analys = TrendAnalys()
        self.insights = AIInsights()
    
    def processera_användar_interaktion(self, användare_id: str, 
                                       interaktion: Dict[str, Any]) -> Dict[str, Any]:
        """
        Processerar användarinteraktion med AI-stöd
        """
        try:
            # Moderera innehåll om det finns text
            if 'text' in interaktion:
                modererings_resultat = self.moderering.moderera_text(
                    interaktion['text'], 
                    interaktion.get('användare_roll', 'användare')
                )
                interaktion['modererings_resultat'] = modererings_resultat
            
            # Generera rekommendationer om relevant
            if interaktion.get('typ') == 'sök_verksamhet':
                rekommendationer = self._generera_verksamhets_rekommendationer(
                    användare_id, interaktion
                )
                interaktion['rekommendationer'] = rekommendationer
            
            return interaktion
            
        except Exception as e:
            logger.error(f"Fel vid processering av interaktion: {e}")
            return {'fel': str(e)}
    
    def _generera_verksamhets_rekommendationer(self, användare_id: str, 
                                              interaktion: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Genererar verksamhetsrekommendationer för användare"""
        # Här skulle vi hämta användarprofil och verksamheter från databasen
        # För nu returnerar vi mockade rekommendationer
        
        return [
            {
                'verksamhet_id': 'mock-1',
                'matchning': 0.95,
                'anledning': 'Perfekt matchning baserat på dina behov och preferenser'
            },
            {
                'verksamhet_id': 'mock-2', 
                'matchning': 0.87,
                'anledning': 'Hög empati-poäng i recensioner och bra kommunikation'
            }
        ]

# Exempel på användning
if __name__ == "__main__":
    # Skapa AI-instans
    ai = NeuroljusAI()
    
    # Exempel på användning av rekommendationssystem
    användar_profil = AnvändarProfil(
        användare_id="user-123",
        roll="familj",
        kommun="Stockholm",
        preferenser={"nära_hem": True, "djur": False},
        tidigare_interaktioner=[],
        diagnoser=["Autism"],
        åldersgrupp="18-65",
        behov=["Personlig assistans", "Dagverksamhet"]
    )
    
    verksamhets_profil = VerksamhetsProfil(
        verksamhet_id="verk-456",
        typ="gruppboende",
        kommun="Stockholm",
        diagnoser=["Autism", "ADHD"],
        tjänster=["Personlig assistans", "Dagverksamhet"],
        åldersgrupp="18-65",
        kapacitet=8,
        recensioner=[
            {"innehåll": "Fantastiskt stöd och förståelse för autism", "betyg": 5},
            {"innehåll": "Mycket professionell och empatisk personal", "betyg": 5}
        ],
        kvalitetsindikatorer={"trygghet": 4.8, "kommunikation": 4.6}
    )
    
    # Beräkna matchning
    matchning = ai.rekommendation.beräkna_matchning(användar_profil, verksamhets_profil)
    print(f"Matchning: {matchning:.2f}")
    
    # Exempel på moderering
    modererings_resultat = ai.moderering.moderera_text(
        "Detta boende är verkligen fantastiskt! Personalen visar så mycket empati och förståelse.",
        "familj"
    )
    print(f"Moderering godkänd: {modererings_resultat['godkänd']}")
    
    print("AI-moduler initialiserade och redo för användning!")
