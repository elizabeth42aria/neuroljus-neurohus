# Neuroljus Neurohus Academy
# Utbildning och certifikat för empati och neurodiversitet

import json
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
from dataclasses import dataclass
import uuid

logger = logging.getLogger(__name__)

@dataclass
class KursModul:
    """En modul i en kurs"""
    titel: str
    innehåll: str
    exempel: str
    längd_minuter: int

@dataclass
class QuizFråga:
    """En fråga i kursquiz"""
    fråga: str
    alternativ: List[str]
    rätt_svar: int
    förklaring: str

@dataclass
class Kurs:
    """En komplett kurs"""
    id: str
    titel: str
    beskrivning: str
    kategori: str
    svårighetsgrad: str
    målgrupp: List[str]
    längd_minuter: int
    moduler: List[KursModul]
    quiz_frågor: List[QuizFråga]
    skapad: datetime
    aktiv: bool
    språk: str

class KursManager:
    """Hanterar kurser och kursinnehåll"""
    
    def __init__(self):
        self.kurser = {}
        self._skapa_första_kursen()
    
    def _skapa_första_kursen(self):
        """Skapar första kursen: Kommunikation och lugn kontakt"""
        
        # Kursmoduler
        moduler = [
            KursModul(
                titel="Förstå autism och kommunikation",
                innehåll="Autism påverkar hur personer uppfattar och kommunicerar med världen. Vi går igenom grundläggande förståelse för olika kommunikationsstilar och hur man kan anpassa sin kommunikation för att vara mer inkluderande.",
                exempel="En person med autism kan behöva mer tid att processa information. Ge dem tid att svara innan du upprepar frågan.",
                längd_minuter=8
            ),
            KursModul(
                titel="Lugn och tydlig kommunikation",
                innehåll="Hur man skapar en lugn kommunikationsmiljö med tydliga signaler och förutsägbar struktur. Vi lär oss om vikten av att minska sensorisk överbelastning och skapa trygga kommunikationssituationer.",
                exempel="Använd korta, tydliga meningar. Undvik ironi och metaforer som kan vara förvirrande.",
                längd_minuter=10
            ),
            KursModul(
                titel="Visuell kommunikation",
                innehåll="Bilder, symboler och visuella hjälpmedel kan förbättra förståelsen avsevärt. Vi utforskar olika visuella kommunikationsmetoder och hur de kan användas i vardagen.",
                exempel="Använd bilder för att visa vad som kommer att hända härnäst, som en visuell schema.",
                längd_minuter=9
            ),
            KursModul(
                titel="Lyssna med hela kroppen",
                innehåll="Kommunikation handlar inte bara om ord. Kroppsspråk, ansiktsuttryck och tonfall är lika viktiga. Vi lär oss att läsa och förstå icke-verbal kommunikation.",
                exempel="Märk när en person blir obekväm eller stressad genom att observera deras kroppsspråk.",
                längd_minuter=8
            ),
            KursModul(
                titel="Skapa trygga relationer",
                innehåll="Bygg förtroende genom konsekvent beteende, respekt för gränser och genuin empati. Vi utforskar hur man skapar långsiktiga, meningsfulla relationer.",
                exempel="Respektera när någon behöver en paus eller vill vara ensam. Det är inte en avvisning av dig.",
                längd_minuter=10
            )
        ]
        
        # Quiz-frågor
        quiz_frågor = [
            QuizFråga(
                fråga="Vad är viktigt att komma ihåg när man kommunicerar med en person som har autism?",
                alternativ=[
                    "Använda korta, tydliga meningar",
                    "Prata snabbt för att få svar",
                    "Använda mycket ironi",
                    "Undvika ögonkontakt"
                ],
                rätt_svar=0,
                förklaring="Korta, tydliga meningar hjälper personer med autism att förstå och processa information bättre."
            ),
            QuizFråga(
                fråga="Vilken typ av kommunikation kan vara förvirrande för personer med autism?",
                alternativ=[
                    "Tydliga instruktioner",
                    "Metaforer och ironi",
                    "Visuella hjälpmedel",
                    "Korta meningar"
                ],
                rätt_svar=1,
                förklaring="Metaforer och ironi kan vara svåra att förstå för personer med autism som ofta tar saker bokstavligt."
            ),
            QuizFråga(
                fråga="Vad betyder det att 'lyssna med hela kroppen'?",
                alternativ=[
                    "Bara lyssna på ord",
                    "Observera kroppsspråk och ansiktsuttryck",
                    "Prata högt",
                    "Undvika ögonkontakt"
                ],
                rätt_svar=1,
                förklaring="Kommunikation handlar inte bara om ord - kroppsspråk och ansiktsuttryck ger viktig information."
            ),
            QuizFråga(
                fråga="Hur kan du visa respekt för en persons gränser?",
                alternativ=[
                    "Fortsätta prata även om de verkar obekväma",
                    "Respektera när de behöver en paus",
                    "Ignorera deras kroppsspråk",
                    "Tvinga dem att svara"
                ],
                rätt_svar=1,
                förklaring="Att respektera när någon behöver en paus visar att du förstår och respekterar deras behov."
            ),
            QuizFråga(
                fråga="Vad är viktigt för att skapa trygga relationer?",
                alternativ=[
                    "Konsekvent beteende och respekt",
                    "Varierande rutiner",
                    "Ignorera personens behov",
                    "Bara fokusera på ord"
                ],
                rätt_svar=0,
                förklaring="Konsekvent beteende och respekt för personens behov är grunden för trygga relationer."
            )
        ]
        
        # Skapa kursen
        kurs = Kurs(
            id=str(uuid.uuid4()),
            titel="Kommunikation och lugn kontakt",
            beskrivning="En grundläggande kurs om hur man kommunicerar empatiskt med personer som har autism och neuropsykiatriska funktionsnedsättningar. Kursen fokuserar på praktiska verktyg och metoder för att skapa trygga kommunikationssituationer.",
            kategori="Kommunikation",
            svårighetsgrad="nybörjare",
            målgrupp=["familj", "assistent"],
            längd_minuter=45,
            moduler=moduler,
            quiz_frågor=quiz_frågor,
            skapad=datetime.now(),
            aktiv=True,
            språk="sv"
        )
        
        self.kurser[kurs.id] = kurs
        logger.info(f"Skapade första kursen: {kurs.titel}")
    
    def hämta_kurs(self, kurs_id: str) -> Optional[Kurs]:
        """Hämtar en kurs baserat på ID"""
        return self.kurser.get(kurs_id)
    
    def hämta_alla_kurser(self) -> List[Kurs]:
        """Hämtar alla aktiva kurser"""
        return [kurs for kurs in self.kurser.values() if kurs.aktiv]
    
    def hämta_kurser_för_målgrupp(self, målgrupp: str) -> List[Kurs]:
        """Hämtar kurser för en specifik målgrupp"""
        return [kurs for kurs in self.kurser.values() 
                if kurs.aktiv and målgrupp in kurs.målgrupp]
    
    def skapa_ny_kurs(self, kurs_data: Dict[str, Any]) -> Kurs:
        """Skapar en ny kurs"""
        kurs = Kurs(
            id=str(uuid.uuid4()),
            titel=kurs_data['titel'],
            beskrivning=kurs_data['beskrivning'],
            kategori=kurs_data['kategori'],
            svårighetsgrad=kurs_data['svårighetsgrad'],
            målgrupp=kurs_data['målgrupp'],
            längd_minuter=kurs_data['längd_minuter'],
            moduler=[KursModul(**modul) for modul in kurs_data['moduler']],
            quiz_frågor=[QuizFråga(**fråga) for fråga in kurs_data['quiz_frågor']],
            skapad=datetime.now(),
            aktiv=True,
            språk=kurs_data.get('språk', 'sv')
        )
        
        self.kurser[kurs.id] = kurs
        return kurs

