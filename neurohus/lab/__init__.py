# Neuroljus Neurohus Lab
# Forskning och öppna data för neurodiversitet

import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
from dataclasses import dataclass
import uuid
import json

logger = logging.getLogger(__name__)

@dataclass
class ForskningPost:
    """En forskningspost"""
    id: str
    titel: str
    författare: List[str]
    universitet: str
    år: int
    doi: str
    abstract: str
    nyckelord: List[str]
    kategori: str
    länk: str
    pdf_url: str
    skapad: datetime
    publicerad: bool
    citeringar: int
    impact_score: float

@dataclass
class Dataset:
    """En dataset för öppna data"""
    id: str
    namn: str
    beskrivning: str
    kategori: str
    storlek: str
    format: str
    källa: str
    licens: str
    skapad: datetime
    uppdaterad: datetime
    nedladdningar: int
    aktiv: bool

class LabManager:
    """Hanterar forskning och öppna data"""
    
    def __init__(self):
        self.forskning_poster = {}
        self.datasets = {}
        self._skapa_exempel_forskning()
        self._skapa_exempel_datasets()
    
    def _skapa_exempel_forskning(self):
        """Skapar exempel på forskningsposter"""
        forskning_poster = [
            ForskningPost(
                id="forskning-1",
                titel="Empatiska algoritmer i välfärdsteknik",
                författare=["Dr. Anna Lindberg", "Prof. Erik Svensson"],
                universitet="Karolinska Institutet",
                år=2023,
                doi="10.1000/empathic-algorithms-2023",
                abstract="Denna studie undersöker hur AI-teknologi kan användas för att förbättra empati och förståelse inom välfärdsteknik, särskilt för personer med neuropsykiatriska funktionsnedsättningar. Vi presenterar en ny metod för att mäta och förbättra empatiska interaktioner mellan människor och AI-system.",
                nyckelord=["AI", "empati", "välfärdsteknik", "autism", "neurodiversitet"],
                kategori="Teknologi",
                länk="https://example.com/empathic-algorithms",
                pdf_url="/lab/pdfs/empathic-algorithms-2023.pdf",
                skapad=datetime.now(),
                publicerad=True,
                citeringar=15,
                impact_score=8.5
            ),
            ForskningPost(
                id="forskning-2",
                titel="Ljus och perception i autismforskning",
                författare=["Dr. Maria Andersson", "Dr. Lars Johansson"],
                universitet="Uppsala Universitet",
                år=2023,
                doi="10.1000/light-perception-autism-2023",
                abstract="Forskning om hur olika ljusmiljöer påverkar personer med autism och hur detta kan användas för att skapa mer inkluderande miljöer. Studien visar att anpassade ljusmiljöer kan förbättra välbefinnande och minska sensorisk överbelastning.",
                nyckelord=["autism", "ljus", "perception", "miljö", "sensorik"],
                kategori="Neurovetenskap",
                länk="https://example.com/light-perception-autism",
                pdf_url="/lab/pdfs/light-perception-autism-2023.pdf",
                skapad=datetime.now(),
                publicerad=True,
                citeringar=8,
                impact_score=7.2
            ),
            ForskningPost(
                id="forskning-3",
                titel="Sociala indikatorer i svensk omsorg",
                författare=["Prof. Sofia Eriksson", "Dr. Peter Nilsson"],
                universitet="Göteborgs Universitet",
                år=2023,
                doi="10.1000/social-indicators-care-2023",
                abstract="En omfattande studie av sociala indikatorer som påverkar kvaliteten i svensk LSS-omsorg och hur dessa kan förbättras. Studien analyserar data från över 1000 verksamheter och identifierar nyckelfaktorer för framgångsrik omsorg.",
                nyckelord=["LSS", "omsorg", "sociala indikatorer", "kvalitet", "Sverige"],
                kategori="Samhällsvetenskap",
                länk="https://example.com/social-indicators-care",
                pdf_url="/lab/pdfs/social-indicators-care-2023.pdf",
                skapad=datetime.now(),
                publicerad=True,
                citeringar=23,
                impact_score=9.1
            )
        ]
        
        for post in forskning_poster:
            self.forskning_poster[post.id] = post
        
        logger.info(f"Skapade {len(forskning_poster)} forskningsposter")
    
    def _skapa_exempel_datasets(self):
        """Skapar exempel på öppna datasets"""
        datasets = [
            Dataset(
                id="dataset-1",
                namn="LSS-verksamheter Sverige 2023",
                beskrivning="Komplett dataset över alla LSS-verksamheter i Sverige med information om typ, kapacitet, kommun och kvalitetsindikatorer.",
                kategori="Verksamhetsdata",
                storlek="2.5 MB",
                format="CSV",
                källa="Socialstyrelsen",
                licens="CC BY 4.0",
                skapad=datetime.now(),
                uppdaterad=datetime.now(),
                nedladdningar=156,
                aktiv=True
            ),
            Dataset(
                id="dataset-2",
                namn="Autismforskning Sverige 2020-2023",
                beskrivning="Sammanställd data från svenska autismforskning med fokus på kommunikation, perception och välbefinnande.",
                kategori="Forskningsdata",
                storlek="8.7 MB",
                format="JSON",
                källa="Vetenskapsrådet",
                licens="CC BY-SA 4.0",
                skapad=datetime.now(),
                uppdaterad=datetime.now(),
                nedladdningar=89,
                aktiv=True
            ),
            Dataset(
                id="dataset-3",
                namn="Kommunindikatorer LSS 2023",
                beskrivning="KOLADA-data för LSS-relaterade indikatorer per kommun inklusive väntetider, kvalitet och tillgänglighet.",
                kategori="Kommunaldata",
                storlek="1.2 MB",
                format="Excel",
                källa="KOLADA",
                licens="CC0",
                skapad=datetime.now(),
                uppdaterad=datetime.now(),
                nedladdningar=234,
                aktiv=True
            )
        ]
        
        for dataset in datasets:
            self.datasets[dataset.id] = dataset
        
        logger.info(f"Skapade {len(datasets)} datasets")
    
    def hämta_forskning_poster(self, kategori: str = None, 
                              sökterm: str = None) -> List[Dict[str, Any]]:
        """Hämtar forskningsposter med filtrering"""
        poster = list(self.forskning_poster.values())
        
        # Filtrera efter kategori
        if kategori:
            poster = [p for p in poster if p.kategori == kategori]
        
        # Filtrera efter sökterm
        if sökterm:
            sökterm_lower = sökterm.lower()
            poster = [p for p in poster 
                     if sökterm_lower in p.titel.lower() or 
                        sökterm_lower in p.abstract.lower() or
                        any(sökterm_lower in nyckelord.lower() for nyckelord in p.nyckelord)]
        
        # Sortera efter impact score
        poster.sort(key=lambda p: p.impact_score, reverse=True)
        
        return [self._forskning_post_till_dict(post) for post in poster]
    
    def hämta_forskning_post(self, post_id: str) -> Optional[Dict[str, Any]]:
        """Hämtar en specifik forskningspost"""
        if post_id not in self.forskning_poster:
            return None
        
        post = self.forskning_poster[post_id]
        return self._forskning_post_till_dict(post)
    
    def skapa_forskning_post(self, post_data: Dict[str, Any]) -> Dict[str, Any]:
        """Skapar en ny forskningspost"""
        post_id = str(uuid.uuid4())
        
        post = ForskningPost(
            id=post_id,
            titel=post_data['titel'],
            författare=post_data['författare'],
            universitet=post_data['universitet'],
            år=post_data['år'],
            doi=post_data.get('doi', ''),
            abstract=post_data['abstract'],
            nyckelord=post_data['nyckelord'],
            kategori=post_data['kategori'],
            länk=post_data.get('länk', ''),
            pdf_url=post_data.get('pdf_url', ''),
            skapad=datetime.now(),
            publicerad=post_data.get('publicerad', True),
            citeringar=post_data.get('citeringar', 0),
            impact_score=post_data.get('impact_score', 0.0)
        )
        
        self.forskning_poster[post_id] = post
        
        logger.info(f"Skapade forskningspost: {post.titel}")
        
        return {
            'meddelande': 'Forskningspost skapad framgångsrikt',
            'post_id': post_id,
            'post': self._forskning_post_till_dict(post)
        }
    
    def hämta_datasets(self, kategori: str = None) -> List[Dict[str, Any]]:
        """Hämtar datasets med filtrering"""
        datasets = [d for d in self.datasets.values() if d.aktiv]
        
        if kategori:
            datasets = [d for d in datasets if d.kategori == kategori]
        
        # Sortera efter nedladdningar
        datasets.sort(key=lambda d: d.nedladdningar, reverse=True)
        
        return [self._dataset_till_dict(dataset) for dataset in datasets]
    
    def hämta_dataset(self, dataset_id: str) -> Optional[Dict[str, Any]]:
        """Hämtar en specifik dataset"""
        if dataset_id not in self.datasets:
            return None
        
        dataset = self.datasets[dataset_id]
        return self._dataset_till_dict(dataset)
    
    def nedladda_dataset(self, dataset_id: str) -> Dict[str, Any]:
        """Registrerar en nedladdning av dataset"""
        if dataset_id not in self.datasets:
            return {'fel': 'Dataset inte hittad'}
        
        dataset = self.datasets[dataset_id]
        dataset.nedladdningar += 1
        
        logger.info(f"Dataset nedladdad: {dataset.namn}")
        
        return {
            'meddelande': 'Dataset nedladdad framgångsrikt',
            'dataset': self._dataset_till_dict(dataset),
            'nedladdnings_url': f"/lab/datasets/{dataset_id}/download"
        }
    
    def skapa_dataset(self, dataset_data: Dict[str, Any]) -> Dict[str, Any]:
        """Skapar en ny dataset"""
        dataset_id = str(uuid.uuid4())
        
        dataset = Dataset(
            id=dataset_id,
            namn=dataset_data['namn'],
            beskrivning=dataset_data['beskrivning'],
            kategori=dataset_data['kategori'],
            storlek=dataset_data['storlek'],
            format=dataset_data['format'],
            källa=dataset_data['källa'],
            licens=dataset_data['licens'],
            skapad=datetime.now(),
            uppdaterad=datetime.now(),
            nedladdningar=0,
            aktiv=True
        )
        
        self.datasets[dataset_id] = dataset
        
        logger.info(f"Skapade dataset: {dataset.namn}")
        
        return {
            'meddelande': 'Dataset skapad framgångsrikt',
            'dataset_id': dataset_id,
            'dataset': self._dataset_till_dict(dataset)
        }
    
    def hämta_lab_statistik(self) -> Dict[str, Any]:
        """Hämtar statistik över lab-aktivitet"""
        total_forskning = len(self.forskning_poster)
        publicerad_forskning = len([p for p in self.forskning_poster.values() if p.publicerad])
        
        total_datasets = len(self.datasets)
        aktiva_datasets = len([d for d in self.datasets.values() if d.aktiv])
        total_nedladdningar = sum(d.nedladdningar for d in self.datasets.values())
        
        # Kategorier
        forskning_kategorier = list(set(p.kategori for p in self.forskning_poster.values()))
        dataset_kategorier = list(set(d.kategori for d in self.datasets.values()))
        
        return {
            'forskning': {
                'total_poster': total_forskning,
                'publicerade_poster': publicerad_forskning,
                'kategorier': forskning_kategorier,
                'genomsnittlig_impact_score': sum(p.impact_score for p in self.forskning_poster.values()) / total_forskning if total_forskning > 0 else 0
            },
            'datasets': {
                'total_datasets': total_datasets,
                'aktiva_datasets': aktiva_datasets,
                'total_nedladdningar': total_nedladdningar,
                'kategorier': dataset_kategorier
            },
            'genererat_datum': datetime.now().isoformat()
        }
    
    def sök_forskning(self, sökterm: str) -> Dict[str, Any]:
        """Söker i forskningsposter"""
        poster = self.hämta_forskning_poster(sökterm=sökterm)
        
        # Gruppera efter kategori
        kategorier = {}
        for post in poster:
            kategori = post['kategori']
            if kategori not in kategorier:
                kategorier[kategori] = []
            kategorier[kategori].append(post)
        
        return {
            'sökterm': sökterm,
            'antal_träffar': len(poster),
            'kategorier': kategorier,
            'alla_poster': poster
        }
    
    def _forskning_post_till_dict(self, post: ForskningPost) -> Dict[str, Any]:
        """Konverterar ForskningPost till dictionary"""
        return {
            'id': post.id,
            'titel': post.titel,
            'författare': post.författare,
            'universitet': post.universitet,
            'år': post.år,
            'doi': post.doi,
            'abstract': post.abstract,
            'nyckelord': post.nyckelord,
            'kategori': post.kategori,
            'länk': post.länk,
            'pdf_url': post.pdf_url,
            'skapad': post.skapad.isoformat(),
            'publicerad': post.publicerad,
            'citeringar': post.citeringar,
            'impact_score': post.impact_score
        }
    
    def _dataset_till_dict(self, dataset: Dataset) -> Dict[str, Any]:
        """Konverterar Dataset till dictionary"""
        return {
            'id': dataset.id,
            'namn': dataset.namn,
            'beskrivning': dataset.beskrivning,
            'kategori': dataset.kategori,
            'storlek': dataset.storlek,
            'format': dataset.format,
            'källa': dataset.källa,
            'licens': dataset.licens,
            'skapad': dataset.skapad.isoformat(),
            'uppdaterad': dataset.uppdaterad.isoformat(),
            'nedladdningar': dataset.nedladdningar,
            'aktiv': dataset.aktiv
        }

