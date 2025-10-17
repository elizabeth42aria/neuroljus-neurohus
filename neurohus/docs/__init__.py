# Neuroljus Neurohus Docs
# Processguider för LSS-ansökan, överklagan och rättigheter

import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
from dataclasses import dataclass
import uuid
import json

logger = logging.getLogger(__name__)

@dataclass
class ProcessGuide:
    """En processguide"""
    id: str
    titel: str
    beskrivning: str
    kategori: str
    språk: str
    steg: List[Dict[str, Any]]
    skapad: datetime
    uppdaterad: datetime
    aktiv: bool
    målgrupp: List[str]

class DocsManager:
    """Hanterar processguider och dokumentation"""
    
    def __init__(self):
        self.processguider = {}
        self._skapa_standard_guider()
    
    def _skapa_standard_guider(self):
        """Skapar standardprocessguider"""
        nu = datetime.now()
        
        guider = [
            ProcessGuide(
                id="lss-ansökan-sv",
                titel="Hur ansöker man om LSS?",
                beskrivning="En steg-för-steg guide för att ansöka om LSS-insatser. Inkluderar vilka dokument som behövs, var man ansöker och vad som händer efter ansökan.",
                kategori="Ansökan",
                språk="sv",
                steg=[
                    {
                        "steg": 1,
                        "rubrik": "Förberedelser",
                        "beskrivning": "Innan du ansöker om LSS-insatser",
                        "innehåll": [
                            "Samla in medicinska intyg och utredningar som visar ditt behov av stöd",
                            "Kontakta din kommuns LSS-handläggare för information om processen",
                            "Förbered dokumentation om din nuvarande situation och behov",
                            "Överväg vilka typer av insatser som skulle passa dig bäst"
                        ],
                        "dokument": [
                            "Medicinska intyg",
                            "Utredningar från BUP, habilitering eller liknande",
                            "Dokumentation av nuvarande behov",
                            "Personlig assistansbedömning (om relevant)"
                        ],
                        "tips": [
                            "Börja samla dokumentation i god tid",
                            "Kontakta tidigt med din kommun för rådgivning",
                            "Be om hjälp från familj eller stödpersoner"
                        ]
                    },
                    {
                        "steg": 2,
                        "rubrik": "Ansökan",
                        "beskrivning": "Så här gör du ansökan",
                        "innehåll": [
                            "Fyll i LSS-ansökan (formulär från din kommun)",
                            "Bifoga alla nödvändiga dokument",
                            "Beskriv ditt behov av stöd tydligt och konkret",
                            "Skicka in ansökan till din kommun"
                        ],
                        "dokument": [
                            "LSS-ansökan (kommunens formulär)",
                            "Medicinska intyg",
                            "Utredningar",
                            "Personlig assistansbedömning"
                        ],
                        "tips": [
                            "Var konkret när du beskriver dina behov",
                            "Inkludera alla relevanta dokument",
                            "Be om kvitto på att ansökan mottagits"
                        ]
                    },
                    {
                        "steg": 3,
                        "rubrik": "Handläggning",
                        "beskrivning": "Vad händer efter ansökan",
                        "innehåll": [
                            "Kommunen handlägger din ansökan",
                            "Du kan bli kallad till samtal eller möten",
                            "Kommunen fattar beslut om insatser",
                            "Du får ett skriftligt beslut"
                        ],
                        "dokument": [
                            "Beslut från kommunen",
                            "Information om insatser",
                            "Kontaktuppgifter till handläggare"
                        ],
                        "tips": [
                            "Håll kontakt med din handläggare",
                            "Ställ frågor om du inte förstår något",
                            "Be om skriftlig information"
                        ]
                    },
                    {
                        "steg": 4,
                        "rubrik": "Efter beslut",
                        "beskrivning": "När du fått beslut",
                        "innehåll": [
                            "Läs igenom beslutet noggrant",
                            "Kontakta kommunen om du har frågor",
                            "Börja planera implementeringen av insatser",
                            "Överväg överklagan om du inte är nöjd"
                        ],
                        "dokument": [
                            "Beslut från kommunen",
                            "Plan för insatser",
                            "Kontaktuppgifter"
                        ],
                        "tips": [
                            "Spara alla dokument på en säker plats",
                            "Kontakta kommunen direkt om frågor",
                            "Överväg stöd från familj eller organisationer"
                        ]
                    }
                ],
                skapad=nu,
                uppdaterad=nu,
                aktiv=True,
                målgrupp=["familj", "brukare"]
            ),
            ProcessGuide(
                id="lss-överklagan-sv",
                titel="Hur överklagar man ett LSS-beslut?",
                beskrivning="Guide för att överklaga ett LSS-beslut som du inte är nöjd med. Inkluderar tidsfrister, process och vad som händer vid överklagan.",
                kategori="Överklagan",
                språk="sv",
                steg=[
                    {
                        "steg": 1,
                        "rubrik": "Förstå beslutet",
                        "beskrivning": "Analysera beslutet innan du överklagar",
                        "innehåll": [
                            "Läs igenom beslutet noggrant",
                            "Förstå vad kommunen har beslutat",
                            "Identifiera vilka delar du vill överklaga",
                            "Kontrollera tidsfrister för överklagan"
                        ],
                        "dokument": [
                            "Beslut från kommunen",
                            "LSS-lagen (för referens)",
                            "Kommunens rutiner för överklagan"
                        ],
                        "tips": [
                            "Sök juridisk rådgivning om du är osäker",
                            "Kontakta LSS-handläggaren för förtydliganden",
                            "Samla in ytterligare dokumentation om behovet"
                        ]
                    },
                    {
                        "steg": 2,
                        "rubrik": "Förbered överklagan",
                        "beskrivning": "Så här förbereder du överklagan",
                        "innehåll": [
                            "Samla in ytterligare dokumentation",
                            "Skriv en tydlig motivering till överklagan",
                            "Kontakta eventuella stödpersoner eller organisationer",
                            "Förbered alla nödvändiga dokument"
                        ],
                        "dokument": [
                            "Ytterligare medicinska intyg",
                            "Nya utredningar",
                            "Motivering till överklagan",
                            "Stödbrev från familj eller organisationer"
                        ],
                        "tips": [
                            "Var konkret i din motivering",
                            "Inkludera alla relevanta dokument",
                            "Sök stöd från organisationer som Riksförbundet för Utvecklingsstörda"
                        ]
                    },
                    {
                        "steg": 3,
                        "rubrik": "Skicka överklagan",
                        "beskrivning": "Så här skickar du överklagan",
                        "innehåll": [
                            "Fyll i överklagansformulär",
                            "Bifoga alla dokument",
                            "Skicka till rätt myndighet inom tidsfrist",
                            "Be om kvitto på att överklagan mottagits"
                        ],
                        "dokument": [
                            "Överklagansformulär",
                            "Motivering",
                            "Alla relevanta dokument",
                            "Kvitto på mottagande"
                        ],
                        "tips": [
                            "Respektera tidsfrister (oftast 3 veckor)",
                            "Skicka med rekommenderat brev",
                            "Be om kvitto på mottagande"
                        ]
                    },
                    {
                        "steg": 4,
                        "rubrik": "Handläggning av överklagan",
                        "beskrivning": "Vad händer efter överklagan",
                        "innehåll": [
                            "Myndigheten handlägger överklagan",
                            "Du kan bli kallad till samtal eller möten",
                            "Myndigheten fattar nytt beslut",
                            "Du får skriftligt beslut"
                        ],
                        "dokument": [
                            "Nytt beslut från myndigheten",
                            "Motivering till beslutet",
                            "Information om vidare överklagan"
                        ],
                        "tips": [
                            "Håll kontakt med handläggaren",
                            "Ställ frågor om processen",
                            "Överväg vidare överklagan om nödvändigt"
                        ]
                    }
                ],
                skapad=nu,
                uppdaterad=nu,
                aktiv=True,
                målgrupp=["familj", "brukare"]
            ),
            ProcessGuide(
                id="familjens-rättigheter-sv",
                titel="Familjens rättigheter i LSS-systemet",
                beskrivning="En guide som förklarar familjens rättigheter och möjligheter inom LSS-systemet. Inkluderar information om stöd, rådgivning och delaktighet.",
                kategori="Rättigheter",
                språk="sv",
                steg=[
                    {
                        "steg": 1,
                        "rubrik": "Rätt till information",
                        "beskrivning": "Familjens rätt till information",
                        "innehåll": [
                            "Rätt till tydlig information om LSS-insatser",
                            "Rätt till förklaring av beslut",
                            "Rätt till information om överklagan",
                            "Rätt till regelbunden uppdatering"
                        ],
                        "dokument": [
                            "Information om LSS-insatser",
                            "Beslut från kommunen",
                            "Rutiner för information",
                            "Kontaktuppgifter"
                        ],
                        "tips": [
                            "Be om skriftlig information",
                            "Ställ frågor om du inte förstår",
                            "Kräv tydliga förklaringar"
                        ]
                    },
                    {
                        "steg": 2,
                        "rubrik": "Rätt till delaktighet",
                        "beskrivning": "Familjens rätt till delaktighet",
                        "innehåll": [
                            "Rätt att delta i planering av insatser",
                            "Rätt att ge sin åsikt om insatser",
                            "Rätt att vara med vid utvärdering",
                            "Rätt till regelbunden kontakt"
                        ],
                        "dokument": [
                            "Plan för insatser",
                            "Utvärderingsrapporter",
                            "Mötesprotokoll",
                            "Kontaktuppgifter"
                        ],
                        "tips": [
                            "Kräv att vara med vid möten",
                            "Ge din åsikt om insatser",
                            "Be om regelbunden kontakt"
                        ]
                    },
                    {
                        "steg": 3,
                        "rubrik": "Rätt till stöd",
                        "beskrivning": "Familjens rätt till stöd",
                        "innehåll": [
                            "Rätt till rådgivning och stöd",
                            "Rätt till information om stödorganisationer",
                            "Rätt till ekonomiskt stöd vid behov",
                            "Rätt till respitvård"
                        ],
                        "dokument": [
                            "Information om stödorganisationer",
                            "Rådgivning från kommunen",
                            "Information om ekonomiskt stöd",
                            "Plan för respitvård"
                        ],
                        "tips": [
                            "Sök rådgivning från kommunen",
                            "Kontakta stödorganisationer",
                            "Be om information om ekonomiskt stöd"
                        ]
                    },
                    {
                        "steg": 4,
                        "rubrik": "Rätt till överklagan",
                        "beskrivning": "Familjens rätt till överklagan",
                        "innehåll": [
                            "Rätt att överklaga beslut",
                            "Rätt till juridisk rådgivning",
                            "Rätt till stöd vid överklagan",
                            "Rätt till information om processen"
                        ],
                        "dokument": [
                            "Information om överklagan",
                            "Juridisk rådgivning",
                            "Stöd från organisationer",
                            "Processinformation"
                        ],
                        "tips": [
                            "Sök juridisk rådgivning",
                            "Kontakta stödorganisationer",
                            "Följ tidsfrister noggrant"
                        ]
                    }
                ],
                skapad=nu,
                uppdaterad=nu,
                aktiv=True,
                målgrupp=["familj"]
            )
        ]
        
        for guide in guider:
            self.processguider[guide.id] = guide
        
        logger.info(f"Skapade {len(guider)} processguider")
    
    def hämta_guider(self, kategori: str = None, språk: str = "sv") -> List[Dict[str, Any]]:
        """Hämtar processguider med filtrering"""
        guider = [g for g in self.processguider.values() if g.aktiv and g.språk == språk]
        
        if kategori:
            guider = [g for g in guider if g.kategori == kategori]
        
        return [self._guide_till_dict(guide) for guide in guider]
    
    def hämta_guide(self, guide_id: str) -> Optional[Dict[str, Any]]:
        """Hämtar en specifik processguide"""
        if guide_id not in self.processguider:
            return None
        
        guide = self.processguider[guide_id]
        return self._guide_till_dict(guide)
    
    def skapa_guide(self, guide_data: Dict[str, Any]) -> Dict[str, Any]:
        """Skapar en ny processguide"""
        guide_id = str(uuid.uuid4())
        
        guide = ProcessGuide(
            id=guide_id,
            titel=guide_data['titel'],
            beskrivning=guide_data['beskrivning'],
            kategori=guide_data['kategori'],
            språk=guide_data.get('språk', 'sv'),
            steg=guide_data['steg'],
            skapad=datetime.now(),
            uppdaterad=datetime.now(),
            aktiv=True,
            målgrupp=guide_data.get('målgrupp', [])
        )
        
        self.processguider[guide_id] = guide
        
        logger.info(f"Skapade processguide: {guide.titel}")
        
        return {
            'meddelande': 'Processguide skapad framgångsrikt',
            'guide_id': guide_id,
            'guide': self._guide_till_dict(guide)
        }
    
    def uppdatera_guide(self, guide_id: str, guide_data: Dict[str, Any]) -> Dict[str, Any]:
        """Uppdaterar en befintlig processguide"""
        if guide_id not in self.processguider:
            return {'fel': 'Processguide inte hittad'}
        
        guide = self.processguider[guide_id]
        
        # Uppdatera fält
        if 'titel' in guide_data:
            guide.titel = guide_data['titel']
        if 'beskrivning' in guide_data:
            guide.beskrivning = guide_data['beskrivning']
        if 'kategori' in guide_data:
            guide.kategori = guide_data['kategori']
        if 'steg' in guide_data:
            guide.steg = guide_data['steg']
        if 'målgrupp' in guide_data:
            guide.målgrupp = guide_data['målgrupp']
        
        guide.uppdaterad = datetime.now()
        
        logger.info(f"Uppdaterade processguide: {guide.titel}")
        
        return {
            'meddelande': 'Processguide uppdaterad framgångsrikt',
            'guide': self._guide_till_dict(guide)
        }
    
    def hämta_guide_kategorier(self) -> List[str]:
        """Hämtar alla kategorier av processguider"""
        kategorier = list(set(g.kategori for g in self.processguider.values() if g.aktiv))
        return sorted(kategorier)
    
    def sök_guider(self, sökterm: str, språk: str = "sv") -> List[Dict[str, Any]]:
        """Söker i processguider"""
        sökterm_lower = sökterm.lower()
        guider = [g for g in self.processguider.values() 
                 if g.aktiv and g.språk == språk]
        
        träffar = []
        for guide in guider:
            # Sök i titel, beskrivning och steg
            if (sökterm_lower in guide.titel.lower() or 
                sökterm_lower in guide.beskrivning.lower() or
                any(sökterm_lower in steg.get('rubrik', '').lower() or 
                    sökterm_lower in steg.get('beskrivning', '').lower()
                    for steg in guide.steg)):
                träffar.append(self._guide_till_dict(guide))
        
        return träffar
    
    def hämta_docs_statistik(self) -> Dict[str, Any]:
        """Hämtar statistik över dokumentation"""
        totala_guider = len(self.processguider)
        aktiva_guider = len([g for g in self.processguider.values() if g.aktiv])
        
        # Gruppera efter kategori
        kategorier = {}
        for guide in self.processguider.values():
            if guide.aktiv:
                if guide.kategori not in kategorier:
                    kategorier[guide.kategori] = 0
                kategorier[guide.kategori] += 1
        
        # Gruppera efter språk
        språk = {}
        for guide in self.processguider.values():
            if guide.aktiv:
                if guide.språk not in språk:
                    språk[guide.språk] = 0
                språk[guide.språk] += 1
        
        return {
            'guider': {
                'totala_guider': totala_guider,
                'aktiva_guider': aktiva_guider
            },
            'kategorier': kategorier,
            'språk': språk,
            'genererat_datum': datetime.now().isoformat()
        }
    
    def _guide_till_dict(self, guide: ProcessGuide) -> Dict[str, Any]:
        """Konverterar ProcessGuide till dictionary"""
        return {
            'id': guide.id,
            'titel': guide.titel,
            'beskrivning': guide.beskrivning,
            'kategori': guide.kategori,
            'språk': guide.språk,
            'steg': guide.steg,
            'skapad': guide.skapad.isoformat(),
            'uppdaterad': guide.uppdaterad.isoformat(),
            'aktiv': guide.aktiv,
            'målgrupp': guide.målgrupp,
            'antal_steg': len(guide.steg)
        }