class KursProgress:
    """Hanterar kursframsteg för användare"""
    
    def __init__(self):
        self.progress_data = {}
    
    def påbörja_kurs(self, användare_id: str, kurs_id: str) -> Dict[str, Any]:
        """Påbörjar en kurs för en användare"""
        progress_key = f"{användare_id}_{kurs_id}"
        
        if progress_key not in self.progress_data:
            self.progress_data[progress_key] = {
                'användare_id': användare_id,
                'kurs_id': kurs_id,
                'status': 'påbörjad',
                'progress_procent': 0,
                'quiz_poäng': 0,
                'påbörjad': datetime.now().isoformat(),
                'avslutad': None,
                'certifikat_url': None,
                'moduler_avslutade': [],
                'quiz_svar': []
            }
        
        return self.progress_data[progress_key]
    
    def uppdatera_progress(self, användare_id: str, kurs_id: str, 
                          modul_index: int) -> Dict[str, Any]:
        """Uppdaterar kursframsteg när en modul avslutas"""
        progress_key = f"{användare_id}_{kurs_id}"
        
        if progress_key not in self.progress_data:
            return {'fel': 'Kurs inte påbörjad'}
        
        progress = self.progress_data[progress_key]
        
        if modul_index not in progress['moduler_avslutade']:
            progress['moduler_avslutade'].append(modul_index)
        
        # Beräkna progress procent
        kurs_manager = KursManager()
        kurs = kurs_manager.hämta_kurs(kurs_id)
        
        if kurs:
            progress['progress_procent'] = (len(progress['moduler_avslutade']) / 
                                          len(kurs.moduler)) * 100
            
            if progress['progress_procent'] >= 100:
                progress['status'] = 'klar_för_quiz'
        
        return progress
    
    def genomför_quiz(self, användare_id: str, kurs_id: str, 
                     svar: List[int]) -> Dict[str, Any]:
        """Genomför quiz och beräknar poäng"""
        progress_key = f"{användare_id}_{kurs_id}"
        
        if progress_key not in self.progress_data:
            return {'fel': 'Kurs inte påbörjad'}
        
        progress = self.progress_data[progress_key]
        
        # Hämta kurs för att få rätta svar
        kurs_manager = KursManager()
        kurs = kurs_manager.hämta_kurs(kurs_id)
        
        if not kurs:
            return {'fel': 'Kurs inte hittad'}
        
        # Beräkna poäng
        rätta_svar = 0
        quiz_resultat = []
        
        for i, (användar_svar, fråga) in enumerate(zip(svar, kurs.quiz_frågor)):
            korrekt = användar_svar == fråga.rätt_svar
            if korrekt:
                rätta_svar += 1
            
            quiz_resultat.append({
                'fråga': fråga.fråga,
                'användar_svar': användar_svar,
                'rätt_svar': fråga.rätt_svar,
                'korrekt': korrekt,
                'förklaring': fråga.förklaring
            })
        
        poäng_procent = (rätta_svar / len(kurs.quiz_frågor)) * 100
        
        progress['quiz_poäng'] = poäng_procent
        progress['quiz_svar'] = quiz_resultat
        
        if poäng_procent >= 100:
            progress['status'] = 'avslutad'
            progress['avslutad'] = datetime.now().isoformat()
            # Generera certifikat
            progress['certifikat_url'] = self._generera_certifikat_url(användare_id, kurs_id)
        
        return {
            'poäng_procent': poäng_procent,
            'rätta_svar': rätta_svar,
            'total_frågor': len(kurs.quiz_frågor),
            'quiz_resultat': quiz_resultat,
            'certifikat_tillgängligt': poäng_procent >= 100,
            'certifikat_url': progress.get('certifikat_url')
        }
    
    def _generera_certifikat_url(self, användare_id: str, kurs_id: str) -> str:
        """Genererar URL för certifikat"""
        return f"/academy/certifikat/{användare_id}/{kurs_id}"
    
    def hämta_progress(self, användare_id: str, kurs_id: str) -> Optional[Dict[str, Any]]:
        """Hämtar kursframsteg för en användare"""
        progress_key = f"{användare_id}_{kurs_id}"
        return self.progress_data.get(progress_key)
    
    def hämta_användares_kurser(self, användare_id: str) -> List[Dict[str, Any]]:
        """Hämtar alla kurser för en användare"""
        användares_kurser = []
        
        for progress_key, progress in self.progress_data.items():
            if progress['användare_id'] == användare_id:
                användares_kurser.append(progress)
        
        return användares_kurser

