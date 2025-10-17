# Neuroljus Neurohus Community
# Forum, privata cirklar och gemenskapsbyggande

import logging
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
from dataclasses import dataclass
import uuid
import json

logger = logging.getLogger(__name__)

@dataclass
class ForumKategori:
    """En kategori i forumet"""
    id: str
    namn: str
    beskrivning: str
    ikon: str
    färg: str
    skapad: datetime
    aktiv: bool

@dataclass
class ForumTråd:
    """En tråd i forumet"""
    id: str
    kategori_id: str
    skapare_id: str
    titel: str
    innehåll: str
    stängd: bool
    pinnad: bool
    skapad: datetime
    senast_svar: datetime
    antal_svar: int
    antal_visningar: int
    modererad: bool

@dataclass
class ForumSvar:
    """Ett svar i en forumtråd"""
    id: str
    tråd_id: str
    författare_id: str
    innehåll: str
    modererad: bool
    skapad: datetime
    redigerad: Optional[datetime]

@dataclass
class PrivatCirkel:
    """En privat cirkel för specifika grupper"""
    id: str
    namn: str
    beskrivning: str
    skapare_id: str
    medlemmar: List[str]
    privat: bool
    skapad: datetime
    aktiv: bool

class CommunityManager:
    """Hanterar community-funktionalitet"""
    
    def __init__(self):
        self.forum_kategorier = {}
        self.forum_trådar = {}
        self.forum_svar = {}
        self.privata_cirklar = {}
        self._skapa_standard_kategorier()
    
    def _skapa_standard_kategorier(self):
        """Skapar standardforumkategorier"""
        kategorier = [
            ForumKategori(
                id="allmänt",
                namn="Allmänt",
                beskrivning="Allmänna diskussioner om LSS och neurodiversitet",
                ikon="💬",
                färg="#3B82F6",
                skapad=datetime.now(),
                aktiv=True
            ),
            ForumKategori(
                id="boende",
                namn="Boende",
                beskrivning="Diskussioner om LSS-boenden och boendeformer",
                ikon="🏠",
                färg="#10B981",
                skapad=datetime.now(),
                aktiv=True
            ),
            ForumKategori(
                id="assistans",
                namn="Assistans",
                beskrivning="Frågor och tips om personlig assistans",
                ikon="🤝",
                färg="#F59E0B",
                skapad=datetime.now(),
                aktiv=True
            ),
            ForumKategori(
                id="familj",
                namn="Familj",
                beskrivning="Stöd och råd för familjer",
                ikon="👨‍👩‍👧‍👦",
                färg="#EF4444",
                skapad=datetime.now(),
                aktiv=True
            ),
            ForumKategori(
                id="forskning",
                namn="Forskning",
                beskrivning="Senaste forskning och utveckling",
                ikon="🔬",
                färg="#8B5CF6",
                skapad=datetime.now(),
                aktiv=True
            )
        ]
        
        for kategori in kategorier:
            self.forum_kategorier[kategori.id] = kategori
        
        logger.info(f"Skapade {len(kategorier)} forumkategorier")
    
    def hämta_kategorier(self) -> List[Dict[str, Any]]:
        """Hämtar alla aktiva forumkategorier"""
        return [
            {
                'id': kategori.id,
                'namn': kategori.namn,
                'beskrivning': kategori.beskrivning,
                'ikon': kategori.ikon,
                'färg': kategori.färg,
                'skapad': kategori.skapad.isoformat(),
                'antal_trådar': len([t for t in self.forum_trådar.values() 
                                   if t.kategori_id == kategori.id])
            }
            for kategori in self.forum_kategorier.values() if kategori.aktiv
        ]
    
    def skapa_tråd(self, kategori_id: str, skapare_id: str, 
                   titel: str, innehåll: str) -> Dict[str, Any]:
        """Skapar en ny forumtråd"""
        if kategori_id not in self.forum_kategorier:
            return {'fel': 'Kategori inte hittad'}
        
        tråd_id = str(uuid.uuid4())
        tråd = ForumTråd(
            id=tråd_id,
            kategori_id=kategori_id,
            skapare_id=skapare_id,
            titel=titel,
            innehåll=innehåll,
            stängd=False,
            pinnad=False,
            skapad=datetime.now(),
            senast_svar=datetime.now(),
            antal_svar=0,
            antal_visningar=0,
            modererad=False
        )
        
        self.forum_trådar[tråd_id] = tråd
        
        logger.info(f"Skapade forumtråd: {titel}")
        
        return {
            'meddelande': 'Tråd skapad framgångsrikt',
            'tråd_id': tråd_id,
            'tråd': self._tråd_till_dict(tråd)
        }
    
    def hämta_trådar(self, kategori_id: str = None, 
                    sida: int = 1, per_sida: int = 20) -> Dict[str, Any]:
        """Hämtar forumtrådar med paginering"""
        trådar = list(self.forum_trådar.values())
        
        if kategori_id:
            trådar = [t for t in trådar if t.kategori_id == kategori_id]
        
        # Sortera efter senaste aktivitet
        trådar.sort(key=lambda t: t.senast_svar, reverse=True)
        
        # Paginering
        start_index = (sida - 1) * per_sida
        end_index = start_index + per_sida
        trådar_sida = trådar[start_index:end_index]
        
        return {
            'trådar': [self._tråd_till_dict(tråd) for tråd in trådar_sida],
            'paginering': {
                'sida': sida,
                'per_sida': per_sida,
                'total': len(trådar),
                'antal_sidor': (len(trådar) + per_sida - 1) // per_sida
            }
        }
    
    def hämta_tråd(self, tråd_id: str) -> Optional[Dict[str, Any]]:
        """Hämtar en specifik tråd med svar"""
        if tråd_id not in self.forum_trådar:
            return None
        
        tråd = self.forum_trådar[tråd_id]
        
        # Öka visningsräknare
        tråd.antal_visningar += 1
        
        # Hämta svar
        svar = [s for s in self.forum_svar.values() if s.tråd_id == tråd_id]
        svar.sort(key=lambda s: s.skapad)
        
        return {
            'tråd': self._tråd_till_dict(tråd),
            'svar': [self._svar_till_dict(s) for s in svar]
        }
    
    def skapa_svar(self, tråd_id: str, författare_id: str, 
                   innehåll: str) -> Dict[str, Any]:
        """Skapar ett svar på en tråd"""
        if tråd_id not in self.forum_trådar:
            return {'fel': 'Tråd inte hittad'}
        
        tråd = self.forum_trådar[tråd_id]
        
        if tråd.stängd:
            return {'fel': 'Tråden är stängd för nya svar'}
        
        svar_id = str(uuid.uuid4())
        svar = ForumSvar(
            id=svar_id,
            tråd_id=tråd_id,
            författare_id=författare_id,
            innehåll=innehåll,
            modererad=False,
            skapad=datetime.now(),
            redigerad=None
        )
        
        self.forum_svar[svar_id] = svar
        
        # Uppdatera trådstatistik
        tråd.antal_svar += 1
        tråd.senast_svar = datetime.now()
        
        logger.info(f"Skapade svar på tråd: {tråd.titel}")
        
        return {
            'meddelande': 'Svar skapat framgångsrikt',
            'svar_id': svar_id,
            'svar': self._svar_till_dict(svar)
        }
    
    def skapa_privat_cirkel(self, namn: str, beskrivning: str, 
                           skapare_id: str, medlemmar: List[str]) -> Dict[str, Any]:
        """Skapar en privat cirkel"""
        cirkel_id = str(uuid.uuid4())
        
        # Lägg till skaparen som medlem
        alla_medlemmar = [skapare_id] + medlemmar
        alla_medlemmar = list(set(alla_medlemmar))  # Ta bort dubletter
        
        cirkel = PrivatCirkel(
            id=cirkel_id,
            namn=namn,
            beskrivning=beskrivning,
            skapare_id=skapare_id,
            medlemmar=alla_medlemmar,
            privat=True,
            skapad=datetime.now(),
            aktiv=True
        )
        
        self.privata_cirklar[cirkel_id] = cirkel
        
        logger.info(f"Skapade privat cirkel: {namn}")
        
        return {
            'meddelande': 'Privat cirkel skapad framgångsrikt',
            'cirkel_id': cirkel_id,
            'cirkel': self._cirkel_till_dict(cirkel)
        }
    
    def hämta_användares_cirklar(self, användare_id: str) -> List[Dict[str, Any]]:
        """Hämtar cirklar som användaren är medlem i"""
        användares_cirklar = []
        
        for cirkel in self.privata_cirklar.values():
            if användare_id in cirkel.medlemmar:
                användares_cirklar.append(self._cirkel_till_dict(cirkel))
        
        return användares_cirklar
    
    def lägg_till_medlem_i_cirkel(self, cirkel_id: str, användare_id: str) -> Dict[str, Any]:
        """Lägger till en medlem i en privat cirkel"""
        if cirkel_id not in self.privata_cirklar:
            return {'fel': 'Cirkel inte hittad'}
        
        cirkel = self.privata_cirklar[cirkel_id]
        
        if användare_id in cirkel.medlemmar:
            return {'fel': 'Användaren är redan medlem'}
        
        cirkel.medlemmar.append(användare_id)
        
        logger.info(f"Lade till medlem i cirkel: {cirkel.namn}")
        
        return {
            'meddelande': 'Medlem tillagd framgångsrikt',
            'cirkel': self._cirkel_till_dict(cirkel)
        }
    
    def ta_bort_medlem_från_cirkel(self, cirkel_id: str, användare_id: str) -> Dict[str, Any]:
        """Tar bort en medlem från en privat cirkel"""
        if cirkel_id not in self.privata_cirklar:
            return {'fel': 'Cirkel inte hittad'}
        
        cirkel = self.privata_cirklar[cirkel_id]
        
        if användare_id not in cirkel.medlemmar:
            return {'fel': 'Användaren är inte medlem'}
        
        if användare_id == cirkel.skapare_id:
            return {'fel': 'Skaparen kan inte tas bort från cirkeln'}
        
        cirkel.medlemmar.remove(användare_id)
        
        logger.info(f"Tog bort medlem från cirkel: {cirkel.namn}")
        
        return {
            'meddelande': 'Medlem borttagen framgångsrikt',
            'cirkel': self._cirkel_till_dict(cirkel)
        }
    
    def moderera_innehåll(self, innehåll_id: str, innehåll_typ: str, 
                          moderering: Dict[str, Any]) -> Dict[str, Any]:
        """Modererar forumtrådar och svar"""
        try:
            if innehåll_typ == 'tråd':
                if innehåll_id in self.forum_trådar:
                    tråd = self.forum_trådar[innehåll_id]
                    tråd.modererad = moderering.get('godkänd', False)
                    
                    if moderering.get('stäng'):
                        tråd.stängd = True
                    
                    if moderering.get('pinna'):
                        tråd.pinnad = True
                    
                    return {'meddelande': 'Tråd modererad framgångsrikt'}
            
            elif innehåll_typ == 'svar':
                if innehåll_id in self.forum_svar:
                    svar = self.forum_svar[innehåll_id]
                    svar.modererad = moderering.get('godkänd', False)
                    
                    return {'meddelande': 'Svar modererat framgångsrikt'}
            
            return {'fel': 'Innehåll inte hittat'}
            
        except Exception as e:
            logger.error(f"Fel vid moderering: {e}")
            return {'fel': str(e)}
    
    def hämta_community_statistik(self) -> Dict[str, Any]:
        """Hämtar statistik över community-aktivitet"""
        nu = datetime.now()
        senaste_vecka = nu - timedelta(days=7)
        senaste_månad = nu - timedelta(days=30)
        
        trådar_senaste_vecka = len([t for t in self.forum_trådar.values() 
                                   if t.skapad >= senaste_vecka])
        trådar_senaste_månad = len([t for t in self.forum_trådar.values() 
                                   if t.skapad >= senaste_månad])
        
        svar_senaste_vecka = len([s for s in self.forum_svar.values() 
                                if s.skapad >= senaste_vecka])
        svar_senaste_månad = len([s for s in self.forum_svar.values() 
                                if s.skapad >= senaste_månad])
        
        return {
            'forum': {
                'total_trådar': len(self.forum_trådar),
                'total_svar': len(self.forum_svar),
                'trådar_senaste_vecka': trådar_senaste_vecka,
                'trådar_senaste_månad': trådar_senaste_månad,
                'svar_senaste_vecka': svar_senaste_vecka,
                'svar_senaste_månad': svar_senaste_månad,
                'aktiva_kategorier': len([k for k in self.forum_kategorier.values() if k.aktiv])
            },
            'privata_cirklar': {
                'total_cirklar': len(self.privata_cirklar),
                'aktiva_cirklar': len([c for c in self.privata_cirklar.values() if c.aktiv]),
                'total_medlemmar': sum(len(c.medlemmar) for c in self.privata_cirklar.values())
            },
            'genererat_datum': nu.isoformat()
        }
    
    def _tråd_till_dict(self, tråd: ForumTråd) -> Dict[str, Any]:
        """Konverterar ForumTråd till dictionary"""
        return {
            'id': tråd.id,
            'kategori_id': tråd.kategori_id,
            'skapare_id': tråd.skapare_id,
            'titel': tråd.titel,
            'innehåll': tråd.innehåll,
            'stängd': tråd.stängd,
            'pinnad': tråd.pinnad,
            'skapad': tråd.skapad.isoformat(),
            'senast_svar': tråd.senast_svar.isoformat(),
            'antal_svar': tråd.antal_svar,
            'antal_visningar': tråd.antal_visningar,
            'modererad': tråd.modererad
        }
    
    def _svar_till_dict(self, svar: ForumSvar) -> Dict[str, Any]:
        """Konverterar ForumSvar till dictionary"""
        return {
            'id': svar.id,
            'tråd_id': svar.tråd_id,
            'författare_id': svar.författare_id,
            'innehåll': svar.innehåll,
            'modererad': svar.modererad,
            'skapad': svar.skapad.isoformat(),
            'redigerad': svar.redigerad.isoformat() if svar.redigerad else None
        }
    
    def _cirkel_till_dict(self, cirkel: PrivatCirkel) -> Dict[str, Any]:
        """Konverterar PrivatCirkel till dictionary"""
        return {
            'id': cirkel.id,
            'namn': cirkel.namn,
            'beskrivning': cirkel.beskrivning,
            'skapare_id': cirkel.skapare_id,
            'medlemmar': cirkel.medlemmar,
            'antal_medlemmar': len(cirkel.medlemmar),
            'privat': cirkel.privat,
            'skapad': cirkel.skapad.isoformat(),
            'aktiv': cirkel.aktiv
        }

