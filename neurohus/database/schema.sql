-- Neuroljus Neurohus Database Schema
-- PostgreSQL Database för Sveriges första digitala hus för empati, kunskap och neurodiversitet

-- Skapa databas
CREATE DATABASE neurohus;

-- Använd databasen
\c neurohus;

-- Skapa extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "postgis";

-- ==============================================
-- ANVÄNDARE OCH AUTENTISERING
-- ==============================================

CREATE TABLE användare (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    lösenord_hash VARCHAR(255) NOT NULL,
    förnamn VARCHAR(100) NOT NULL,
    efternamn VARCHAR(100) NOT NULL,
    telefon VARCHAR(20),
    roll VARCHAR(50) NOT NULL CHECK (roll IN ('familj', 'assistent', 'kommun', 'forskare', 'admin')),
    kommun VARCHAR(100),
    skapad TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    senast_aktiv TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    verifierad BOOLEAN DEFAULT FALSE,
    profil_bild_url TEXT,
    bio TEXT,
    preferenser JSONB DEFAULT '{}'::jsonb
);

-- ==============================================
-- VERKSAMHETER (LSS-BOENDEN)
-- ==============================================

CREATE TABLE verksamheter (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    namn VARCHAR(255) NOT NULL,
    typ VARCHAR(100) NOT NULL CHECK (typ IN ('gruppboende', 'familjehem', 'särskilt boende', 'dagverksamhet')),
    adress TEXT NOT NULL,
    postnummer VARCHAR(10) NOT NULL,
    ort VARCHAR(100) NOT NULL,
    kommun VARCHAR(100) NOT NULL,
    län VARCHAR(100) NOT NULL,
    telefon VARCHAR(20),
    email VARCHAR(255),
    hemsida TEXT,
    beskrivning TEXT,
    kapacitet INTEGER,
    åldersgrupp VARCHAR(100),
    diagnoser TEXT[], -- Array av diagnoser som stöds
    tjänster TEXT[], -- Array av tjänster som erbjuds
    koordinater POINT, -- PostGIS punkt för kartvisning
    bild_url TEXT,
    skapad TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    uppdaterad TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    aktiv BOOLEAN DEFAULT TRUE
);

-- ==============================================
-- ASSISTANSFÖRETAG
-- ==============================================

CREATE TABLE assistansföretag (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    namn VARCHAR(255) NOT NULL,
    organisationsnummer VARCHAR(20) UNIQUE NOT NULL,
    adress TEXT NOT NULL,
    postnummer VARCHAR(10) NOT NULL,
    ort VARCHAR(100) NOT NULL,
    telefon VARCHAR(20),
    email VARCHAR(255),
    hemsida TEXT,
    beskrivning TEXT,
    specialiseringar TEXT[],
    verksamhetsområden TEXT[],
    skapad TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    aktiv BOOLEAN DEFAULT TRUE
);

-- ==============================================
-- RECENSIONER OCH BEDÖMNINGAR
-- ==============================================

CREATE TABLE recensioner (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    användare_id UUID REFERENCES användare(id) ON DELETE CASCADE,
    verksamhet_id UUID REFERENCES verksamheter(id) ON DELETE CASCADE,
    assistansföretag_id UUID REFERENCES assistansföretag(id) ON DELETE CASCADE,
    typ VARCHAR(50) NOT NULL CHECK (typ IN ('verksamhet', 'assistansföretag')),
    betyg INTEGER NOT NULL CHECK (betyg >= 1 AND betyg <= 5),
    rubrik VARCHAR(255) NOT NULL,
    innehåll TEXT NOT NULL,
    trygghet INTEGER CHECK (trygghet >= 1 AND trygghet <= 5),
    kommunikation INTEGER CHECK (kommunikation >= 1 AND kommunikation <= 5),
    delaktighet INTEGER CHECK (delaktighet >= 1 AND delaktighet <= 5),
    anonym BOOLEAN DEFAULT TRUE,
    skapad TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modererad BOOLEAN DEFAULT FALSE,
    godkänd BOOLEAN DEFAULT FALSE
);

-- ==============================================
-- KOMMUNINDIKATORER (KOLADA DATA)
-- ==============================================