class CertifikatGenerator:
    """Genererar PDF-certifikat för avslutade kurser"""
    
    def __init__(self):
        self.certifikat_mall = self._skapa_certifikat_mall()
    
    def _skapa_certifikat_mall(self) -> Dict[str, Any]:
        """Skapar mall för certifikat"""
        return {
            'rubrik': 'Neuroljus Neurohus Diplom',
            'underrubrik': 'Empati – Kunskap – Neurodiversitet',
            'logotyp_url': '/brand/neuroljus-logo.svg',
            'bakgrundsfärg': '#F0F9FF',
            'textfärg': '#1E40AF',
            'ram_färg': '#3B82F6',
            'signatur_url': '/academy/signatur.png',
            'qr_kod_url': '/academy/qr-kod.png'
        }
    
    def generera_certifikat(self, användare_data: Dict[str, Any], 
                           kurs_data: Dict[str, Any]) -> Dict[str, Any]:
        """Genererar certifikatdata"""
        
        certifikat = {
            'mall': self.certifikat_mall,
            'användare': {
                'namn': f"{användare_data.get('förnamn', '')} {användare_data.get('efternamn', '')}",
                'email': användare_data.get('email', ''),
                'roll': användare_data.get('roll', '')
            },
            'kurs': {
                'titel': kurs_data.get('titel', ''),
                'kategori': kurs_data.get('kategori', ''),
                'längd_minuter': kurs_data.get('längd_minuter', 0),
                'svårighetsgrad': kurs_data.get('svårighetsgrad', '')
            },
            'certifikat': {
                'diplom_text': self._generera_diplom_text(användare_data, kurs_data),
                'datum': datetime.now().strftime('%Y-%m-%d'),
                'certifikat_id': f"NL-{datetime.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:8].upper()}",
                'verifierings_url': f"https://neuroljus.se/verify/{uuid.uuid4().hex}"
            },
            'genererat_datum': datetime.now().isoformat()
        }
        
        return certifikat
    
    def _generera_diplom_text(self, användare_data: Dict[str, Any], 
                              kurs_data: Dict[str, Any]) -> str:
        """Genererar diplomtext"""
        namn = f"{användare_data.get('förnamn', '')} {användare_data.get('efternamn', '')}"
        kurs_titel = kurs_data.get('titel', '')
        
        diplom_text = f"""Det här intygar att {namn}
har genomfört kursen
"{kurs_titel}"
genom Neuroljus Neurohus Academy,
för att stärka förståelse och empati inom autism och omsorg.

Empati – Kunskap – Neurodiversitet
Datum: {datetime.now().strftime('%Y-%m-%d')}
Signerat: Neuroljus Neurohus"""
        
        return diplom_text
    
    def skapa_pdf_certifikat(self, certifikat_data: Dict[str, Any]) -> str:
        """Skapar PDF-certifikat (mockad implementation)"""
        # I verkligheten skulle detta använda ReportLab eller liknande
        # För nu returnerar vi en mockad PDF-URL
        
        certifikat_id = certifikat_data['certifikat']['certifikat_id']
        pdf_url = f"/academy/certifikat/pdf/{certifikat_id}.pdf"
        
        logger.info(f"Skapade PDF-certifikat: {pdf_url}")
        
        return pdf_url

