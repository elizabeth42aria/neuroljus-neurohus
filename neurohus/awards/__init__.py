# Neuroljus Neurohus Awards
# Nomineringar och erkännande för empati och kvalitet

import logging
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
from dataclasses import dataclass
import uuid
import json

logger = logging.getLogger(__name__)

@dataclass
class Utmärkelse:
    """En utmärkelse som kan delas ut"""
    id: str
    namn: str
    beskrivning: str
    kategori: str
    år: int
    aktiv: bool
    skapad: datetime
    röstningsperiod_start: datetime
    röstningsperiod_slut: datetime

@dataclass
class Nominering:
    """En nominering för en utmärkelse"""
    id: str
    utmärkelse_id: str
    nominerad_verksamhet_id: Optional[str]
    nominerad_assistans_id: Optional[str]
    nominerad_användare_id: Optional[str]
    typ: str  # verksamhet, assistansföretag, person
    motivering: str
    nominerad_av: str
    skapad: datetime
    status: str  # aktiv, vinnare, nominerad
    antal_röster: int

@dataclass
class Röst:
    """En röst på en nominering"""
    id: str
    nominering_id: str
    användare_id: str
    skapad: datetime
    anledning: str

class AwardsManager:
    """Hanterar utmärkelser och nomineringar"""
    
    def __init__(self):
        self.utmärkelser = {}
        self.nomineringar = {}
        self.röster = {}
        self._skapa_standard_utmärkelser()
        self._skapa_exempel_nomineringar()
    
    def _skapa_standard_utmärkelser(self):
        """Skapar standardutmärkelser"""
        nu = datetime.now()
        röstningsperiod_start = nu - timedelta(days=30)
        röstningsperiod_slut = nu + timedelta(days=30)
        
        utmärkelser = [
            Utmärkelse(
                id="årets-boende",
                namn="Årets Boende",
                beskrivning="Utmärkelse för det bästa LSS-boendet baserat på brukarrecensioner och kvalitetsindikatorer. Fokuserar på empati, trygghet och personcentrerad omsorg.",
                kategori="Boende",
                år=2023,
                aktiv=True,
                skapad=nu,
                röstningsperiod_start=röstningsperiod_start,
                röstningsperiod_slut=röstningsperiod_slut
            ),
            Utmärkelse(
                id="årets-assistent",
                namn="Årets Assistent",
                beskrivning="Utmärkelse för assistenter som visat exceptionell empati och professionalism. Erkänner personer som gjort skillnad i brukarnas vardag.",
                kategori="Person",
                år=2023,
                aktiv=True,
                skapad=nu,
                röstningsperiod_start=röstningsperiod_start,
                röstningsperiod_slut=röstningsperiod_slut
            ),
            Utmärkelse(
                id="brukarens-röst",
                namn="Brukarens Röst",
                beskrivning="Utmärkelse som röstas fram direkt av brukare och deras familjer. Den mest autentiska bedömningen av kvalitet och empati.",
                kategori="Brukarval",
                år=2023,
                aktiv=True,
                skapad=nu,
                röstningsperiod_start=röstningsperiod_start,
                röstningsperiod_slut=röstningsperiod_slut
            )
        ]
        
        for utmärkelse in utmärkelser:
            self.utmärkelser[utmärkelse.id] = utmärkelse
        
        logger.info(f"Skapade {len(utmärkelser)} utmärkelser")
    
    def _skapa_exempel_nomineringar(self):
        """Skapar exempel på nomineringar"""
        nu = datetime.now()
        
        nomineringar = [
            Nominering(
                id="nominering-1",
                utmärkelse_id="årets-boende",
                nominerad_verksamhet_id="verksamhet-solgården",
                nominerad_assistans_id=None,
                nominerad_användare_id=None,
                typ="verksamhet",
                motivering="Solgården visar exceptionell förståelse för sina brukares behov och skapar en verkligt trygg och utvecklande miljö. Personalen är professionell, empatisk och skapar genuina relationer med brukarna.",
                nominerad_av="anna-larsson",
                skapad=nu,
                status="aktiv",
                antal_röster=0
            ),
            Nominering(
                id="nominering-2",
                utmärkelse_id="årets-boende",
                nominerad_verksamhet_id="verksamhet-framtidens-boende",
                nominerad_assistans_id=None,
                nominerad_användare_id=None,
                typ="verksamhet",
                motivering="Framtidens Boende visar hur framtiden kan se ut för LSS-omsorg. Modernt tänkande, fokus på självständighet och respekt för individen gör detta boende till en förebild.",
                nominerad_av="erik-johansson",
                skapad=nu,
                status="aktiv",
                antal_röster=0
            ),
            Nominering(
                id="nominering-3",
                utmärkelse_id="årets-assistent",
                nominerad_verksamhet_id=None,
                nominerad_assistans_id=None,
                nominerad_användare_id="maria-svensson",
                typ="person",
                motivering="Maria visar dagligen exceptionell empati och förståelse för sina brukares behov. Hon går alltid det extra steget för att skapa trygga och meningsfulla relationer.",
                nominerad_av="anna-larsson",
                skapad=nu,
                status="aktiv",
                antal_röster=0
            )
        ]
        
        for nominering in nomineringar:
            self.nomineringar[nominering.id] = nominering
        
        logger.info(f"Skapade {len(nomineringar)} nomineringar")
    
    def hämta_utmärkelser(self) -> List[Dict[str, Any]]:
        """Hämtar alla aktiva utmärkelser"""
        utmärkelser = [u for u in self.utmärkelser.values() if u.aktiv]
        
        # Lägg till nomineringsstatistik
        resultat = []
        for utmärkelse in utmärkelser:
            nomineringar_för_utmärkelse = [n for n in self.nomineringar.values() 
                                          if n.utmärkelse_id == utmärkelse.id]
            
            resultat.append({
                'id': utmärkelse.id,
                'namn': utmärkelse.namn,
                'beskrivning': utmärkelse.beskrivning,
                'kategori': utmärkelse.kategori,
                'år': utmärkelse.år,
                'skapad': utmärkelse.skapad.isoformat(),
                'röstningsperiod_start': utmärkelse.röstningsperiod_start.isoformat(),
                'röstningsperiod_slut': utmärkelse.röstningsperiod_slut.isoformat(),
                'antal_nomineringar': len(nomineringar_för_utmärkelse),
                'röstningsperiod_aktiv': self._är_röstningsperiod_aktiv(utmärkelse)
            })
        
        return resultat
    
    def hämta_nomineringar(self, utmärkelse_id: str = None) -> List[Dict[str, Any]]:
        """Hämtar nomineringar med filtrering"""
        nomineringar = list(self.nomineringar.values())
        
        if utmärkelse_id:
            nomineringar = [n for n in nomineringar if n.utmärkelse_id == utmärkelse_id]
        
        # Sortera efter antal röster
        nomineringar.sort(key=lambda n: n.antal_röster, reverse=True)
        
        return [self._nominering_till_dict(nominering) for nominering in nomineringar]
    
    def skapa_nominering(self, nominering_data: Dict[str, Any]) -> Dict[str, Any]:
        """Skapar en ny nominering"""
        nominering_id = str(uuid.uuid4())
        
        # Validera att utmärkelsen finns och är aktiv
        utmärkelse_id = nominering_data['utmärkelse_id']
        if utmärkelse_id not in self.utmärkelser:
            return {'fel': 'Utmärkelse inte hittad'}
        
        utmärkelse = self.utmärkelser[utmärkelse_id]
        if not utmärkelse.aktiv:
            return {'fel': 'Utmärkelse inte aktiv'}
        
        # Kontrollera att röstningsperioden är aktiv
        if not self._är_röstningsperiod_aktiv(utmärkelse):
            return {'fel': 'Röstningsperioden är inte aktiv'}
        
        nominering = Nominering(
            id=nominering_id,
            utmärkelse_id=utmärkelse_id,
            nominerad_verksamhet_id=nominering_data.get('nominerad_verksamhet_id'),
            nominerad_assistans_id=nominering_data.get('nominerad_assistans_id'),
            nominerad_användare_id=nominering_data.get('nominerad_användare_id'),
            typ=nominering_data['typ'],
            motivering=nominering_data['motivering'],
            nominerad_av=nominering_data['nominerad_av'],
            skapad=datetime.now(),
            status='aktiv',
            antal_röster=0
        )
        
        self.nomineringar[nominering_id] = nominering
        
        logger.info(f"Skapade nominering: {nominering.motivering[:50]}...")
        
        return {
            'meddelande': 'Nominering skapad framgångsrikt',
            'nominering_id': nominering_id,
            'nominering': self._nominering_till_dict(nominering)
        }
    
    def rösta_på_nominering(self, nominering_id: str, användare_id: str, 
                           anledning: str) -> Dict[str, Any]:
        """Röstar på en nominering"""
        if nominering_id not in self.nomineringar:
            return {'fel': 'Nominering inte hittad'}
        
        nominering = self.nomineringar[nominering_id]
        
        # Kontrollera att röstningsperioden är aktiv
        utmärkelse = self.utmärkelser[nominering.utmärkelse_id]
        if not self._är_röstningsperiod_aktiv(utmärkelse):
            return {'fel': 'Röstningsperioden är inte aktiv'}
        
        # Kontrollera att användaren inte redan röstat
        befintlig_röst = [r for r in self.röster.values() 
                         if r.nominering_id == nominering_id and r.användare_id == användare_id]
        
        if befintlig_röst:
            return {'fel': 'Du har redan röstat på denna nominering'}
        
        # Skapa röst
        röst_id = str(uuid.uuid4())
        röst = Röst(
            id=röst_id,
            nominering_id=nominering_id,
            användare_id=användare_id,
            skapad=datetime.now(),
            anledning=anledning
        )
        
        self.röster[röst_id] = röst
        
        # Uppdatera antal röster på nominering
        nominering.antal_röster += 1
        
        logger.info(f"Röst registrerad: {användare_id} röstade på {nominering_id}")
        
        return {
            'meddelande': 'Röst registrerad framgångsrikt',
            'röst_id': röst_id,
            'nominering': self._nominering_till_dict(nominering)
        }
    
    def hämta_röstningsresultat(self, utmärkelse_id: str) -> Dict[str, Any]:
        """Hämtar röstningsresultat för en utmärkelse"""
        if utmärkelse_id not in self.utmärkelser:
            return {'fel': 'Utmärkelse inte hittad'}
        
        utmärkelse = self.utmärkelser[utmärkelse_id]
        nomineringar = [n for n in self.nomineringar.values() 
                       if n.utmärkelse_id == utmärkelse_id]
        
        # Sortera efter antal röster
        nomineringar.sort(key=lambda n: n.antal_röster, reverse=True)
        
        # Beräkna totala antal röster
        totala_röster = sum(n.antal_röster for n in nomineringar)
        
        # Lägg till procentuell fördelning
        resultat = []
        for nominering in nomineringar:
            procent = (nominering.antal_röster / totala_röster * 100) if totala_röster > 0 else 0
            
            resultat.append({
                'nominering': self._nominering_till_dict(nominering),
                'antal_röster': nominering.antal_röster,
                'procent': round(procent, 1)
            })
        
        return {
            'utmärkelse': {
                'id': utmärkelse.id,
                'namn': utmärkelse.namn,
                'beskrivning': utmärkelse.beskrivning,
                'år': utmärkelse.år
            },
            'resultat': resultat,
            'totala_röster': totala_röster,
            'antal_nomineringar': len(nomineringar),
            'röstningsperiod_aktiv': self._är_röstningsperiod_aktiv(utmärkelse)
        }
    
    def hämta_användares_röster(self, användare_id: str) -> List[Dict[str, Any]]:
        """Hämtar alla röster från en användare"""
        användares_röster = [r for r in self.röster.values() if r.användare_id == användare_id]
        
        resultat = []
        for röst in användares_röster:
            nominering = self.nomineringar.get(röst.nominering_id)
            if nominering:
                utmärkelse = self.utmärkelser.get(nominering.utmärkelse_id)
                
                resultat.append({
                    'röst': {
                        'id': röst.id,
                        'skapad': röst.skapad.isoformat(),
                        'anledning': röst.anledning
                    },
                    'nominering': self._nominering_till_dict(nominering),
                    'utmärkelse': {
                        'id': utmärkelse.id,
                        'namn': utmärkelse.namn
                    } if utmärkelse else None
                })
        
        return resultat
    
    def hämta_awards_statistik(self) -> Dict[str, Any]:
        """Hämtar statistik över awards-systemet"""
        totala_utmärkelser = len(self.utmärkelser)
        aktiva_utmärkelser = len([u for u in self.utmärkelser.values() if u.aktiv])
        
        totala_nomineringar = len(self.nomineringar)
        aktiva_nomineringar = len([n for n in self.nomineringar.values() if n.status == 'aktiv'])
        
        totala_röster = len(self.röster)
        
        # Röster per utmärkelse
        röster_per_utmärkelse = {}
        for utmärkelse in self.utmärkelser.values():
            nomineringar_för_utmärkelse = [n for n in self.nomineringar.values() 
                                          if n.utmärkelse_id == utmärkelse.id]
            röster_för_utmärkelse = sum(n.antal_röster for n in nomineringar_för_utmärkelse)
            röster_per_utmärkelse[utmärkelse.namn] = röster_för_utmärkelse
        
        return {
            'utmärkelser': {
                'totala_utmärkelser': totala_utmärkelser,
                'aktiva_utmärkelser': aktiva_utmärkelser
            },
            'nomineringar': {
                'totala_nomineringar': totala_nomineringar,
                'aktiva_nomineringar': aktiva_nomineringar
            },
            'röster': {
                'totala_röster': totala_röster,
                'röster_per_utmärkelse': röster_per_utmärkelse
            },
            'genererat_datum': datetime.now().isoformat()
        }
    
    def _är_röstningsperiod_aktiv(self, utmärkelse: Utmärkelse) -> bool:
        """Kontrollerar om röstningsperioden är aktiv"""
        nu = datetime.now()
        return utmärkelse.röstningsperiod_start <= nu <= utmärkelse.röstningsperiod_slut
    
    def _nominering_till_dict(self, nominering: Nominering) -> Dict[str, Any]:
        """Konverterar Nominering till dictionary"""
        return {
            'id': nominering.id,
            'utmärkelse_id': nominering.utmärkelse_id,
            'nominerad_verksamhet_id': nominering.nominerad_verksamhet_id,
            'nominerad_assistans_id': nominering.nominerad_assistans_id,
            'nominerad_användare_id': nominering.nominerad_användare_id,
            'typ': nominering.typ,
            'motivering': nominering.motivering,
            'nominerad_av': nominering.nominerad_av,
            'skapad': nominering.skapad.isoformat(),
            'status': nominering.status,
            'antal_röster': nominering.antal_röster
        }