CREATE TABLE kommunindikatorer (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    kommun VARCHAR(100) NOT NULL,
    län VARCHAR(100) NOT NULL,
    kategori VARCHAR(100) NOT NULL,
    indikator VARCHAR(255) NOT NULL,
    värde DECIMAL(10,2),
    enhet VARCHAR(50),
    år INTEGER NOT NULL,
    källa VARCHAR(100) DEFAULT 'KOLADA',
    skapad TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(kommun, indikator, år)
);

-- ==============================================
-- AKADEMI - KURSER OCH UTBILDNING
-- ==============================================

CREATE TABLE kurser (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    titel VARCHAR(255) NOT NULL,
    beskrivning TEXT NOT NULL,
    kategori VARCHAR(100) NOT NULL,
    svårighetsgrad VARCHAR(50) CHECK (svårighetsgrad IN ('nybörjare', 'medel', 'avancerad')),
    målgrupp TEXT[] NOT NULL, -- Array av målgrupper
    längd_minuter INTEGER NOT NULL,
    moduler JSONB NOT NULL, -- JSON med kursmoduler
    quiz_frågor JSONB NOT NULL, -- JSON med quiz-frågor
    skapad TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    aktiv BOOLEAN DEFAULT TRUE,
    språk VARCHAR(10) DEFAULT 'sv'
);

CREATE TABLE kurs_progress (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    användare_id UUID REFERENCES användare(id) ON DELETE CASCADE,
    kurs_id UUID REFERENCES kurser(id) ON DELETE CASCADE,
    status VARCHAR(50) DEFAULT 'påbörjad' CHECK (status IN ('påbörjad', 'pågående', 'avslutad')),
    progress_procent INTEGER DEFAULT 0 CHECK (progress_procent >= 0 AND progress_procent <= 100),
    quiz_poäng INTEGER DEFAULT 0,
    påbörjad TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    avslutad TIMESTAMP,
    certifikat_url TEXT,
    UNIQUE(användare_id, kurs_id)
);

-- ==============================================
-- FORSKNING OCH LAB
-- ==============================================

CREATE TABLE forskning (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    titel VARCHAR(500) NOT NULL,
    författare TEXT[] NOT NULL,
    universitet VARCHAR(255),
    år INTEGER NOT NULL,
    doi VARCHAR(255),
    abstract TEXT,
    nyckelord TEXT[],
    kategori VARCHAR(100),
    länk TEXT,
    pdf_url TEXT,
    skapad TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    publicerad BOOLEAN DEFAULT TRUE
);

-- ==============================================
-- AWARDS OCH NOMINERINGAR
-- ==============================================

CREATE TABLE utmärkelser (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    namn VARCHAR(255) NOT NULL,
    beskrivning TEXT NOT NULL,
    kategori VARCHAR(100) NOT NULL,
    år INTEGER NOT NULL,
    aktiv BOOLEAN DEFAULT TRUE,
    skapad TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE nomineringar (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    utmärkelse_id UUID REFERENCES utmärkelser(id) ON DELETE CASCADE,
    nominerad_verksamhet_id UUID REFERENCES verksamheter(id) ON DELETE CASCADE,
    nominerad_assistans_id UUID REFERENCES assistansföretag(id) ON DELETE CASCADE,
    nominerad_användare_id UUID REFERENCES användare(id) ON DELETE CASCADE,
    typ VARCHAR(50) NOT NULL CHECK (typ IN ('verksamhet', 'assistansföretag', 'person')),
    motivering TEXT NOT NULL,
    nominerad_av UUID REFERENCES användare(id) ON DELETE CASCADE,
    skapad TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50) DEFAULT 'aktiv' CHECK (status IN ('aktiv', 'vinnare', 'nominerad'))
);

CREATE TABLE röster (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    nominering_id UUID REFERENCES nomineringar(id) ON DELETE CASCADE,
    användare_id UUID REFERENCES användare(id) ON DELETE CASCADE,
    skapad TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(nominering_id, användare_id)
);

-- ==============================================
-- COMMUNITY - FORUM OCH CIRKLAR
-- ==============================================