class AcademyAPI:
    """API för Academy-funktionalitet"""
    
    def __init__(self):
        self.kurs_manager = KursManager()
        self.progress_manager = KursProgress()
        self.certifikat_generator = CertifikatGenerator()
    
    def hämta_kurslista(self, målgrupp: str = None) -> List[Dict[str, Any]]:
        """Hämtar lista över kurser"""
        if målgrupp:
            kurser = self.kurs_manager.hämta_kurser_för_målgrupp(målgrupp)
        else:
            kurser = self.kurs_manager.hämta_alla_kurser()
        
        return [
            {
                'id': kurs.id,
                'titel': kurs.titel,
                'beskrivning': kurs.beskrivning,
                'kategori': kurs.kategori,
                'svårighetsgrad': kurs.svårighetsgrad,
                'målgrupp': kurs.målgrupp,
                'längd_minuter': kurs.längd_minuter,
                'antal_moduler': len(kurs.moduler),
                'antal_quiz_frågor': len(kurs.quiz_frågor),
                'skapad': kurs.skapad.isoformat(),
                'språk': kurs.språk
            }
            for kurs in kurser
        ]
    
    def hämta_kursdetaljer(self, kurs_id: str) -> Optional[Dict[str, Any]]:
        """Hämtar detaljerad information om en kurs"""
        kurs = self.kurs_manager.hämta_kurs(kurs_id)
        
        if not kurs:
            return None
        
        return {
            'id': kurs.id,
            'titel': kurs.titel,
            'beskrivning': kurs.beskrivning,
            'kategori': kurs.kategori,
            'svårighetsgrad': kurs.svårighetsgrad,
            'målgrupp': kurs.målgrupp,
            'längd_minuter': kurs.längd_minuter,
            'moduler': [
                {
                    'titel': modul.titel,
                    'innehåll': modul.innehåll,
                    'exempel': modul.exempel,
                    'längd_minuter': modul.längd_minuter
                }
                for modul in kurs.moduler
            ],
            'quiz_frågor': [
                {
                    'fråga': fråga.fråga,
                    'alternativ': fråga.alternativ,
                    'förklaring': fråga.förklaring
                }
                for fråga in kurs.quiz_frågor
            ],
            'skapad': kurs.skapad.isoformat(),
            'språk': kurs.språk
        }
    
    def påbörja_kurs(self, användare_id: str, kurs_id: str) -> Dict[str, Any]:
        """Påbörjar en kurs för en användare"""
        kurs = self.kurs_manager.hämta_kurs(kurs_id)
        
        if not kurs:
            return {'fel': 'Kurs inte hittad'}
        
        if not kurs.aktiv:
            return {'fel': 'Kurs inte tillgänglig'}
        
        progress = self.progress_manager.påbörja_kurs(användare_id, kurs_id)
        
        return {
            'meddelande': 'Kurs påbörjad framgångsrikt',
            'progress': progress,
            'kurs_info': {
                'titel': kurs.titel,
                'antal_moduler': len(kurs.moduler),
                'längd_minuter': kurs.längd_minuter
            }
        }
    
    def avsluta_modul(self, användare_id: str, kurs_id: str, 
                     modul_index: int) -> Dict[str, Any]:
        """Avslutar en modul och uppdaterar progress"""
        progress = self.progress_manager.uppdatera_progress(användare_id, kurs_id, modul_index)
        
        if 'fel' in progress:
            return progress
        
        return {
            'meddelande': 'Modul avslutad framgångsrikt',
            'progress': progress
        }
    
    def genomför_quiz(self, användare_id: str, kurs_id: str, 
                    svar: List[int]) -> Dict[str, Any]:
        """Genomför quiz för en kurs"""
        resultat = self.progress_manager.genomför_quiz(användare_id, kurs_id, svar)
        
        if 'fel' in resultat:
            return resultat
        
        # Om certifikat är tillgängligt, generera det
        if resultat['certifikat_tillgängligt']:
            # Hämta användar- och kursdata för certifikatgenerering
            # Detta skulle normalt hämtas från databasen
            användare_data = {'förnamn': 'Användare', 'efternamn': 'Test'}  # Mockad data
            kurs_data = {'titel': 'Kommunikation och lugn kontakt'}  # Mockad data
            
            certifikat_data = self.certifikat_generator.generera_certifikat(
                användare_data, kurs_data
            )
            
            pdf_url = self.certifikat_generator.skapa_pdf_certifikat(certifikat_data)
            resultat['certifikat_pdf_url'] = pdf_url
        
        return resultat
    
    def hämta_certifikat(self, användare_id: str, kurs_id: str) -> Optional[Dict[str, Any]]:
        """Hämtar certifikat för en avslutad kurs"""
        progress = self.progress_manager.hämta_progress(användare_id, kurs_id)
        
        if not progress or progress['status'] != 'avslutad':
            return None
        
        # Generera certifikatdata
        användare_data = {'förnamn': 'Användare', 'efternamn': 'Test'}  # Mockad data
        kurs_data = {'titel': 'Kommunikation och lugn kontakt'}  # Mockad data
        
        certifikat_data = self.certifikat_generator.generera_certifikat(
            användare_data, kurs_data
        )
        
        return certifikat_data
    
    def hämta_användares_kurser(self, användare_id: str) -> List[Dict[str, Any]]:
        """Hämtar alla kurser för en användare"""
        användares_kurser = self.progress_manager.hämta_användares_kurser(användare_id)
        
        # Anrika med kursinformation
        resultat = []
        for progress in användares_kurser:
            kurs = self.kurs_manager.hämta_kurs(progress['kurs_id'])
            if kurs:
                resultat.append({
                    'kurs': {
                        'id': kurs.id,
                        'titel': kurs.titel,
                        'kategori': kurs.kategori,
                        'längd_minuter': kurs.längd_minuter
                    },
                    'progress': progress
                })
        
        return resultat

