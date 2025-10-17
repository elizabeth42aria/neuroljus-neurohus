# Empatisk moderering av innehåll
# Språkgranskning, empati-ton, borttagning av persondata

import re
import logging
from typing import Dict, Any, List
from datetime import datetime

logger = logging.getLogger(__name__)

class EmpatiModerering:
    """AI-modul för empatisk moderering av innehåll"""
    
    def __init__(self):
        self.negativa_nyckelord = [
            'hat', 'diskriminering', 'kränkande', 'nedvärderande',
            'förnedrande', 'hot', 'mobbning', 'trakasseri', 'dum',
            'korkad', 'idiot', 'avskum', 'värdelös'
        ]
        
        self.empatiska_nyckelord = [
            'respekt', 'förståelse', 'empati', 'stöd', 'hjälp',
            'tack', 'uppskattning', 'värdefull', 'viktig', 'bra',
            'fantastisk', 'professionell', 'kompetent', 'varm'
        ]
        
        self.personuppgifts_mönster = [
            r'\b\d{4}-\d{2}-\d{2}\b',  # Personnummer
            r'\b\d{10,12}\b',          # Telefonnummer
            r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # E-post
            r'\b\d{3}-\d{2}-\d{2}\b'   # Personnummer med bindestreck
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
                'modererad_text': self._förbättra_text(text) if not godkänd else text,
                'modererings_datum': datetime.now().isoformat()
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
        
        # Kontrollera personuppgifter
        personuppgifter = []
        for mönster in self.personuppgifts_mönster:
            träffar = re.findall(mönster, text)
            personuppgifter.extend(träffar)
        
        # Kontrollera potentiella hot eller kränkningar
        hot_mönster = [
            r'jag ska.*döda',
            r'jag kommer.*skada',
            r'jag vill.*döda',
            r'hotar.*att',
            r'kommer.*att.*skada'
        ]
        
        hot_träffar = []
        for mönster in hot_mönster:
            if re.search(mönster, text_lower):
                hot_träffar.append(mönster)
        
        säker = (len(negativa_träffar) == 0 and 
                len(personuppgifter) == 0 and 
                len(hot_träffar) == 0)
        
        return {
            'säker': säker,
            'poäng': 1.0 if säker else 0.0,
            'negativa_träffar': negativa_träffar,
            'personuppgifter': personuppgifter,
            'hot_träffar': hot_träffar
        }
    
    def _analysera_empati(self, text: str) -> Dict[str, Any]:
        """Analyserar empati och respekt i texten"""
        text_lower = text.lower()
        
        # Räkna empatiska nyckelord
        empatiska_träffar = [ord for ord in self.empatiska_nyckelord if ord in text_lower]
        
        # Enkel sentimentanalys baserat på nyckelord
        positiva_ord = ['bra', 'fantastisk', 'utmärkt', 'perfekt', 'rekommenderar', 'tack']
        negativa_ord = ['dålig', 'fruktansvärd', 'undvik', 'problem', 'fel', 'hatar']
        
        positiva_träffar = sum(1 for ord in positiva_ord if ord in text_lower)
        negativa_träffar = sum(1 for ord in negativa_ord if ord in text_lower)
        
        sentiment_poäng = 0.5
        if positiva_träffar > negativa_träffar:
            sentiment_poäng = min(1.0, 0.5 + (positiva_träffar - negativa_träffar) * 0.1)
        elif negativa_träffar > positiva_träffar:
            sentiment_poäng = max(0.0, 0.5 - (negativa_träffar - positiva_träffar) * 0.1)
        
        # Beräkna empati-poäng
        empati_poäng = min(1.0, len(empatiska_träffar) / 5 + sentiment_poäng * 0.5)
        
        return {
            'poäng': empati_poäng,
            'empatiska_träffar': empatiska_träffar,
            'sentiment_poäng': sentiment_poäng,
            'positiva_träffar': positiva_träffar,
            'negativa_träffar': negativa_träffar
        }
    
    def _moderera_för_roll(self, text: str, roll: str) -> Dict[str, Any]:
        """Rollspecifik moderering"""
        text_lower = text.lower()
        
        if roll == 'familj':
            # Familjer bör undvika specifika medicinska termer utan kontext
            medicinska_termer = ['diagnos', 'behandling', 'terapi', 'medicin']
            medicinska_träffar = [term for term in medicinska_termer if term in text_lower]
            
            poäng = 1.0 if len(medicinska_träffar) == 0 else 0.7
            
        elif roll == 'assistent':
            # Assistenter bör använda professionellt språk
            professionella_termer = ['brukare', 'omsorg', 'stöd', 'assistans', 'professionell']
            professionella_träffar = [term for term in professionella_termer if term in text_lower]
            
            poäng = min(1.0, len(professionella_träffar) / 3 + 0.5)
            
        elif roll == 'kommun':
            # Kommuner bör använda formellt språk
            formella_termer = ['verksamhet', 'tjänst', 'insats', 'samhällsansvar']
            formella_träffar = [term for term in formella_termer if term in text_lower]
            
            poäng = min(1.0, len(formella_träffar) / 3 + 0.6)
            
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
            rekommendationer.append("Fokusera på konstruktiva förslag istället för kritik")
        
        if poäng < 0.7:
            rekommendationer.append("Fokusera på respekt och förståelse i ditt meddelande")
            rekommendationer.append("Använd konstruktivt språk som bygger broar")
            rekommendationer.append("Tänk på hur ditt meddelande kan påverka andra")
        
        # Specifika rekommendationer baserat på innehåll
        text_lower = text.lower()
        if 'problem' in text_lower and 'lösning' not in text_lower:
            rekommendationer.append("Överväg att föreslå konkreta lösningar på problem du identifierar")
        
        if len(text) < 10:
            rekommendationer.append("Utveckla ditt meddelande för att ge mer värde till andra")
        
        return rekommendationer
    
    def _förbättra_text(self, text: str) -> str:
        """Förbättrar text med empatiska förslag"""
        # Enkel implementation - i verkligheten skulle detta vara mer sofistikerat
        förbättringar = {
            'inte bra': 'kan förbättras',
            'dålig': 'utvecklingspotential',
            'problem': 'utmaning',
            'fel': 'förbättringsområde',
            'hatar': 'tycker inte om',
            'idiot': 'person',
            'dum': 'ovan',
            'korkad': 'ovan'
        }
        
        förbättrad_text = text
        for gammalt, nytt in förbättringar.items():
            förbättrad_text = förbättrad_text.replace(gammalt, nytt)
        
        return förbättrad_text
    
    def moderera_recension(self, recension: Dict[str, Any]) -> Dict[str, Any]:
        """Specialiserad moderering för recensioner"""
        text = recension.get('innehåll', '')
        användare_roll = recension.get('användare_roll', 'användare')
        
        # Grundmoderering
        modererings_resultat = self.moderera_text(text, användare_roll)
        
        # Specifika kontroller för recensioner
        recension_specifika_kontroller = self._kontrollera_recension_specifikt(recension)
        
        # Kombinera resultat
        modererings_resultat.update(recension_specifika_kontroller)
        
        return modererings_resultat
    
    def _kontrollera_recension_specifikt(self, recension: Dict[str, Any]) -> Dict[str, Any]:
        """Specifika kontroller för recensioner"""
        kontroller = {
            'har_betyg': 'betyg' in recension and recension['betyg'] is not None,
            'har_innehåll': len(recension.get('innehåll', '')) > 10,
            'har_rubrik': len(recension.get('rubrik', '')) > 5,
            'betyg_rimligt': True
        }
        
        # Kontrollera om betyg är rimligt
        if 'betyg' in recension:
            betyg = recension['betyg']
            kontroller['betyg_rimligt'] = 1 <= betyg <= 5
        
        # Kontrollera om innehållet matchar betyget
        text = recension.get('innehåll', '').lower()
        betyg = recension.get('betyg', 0)
        
        if betyg >= 4 and any(ord in text for ord in ['dålig', 'fruktansvärd', 'hatar', 'undvik']):
            kontroller['betyg_matchar_innehåll'] = False
        elif betyg <= 2 and any(ord in text for ord in ['fantastisk', 'perfekt', 'rekommenderar', 'utmärkt']):
            kontroller['betyg_matchar_innehåll'] = False
        else:
            kontroller['betyg_matchar_innehåll'] = True
        
        # Beräkna total poäng för recension
        recension_poäng = sum(1 for v in kontroller.values() if v) / len(kontroller)
        
        return {
            'recension_kontroller': kontroller,
            'recension_poäng': recension_poäng,
            'recension_godkänd': recension_poäng >= 0.7
        }