class LabAPI:
    """API för Lab-funktionalitet"""
    
    def __init__(self):
        self.lab_manager = LabManager()
    
    def hämta_lab_översikt(self) -> Dict[str, Any]:
        """Hämtar översikt över lab-avdelningen"""
        statistik = self.lab_manager.hämta_lab_statistik()
        senaste_forskning = self._hämta_senaste_forskning(3)
        populära_datasets = self._hämta_populära_datasets(3)
        
        return {
            'statistik': statistik,
            'senaste_forskning': senaste_forskning,
            'populära_datasets': populära_datasets,
            'kategorier': {
                'forskning': statistik['forskning']['kategorier'],
                'datasets': statistik['datasets']['kategorier']
            }
        }
    
    def _hämta_senaste_forskning(self, antal: int) -> List[Dict[str, Any]]:
        """Hämtar de senaste forskningsposterna"""
        poster = list(self.lab_manager.forskning_poster.values())
        poster.sort(key=lambda p: p.skapad, reverse=True)
        
        return [self.lab_manager._forskning_post_till_dict(p) for p in poster[:antal]]
    
    def _hämta_populära_datasets(self, antal: int) -> List[Dict[str, Any]]:
        """Hämtar de mest nedladdade datasets"""
        datasets = [d for d in self.lab_manager.datasets.values() if d.aktiv]
        datasets.sort(key=lambda d: d.nedladdningar, reverse=True)
        
        return [self.lab_manager._dataset_till_dict(d) for d in datasets[:antal]]
    
    def hämta_forskning_poster(self, kategori: str = None, 
                              sökterm: str = None) -> List[Dict[str, Any]]:
        """Hämtar forskningsposter med filtrering"""
        return self.lab_manager.hämta_forskning_poster(kategori, sökterm)
    
    def hämta_forskning_post(self, post_id: str) -> Optional[Dict[str, Any]]:
        """Hämtar en specifik forskningspost"""
        return self.lab_manager.hämta_forskning_post(post_id)
    
    def skapa_forskning_post(self, post_data: Dict[str, Any]) -> Dict[str, Any]:
        """Skapar en ny forskningspost"""
        return self.lab_manager.skapa_forskning_post(post_data)
    
    def hämta_datasets(self, kategori: str = None) -> List[Dict[str, Any]]:
        """Hämtar datasets med filtrering"""
        return self.lab_manager.hämta_datasets(kategori)
    
    def hämta_dataset(self, dataset_id: str) -> Optional[Dict[str, Any]]:
        """Hämtar en specifik dataset"""
        return self.lab_manager.hämta_dataset(dataset_id)
    
    def nedladda_dataset(self, dataset_id: str) -> Dict[str, Any]:
        """Registrerar en nedladdning av dataset"""
        return self.lab_manager.nedladda_dataset(dataset_id)
    
    def skapa_dataset(self, dataset_data: Dict[str, Any]) -> Dict[str, Any]:
        """Skapar en ny dataset"""
        return self.lab_manager.skapa_dataset(dataset_data)
    
    def sök_forskning(self, sökterm: str) -> Dict[str, Any]:
        """Söker i forskningsposter"""
        return self.lab_manager.sök_forskning(sökterm)
    
    def hämta_lab_statistik(self) -> Dict[str, Any]:
        """Hämtar statistik över lab-aktivitet"""
        return self.lab_manager.hämta_lab_statistik()

