# Certifikatgenerator för Neuroljus Neurohus Academy
# Genererar PDF-certifikat med ReportLab

import logging
from typing import Dict, Any
from datetime import datetime
import uuid
import os
from io import BytesIO

# Mockad ReportLab implementation
# I verkligheten skulle detta använda: from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter, A4
# from reportlab.lib.units import inch
# from reportlab.lib.colors import Color

logger = logging.getLogger(__name__)

class CertifikatGenerator:
    """Genererar PDF-certifikat för avslutade kurser"""
    
    def __init__(self):
        self.certifikat_mall = self._skapa_certifikat_mall()
        self.output_dir = "/tmp/certifikat"  # I verkligheten: "/app/certifikat"
        
        # Skapa output-katalog om den inte finns
        os.makedirs(self.output_dir, exist_ok=True)
    
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
            'qr_kod_url': '/academy/qr-kod.png',
            'font_storlek_rubrik': 24,
            'font_storlek_text': 14,
            'font_storlek_signatur': 12
        }
    
    def generera_certifikat(self, användare_data: Dict[str, Any], 
                           kurs_data: Dict[str, Any]) -> Dict[str, Any]:
        """Genererar certifikatdata"""
        
        certifikat_id = f"NL-{datetime.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:8].upper()}"
        
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
                'certifikat_id': certifikat_id,
                'verifierings_url': f"https://neuroljus.se/verify/{certifikat_id}",
                'qr_kod_data': f"https://neuroljus.se/verify/{certifikat_id}"
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
        """Skapar PDF-certifikat med ReportLab"""
        try:
            certifikat_id = certifikat_data['certifikat']['certifikat_id']
            pdf_filename = f"{certifikat_id}.pdf"
            pdf_path = os.path.join(self.output_dir, pdf_filename)
            
            # Mockad PDF-generering
            # I verkligheten skulle detta använda ReportLab:
            """
            c = canvas.Canvas(pdf_path, pagesize=A4)
            width, height = A4
            
            # Bakgrundsfärg
            c.setFillColor(Color(0.94, 0.97, 1.0))  # #F0F9FF
            c.rect(0, 0, width, height, fill=True, stroke=False)
            
            # Ram
            c.setStrokeColor(Color(0.23, 0.51, 0.96))  # #3B82F6
            c.setLineWidth(3)
            c.rect(50, 50, width-100, height-100, fill=False, stroke=True)
            
            # Rubrik
            c.setFillColor(Color(0.12, 0.25, 0.69))  # #1E40AF
            c.setFont("Helvetica-Bold", 24)
            c.drawCentredText(width/2, height-150, "Neuroljus Neurohus Diplom")
            
            # Underrubrik
            c.setFont("Helvetica", 16)
            c.drawCentredText(width/2, height-200, "Empati – Kunskap – Neurodiversitet")
            
            # Diplomtext
            c.setFont("Helvetica", 14)
            diplom_text = certifikat_data['certifikat']['diplom_text']
            lines = diplom_text.split('\n')
            
            y_position = height - 300
            for line in lines:
                c.drawCentredText(width/2, y_position, line)
                y_position -= 25
            
            # Signatur
            c.setFont("Helvetica", 12)
            c.drawCentredText(width/2, 200, "Signerat: Neuroljus Neurohus")
            
            # QR-kod (mockad)
            c.setFont("Helvetica", 10)
            c.drawCentredText(width/2, 150, f"Verifiera: {certifikat_data['certifikat']['verifierings_url']}")
            
            c.save()
            """
            
            # Mockad implementation - skapa en textfil istället
            with open(pdf_path.replace('.pdf', '.txt'), 'w', encoding='utf-8') as f:
                f.write("NEUROLJUS NEUROHUS DIPLOM\n")
                f.write("Empati – Kunskap – Neurodiversitet\n\n")
                f.write(certifikat_data['certifikat']['diplom_text'])
                f.write(f"\n\nVerifiera: {certifikat_data['certifikat']['verifierings_url']}")
            
            logger.info(f"Skapade certifikat: {pdf_path}")
            
            # Returnera URL för nedladdning
            return f"/academy/certifikat/pdf/{pdf_filename}"
            
        except Exception as e:
            logger.error(f"Fel vid skapande av PDF-certifikat: {e}")
            return None
    
    def verifiera_certifikat(self, certifikat_id: str) -> Dict[str, Any]:
        """Verifierar ett certifikat baserat på ID"""
        try:
            # I verkligheten skulle detta söka i databasen
            # För nu returnerar vi mockad verifiering
            
            if certifikat_id.startswith('NL-'):
                return {
                    'giltigt': True,
                    'certifikat_id': certifikat_id,
                    'användare': 'Användare Test',
                    'kurs': 'Kommunikation och lugn kontakt',
                    'datum': datetime.now().strftime('%Y-%m-%d'),
                    'verifierat_datum': datetime.now().isoformat()
                }
            else:
                return {
                    'giltigt': False,
                    'fel': 'Ogiltigt certifikat-ID'
                }
                
        except Exception as e:
            logger.error(f"Fel vid verifiering av certifikat: {e}")
            return {
                'giltigt': False,
                'fel': str(e)
            }
    
    def hämta_certifikat_statistik(self) -> Dict[str, Any]:
        """Hämtar statistik över genererade certifikat"""
        try:
            # Räkna filer i output-katalog
            certifikat_filer = [f for f in os.listdir(self.output_dir) if f.endswith('.txt')]
            
            return {
                'total_certifikat': len(certifikat_filer),
                'certifikat_denna_månad': len([f for f in certifikat_filer 
                                             if datetime.now().strftime('%Y%m') in f]),
                'certifikat_denna_vecka': len([f for f in certifikat_filer 
                                             if datetime.now().strftime('%Y%m%d') in f]),
                'senaste_certifikat': max(certifikat_filer) if certifikat_filer else None
            }
            
        except Exception as e:
            logger.error(f"Fel vid hämtning av certifikatstatistik: {e}")
            return {'fel': str(e)}
    
    def skapa_certifikat_mall(self, mall_data: Dict[str, Any]) -> Dict[str, Any]:
        """Skapar en anpassad certifikatmall"""
        try:
            mall_id = f"mall-{uuid.uuid4().hex[:8]}"
            
            anpassad_mall = {
                'mall_id': mall_id,
                'rubrik': mall_data.get('rubrik', 'Neuroljus Neurohus Diplom'),
                'underrubrik': mall_data.get('underrubrik', 'Empati – Kunskap – Neurodiversitet'),
                'bakgrundsfärg': mall_data.get('bakgrundsfärg', '#F0F9FF'),
                'textfärg': mall_data.get('textfärg', '#1E40AF'),
                'ram_färg': mall_data.get('ram_färg', '#3B82F6'),
                'font_storlek_rubrik': mall_data.get('font_storlek_rubrik', 24),
                'font_storlek_text': mall_data.get('font_storlek_text', 14),
                'logotyp_url': mall_data.get('logotyp_url', '/brand/neuroljus-logo.svg'),
                'signatur_text': mall_data.get('signatur_text', 'Signerat: Neuroljus Neurohus'),
                'skapad': datetime.now().isoformat(),
                'aktiv': True
            }
            
            logger.info(f"Skapade anpassad certifikatmall: {mall_id}")
            return anpassad_mall
            
        except Exception as e:
            logger.error(f"Fel vid skapande av certifikatmall: {e}")
            return {'fel': str(e)}