class DocsAPI:
    """API för Docs-funktionalitet"""
    
    def __init__(self):
        self.docs_manager = DocsManager()
    
    def hämta_docs_översikt(self) -> Dict[str, Any]:
        """Hämtar översikt över dokumentation"""
        kategorier = self.docs_manager.hämta_guide_kategorier()
        statistik = self.docs_manager.hämta_docs_statistik()
        
        return {
            'kategorier': kategorier,
            'statistik': statistik,
            'populära_guider': self._hämta_populära_guider(3)
        }
    
    def _hämta_populära_guider(self, antal: int) -> List[Dict[str, Any]]:
        """Hämtar populära processguider"""
        guider = [g for g in self.docs_manager.processguider.values() if g.aktiv]
        # Sortera efter uppdateringsdatum (senaste först)
        guider.sort(key=lambda g: g.uppdaterad, reverse=True)
        
        return [self.docs_manager._guide_till_dict(g) for g in guider[:antal]]
    
    def hämta_guider(self, kategori: str = None, språk: str = "sv") -> List[Dict[str, Any]]:
        """Hämtar processguider med filtrering"""
        return self.docs_manager.hämta_guider(kategori, språk)
    
    def hämta_guide(self, guide_id: str) -> Optional[Dict[str, Any]]:
        """Hämtar en specifik processguide"""
        return self.docs_manager.hämta_guide(guide_id)
    
    def skapa_guide(self, guide_data: Dict[str, Any]) -> Dict[str, Any]:
        """Skapar en ny processguide"""
        return self.docs_manager.skapa_guide(guide_data)
    
    def uppdatera_guide(self, guide_id: str, guide_data: Dict[str, Any]) -> Dict[str, Any]:
        """Uppdaterar en befintlig processguide"""
        return self.docs_manager.uppdatera_guide(guide_id, guide_data)
    
    def hämta_guide_kategorier(self) -> List[str]:
        """Hämtar alla kategorier av processguider"""
        return self.docs_manager.hämta_guide_kategorier()
    
    def sök_guider(self, sökterm: str, språk: str = "sv") -> List[Dict[str, Any]]:
        """Söker i processguider"""
        return self.docs_manager.sök_guider(sökterm, språk)
    
    def hämta_docs_statistik(self) -> Dict[str, Any]:
        """Hämtar statistik över dokumentation"""
        return self.docs_manager.hämta_docs_statistik()