class AwardsAPI:
    """API för Awards-funktionalitet"""
    
    def __init__(self):
        self.awards_manager = AwardsManager()
    
    def hämta_awards_översikt(self) -> Dict[str, Any]:
        """Hämtar översikt över awards-systemet"""
        utmärkelser = self.awards_manager.hämta_utmärkelser()
        statistik = self.awards_manager.hämta_awards_statistik()
        
        return {
            'utmärkelser': utmärkelser,
            'statistik': statistik,
            'aktiva_röstningar': len([u for u in utmärkelser if u['röstningsperiod_aktiv']])
        }
    
    def hämta_utmärkelser(self) -> List[Dict[str, Any]]:
        """Hämtar alla aktiva utmärkelser"""
        return self.awards_manager.hämta_utmärkelser()
    
    def hämta_nomineringar(self, utmärkelse_id: str = None) -> List[Dict[str, Any]]:
        """Hämtar nomineringar med filtrering"""
        return self.awards_manager.hämta_nomineringar(utmärkelse_id)
    
    def skapa_nominering(self, nominering_data: Dict[str, Any]) -> Dict[str, Any]:
        """Skapar en ny nominering"""
        return self.awards_manager.skapa_nominering(nominering_data)
    
    def rösta_på_nominering(self, nominering_id: str, användare_id: str, 
                           anledning: str) -> Dict[str, Any]:
        """Röstar på en nominering"""
        return self.awards_manager.rösta_på_nominering(nominering_id, användare_id, anledning)
    
    def hämta_röstningsresultat(self, utmärkelse_id: str) -> Dict[str, Any]:
        """Hämtar röstningsresultat för en utmärkelse"""
        return self.awards_manager.hämta_röstningsresultat(utmärkelse_id)
    
    def hämta_användares_röster(self, användare_id: str) -> List[Dict[str, Any]]:
        """Hämtar alla röster från en användare"""
        return self.awards_manager.hämta_användares_röster(användare_id)
    
    def hämta_awards_statistik(self) -> Dict[str, Any]:
        """Hämtar statistik över awards-systemet"""
        return self.awards_manager.hämta_awards_statistik()