# Exempel på användning
if __name__ == "__main__":
    # Skapa certifikatgenerator
    generator = CertifikatGenerator()
    
    # Mockad användar- och kursdata
    användare_data = {
        'förnamn': 'Anna',
        'efternamn': 'Larsson',
        'email': 'anna.larsson@email.se',
        'roll': 'familj'
    }
    
    kurs_data = {
        'titel': 'Kommunikation och lugn kontakt',
        'kategori': 'Kommunikation',
        'längd_minuter': 45,
        'svårighetsgrad': 'nybörjare'
    }
    
    # Generera certifikat
    certifikat_data = generator.generera_certifikat(användare_data, kurs_data)
    print(f"Certifikat genererat: {certifikat_data['certifikat']['certifikat_id']}")
    
    # Skapa PDF
    pdf_url = generator.skapa_pdf_certifikat(certifikat_data)
    print(f"PDF skapad: {pdf_url}")
    
    # Verifiera certifikat
    verifiering = generator.verifiera_certifikat(certifikat_data['certifikat']['certifikat_id'])
    print(f"Certifikat giltigt: {verifiering['giltigt']}")
    
    # Hämta statistik
    statistik = generator.hämta_certifikat_statistik()
    print(f"Total certifikat: {statistik['total_certifikat']}")
    
    print("Certifikatgenerator initialiserad och redo!")
