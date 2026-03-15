import streamlit as st

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Ayoade Adegbite | Analytics Engineer & Speaker",
    page_icon="logo.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# Custom CSS
# ---------------------------------------------------------------------------
st.markdown("""
<style>
/* ---- Import fonts ---- */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap');

/* ---- Root variables ---- */
:root {
    --bg-primary: #0A0E17;
    --bg-secondary: #131A2B;
    --bg-card: #1A2235;
    --bg-card-hover: #1E2840;
    --accent: #4FC3F7;
    --accent-glow: rgba(79, 195, 247, 0.15);
    --accent-secondary: #7C4DFF;
    --text-primary: #E8EAF0;
    --text-secondary: #9EA7B8;
    --text-muted: #6B7280;
    --border: rgba(79, 195, 247, 0.12);
    --gradient-1: linear-gradient(135deg, #4FC3F7, #7C4DFF);
    --gradient-2: linear-gradient(135deg, #0A0E17 0%, #131A2B 100%);
    --radius: 16px;
    --radius-sm: 10px;
    --shadow: 0 4px 24px rgba(0,0,0,0.3);
    --shadow-glow: 0 0 40px rgba(79, 195, 247, 0.08);
}

/* ---- Global resets ---- */
html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background-color: var(--bg-primary) !important;
    color: var(--text-primary) !important;
    font-family: 'Inter', sans-serif !important;
}

[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stSidebar"] { display: none !important; }
#MainMenu, footer, header { visibility: hidden !important; }
.block-container { padding-top: 0 !important; max-width: 1200px !important; }

/* ---- Scrollbar ---- */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg-primary); }
::-webkit-scrollbar-thumb { background: var(--accent); border-radius: 3px; }

/* ---- Navbar ---- */
.navbar {
    position: fixed; top: 0; left: 0; right: 0; z-index: 9999;
    background: rgba(10, 14, 23, 0.85);
    backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--border);
    padding: 0 2rem;
    display: flex; align-items: center; justify-content: space-between;
    height: 64px;
}
.nav-logo {
    font-weight: 800; font-size: 1.2rem; color: var(--text-primary);
    text-decoration: none; letter-spacing: -0.02em;
}
.nav-logo span { color: var(--accent); }
.nav-links { display: flex; gap: 2rem; align-items: center; }
.nav-links a {
    color: var(--text-secondary); text-decoration: none; font-size: 0.85rem;
    font-weight: 500; transition: color 0.2s; letter-spacing: 0.02em;
    text-transform: uppercase;
}
.nav-links a:hover { color: var(--accent); }
.nav-cta {
    background: var(--gradient-1); color: #fff !important; padding: 8px 20px;
    border-radius: 8px; font-weight: 600; font-size: 0.82rem;
    text-transform: uppercase; letter-spacing: 0.04em;
}
.nav-cta:hover { opacity: 0.9; transform: translateY(-1px); }

/* ---- Spacer for fixed navbar ---- */
.nav-spacer { height: 80px; }

/* ---- Hero ---- */
.hero-section {
    padding: 6rem 0 4rem; text-align: center; position: relative;
}
.hero-section::before {
    content: ''; position: absolute; top: -100px; left: 50%;
    transform: translateX(-50%);
    width: 600px; height: 600px;
    background: radial-gradient(circle, rgba(79,195,247,0.06) 0%, transparent 70%);
    pointer-events: none;
}
.hero-badge {
    display: inline-block; background: var(--accent-glow);
    border: 1px solid var(--border); border-radius: 50px;
    padding: 6px 18px; font-size: 0.78rem; color: var(--accent);
    font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase;
    margin-bottom: 1.5rem;
}
.hero-title {
    font-size: clamp(2.5rem, 5.5vw, 4.2rem); font-weight: 900;
    line-height: 1.08; margin-bottom: 1.5rem; letter-spacing: -0.03em;
    color: var(--text-primary);
}
.hero-title .accent { color: var(--accent); }
.hero-title .accent-purple { color: var(--accent-secondary); }
.hero-subtitle {
    font-size: 1.15rem; color: var(--text-secondary); max-width: 680px;
    margin: 0 auto 2.5rem; line-height: 1.7; font-weight: 400;
}
.hero-buttons { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
.btn-primary {
    background: var(--gradient-1); color: #fff; padding: 14px 32px;
    border-radius: 10px; font-weight: 700; font-size: 0.95rem;
    text-decoration: none; transition: all 0.3s;
    box-shadow: 0 4px 20px rgba(79,195,247,0.25);
}
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 6px 28px rgba(79,195,247,0.35); }
.btn-secondary {
    background: transparent; color: var(--text-primary); padding: 14px 32px;
    border-radius: 10px; font-weight: 600; font-size: 0.95rem;
    text-decoration: none; border: 1.5px solid var(--border);
    transition: all 0.3s;
}
.btn-secondary:hover { border-color: var(--accent); color: var(--accent); }

/* ---- Stats bar ---- */
.stats-bar {
    display: flex; justify-content: center; gap: 3rem; flex-wrap: wrap;
    padding: 3rem 0; margin-top: 1rem;
    border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);
}
.stat-item { text-align: center; }
.stat-number {
    font-size: 2.2rem; font-weight: 800; color: var(--accent);
    letter-spacing: -0.02em;
    font-family: 'JetBrains Mono', monospace;
}
.stat-label {
    font-size: 0.78rem; color: var(--text-muted); text-transform: uppercase;
    letter-spacing: 0.08em; margin-top: 4px; font-weight: 500;
}

/* ---- Section styling ---- */
.section { padding: 5rem 0; }
.section-header { text-align: center; margin-bottom: 3.5rem; }
.section-badge {
    display: inline-block; background: var(--accent-glow);
    border: 1px solid var(--border); border-radius: 50px;
    padding: 5px 16px; font-size: 0.72rem; color: var(--accent);
    font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase;
    margin-bottom: 1rem;
}
.section-title {
    font-size: clamp(1.8rem, 3.5vw, 2.6rem); font-weight: 800;
    letter-spacing: -0.02em; margin-bottom: 0.8rem; color: var(--text-primary);
}
.section-subtitle {
    font-size: 1.05rem; color: var(--text-secondary); max-width: 600px;
    margin: 0 auto; line-height: 1.7;
}

/* ---- Cards ---- */
.card {
    background: var(--bg-card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 2rem;
    transition: all 0.3s ease; height: 100%;
}
.card:hover {
    border-color: var(--accent); transform: translateY(-4px);
    box-shadow: var(--shadow-glow);
}
.card-icon {
    width: 48px; height: 48px; border-radius: 12px;
    background: var(--accent-glow); display: flex; align-items: center;
    justify-content: center; margin-bottom: 1.2rem; font-size: 1.4rem;
}
.card-title {
    font-size: 1.15rem; font-weight: 700; margin-bottom: 0.6rem;
    color: var(--text-primary);
}
.card-text {
    font-size: 0.9rem; color: var(--text-secondary); line-height: 1.7;
}

/* ---- Speaking table ---- */
.talk-row {
    display: grid; grid-template-columns: 1fr 200px 120px 140px;
    padding: 1.2rem 1.5rem; border-bottom: 1px solid var(--border);
    align-items: center; transition: background 0.2s;
}
.talk-row:hover { background: var(--bg-card); }
.talk-title-cell { font-weight: 600; color: var(--text-primary); font-size: 0.95rem; }
.talk-meta { font-size: 0.85rem; color: var(--text-secondary); }
.talk-badge {
    display: inline-block; background: var(--accent-glow);
    color: var(--accent); padding: 3px 10px; border-radius: 6px;
    font-size: 0.72rem; font-weight: 600;
}
.talk-header {
    display: grid; grid-template-columns: 1fr 200px 120px 140px;
    padding: 0.8rem 1.5rem; border-bottom: 2px solid var(--accent);
    font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.08em;
    color: var(--text-muted); font-weight: 600;
}

/* ---- OS projects ---- */
.repo-card {
    background: var(--bg-card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 1.8rem;
    transition: all 0.3s;
}
.repo-card:hover {
    border-color: var(--accent); transform: translateY(-3px);
    box-shadow: var(--shadow-glow);
}
.repo-name {
    font-family: 'JetBrains Mono', monospace; font-size: 1.05rem;
    font-weight: 600; color: var(--accent); margin-bottom: 0.6rem;
}
.repo-desc { font-size: 0.88rem; color: var(--text-secondary); line-height: 1.65; margin-bottom: 1rem; }
.repo-stats { display: flex; gap: 1rem; align-items: center; }
.repo-stat {
    font-size: 0.78rem; color: var(--text-muted); display: flex;
    align-items: center; gap: 4px;
}

/* ---- Timeline ---- */
.timeline-item {
    position: relative; padding-left: 2.5rem; padding-bottom: 2.5rem;
    border-left: 2px solid var(--border);
}
.timeline-item::before {
    content: ''; position: absolute; left: -6px; top: 6px;
    width: 10px; height: 10px; border-radius: 50%;
    background: var(--accent); border: 2px solid var(--bg-primary);
}
.timeline-role { font-size: 1.05rem; font-weight: 700; color: var(--text-primary); }
.timeline-org { font-size: 0.92rem; color: var(--accent); font-weight: 600; }
.timeline-date { font-size: 0.8rem; color: var(--text-muted); margin: 4px 0 8px; }
.timeline-desc { font-size: 0.88rem; color: var(--text-secondary); line-height: 1.65; }

/* ---- Community logos ---- */
.community-grid {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 1rem;
}
.community-badge {
    background: var(--bg-card); border: 1px solid var(--border);
    border-radius: var(--radius-sm); padding: 1.2rem; text-align: center;
    font-weight: 600; font-size: 0.9rem; color: var(--text-primary);
    transition: all 0.3s;
}
.community-badge:hover { border-color: var(--accent); background: var(--bg-card-hover); }
.community-role {
    font-size: 0.72rem; color: var(--accent); text-transform: uppercase;
    letter-spacing: 0.06em; margin-top: 6px;
}

/* ---- Newsletter section ---- */
.newsletter-box {
    background: linear-gradient(135deg, var(--bg-card) 0%, rgba(79,195,247,0.05) 100%);
    border: 1px solid var(--border); border-radius: var(--radius);
    padding: 3rem; text-align: center;
}
.newsletter-title {
    font-size: 1.8rem; font-weight: 800; margin-bottom: 0.8rem;
    color: var(--text-primary);
}
.newsletter-desc {
    font-size: 1rem; color: var(--text-secondary); max-width: 500px;
    margin: 0 auto 2rem; line-height: 1.7;
}
.newsletter-stat {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem; color: var(--accent); margin-bottom: 1.5rem;
}

/* ---- Contact grid ---- */
.contact-card {
    background: var(--bg-card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 2rem; text-align: center;
    transition: all 0.3s;
}
.contact-card:hover { border-color: var(--accent); transform: translateY(-3px); }
.contact-icon { font-size: 2rem; margin-bottom: 1rem; }
.contact-label {
    font-size: 0.72rem; color: var(--text-muted); text-transform: uppercase;
    letter-spacing: 0.08em; margin-bottom: 0.5rem; font-weight: 600;
}
.contact-value {
    font-size: 1rem; font-weight: 600; color: var(--text-primary);
}
.contact-value a { color: var(--accent); text-decoration: none; }
.contact-value a:hover { text-decoration: underline; }

/* ---- Footer ---- */
.footer {
    border-top: 1px solid var(--border); padding: 2.5rem 0;
    text-align: center; margin-top: 2rem;
}
.footer-text { font-size: 0.82rem; color: var(--text-muted); }
.footer-links { display: flex; gap: 1.5rem; justify-content: center; margin-bottom: 1rem; }
.footer-links a {
    color: var(--text-secondary); text-decoration: none; font-size: 0.85rem;
    transition: color 0.2s;
}
.footer-links a:hover { color: var(--accent); }

/* ---- About section ---- */
.about-text {
    font-size: 1.05rem; line-height: 1.85; color: var(--text-secondary);
}
.about-text strong { color: var(--text-primary); font-weight: 600; }
.about-highlight {
    border-left: 3px solid var(--accent); padding-left: 1.5rem;
    margin: 2rem 0; font-style: italic; color: var(--text-secondary);
    font-size: 1.1rem; line-height: 1.7;
}

/* ---- Tag / pill ---- */
.tag {
    display: inline-block; background: var(--accent-glow);
    border: 1px solid var(--border); border-radius: 6px;
    padding: 4px 12px; font-size: 0.75rem; color: var(--accent);
    font-weight: 600; margin: 3px;
}

/* ---- Divider ---- */
.divider {
    height: 1px; background: var(--border); margin: 3rem 0;
}

/* ---- Responsive ---- */
@media (max-width: 768px) {
    .navbar { padding: 0 1rem; }
    .nav-links { gap: 1rem; }
    .nav-links a { font-size: 0.75rem; }
    .hero-title { font-size: 2rem; }
    .stats-bar { gap: 1.5rem; }
    .stat-number { font-size: 1.6rem; }
    .talk-row, .talk-header {
        grid-template-columns: 1fr;
        gap: 0.3rem;
    }
    .talk-header { display: none; }
    .hero-buttons { flex-direction: column; align-items: center; }
}

/* Hide streamlit elements */
div[data-testid="stDecoration"] { display: none !important; }
.stDeployButton { display: none !important; }
div[data-testid="stToolbar"] { display: none !important; }
div[data-testid="stStatusWidget"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Navbar
# ---------------------------------------------------------------------------
st.markdown("""
<div class="navbar">
    <a href="#" class="nav-logo">Ayoade<span>.</span></a>
    <div class="nav-links">
        <a href="#about">About</a>
        <a href="#services">Services</a>
        <a href="#speaking">Speaking</a>
        <a href="#opensource">Open Source</a>
        <a href="#mentorship">Mentorship</a>
        <a href="#community">Community</a>
        <a href="#contact" class="nav-cta">Book Me</a>
    </div>
</div>
<div class="nav-spacer"></div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Hero
# ---------------------------------------------------------------------------
st.markdown("""
<div class="hero-section">
    <div class="hero-badge">Senior Analytics Engineer &bull; Speaker &bull; OSS Contributor</div>
    <h1 class="hero-title">
        Turning <span class="accent">AI Ambition</span> Into<br>
        <span class="accent-purple">Operational Reality</span>
    </h1>
    <p class="hero-subtitle">
        I help teams and organizations build the data foundations that make AI
        trustworthy, explainable, and production-ready &mdash; from data modeling
        and documentation automation to analytics engineering and team enablement.
    </p>
    <div class="hero-buttons">
        <a href="#contact" class="btn-primary">Book Me to Speak</a>
        <a href="#about" class="btn-secondary">Explore My Work</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Stats bar
st.markdown("""
<div class="stats-bar">
    <div class="stat-item">
        <div class="stat-number">5+</div>
        <div class="stat-label">Years in Data</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">8+</div>
        <div class="stat-label">Conference Talks</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">39+</div>
        <div class="stat-label">Newsletter Editions</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">151</div>
        <div class="stat-label">GitHub Repos</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">900+</div>
        <div class="stat-label">Students Trained</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">6</div>
        <div class="stat-label">Countries</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# About
# ---------------------------------------------------------------------------
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <div class="section-header">
        <div class="section-badge">About Me</div>
        <h2 class="section-title">The Story Behind The Data</h2>
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([3, 2], gap="large")

with col1:
    st.markdown("""
    <div class="about-text">
        <p>I'm <strong>Ayoade Adegbite</strong> &mdash; an Analytics Engineer, international speaker,
        and the founder of <strong>Behind The Data</strong>.</p>

        <p>My career started in Mechatronics Engineering in Nigeria, but I quickly discovered
        that the most impactful problems weren't hardware problems &mdash; they were
        <strong>data problems</strong>. Since then, I've worked across Nigeria, Canada, the UK,
        the US, and Poland, helping organizations turn messy, undocumented data systems into
        production-ready analytics platforms.</p>

        <div class="about-highlight">
            "I don't just build systems &mdash; I build people. Through academies, bootcamps,
            and mentorship programs across three continents, I've trained hundreds of analysts
            and engineers."
        </div>

        <p>At <strong>The Bredge</strong>, I build custom dashboards tracking dbt model usage and
        Snowflake costs, and I've automated documentation using LLMs &mdash; increasing
        coverage by <strong>35%+</strong>. Previously at YipYip Media, I migrated legacy stored
        procedures to modular dbt models, reducing maintenance time by <strong>45%</strong>.</p>

        <p>Currently pursuing my <strong>Master's in Information Technology</strong> at
        Miva Open University, and I hold certifications in <strong>Tableau</strong> and
        <strong>Apache Airflow</strong> (Astronomer DAG Authoring).</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card" style="margin-bottom: 1.2rem;">
        <div class="card-title">Currently</div>
        <div class="card-text">
            Senior Analytics Engineer @ <strong style="color: var(--accent);">The Bredge</strong><br>
            <span style="color: var(--text-muted); font-size: 0.82rem;">Oct 2025 &ndash; Present &bull; United States</span>
        </div>
    </div>
    <div class="card" style="margin-bottom: 1.2rem;">
        <div class="card-title">Education</div>
        <div class="card-text">
            MTech, Information Technology<br>
            <span style="color: var(--accent);">Miva Open University</span><br>
            <span style="color: var(--text-muted); font-size: 0.82rem;">Sep 2025 &ndash; Dec 2026</span>
        </div>
    </div>
    <div class="card" style="margin-bottom: 1.2rem;">
        <div class="card-title">Certifications</div>
        <div class="card-text">
            <span class="tag">Tableau Certified</span>
            <span class="tag">Astronomer Airflow</span>
            <span class="tag">Scientific Computing w/ Python</span>
        </div>
    </div>
    <div class="card">
        <div class="card-title">Top Skills</div>
        <div class="card-text">
            <span class="tag">dbt</span>
            <span class="tag">Snowflake</span>
            <span class="tag">Airflow</span>
            <span class="tag">BigQuery</span>
            <span class="tag">SQL</span>
            <span class="tag">Python</span>
            <span class="tag">Tableau</span>
            <span class="tag">Streamlit</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Services
# ---------------------------------------------------------------------------
st.markdown('<div id="services"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <div class="section-header">
        <div class="section-badge">What I Do</div>
        <h2 class="section-title">Services & Expertise</h2>
        <p class="section-subtitle">
            From stage to codebase &mdash; I help organizations build scalable analytics
            foundations and develop the talent to sustain them.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

svc_cols = st.columns(4, gap="medium")

services = [
    {
        "icon": "&#127908;",
        "title": "Speaking & Keynotes",
        "text": "Conference talks on analytics engineering, data quality, AI-readiness, and documentation automation. Real case studies, actionable frameworks. Available for virtual, in-person, and hybrid events."
    },
    {
        "icon": "&#127891;",
        "title": "Training & Workshops",
        "text": "Hands-on training via Behind The Data Academy: dbt, Snowflake, data modeling, Python, CI/CD for analytics. Multi-week bootcamps, intensive workshops, or embedded team training."
    },
    {
        "icon": "&#128736;",
        "title": "Consulting",
        "text": "Data pipeline architecture, dbt implementation, documentation automation with AI/LLMs, governance frameworks, and team capability assessments for organizations scaling their data practice."
    },
    {
        "icon": "&#128218;",
        "title": "Curriculum Development",
        "text": "Data analytics curriculum and educational content for academies and EdTech platforms. Topics from Big Data & BI to ML Engineering and Data Strategy for AI implementation."
    },
]

for col, svc in zip(svc_cols, services):
    with col:
        st.markdown(f"""
        <div class="card">
            <div class="card-icon">{svc["icon"]}</div>
            <div class="card-title">{svc["title"]}</div>
            <div class="card-text">{svc["text"]}</div>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Speaking
# ---------------------------------------------------------------------------
st.markdown('<div id="speaking"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <div class="section-header">
        <div class="section-badge">Speaking</div>
        <h2 class="section-title">Conference & Event Talks</h2>
        <p class="section-subtitle">
            I speak at conferences and events across Africa and globally, sharing practical
            insights on analytics engineering, data quality, and AI-ready data foundations.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

talks = [
    ("Data Before AI: Establishing Data Foundations for AI Readiness", "move(data) 2025", "Mar 2025", "Virtual"),
    ("The Art of Engaging Documentation", "Write The Docs Kenya", "Jun 2025", "Nairobi"),
    ("Building Effective Docs and Culture", "WriteTheDocs Nigeria 2024", "Nov 2024", "Lagos"),
    ("From Raw Data to Insights: Pipelines with Airbyte, dbt & Airflow", "DevFest Osogbo 2024", "Dec 2024", "Osogbo"),
    ("The Hidden Costs of Bad Data", "DevFest Lagos", "2024", "Lagos"),
    ("Driving Economic Growth with Data Observability", "Conference Talk", "2024", "Africa"),
    ("Data Quality = Business Success", "Conference Talk", "2024", "Africa"),
    ("Driving Analytics with Open Source", "KwaraBuild Ilorin", "2025", "Ilorin"),
    ("AI-Powered Documentation Automation (Guest Lecture)", "WSKZ University", "Nov 2025", "Poland"),
]

st.markdown("""
<div class="talk-header">
    <div>Talk</div>
    <div>Event</div>
    <div>Date</div>
    <div>Location</div>
</div>
""", unsafe_allow_html=True)

for title, event, date, location in talks:
    st.markdown(f"""
    <div class="talk-row">
        <div class="talk-title-cell">{title}</div>
        <div class="talk-meta">{event}</div>
        <div class="talk-meta"><span class="talk-badge">{date}</span></div>
        <div class="talk-meta">{location}</div>
    </div>
    """, unsafe_allow_html=True)

# Speaking topics
st.markdown("<br>", unsafe_allow_html=True)
topics = [
    "Analytics Engineering", "Data Quality & Testing", "AI-Readiness & Data Foundations",
    "Documentation Automation", "Open Source Data Stack", "Data Observability",
    "Career Development in Data",
]
tags_html = " ".join(f'<span class="tag">{t}</span>' for t in topics)
st.markdown(f"""
<div style="text-align:center; margin-top: 2rem;">
    <div style="font-size: 0.82rem; color: var(--text-muted); text-transform: uppercase;
                letter-spacing: 0.06em; margin-bottom: 0.8rem; font-weight: 600;">
        Topics I Cover
    </div>
    {tags_html}
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Open Source
# ---------------------------------------------------------------------------
st.markdown('<div id="opensource"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <div class="section-header">
        <div class="section-badge">Open Source</div>
        <h2 class="section-title">Tools I've Built</h2>
        <p class="section-subtitle">
            Open-source tools solving real problems in analytics engineering &mdash;
            particularly around documentation, data quality, and observability.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

repos = [
    {
        "name": "dbt-doc-tracker",
        "stars": 6,
        "desc": "Detects and records documentation changes across your dbt project. Records only the diffs &mdash; when a description is added, modified, or removed. Built for documentation governance.",
        "lang": "SQL / Jinja",
    },
    {
        "name": "dbt-doc-inherit",
        "stars": 3,
        "desc": "Propagates column descriptions along the DAG &mdash; define once, inherit downstream. Eliminates repetitive documentation of the same column across dozens of models.",
        "lang": "SQL / Jinja",
    },
    {
        "name": "dbt-autodoc",
        "stars": 0,
        "desc": "Auto-generate dbt model and column descriptions using heuristics or LLMs. The tool behind the 35%+ documentation coverage improvement at The Bredge.",
        "lang": "Python",
    },
    {
        "name": "dbt-anomaly-detector",
        "stars": 1,
        "desc": "Lightweight dbt package for statistical anomaly detection on warehouse metrics using Python models. Catch data quality issues before they hit dashboards.",
        "lang": "Python / SQL",
    },
    {
        "name": "awesome-modern-data-stack",
        "stars": 0,
        "desc": "Curated list of open-source tools covering every layer of the modern data stack &mdash; ingestion, warehousing, transformation, orchestration, quality, cataloging, and more.",
        "lang": "Markdown",
    },
    {
        "name": "tap-substack",
        "stars": 1,
        "desc": "Singer tap for extracting Substack newsletter data. Built to support analytics on newsletter performance and subscriber engagement.",
        "lang": "Python",
    },
]

repo_cols = st.columns(3, gap="medium")
for i, repo in enumerate(repos):
    with repo_cols[i % 3]:
        stars_display = f'&#9733; {repo["stars"]}' if repo["stars"] > 0 else ""
        st.markdown(f"""
        <div class="repo-card" style="margin-bottom: 1rem;">
            <div class="repo-name">{repo["name"]}</div>
            <div class="repo-desc">{repo["desc"]}</div>
            <div class="repo-stats">
                <span class="repo-stat">{stars_display}</span>
                <span class="repo-stat">&#128992; {repo["lang"]}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin-top: 1.5rem;">
    <a href="https://github.com/tripleaceme" target="_blank" class="btn-secondary"
       style="display: inline-block;">
        View All 151 Repos on GitHub &rarr;
    </a>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Mentorship & Training
# ---------------------------------------------------------------------------
st.markdown('<div id="mentorship"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <div class="section-header">
        <div class="section-badge">Mentorship & Training</div>
        <h2 class="section-title">Building People, Not Just Pipelines</h2>
        <p class="section-subtitle">
            I've trained hundreds of analysts, engineers, and career-switchers across
            three continents. My approach: build reliable analytics foundations
            <em>before</em> the dashboard.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

training_roles = [
    {
        "role": "Senior Analytics Trainer",
        "org": "Behind The Data Academy",
        "date": "Aug 2025 &ndash; Present",
        "desc": "Teaching dbt, data modeling, Snowflake, data quality, CI/CD pipelines, Git workflows, and Python for analytics. Focus on production-ready systems."
    },
    {
        "role": "Specialized Data Analytics Mentor",
        "org": "CareerFoundry",
        "date": "Jun 2023 &ndash; Feb 2026 &bull; 2 yrs 9 mos",
        "desc": "2+ years mentoring aspiring data analysts through personalized 1:1 guidance covering data analysis, statistical techniques, visualization, and career development."
    },
    {
        "role": "Internship Coordinator, Data Analytics",
        "org": "Trevotech Academy",
        "date": "May 2024 &ndash; Oct 2025 &bull; 1 yr 6 mos",
        "desc": "Designed internship program structure, led bi-weekly sessions, tracked intern progress, and coordinated real-world project integration."
    },
    {
        "role": "Tableau Bootcamp Trainer",
        "org": "Trevotech Academy",
        "date": "Jul 2022 &ndash; May 2024 &bull; 1 yr 11 mos",
        "desc": "Designed comprehensive Tableau curriculum from beginner to advanced. Trained 900+ students across 7 countries. Students placed at major companies."
    },
    {
        "role": "Data Analytics Tutor Assistant",
        "org": "Millennials and Data",
        "date": "Sep 2023 &ndash; Dec 2024 &bull; 1 yr 4 mos",
        "desc": "Facilitated learning in SQL, Excel, and Tableau with real-world datasets. Guided students through Tableau Desktop Specialist Certification prep."
    },
]

for t in training_roles:
    st.markdown(f"""
    <div class="timeline-item">
        <div class="timeline-role">{t["role"]}</div>
        <div class="timeline-org">{t["org"]}</div>
        <div class="timeline-date">{t["date"]}</div>
        <div class="timeline-desc">{t["desc"]}</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Community
# ---------------------------------------------------------------------------
st.markdown('<div id="community"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <div class="section-header">
        <div class="section-badge">Community & Leadership</div>
        <h2 class="section-title">Growing the Ecosystem</h2>
        <p class="section-subtitle">
            I believe the data ecosystem grows when we invest in community.
            Here's how I contribute beyond my day job.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

communities = [
    ("Behind The Data", "Founder"),
    ("dbt Lagos", "Organizer"),
    ("CDIPS", "Contributor"),
    ("Osacon", "Community"),
    ("3MTT Nigeria", "Involvement"),
    ("DataGlobal Hub Elite", "Member"),
]

st.markdown('<div class="community-grid">', unsafe_allow_html=True)
comm_html = ""
for name, role in communities:
    comm_html += f"""
    <div class="community-badge">
        {name}
        <div class="community-role">{role}</div>
    </div>
    """
st.markdown(f'<div class="community-grid">{comm_html}</div>', unsafe_allow_html=True)

# Guest Lecturing
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
    <div class="card-title">&#127891; Guest Lecturing</div>
    <div class="card-text">
        <strong style="color: var(--text-primary);">WSKZ University College of Professional Education, Poland</strong>
        (Nov &ndash; Dec 2025)<br><br>
        Delivered lectures on building scalable data infrastructure using open-source tools.
        Included a practical case study on AI-powered documentation automation with
        Gemini AI and dbt &mdash; demonstrating how generative AI can improve data quality,
        trust, and maintainability in analytics workflows.
    </div>
</div>
""", unsafe_allow_html=True)

# Publications
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
    <div class="card-title">&#128221; Publications</div>
    <div class="card-text">
        <span class="tag">Africa Beer Consumption Analysis</span>
        <span class="tag">Data Science in Inventory Management</span>
        <span class="tag">Intro to SQL for Business Management</span>
        <span class="tag">Region Performance Dashboard</span>
        <span class="tag">The Most Searched Artist in Nigeria?</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Newsletter
# ---------------------------------------------------------------------------
st.markdown('<div id="newsletter"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <div class="newsletter-box">
        <div class="section-badge">Newsletter</div>
        <div class="newsletter-title">Behind The Data</div>
        <div class="newsletter-desc">
            Insightful stories and in-depth conversations with professionals across the
            data industry &mdash; their journeys, expertise, and the impact of their work.
        </div>
        <div class="newsletter-stat">39+ EDITIONS &bull; HUNDREDS OF SUBSCRIBERS &bull; WEEKLY</div>
        <div style="margin-bottom: 1.5rem;">
            <span class="tag">Career Journeys</span>
            <span class="tag">Data Engineering</span>
            <span class="tag">Analytics Insights</span>
            <span class="tag">Mentorship</span>
            <span class="tag">Podcast Episodes</span>
        </div>
        <div style="margin-top: 1rem;">
            <strong style="color: var(--text-primary); font-size: 0.9rem;">Recent Editions:</strong><br>
            <span style="color: var(--text-secondary); font-size: 0.88rem;">
                Issue 039 &mdash; Meet Abiodun Sanni &bull;
                Issue 038 &mdash; Meet Marta Gonz&aacute;lez Urue&ntilde;a &bull;
                and 37 more...
            </span>
        </div>
        <br>
        <a href="https://behindthedata.substack.com" target="_blank" class="btn-primary"
           style="display: inline-block;">
            Subscribe to Behind The Data &rarr;
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Contact
# ---------------------------------------------------------------------------
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <div class="section-header">
        <div class="section-badge">Get In Touch</div>
        <h2 class="section-title">Let's Work Together</h2>
        <p class="section-subtitle">
            Whether you want me on stage, training your team, or consulting on your
            data architecture &mdash; I'd love to hear from you.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3, gap="medium")

with c1:
    st.markdown("""
    <div class="contact-card">
        <div class="contact-icon">&#127908;</div>
        <div class="contact-label">Book Me to Speak</div>
        <div class="contact-value">
            <a href="https://sessionize.com/ayoade" target="_blank">View Sessionize Profile</a>
        </div>
        <div style="color: var(--text-muted); font-size: 0.82rem; margin-top: 0.5rem;">
            Conference, meetup, or corporate event
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="contact-card">
        <div class="contact-icon">&#127891;</div>
        <div class="contact-label">Train Your Team</div>
        <div class="contact-value">
            <a href="https://academy.behindthedata.tech" target="_blank">Behind The Data Academy</a>
        </div>
        <div style="color: var(--text-muted); font-size: 0.82rem; margin-top: 0.5rem;">
            Workshops, bootcamps, or embedded training
        </div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="contact-card">
        <div class="contact-icon">&#128231;</div>
        <div class="contact-label">Consulting & Other</div>
        <div class="contact-value">
            <a href="mailto:tripleaceme@gmail.com">tripleaceme@gmail.com</a>
        </div>
        <div style="color: var(--text-muted); font-size: 0.82rem; margin-top: 0.5rem;">
            Data architecture, dbt, documentation automation
        </div>
    </div>
    """, unsafe_allow_html=True)

# Social links
st.markdown("""
<div style="text-align: center; margin-top: 2.5rem;">
    <div style="display: flex; gap: 1.5rem; justify-content: center; flex-wrap: wrap;">
        <a href="https://www.linkedin.com/in/tripleaceme" target="_blank" class="btn-secondary"
           style="display: inline-block; padding: 10px 20px; font-size: 0.85rem;">LinkedIn</a>
        <a href="https://github.com/tripleaceme" target="_blank" class="btn-secondary"
           style="display: inline-block; padding: 10px 20px; font-size: 0.85rem;">GitHub</a>
        <a href="https://twitter.com/abel_analytics" target="_blank" class="btn-secondary"
           style="display: inline-block; padding: 10px 20px; font-size: 0.85rem;">Twitter / X</a>
        <a href="https://instagram.com/abel_analytics" target="_blank" class="btn-secondary"
           style="display: inline-block; padding: 10px 20px; font-size: 0.85rem;">Instagram</a>
        <a href="https://behindthedata.substack.com" target="_blank" class="btn-secondary"
           style="display: inline-block; padding: 10px 20px; font-size: 0.85rem;">Newsletter</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown("""
<div class="footer">
    <div class="footer-links">
        <a href="#about">About</a>
        <a href="#services">Services</a>
        <a href="#speaking">Speaking</a>
        <a href="#opensource">Open Source</a>
        <a href="#mentorship">Mentorship</a>
        <a href="#community">Community</a>
        <a href="#newsletter">Newsletter</a>
        <a href="#contact">Contact</a>
    </div>
    <div class="footer-text">
        &copy; 2025 Ayoade Adegbite. All rights reserved. &nbsp;&bull;&nbsp;
        Built with purpose, powered by data.
    </div>
</div>
""", unsafe_allow_html=True)