CREATE TABLE forum_kategorier (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    namn VARCHAR(255) NOT NULL,
    beskrivning TEXT,
    ikon VARCHAR(100),
    färg VARCHAR(20),
    skapad TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE forum_trådar (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    kategori_id UUID REFERENCES forum_kategorier(id) ON DELETE CASCADE,
    skapare_id UUID REFERENCES användare(id) ON DELETE CASCADE,
    titel VARCHAR(255) NOT NULL,
    innehåll TEXT NOT NULL,
    stängd BOOLEAN DEFAULT FALSE,
    pinnad BOOLEAN DEFAULT FALSE,
    skapad TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    senast_svar TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    antal_svar INTEGER DEFAULT 0
);

CREATE TABLE forum_svar (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tråd_id UUID REFERENCES forum_trådar(id) ON DELETE CASCADE,
    författare_id UUID REFERENCES användare(id) ON DELETE CASCADE,
    innehåll TEXT NOT NULL,
    modererad BOOLEAN DEFAULT FALSE,
    skapad TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE privata_cirklar (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    namn VARCHAR(255) NOT NULL,
    beskrivning TEXT,
    skapare_id UUID REFERENCES användare(id) ON DELETE CASCADE,
    medlemmar UUID[] DEFAULT '{}', -- Array av användar-ID:n
    privat BOOLEAN DEFAULT TRUE,
    skapad TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==============================================
-- AUDIT LOGGAR
-- ==============================================

CREATE TABLE audit_loggar (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    användare_id UUID REFERENCES användare(id) ON DELETE SET NULL,
    action VARCHAR(100) NOT NULL,
    tabell VARCHAR(100) NOT NULL,
    post_id UUID,
    gamla_värden JSONB,
    nya_värden JSONB,
    ip_adress INET,
    user_agent TEXT,
    skapad TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==============================================
-- INDEX FÖR PRESTANDA
-- ==============================================

CREATE INDEX idx_verksamheter_kommun ON verksamheter(kommun);
CREATE INDEX idx_verksamheter_typ ON verksamheter(typ);
CREATE INDEX idx_recensioner_verksamhet ON recensioner(verksamhet_id);
CREATE INDEX idx_recensioner_användare ON recensioner(användare_id);
CREATE INDEX idx_kurs_progress_användare ON kurs_progress(användare_id);
CREATE INDEX idx_forum_trådar_kategori ON forum_trådar(kategori_id);
CREATE INDEX idx_audit_loggar_användare ON audit_loggar(användare_id);
CREATE INDEX idx_audit_loggar_skapad ON audit_loggar(skapad);

-- ==============================================
-- INSERTS - REALISTISK DATA
-- ==============================================

-- Användare
INSERT INTO användare (email, lösenord_hash, förnamn, efternamn, telefon, roll, kommun) VALUES
('anna.larsson@email.se', '$2b$12$hash1', 'Anna', 'Larsson', '070-1234567', 'familj', 'Stockholm'),
('erik.johansson@email.se', '$2b$12$hash2', 'Erik', 'Johansson', '070-2345678', 'assistent', 'Göteborg'),
('maria.svensson@email.se', '$2b$12$hash3', 'Maria', 'Svensson', '070-3456789', 'kommun', 'Malmö'),
('lars.andersson@email.se', '$2b$12$hash4', 'Lars', 'Andersson', '070-4567890', 'forskare', 'Uppsala'),
('admin@neuroljus.se', '$2b$12$adminhash', 'Admin', 'Neuroljus', '070-0000000', 'admin', 'Stockholm');

-- Verksamheter (LSS-boenden)
INSERT INTO verksamheter (namn, typ, adress, postnummer, ort, kommun, län, telefon, email, beskrivning, kapacitet, åldersgrupp, diagnoser, tjänster, koordinater) VALUES
('Solgården', 'gruppboende', 'Solvägen 15', '12345', 'Stockholm', 'Stockholm', 'Stockholms län', '08-123456', 'solgarden@example.se', 'Ett tryggt gruppboende för vuxna med autism. Vi fokuserar på individuell utveckling och gemenskap.', 8, '18-65', ARRAY['Autism', 'ADHD'], ARRAY['Personlig assistans', 'Dagverksamhet', 'Fritidsaktiviteter'], POINT(59.3293, 18.0686)),
('Lugnets Hus', 'familjehem', 'Lugnet 7', '54321', 'Göteborg', 'Göteborg', 'Västra Götalands län', '031-123456', 'lugnets@example.se', 'Familjehem med fokus på lugn och trygghet för barn och ungdomar med neuropsykiatriska funktionsnedsättningar.', 4, '6-18', ARRAY['Autism', 'ADHD', 'Tourettes'], ARRAY['Familjehem', 'Skola', 'Terapi'], POINT(57.7089, 11.9746)),
('Framtidens Boende', 'särskilt boende', 'Framtiden 22', '98765', 'Malmö', 'Malmö', 'Skåne län', '040-123456', 'framtiden@example.se', 'Modernt särskilt boende med fokus på självständighet och delaktighet i samhället.', 12, '18+', ARRAY['Autism', 'Intellektuell funktionsnedsättning'], ARRAY['Personlig assistans', 'Arbetsförmedling', 'Fritidsaktiviteter'], POINT(55.6050, 13.0038)),
('Hoppets Dagverksamhet', 'dagverksamhet', 'Hoppet 3', '11111', 'Uppsala', 'Uppsala', 'Uppsala län', '018-123456', 'hoppet@example.se', 'Dagverksamhet med fokus på kreativitet, lärande och sociala kontakter.', 20, '18+', ARRAY['Autism', 'ADHD', 'Intellektuell funktionsnedsättning'], ARRAY['Dagverksamhet', 'Arbetsträning', 'Fritidsaktiviteter'], POINT(59.8586, 17.6389)),
('Tryggheten', 'gruppboende', 'Trygg 9', '22222', 'Linköping', 'Linköping', 'Östergötlands län', '013-123456', 'tryggheten@example.se', 'Ett hem där varje person får den individuella stöd de behöver för att trivas och utvecklas.', 6, '18-65', ARRAY['Autism', 'ADHD'], ARRAY['Personlig assistans', 'Dagverksamhet', 'Terapi'], POINT(58.4108, 15.6214));

-- Assistansföretag
INSERT INTO assistansföretag (namn, organisationsnummer, adress, postnummer, ort, telefon, email, beskrivning, specialiseringar, verksamhetsområden) VALUES
('Empati Assistans AB', '556123-4567', 'Empatigatan 1', '12345', 'Stockholm', '08-111111', 'info@empatiassistans.se', 'Vi specialiserar oss på personlig assistans för personer med autism och neuropsykiatriska funktionsnedsättningar.', ARRAY['Autism', 'ADHD'], ARRAY['Personlig assistans', 'Familjehem', 'Dagverksamhet']),
('Trygg Omsorg AB', '556234-5678', 'Tryggvägen 5', '54321', 'Göteborg', '031-222222', 'kontakt@tryggomsorg.se', 'Med över 20 års erfarenhet inom LSS-omsorg erbjuder vi kvalitativ assistans och stöd.', ARRAY['Autism', 'Intellektuell funktionsnedsättning'], ARRAY['Personlig assistans', 'Gruppboende', 'Dagverksamhet']),
('Framåt Assistans', '556345-6789', 'Framåt 12', '98765', 'Malmö', '040-333333', 'info@framatassistans.se', 'Vi fokuserar på att stärka individens självständighet och delaktighet i samhället.', ARRAY['ADHD', 'Tourettes'], ARRAY['Personlig assistans', 'Arbetsträning']);

-- Recensioner
INSERT INTO recensioner (användare_id, verksamhet_id, typ, betyg, rubrik, innehåll, trygghet, kommunikation, delaktighet, anonym) VALUES
((SELECT id FROM användare WHERE email = 'anna.larsson@email.se'), (SELECT id FROM verksamheter WHERE namn = 'Solgården'), 'verksamhet', 5, 'Fantastiskt stöd och förståelse', 'Min son har trivts otroligt bra på Solgården. Personalen visar genuin förståelse för autism och skapar en trygg miljö. Kommunikationen är alltid öppen och transparent.', 5, 5, 5, true),
((SELECT id FROM användare WHERE email = 'erik.johansson@email.se'), (SELECT id FROM verksamheter WHERE namn = 'Lugnets Hus'), 'verksamhet', 4, 'Bra familjehem med utvecklingspotential', 'Arbetar som assistent här och ser hur väl personalen förstår barnens behov. Miljön är lugn och strukturerad, vilket är perfekt för våra brukare.', 4, 4, 4, true),
((SELECT id FROM användare WHERE email = 'anna.larsson@email.se'), (SELECT id FROM verksamheter WHERE namn = 'Framtidens Boende'), 'verksamhet', 5, 'Modernt och inkluderande', 'Detta boende visar hur framtiden kan se ut för LSS-omsorg. Fokus på självständighet och respekt för individen. Rekommenderas varmt!', 5, 5, 5, true);

-- Kurser
INSERT INTO kurser (titel, beskrivning, kategori, svårighetsgrad, målgrupp, längd_minuter, moduler, quiz_frågor) VALUES
('Kommunikation och lugn kontakt', 'En grundläggande kurs om hur man kommunicerar empatiskt med personer som har autism och neuropsykiatriska funktionsnedsättningar.', 'Kommunikation', 'nybörjare', ARRAY['familj', 'assistent'], 45, 
'[
  {
    "titel": "Förstå autism och kommunikation",
    "innehåll": "Autism påverkar hur personer uppfattar och kommunicerar med världen. Vi går igenom grundläggande förståelse för olika kommunikationsstilar.",
    "exempel": "En person med autism kan behöva mer tid att processa information. Ge dem tid att svara innan du upprepar frågan."
  },
  {
    "titel": "Lugn och tydlig kommunikation",
    "innehåll": "Hur man skapar en lugn kommunikationsmiljö med tydliga signaler och förutsägbar struktur.",
    "exempel": "Använd korta, tydliga meningar. Undvik ironi och metaforer som kan vara förvirrande."
  },
  {
    "titel": "Visuell kommunikation",
    "innehåll": "Bilder, symboler och visuella hjälpmedel kan förbättra förståelsen avsevärt.",
    "exempel": "Använd bilder för att visa vad som kommer att hända härnäst, som en visuell schema."
  },
  {
    "titel": "Lyssna med hela kroppen",
    "innehåll": "Kommunikation handlar inte bara om ord. Kroppsspråk, ansiktsuttryck och tonfall är lika viktiga.",
    "exempel": "Märk när en person blir obekväm eller stressad genom att observera deras kroppsspråk."
  },
  {
    "titel": "Skapa trygga relationer",
    "innehåll": "Bygg förtroende genom konsekvent beteende, respekt för gränser och genuin empati.",
    "exempel": "Respektera när någon behöver en paus eller vill vara ensam. Det är inte en avvisning av dig."
  }
]'::jsonb,
'[
  {
    "fråga": "Vad är viktigt att komma ihåg när man kommunicerar med en person som har autism?",
    "alternativ": [
      "Använda korta, tydliga meningar",
      "Prata snabbt för att få svar",
      "Använda mycket ironi",
      "Undvika ögonkontakt"
    ],
    "rätt_svar": 0
  },
  {
    "fråga": "Vilken typ av kommunikation kan vara förvirrande för personer med autism?",
    "alternativ": [
      "Tydliga instruktioner",
      "Metaforer och ironi",
      "Visuella hjälpmedel",
      "Korta meningar"
    ],
    "rätt_svar": 1
  },
  {
    "fråga": "Vad betyder det att 'lyssna med hela kroppen'?",
    "alternativ": [
      "Bara lyssna på ord",
      "Observera kroppsspråk och ansiktsuttryck",
      "Prata högt",
      "Undvika ögonkontakt"
    ],
    "rätt_svar": 1
  },
  {
    "fråga": "Hur kan du visa respekt för en persons gränser?",
    "alternativ": [
      "Fortsätta prata även om de verkar obekväma",
      "Respektera när de behöver en paus",
      "Ignorera deras kroppsspråk",
      "Tvinga dem att svara"
    ],
    "rätt_svar": 1
  },
  {
    "fråga": "Vad är viktigt för att skapa trygga relationer?",
    "alternativ": [
      "Konsekvent beteende och respekt",
      "Varierande rutiner",
      "Ignorera personens behov",
      "Bara fokusera på ord"
    ],
    "rätt_svar": 0
  }
]'::jsonb);

-- Kommunindikatorer (mockad KOLADA-data)
INSERT INTO kommunindikatorer (kommun, län, kategori, indikator, värde, enhet, år) VALUES
('Stockholm', 'Stockholms län', 'LSS-omsorg', 'Antal LSS-boenden per 1000 invånare', 2.3, 'boenden', 2023),
('Göteborg', 'Västra Götalands län', 'LSS-omsorg', 'Antal LSS-boenden per 1000 invånare', 2.1, 'boenden', 2023),
('Malmö', 'Skåne län', 'LSS-omsorg', 'Antal LSS-boenden per 1000 invånare', 1.9, 'boenden', 2023),
('Stockholm', 'Stockholms län', 'LSS-omsorg', 'Genomsnittlig väntetid för LSS-boende', 8.5, 'månader', 2023),
('Göteborg', 'Västra Götalands län', 'LSS-omsorg', 'Genomsnittlig väntetid för LSS-boende', 12.3, 'månader', 2023),
('Malmö', 'Skåne län', 'LSS-omsorg', 'Genomsnittlig väntetid för LSS-boende', 9.7, 'månader', 2023);

-- Forskning
INSERT INTO forskning (titel, författare, universitet, år, doi, abstract, nyckelord, kategori) VALUES
('Empatiska algoritmer i välfärdsteknik', ARRAY['Dr. Anna Lindberg', 'Prof. Erik Svensson'], 'Karolinska Institutet', 2023, '10.1000/empathic-algorithms-2023', 'Denna studie undersöker hur AI-teknologi kan användas för att förbättra empati och förståelse inom välfärdsteknik, särskilt för personer med neuropsykiatriska funktionsnedsättningar.', ARRAY['AI', 'empati', 'välfärdsteknik', 'autism'], 'Teknologi'),
('Ljus och perception i autismforskning', ARRAY['Dr. Maria Andersson', 'Dr. Lars Johansson'], 'Uppsala Universitet', 2023, '10.1000/light-perception-autism-2023', 'Forskning om hur olika ljusmiljöer påverkar personer med autism och hur detta kan användas för att skapa mer inkluderande miljöer.', ARRAY['autism', 'ljus', 'perception', 'miljö'], 'Neurovetenskap'),
('Sociala indikatorer i svensk omsorg', ARRAY['Prof. Sofia Eriksson', 'Dr. Peter Nilsson'], 'Göteborgs Universitet', 2023, '10.1000/social-indicators-care-2023', 'En omfattande studie av sociala indikatorer som påverkar kvaliteten i svensk LSS-omsorg och hur dessa kan förbättras.', ARRAY['LSS', 'omsorg', 'sociala indikatorer', 'kvalitet'], 'Samhällsvetenskap');

-- Utmärkelser
INSERT INTO utmärkelser (namn, beskrivning, kategori, år) VALUES
('Årets Boende', 'Utmärkelse för det bästa LSS-boendet baserat på brukarrecensioner och kvalitetsindikatorer.', 'Boende', 2023),
('Årets Assistent', 'Utmärkelse för assistenter som visat exceptionell empati och professionalism.', 'Person', 2023),
('Brukarens Röst', 'Utmärkelse som röstas fram direkt av brukare och deras familjer.', 'Brukarval', 2023);

-- Nomineringar
INSERT INTO nomineringar (utmärkelse_id, nominerad_verksamhet_id, typ, motivering, nominerad_av) VALUES
((SELECT id FROM utmärkelser WHERE namn = 'Årets Boende'), (SELECT id FROM verksamheter WHERE namn = 'Solgården'), 'verksamhet', 'Solgården visar exceptionell förståelse för sina brukares behov och skapar en verkligt trygg och utvecklande miljö.', (SELECT id FROM användare WHERE email = 'anna.larsson@email.se')),
((SELECT id FROM utmärkelser WHERE namn = 'Årets Boende'), (SELECT id FROM verksamheter WHERE namn = 'Framtidens Boende'), 'verksamhet', 'Modernt tänkande och fokus på självständighet gör detta boende till en förebild för framtiden.', (SELECT id FROM användare WHERE email = 'erik.johansson@email.se'));

-- Forum kategorier
INSERT INTO forum_kategorier (namn, beskrivning, ikon, färg) VALUES
('Allmänt', 'Allmänna diskussioner om LSS och neurodiversitet', '💬', '#3B82F6'),
('Boende', 'Diskussioner om LSS-boenden och boendeformer', '🏠', '#10B981'),
('Assistans', 'Frågor och tips om personlig assistans', '🤝', '#F59E0B'),
('Familj', 'Stöd och råd för familjer', '👨‍👩‍👧‍👦', '#EF4444'),
('Forskning', 'Senaste forskning och utveckling', '🔬', '#8B5CF6');

-- Forum trådar
INSERT INTO forum_trådar (kategori_id, skapare_id, titel, innehåll) VALUES
((SELECT id FROM forum_kategorier WHERE namn = 'Allmänt'), (SELECT id FROM användare WHERE email = 'anna.larsson@email.se'), 'Välkommen till Neuroljus Neurohus!', 'Hej alla! Jag är så glad att vi äntligen har en plattform där vi kan dela erfarenheter och stödja varandra. Låt oss bygga en stark gemenskap tillsammans!'),
((SELECT id FROM forum_kategorier WHERE namn = 'Boende'), (SELECT id FROM användare WHERE email = 'erik.johansson@email.se'), 'Tips för att hitta rätt boende', 'Som assistent har jag sett många olika boenden. Här är mina bästa tips för att hitta ett boende som passar just er familj.');

-- Audit loggar (exempel)
INSERT INTO audit_loggar (användare_id, action, tabell, post_id, nya_värden) VALUES
((SELECT id FROM användare WHERE email = 'anna.larsson@email.se'), 'CREATE', 'recensioner', (SELECT id FROM recensioner LIMIT 1), '{"betyg": 5, "rubrik": "Fantastiskt stöd och förståelse"}');

-- ==============================================
-- TRIGGERS FÖR AUTOMATISK UPPDATERING
-- ==============================================

-- Trigger för att uppdatera senast_aktiv på användare
CREATE OR REPLACE FUNCTION update_senast_aktiv()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE användare SET senast_aktiv = CURRENT_TIMESTAMP WHERE id = NEW.användare_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_senast_aktiv
    AFTER INSERT OR UPDATE ON recensioner
    FOR EACH ROW
    EXECUTE FUNCTION update_senast_aktiv();

-- Trigger för att uppdatera antal_svar på forum_trådar
CREATE OR REPLACE FUNCTION update_antal_svar()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE forum_trådar SET 
        antal_svar = antal_svar + 1,
        senast_svar = CURRENT_TIMESTAMP
    WHERE id = NEW.tråd_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_antal_svar
    AFTER INSERT ON forum_svar
    FOR EACH ROW
    EXECUTE FUNCTION update_antal_svar();

-- ==============================================
-- VIEWS FÖR RAPPORTER
-- ==============================================

-- View för verksamhetsöversikt med genomsnittliga betyg
CREATE VIEW verksamhetsöversikt AS
SELECT 
    v.*,
    COALESCE(AVG(r.betyg), 0) as genomsnittligt_betyg,
    COUNT(r.id) as antal_recensioner,
    COALESCE(AVG(r.trygghet), 0) as genomsnittlig_trygghet,
    COALESCE(AVG(r.kommunikation), 0) as genomsnittlig_kommunikation,
    COALESCE(AVG(r.delaktighet), 0) as genomsnittlig_delaktighet
FROM verksamheter v
LEFT JOIN recensioner r ON v.id = r.verksamhet_id AND r.godkänd = true
GROUP BY v.id;

-- View för användarstatistik
CREATE VIEW användarstatistik AS
SELECT 
    roll,
    kommun,
    COUNT(*) as antal_användare,
    COUNT(CASE WHEN verifierad = true THEN 1 END) as verifierade_användare,
    COUNT(CASE WHEN senast_aktiv > CURRENT_TIMESTAMP - INTERVAL '30 days' THEN 1 END) as aktiva_senaste_månaden
FROM användare
GROUP BY roll, kommun;

COMMENT ON DATABASE neurohus IS 'Neuroljus Neurohus - Sveriges första digitala hus för empati, kunskap och neurodiversitet';
