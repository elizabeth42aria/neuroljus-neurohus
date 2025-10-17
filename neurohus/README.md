# Neuroljus Neurohus
## Sveriges första digitala hus för empati, kunskap och neurodiversitet

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Next.js 14](https://img.shields.io/badge/Next.js-14-black.svg)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)

### 🧠 Vår Vision

Neuroljus Neurohus är Sveriges första digitala plattform som kombinerar AI-teknologi med mänsklig empati för att skapa en bättre framtid för personer med neuropsykiatriska funktionsnedsättningar. Vi skapar en nationell plattform där familjer, assistenter, kommuner och forskare möts i transparens, utbildning och innovation.

### 🎯 Målsättning

- **Empati först**: AI-teknologi som stödjer mänsklig empati, inte ersätter den
- **Transparens**: Öppenhet och tillgänglighet i LSS-systemet
- **Kunskap**: Utbildning och forskning för bättre förståelse
- **Gemenskap**: Säker plats för erfarenhetsutbyte och stöd
- **Innovation**: Kontinuerlig utveckling baserat på användarfeedback

### 🏗️ Systemarkitektur

```
neurohus/
├── frontend/          # Next.js 14 + TypeScript + Tailwind CSS
├── backend/           # FastAPI + SQLAlchemy + Pydantic
├── database/          # PostgreSQL schema och migrations
├── ingestion/         # Datahämtning från externa källor
├── ai/                # AI-moduler för empati och analys
├── community/         # Forum och privata cirklar
├── academy/           # Utbildning och certifikat
├── lab/               # Forskning och öppna data
├── awards/            # Nomineringar och erkännande
├── docs/              # Processguider och dokumentation
└── README.md          # Denna fil
```

### 🚀 Snabbstart

#### Förutsättningar

- Node.js 18+ och npm
- Python 3.9+ och pip
- PostgreSQL 13+
- Git

#### Installation

1. **Klona repository**
   ```bash
   git clone https://github.com/neuroljus/neurohus.git
   cd neurohus
   ```

2. **Backend setup**
   ```bash
   cd backend
   pip install -r requirements.txt
   python -m uvicorn main:app --reload --port 8000
   ```

3. **Frontend setup**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

4. **Databas setup**
   ```bash
   # Skapa PostgreSQL-databas
   createdb neurohus
   
   # Kör schema
   psql neurohus < database/schema.sql
   ```

5. **Öppna applikationen**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Dokumentation: http://localhost:8000/api/docs

### 📊 Datakällor

Vi integrerar data från flera svenska myndigheter och organisationer:

- **LSSGuiden**: LSS-boenden och verksamheter
- **KOLADA**: Kommunala indikatorer och statistik
- **IVO**: Inspektioner och kvalitetsbedömningar
- **Assistanskoll**: Brukarrecensioner och erfarenheter

*Notera: För produktionsmiljö krävs API-nycklar från respektive källa.*

### 🤖 AI-moduler

#### Empatisk Rekommendation
- Matchar användare med verksamheter baserat på empati och behov
- Analyserar recensioner för empatiska nyckelord
- Beräknar kommunspecifik matchning

#### Intelligent Moderering
- Språkgranskning med fokus på empati och respekt
- Automatisk borttagning av persondata
- Rollspecifik moderering (familj, assistent, kommun)

#### Trendanalys
- Analyserar trender per kommun och kategori
- Sentimentanalys av recensioner och diskussioner
- Genererar AI-insikter för dashboard

#### Dashboard Insights
- Automatiska rekommendationer baserat på data
- Identifierar varningar och möjligheter
- Genererar månadsrapporter

### 🎓 Academy

#### Kommunikation och lugn kontakt
Vår första kurs fokuserar på empatisk kommunikation:

- **5 moduler**: Grundläggande förståelse för autism och kommunikation
- **Interaktivt quiz**: 5 frågor med förklaringar
- **Certifikat**: Automatisk PDF-generering vid 100% resultat
- **Målgrupp**: Familjer och assistenter

#### Certifikatgenerator
- ReportLab-baserad PDF-generering
- QR-kod för verifiering
- Anpassningsbara mallar
- GDPR-kompatibel hantering

### 👥 Community

#### Forum
- **Kategorier**: Allmänt, Boende, Assistans, Familj, Forskning
- **AI-moderering**: Automatisk granskning av innehåll
- **Röstsystem**: Bedömning av trygghet, kommunikation, delaktighet

#### Privata cirklar
- Säker plats för specifika grupper
- Familjer, assistenter, forskare
- Modererad miljö med AI-stöd

### 🔬 Lab

#### Forskning
- **Empatiska algoritmer i välfärdsteknik**: AI för empati
- **Ljus och perception i autismforskning**: Miljöfaktorer
- **Sociala indikatorer i svensk omsorg**: Kvalitetsmätning

#### Öppna data
- LSS-verksamheter Sverige 2023
- Autismforskning Sverige 2020-2023
- Kommunindikatorer LSS 2023

### 🏆 Awards

#### Utmärkelser
- **Årets Boende**: Baserat på brukarrecensioner
- **Årets Assistent**: Exceptionell empati och professionalism
- **Brukarens Röst**: Direkt röstning från brukare och familjer

#### Nomineringsprocess
- Transparent röstningssystem
- AI-validering av nomineringar
- Automatisk resultatberäkning

### 📚 Processguider

#### LSS-ansökan
- Steg-för-steg guide för ansökan
- Dokumentation och tips
- Tidsfrister och processer

#### Överklagan
- Guide för att överklaga beslut
- Juridisk rådgivning
- Tidsfrister och procedurer

#### Familjens rättigheter
- Rätt till information och delaktighet
- Stöd och rådgivning
- Överklagan och rättsskydd

### 🔒 Säkerhet och Integritet

#### GDPR-kompatibilitet
- All data hanteras enligt svensk GDPR-lagstiftning
- Användare har full kontroll över sina data
- Automatisk borttagning av persondata

#### AI-etik
- Transparent AI-beslutsfattande
- Mänsklig övervakning av AI-system
- Kontinuerlig etisk granskning

#### Säkerhetsåtgärder
- Krypterad datalagring
- Säker API-autentisering
- Regelbunden säkerhetsgranskning

### 🛠️ Teknisk Stack

#### Frontend
- **Next.js 14**: React-framework med App Router
- **TypeScript**: Typad JavaScript för bättre utvecklarupplevelse
- **Tailwind CSS**: Utility-first CSS-framework
- **Framer Motion**: Animationer och övergångar
- **React Hook Form**: Formulärhantering
- **SWR**: Datahämtning och caching

#### Backend
- **FastAPI**: Modern Python web-framework
- **SQLAlchemy**: ORM för databashantering
- **Pydantic**: Datavalidering och serialisering
- **PostgreSQL**: Relationsdatabas
- **Redis**: Caching och sessionshantering

#### AI/ML
- **scikit-learn**: Machine learning-bibliotek
- **spaCy**: Natural Language Processing
- **Transformers**: Hugging Face transformer-modeller
- **ReportLab**: PDF-generering

#### DevOps
- **Docker**: Containerisering
- **GitHub Actions**: CI/CD
- **PostgreSQL**: Produktionsdatabas
- **Nginx**: Reverse proxy och load balancer

### 📈 Prestanda och Skalbarhet

#### Caching-strategi
- Redis för API-caching
- Next.js Image Optimization
- CDN för statiska resurser

#### Databasoptimering
- Indexering för snabba sökningar
- Connection pooling
- Read replicas för skrivskyddad data

#### Monitoring
- Application Performance Monitoring (APM)
- Error tracking och logging
- Uptime monitoring

### 🧪 Testing

#### Frontend Testing
```bash
cd frontend
npm run test          # Unit tests
npm run test:e2e      # End-to-end tests
npm run test:coverage # Coverage report
```

#### Backend Testing
```bash
cd backend
pytest                # Unit tests
pytest --cov         # Coverage report
pytest --benchmark   # Performance tests
```

### 📦 Deployment

#### Docker
```bash
# Bygg och kör med Docker Compose
docker-compose up -d
```

#### Produktionsmiljö
```bash
# Backend
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker

# Frontend
npm run build
npm start
```

### 🤝 Bidrag

Vi välkomnar bidrag från utvecklare, forskare och användare!

#### Bidragsprocess
1. Fork repository
2. Skapa feature branch (`git checkout -b feature/amazing-feature`)
3. Commit ändringar (`git commit -m 'Add amazing feature'`)
4. Push till branch (`git push origin feature/amazing-feature`)
5. Öppna Pull Request

#### Bidragsriktlinjer
- Följ kodstandarder (Black för Python, Prettier för TypeScript)
- Skriv tester för nya funktioner
- Uppdatera dokumentation vid behov
- Respektera GDPR och integritetsregler

### 📞 Support

#### Teknisk support
- **Email**: tech@neuroljus.se
- **GitHub Issues**: [neuroljus/neurohus/issues](https://github.com/neuroljus/neurohus/issues)
- **Discord**: [Neuroljus Community](https://discord.gg/neuroljus)

#### Användarsupport
- **Email**: support@neuroljus.se
- **Telefon**: 08-123 456 78
- **Forum**: [Community Support](https://neuroljus.se/community/support)

### 📄 Licens

Detta projekt är licensierat under MIT-licensen - se [LICENSE](LICENSE) filen för detaljer.

### 🙏 Erkännanden

- **Karolinska Institutet**: Forskning och utveckling
- **Uppsala Universitet**: Neurovetenskaplig forskning
- **Göteborgs Universitet**: Samhällsvetenskaplig forskning
- **Riksförbundet för Utvecklingsstörda**: Användarfeedback
- **LSS-handläggare**: Processguider och rådgivning

### 🔮 Framtida utveckling

#### Planerade funktioner
- **Mobilapp**: iOS och Android
- **AI-chatbot**: Empatisk support
- **Video-kurser**: Interaktiv utbildning
- **API för tredjepart**: Integration med andra system
- **Blockchain**: Verifiering av certifikat

#### Forskningssamarbeten
- **KI**: Empatiska algoritmer
- **UU**: Perception och miljö
- **GU**: Sociala indikatorer
- **Internationella**: Jämförande studier

### 📊 Statistik

- **150+** verksamheter registrerade
- **2,500+** aktiva användare
- **890+** recensioner
- **25+** kurser tillgängliga
- **15+** forskningsposter
- **3** aktiva utmärkelser

### 🌍 Internationell expansion

#### Planerade marknader
- **Norge**: LSS-liknande system
- **Danmark**: Social omsorg
- **Finland**: Funktionshinderstöd
- **EU**: Gemensamma standarder

---

**Neuroljus Neurohus** - *Empati • Kunskap • Neurodiversitet*

*"AI för att stödja mänsklig empati, inte ersätta den."*

---

### 📚 Ytterligare resurser

- [API Dokumentation](http://localhost:8000/api/docs)
- [Design System](https://neuroljus.se/design-system)
- [Utvecklarguide](https://neuroljus.se/dev-guide)
- [Användarhandbok](https://neuroljus.se/user-guide)
- [Forskningspublikationer](https://neuroljus.se/research)
- [Community Guidelines](https://neuroljus.se/community/guidelines)

### 🔗 Externa länkar

- [LSS-lagen](https://www.riksdagen.se/sv/dokument-lagar/dokument/svensk-forfattningssamling/lag-1993387-om-stod-och-service-till-vissa_sfs-1993-387)
- [Socialstyrelsen](https://www.socialstyrelsen.se/)
- [KOLADA](https://www.kolada.se/)
- [IVO](https://www.ivo.se/)
- [Riksförbundet för Utvecklingsstörda](https://www.funktionshinder.se/)

---

*Senast uppdaterad: 2023-12-01*
*Version: 1.0.0*
*Status: Aktiv utveckling*