class CommunityAPI:
    """API för Community-funktionalitet"""
    
    def __init__(self):
        self.community_manager = CommunityManager()
    
    def hämta_forum_översikt(self) -> Dict[str, Any]:
        """Hämtar översikt över forumet"""
        kategorier = self.community_manager.hämta_kategorier()
        statistik = self.community_manager.hämta_community_statistik()
        
        return {
            'kategorier': kategorier,
            'statistik': statistik,
            'senaste_trådar': self._hämta_senaste_trådar(5)
        }
    
    def _hämta_senaste_trådar(self, antal: int) -> List[Dict[str, Any]]:
        """Hämtar de senaste trådarna"""
        trådar = list(self.community_manager.forum_trådar.values())
        trådar.sort(key=lambda t: t.skapad, reverse=True)
        
        return [self.community_manager._tråd_till_dict(t) for t in trådar[:antal]]
    
    def skapa_forumtråd(self, kategori_id: str, skapare_id: str, 
                       titel: str, innehåll: str) -> Dict[str, Any]:
        """Skapar en ny forumtråd"""
        return self.community_manager.skapa_tråd(kategori_id, skapare_id, titel, innehåll)
    
    def hämta_forumtrådar(self, kategori_id: str = None, 
                         sida: int = 1, per_sida: int = 20) -> Dict[str, Any]:
        """Hämtar forumtrådar med paginering"""
        return self.community_manager.hämta_trådar(kategori_id, sida, per_sida)
    
    def hämta_forumtråd(self, tråd_id: str) -> Optional[Dict[str, Any]]:
        """Hämtar en specifik forumtråd med svar"""
        return self.community_manager.hämta_tråd(tråd_id)
    
    def skapa_forumsvar(self, tråd_id: str, författare_id: str, 
                       innehåll: str) -> Dict[str, Any]:
        """Skapar ett svar på en forumtråd"""
        return self.community_manager.skapa_svar(tråd_id, författare_id, innehåll)
    
    def skapa_privat_cirkel(self, namn: str, beskrivning: str, 
                           skapare_id: str, medlemmar: List[str]) -> Dict[str, Any]:
        """Skapar en privat cirkel"""
        return self.community_manager.skapa_privat_cirkel(namn, beskrivning, skapare_id, medlemmar)
    
    def hämta_användares_cirklar(self, användare_id: str) -> List[Dict[str, Any]]:
        """Hämtar cirklar som användaren är medlem i"""
        return self.community_manager.hämta_användares_cirklar(användare_id)
    
    def lägg_till_medlem_i_cirkel(self, cirkel_id: str, användare_id: str) -> Dict[str, Any]:
        """Lägger till en medlem i en privat cirkel"""
        return self.community_manager.lägg_till_medlem_i_cirkel(cirkel_id, användare_id)
    
    def ta_bort_medlem_från_cirkel(self, cirkel_id: str, användare_id: str) -> Dict[str, Any]:
        """Tar bort en medlem från en privat cirkel"""
        return self.community_manager.ta_bort_medlem_från_cirkel(cirkel_id, användare_id)
    
    def moderera_innehåll(self, innehåll_id: str, innehåll_typ: str, 
                          moderering: Dict[str, Any]) -> Dict[str, Any]:
        """Modererar forumtrådar och svar"""
        return self.community_manager.moderera_innehåll(innehåll_id, innehåll_typ, moderering)
    
    def hämta_community_statistik(self) -> Dict[str, Any]:
        """Hämtar statistik över community-aktivitet"""
        return self.community_manager.hämta_community_statistik()

