# Empatisk rekommendationsmotor
# Matchar användare med verksamheter baserat på empati och behov

import numpy as np
from typing import List, Dict, Any, Tuple
from dataclasses import dataclass
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import logging

logger = logging.getLogger(__name__)

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
            
            # Enkel sentimentanalys baserat på nyckelord
            positiva_ord = ['bra', 'fantastisk', 'utmärkt', 'perfekt', 'rekommenderar']
            negativa_ord = ['dålig', 'fruktansvärd', 'undvik', 'problem', 'fel']
            
            positiva_träffar = sum(1 for ord in positiva_ord if ord in text)
            negativa_träffar = sum(1 for ord in negativa_ord if ord in text)
            
            sentiment_poäng = 0.5
            if positiva_träffar > negativa_träffar:
                sentiment_poäng = 0.7 + (positiva_träffar - negativa_träffar) * 0.1
            elif negativa_träffar > positiva_träffar:
                sentiment_poäng = 0.3 - (negativa_träffar - positiva_träffar) * 0.1
            
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