# Exempel på användning
if __name__ == "__main__":
    # Skapa Awards API
    awards = AwardsAPI()
    
    # Hämta awardsöversikt
    översikt = awards.hämta_awards_översikt()
    print(f"Utmärkelser: {len(översikt['utmärkelser'])}")
    print(f"Aktiva röstningar: {översikt['aktiva_röstningar']}")
    
    # Hämta utmärkelser
    utmärkelser = awards.hämta_utmärkelser()
    print(f"Tillgängliga utmärkelser: {len(utmärkelser)}")
    
    if utmärkelser:
        första_utmärkelse = utmärkelser[0]
        print(f"Första utmärkelse: {första_utmärkelse['namn']}")
        
        # Hämta nomineringar för utmärkelsen
        nomineringar = awards.hämta_nomineringar(första_utmärkelse['id'])
        print(f"Nomineringar för {första_utmärkelse['namn']}: {len(nomineringar)}")
        
        if nomineringar:
            första_nominering = nomineringar[0]
            print(f"Första nominering: {första_nominering['motivering'][:50]}...")
            
            # Rösta på nomineringen
            användare_id = "test-user-123"
            röst_resultat = awards.rösta_på_nominering(
                första_nominering['id'],
                användare_id,
                "Fantastisk nominering som visar verklig empati och professionalism!"
            )
            
            if 'fel' not in röst_resultat:
                print(f"Röst registrerad: {röst_resultat['meddelande']}")
    
    # Skapa en ny nominering
    ny_nominering = awards.skapa_nominering({
        'utmärkelse_id': 'årets-boende',
        'nominerad_verksamhet_id': 'verksamhet-lugnets-hus',
        'typ': 'verksamhet',
        'motivering': 'Lugnets Hus skapar en verkligt trygg miljö för sina brukare med fokus på individuella behov och utveckling.',
        'nominerad_av': 'test-user-456'
    })
    
    if 'fel' not in ny_nominering:
        print(f"Ny nominering skapad: {ny_nominering['meddelande']}")
    
    # Hämta röstningsresultat
    resultat = awards.hämta_röstningsresultat('årets-boende')
    print(f"Röstningsresultat för Årets Boende:")
    print(f"Totala röster: {resultat['totala_röster']}")
    print(f"Antal nomineringar: {resultat['antal_nomineringar']}")
    
    # Hämta användarens röster
    användares_röster = awards.hämta_användares_röster(användare_id)
    print(f"Användarens röster: {len(användares_röster)}")
    
    # Hämta statistik
    statistik = awards.hämta_awards_statistik()
    print(f"Totala utmärkelser: {statistik['utmärkelser']['totala_utmärkelser']}")
    print(f"Totala nomineringar: {statistik['nomineringar']['totala_nomineringar']}")
    print(f"Totala röster: {statistik['röster']['totala_röster']}")
    
    print("Awards-modulen initialiserad och redo!")