# Exempel på användning
if __name__ == "__main__":
    # Skapa Community API
    community = CommunityAPI()
    
    # Hämta forumöversikt
    översikt = community.hämta_forum_översikt()
    print(f"Forumkategorier: {len(översikt['kategorier'])}")
    
    # Skapa en forumtråd
    användare_id = "test-user-123"
    tråd_resultat = community.skapa_forumtråd(
        "allmänt", 
        användare_id, 
        "Välkommen till Neuroljus Neurohus!",
        "Hej alla! Jag är så glad att vi äntligen har en plattform där vi kan dela erfarenheter och stödja varandra. Låt oss bygga en stark gemenskap tillsammans!"
    )
    
    if 'fel' not in tråd_resultat:
        tråd_id = tråd_resultat['tråd_id']
        print(f"Skapade tråd: {tråd_resultat['tråd']['titel']}")
        
        # Skapa ett svar
        svar_resultat = community.skapa_forumsvar(
            tråd_id,
            "test-user-456",
            "Tack för välkomstmeddelandet! Jag ser fram emot att lära mig mer om empatisk kommunikation."
        )
        
        if 'fel' not in svar_resultat:
            print(f"Skapade svar: {svar_resultat['svar']['innehåll'][:50]}...")
    
    # Skapa en privat cirkel
    cirkel_resultat = community.skapa_privat_cirkel(
        "Familjer i Stockholm",
        "En cirkel för familjer i Stockholm som vill dela erfarenheter om LSS-omsorg",
        användare_id,
        ["test-user-456", "test-user-789"]
    )
    
    if 'fel' not in cirkel_resultat:
        print(f"Skapade privat cirkel: {cirkel_resultat['cirkel']['namn']}")
    
    # Hämta statistik
    statistik = community.hämta_community_statistik()
    print(f"Total trådar: {statistik['forum']['total_trådar']}")
    print(f"Total svar: {statistik['forum']['total_svar']}")
    print(f"Privata cirklar: {statistik['privata_cirklar']['total_cirklar']}")
    
    print("Community-modulen initialiserad och redo!")