# Exempel på användning
if __name__ == "__main__":
    # Skapa Docs API
    docs = DocsAPI()
    
    # Hämta docsöversikt
    översikt = docs.hämta_docs_översikt()
    print(f"Kategorier: {len(översikt['kategorier'])}")
    print(f"Aktiva guider: {översikt['statistik']['guider']['aktiva_guider']}")
    
    # Hämta guider
    guider = docs.hämta_guider()
    print(f"Tillgängliga guider: {len(guider)}")
    
    if guider:
        första_guide = guider[0]
        print(f"Första guide: {första_guide['titel']}")
        print(f"Antal steg: {första_guide['antal_steg']}")
        
        # Hämta detaljerad guide
        guide_detaljer = docs.hämta_guide(första_guide['id'])
        if guide_detaljer:
            print(f"Första steget: {guide_detaljer['steg'][0]['rubrik']}")
    
    # Sök guider
    sökresultat = docs.sök_guider("LSS")
    print(f"Sökresultat för 'LSS': {len(sökresultat)} träffar")
    
    # Hämta kategorier
    kategorier = docs.hämta_guide_kategorier()
    print(f"Tillgängliga kategorier: {', '.join(kategorier)}")
    
    # Skapa ny guide
    ny_guide = docs.skapa_guide({
        'titel': 'Guide för personlig assistans',
        'beskrivning': 'En guide för att ansöka om personlig assistans',
        'kategori': 'Ansökan',
        'språk': 'sv',
        'steg': [
            {
                'steg': 1,
                'rubrik': 'Förberedelser',
                'beskrivning': 'Förberedelser inför ansökan',
                'innehåll': ['Samla dokumentation', 'Kontakta kommunen'],
                'dokument': ['Medicinska intyg'],
                'tips': ['Börja i god tid']
            }
        ],
        'målgrupp': ['brukare', 'familj']
    })
    
    if 'fel' not in ny_guide:
        print(f"Ny guide skapad: {ny_guide['meddelande']}")
    
    # Hämta statistik
    statistik = docs.hämta_docs_statistik()
    print(f"Totala guider: {statistik['guider']['totala_guider']}")
    print(f"Aktiva guider: {statistik['guider']['aktiva_guider']}")
    
    print("Docs-modulen initialiserad och redo!")