# Exempel på användning
if __name__ == "__main__":
    # Skapa Academy API
    academy = AcademyAPI()
    
    # Hämta kurslista
    kurser = academy.hämta_kurslista()
    print(f"Tillgängliga kurser: {len(kurser)}")
    
    if kurser:
        första_kurs = kurser[0]
        print(f"Första kurs: {första_kurs['titel']}")
        
        # Påbörja kurs
        användare_id = "test-user-123"
        kurs_id = första_kurs['id']
        
        resultat = academy.påbörja_kurs(användare_id, kurs_id)
        print(f"Kurs påbörjad: {resultat['meddelande']}")
        
        # Avsluta alla moduler
        for i in range(första_kurs['antal_moduler']):
            academy.avsluta_modul(användare_id, kurs_id, i)
        
        # Genomför quiz med alla rätta svar
        rätta_svar = [0, 1, 1, 1, 0]  # Rätta svar för första kursen
        quiz_resultat = academy.genomför_quiz(användare_id, kurs_id, rätta_svar)
        
        print(f"Quiz-resultat: {quiz_resultat['poäng_procent']:.1f}%")
        print(f"Certifikat tillgängligt: {quiz_resultat['certifikat_tillgängligt']}")
        
        if quiz_resultat['certifikat_tillgängligt']:
            certifikat = academy.hämta_certifikat(användare_id, kurs_id)
            print(f"Certifikat genererat: {certifikat['certifikat']['certifikat_id']}")
    
    print("Academy-modulen initialiserad och redo!")
