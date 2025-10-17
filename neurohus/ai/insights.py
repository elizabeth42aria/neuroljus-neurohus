# AI-insikter för dashboard
# Genererar AI-summeringar och rekommendationer

import logging
from typing import Dict, Any, List
from datetime import datetime, timedelta
import numpy as np

logger = logging.getLogger(__name__)

class AIInsights:
    """AI-modul för generering av insikter till dashboard"""
    
    def __init__(self):
        pass
    
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
                'kvalitetsindikatorer': self._beräkna_kvalitetsindikatorer(data),
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
            sammanfattning += f"Genomsnittligt betyg är {genomsnittligt_betyg:.1f}/5.0. "
        
        # Lägg till trendinformation
        trend = data.get('trend', 'stabil')
        if trend == 'tillväxt':
            sammanfattning += "Plattformen visar positiv tillväxt med ökande aktivitet."
        elif trend == 'minskning':
            sammanfattning += "Aktiviteten har minskat - överväg åtgärder för att öka engagemanget."
        else:
            sammanfattning += "Aktiviteten är stabil med konsekvent engagemang."
        
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
        elif genomsnittligt_betyg > 4.5:
            rekommendationer.append("Höga betyg visar på god kvalitet - dela framgångsrika metoder")
        
        # Rekommendationer baserat på geografisk spridning
        kommuner = data.get('kommuner', [])
        if len(kommuner) < 10:
            rekommendationer.append("Utöka verksamhetsnätverket till fler kommuner")
        
        # Rekommendationer baserat på användaraktivitet
        antal_användare = data.get('antal_användare', 0)
        aktiva_användare = data.get('aktiva_användare_senaste_månad', 0)
        
        if antal_användare > 0 and aktiva_användare / antal_användare < 0.3:
            rekommendationer.append("Låg användaraktivitet - överväg engagemangsstrategier")
        
        # Rekommendationer baserat på kursaktivitet
        antal_kurser = data.get('antal_kurser', 0)
        antal_kursavslutningar = data.get('antal_kursavslutningar', 0)
        
        if antal_kurser > 0 and antal_kursavslutningar / antal_kurser < 0.5:
            rekommendationer.append("Förbättra kursavslutningsgraden genom bättre stöd och motivation")
        
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
        
        # Varningar baserat på användaraktivitet
        antal_användare = data.get('antal_användare', 0)
        aktiva_användare = data.get('aktiva_användare_senaste_månad', 0)
        
        if antal_användare > 50 and aktiva_användare < 10:
            varningar.append("Mycket låg användaraktivitet - risk för användarförlust")
        
        # Varningar baserat på kvalitetsindikatorer
        låga_trygghet = data.get('verksamheter_låg_trygghet', 0)
        if låga_trygghet > 0:
            varningar.append(f"{låga_trygghet} verksamheter har låga trygghetsbetyg")
        
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
        
        # Möjligheter baserat på geografisk spridning
        kommuner = data.get('kommuner', [])
        if len(kommuner) > 20:
            möjligheter.append("Bred geografisk spridning - utveckla regionala samarbeten")
        
        # Möjligheter baserat på kursaktivitet
        antal_kursavslutningar = data.get('antal_kursavslutningar', 0)
        if antal_kursavslutningar > 50:
            möjligheter.append("Hög kursaktivitet - utveckla fler utbildningsprogram")
        
        # Möjligheter baserat på forskning
        antal_forskningsposter = data.get('antal_forskningsposter', 0)
        if antal_forskningsposter > 10:
            möjligheter.append("Rik forskningsbas - utveckla akademiska samarbeten")
        
        return möjligheter
    
    def _analysera_globala_trender(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyserar globala trender"""
        trender = {
            'användar_tillväxt': data.get('användar_tillväxt', 0),
            'verksamhets_tillväxt': data.get('verksamhets_tillväxt', 0),
            'kvalitets_trend': data.get('kvalitets_trend', 'stabil'),
            'geografisk_spridning': data.get('geografisk_spridning', []),
            'aktivitet_trend': data.get('aktivitet_trend', 'stabil'),
            'sentiment_trend': data.get('sentiment_trend', 'neutral')
        }
        
        return trender
    
    def _beräkna_kvalitetsindikatorer(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Beräknar kvalitetsindikatorer"""
        indikatorer = {
            'genomsnittligt_betyg': data.get('genomsnittligt_betyg', 0),
            'genomsnittlig_trygghet': data.get('genomsnittlig_trygghet', 0),
            'genomsnittlig_kommunikation': data.get('genomsnittlig_kommunikation', 0),
            'genomsnittlig_delaktighet': data.get('genomsnittlig_delaktighet', 0),
            'antal_verksamheter_höga_betyg': data.get('antal_verksamheter_höga_betyg', 0),
            'antal_verksamheter_låga_betyg': data.get('antal_verksamheter_låga_betyg', 0),
            'kvalitetsindex': 0
        }
        
        # Beräkna kvalitetsindex
        kvalitetsindex = (
            indikatorer['genomsnittligt_betyg'] * 0.4 +
            indikatorer['genomsnittlig_trygghet'] * 0.2 +
            indikatorer['genomsnittlig_kommunikation'] * 0.2 +
            indikatorer['genomsnittlig_delaktighet'] * 0.2
        )
        
        indikatorer['kvalitetsindex'] = kvalitetsindex
        
        return indikatorer
    
    def generera_månadsrapport(self, månads_data: Dict[str, Any]) -> Dict[str, Any]:
        """Genererar månadsrapport med AI-insikter"""
        try:
            rapport = {
                'månad': månads_data.get('månad', datetime.now().strftime('%Y-%m')),
                'sammanfattning': self._generera_månads_sammanfattning(månads_data),
                'nyckeltal': self._beräkna_månads_nyckeltal(månads_data),
                'trender': self._analysera_månads_trender(månads_data),
                'rekommendationer': self._generera_månads_rekommendationer(månads_data),
                'framtida_fokus': self._identifiera_framtida_fokus(månads_data),
                'genererat_datum': datetime.now().isoformat()
            }
            
            return rapport
            
        except Exception as e:
            logger.error(f"Fel vid generering av månadsrapport: {e}")
            return {'fel': str(e)}
    
    def _generera_månads_sammanfattning(self, data: Dict[str, Any]) -> str:
        """Genererar sammanfattning för månaden"""
        nya_användare = data.get('nya_användare', 0)
        nya_recensioner = data.get('nya_recensioner', 0)
        nya_verksamheter = data.get('nya_verksamheter', 0)
        kursavslutningar = data.get('kursavslutningar', 0)
        
        sammanfattning = f"Under månaden har {nya_användare} nya användare registrerats, "
        sammanfattning += f"{nya_recensioner} nya recensioner skrivits och {nya_verksamheter} nya verksamheter lagts till. "
        sammanfattning += f"{kursavslutningar} kurser har avslutats framgångsrikt."
        
        return sammanfattning
    
    def _beräkna_månads_nyckeltal(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Beräknar nyckeltal för månaden"""
        return {
            'nya_användare': data.get('nya_användare', 0),
            'nya_recensioner': data.get('nya_recensioner', 0),
            'nya_verksamheter': data.get('nya_verksamheter', 0),
            'kursavslutningar': data.get('kursavslutningar', 0),
            'genomsnittligt_betyg': data.get('genomsnittligt_betyg', 0),
            'användaraktivitet': data.get('användaraktivitet', 0)
        }
    
    def _analysera_månads_trender(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyserar trender för månaden"""
        return {
            'aktivitet_trend': data.get('aktivitet_trend', 'stabil'),
            'kvalitet_trend': data.get('kvalitet_trend', 'stabil'),
            'användar_tillväxt': data.get('användar_tillväxt', 0),
            'sentiment_trend': data.get('sentiment_trend', 'neutral')
        }
    
    def _generera_månads_rekommendationer(self, data: Dict[str, Any]) -> List[str]:
        """Genererar rekommendationer för månaden"""
        rekommendationer = []
        
        nya_användare = data.get('nya_användare', 0)
        if nya_användare > 20:
            rekommendationer.append("Hög användartillväxt - överväg att utöka supportresurser")
        
        kursavslutningar = data.get('kursavslutningar', 0)
        if kursavslutningar < 5:
            rekommendationer.append("Låg kursaktivitet - utveckla engagemangsstrategier")
        
        return rekommendationer
    
    def _identifiera_framtida_fokus(self, data: Dict[str, Any]) -> List[str]:
        """Identifierar fokusområden för framtiden"""
        fokus = []
        
        nya_användare = data.get('nya_användare', 0)
        if nya_användare > 10:
            fokus.append("Användarupplevelse och onboarding")
        
        kursavslutningar = data.get('kursavslutningar', 0)
        if kursavslutningar > 20:
            fokus.append("Utveckling av nya utbildningsprogram")
        
        nya_verksamheter = data.get('nya_verksamheter', 0)
        if nya_verksamheter > 5:
            fokus.append("Kvalitetssäkring och verksamhetsutveckling")
        
        return fokus