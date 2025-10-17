# Neuroljus Neurohus
## Sveriges första digitala hus för empati, kunskap och neurodiversitet

### 🏗️ Projektstruktur

```
neurohus/
├── frontend/          # Next.js 14 + TypeScript + Tailwind (sv/en)
├── backend/           # FastAPI + SQLAlchemy + Pydantic
├── database/          # PostgreSQL schema och migrations
├── ingestion/         # Datahämtning från externa källor
├── ai/                # AI-moduler för empati och analys
├── community/         # Forum och privata cirklar
├── academy/           # Utbildning och certifikat
├── lab/               # Forskning och öppna data
├── awards/            # Nomineringar och erkännande
├── docs/              # Processguider och dokumentation
└── README.md          # Huvuddokumentation
```

### 🎯 Målsättning
Skapa en nationell plattform där familjer, assistenter, kommuner och forskare möts i transparens, utbildning och innovation.

### 🤖 AI-etik
Neuroljus Neurohus använder AI för att stödja mänsklig empati, inte ersätta den. All data hanteras med respekt för individers integritet och svensk GDPR-lagstiftning.

### 🚀 Snabbstart
```bash
# Installera dependencies
npm install
pip install -r requirements.txt

# Starta utvecklingsmiljö
npm run dev          # Frontend
python -m uvicorn backend.main:app --reload  # Backend
```

### 📊 Datakällor
- LSSGuiden (LSS-boenden)
- KOLADA (kommunindikatorer)
- IVO (inspektioner)
- Assistanskoll (recensioner)

### 🔒 Säkerhet
Alla API-nycklar och känslig data hanteras enligt svensk GDPR och säkerhetsbestämmelser.