# Exempel på användning
if __name__ == "__main__":
    # Skapa Lab API
    lab = LabAPI()
    
    # Hämta laböversikt
    översikt = lab.hämta_lab_översikt()
    print(f"Forskningsposter: {översikt['statistik']['forskning']['total_poster']}")
    print(f"Datasets: {översikt['statistik']['datasets']['total_datasets']}")
    
    # Hämta forskningsposter
    forskning_poster = lab.hämta_forskning_poster()
    print(f"Tillgängliga forskningsposter: {len(forskning_poster)}")
    
    if forskning_poster:
        första_post = forskning_poster[0]
        print(f"Första post: {första_post['titel']}")
        print(f"Impact score: {första_post['impact_score']}")
    
    # Sök forskning
    sökresultat = lab.sök_forskning("empati")
    print(f"Sökresultat för 'empati': {sökresultat['antal_träffar']} träffar")
    
    # Hämta datasets
    datasets = lab.hämta_datasets()
    print(f"Tillgängliga datasets: {len(datasets)}")
    
    if datasets:
        första_dataset = datasets[0]
        print(f"Första dataset: {första_dataset['namn']}")
        print(f"Nedladdningar: {första_dataset['nedladdningar']}")
        
        # Nedladda dataset
        nedladdning = lab.nedladda_dataset(första_dataset['id'])
        print(f"Nedladdning: {nedladdning['meddelande']}")
    
    # Hämta statistik
    statistik = lab.hämta_lab_statistik()
    print(f"Total nedladdningar: {statistik['datasets']['total_nedladdningar']}")
    print(f"Genomsnittlig impact score: {statistik['forskning']['genomsnittlig_impact_score']:.1f}")
    
    print("Lab-modulen initialiserad och redo!")
