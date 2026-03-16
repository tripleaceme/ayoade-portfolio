// ---- Navbar scroll ----
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 50);
});

// ---- Mobile toggle ----
const toggle = document.getElementById('navToggle');
const links = document.getElementById('navLinks');
toggle.addEventListener('click', () => {
    links.classList.toggle('open');
    toggle.classList.toggle('active');
});
links.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => {
        links.classList.remove('open');
        toggle.classList.remove('active');
    });
});

// ---- Smooth scroll (only for same-page anchors) ----
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href === '#') return;
        const target = document.querySelector(href);
        if (target) {
            e.preventDefault();
            const top = target.getBoundingClientRect().top + window.pageYOffset - 80;
            window.scrollTo({ top, behavior: 'smooth' });
        }
    });
});

// ---- Service modals (only on home page) ----
const modalData = {
    speaking: {
        title: 'Speaking & Keynotes',
        icon: '&#127908;',
        details: [
            'Conference talks, keynotes, and panel discussions',
            'Topics: analytics engineering, data quality, AI-readiness, documentation automation',
            'Real-world case studies with actionable takeaways',
            'Available for virtual, in-person, and hybrid events',
            'Past stages: DevFest, WriteTheDocs, move(data), KwaraBuild, WSKZ University',
        ],
        cta: { text: 'Book Me on Sessionize', url: 'https://sessionize.com/ayoade' }
    },
    training: {
        title: 'Training & Workshops',
        icon: '&#127891;',
        details: [
            'Delivered through Behind The Data Academy',
            'dbt, Snowflake, data modeling, data quality & testing',
            'CI/CD pipelines for analytics, Git-based workflows',
            'Python for data analysis, transformation, and automation',
            'Formats: multi-week bootcamps, intensive workshops, embedded team training',
            '900+ students trained across 7 countries',
        ],
        cta: { text: 'Visit Academy', url: 'https://academy.behindthedata.tech' }
    },
    consulting: {
        title: 'Consulting',
        icon: '&#128736;',
        details: [
            'Data pipeline architecture and modernization',
            'dbt implementation and migration from legacy SQL/stored procedures',
            'Documentation automation with AI/LLMs (35%+ coverage improvement)',
            'Data governance and observability frameworks',
            'Team capability assessments and hiring guidance',
            'Proven: $20K/yr saved through automation, 45% maintenance reduction',
        ],
        cta: { text: 'Get In Touch', url: 'mailto:tripleaceme@gmail.com' }
    },
    curriculum: {
        title: 'Curriculum Development',
        icon: '&#128218;',
        details: [
            'Data analytics curriculum for academies and EdTech platforms',
            'Big Data & Business Intelligence modules',
            'Data Strategy for AI Project Implementation',
            'Machine Learning Engineering course design',
            'Past clients: Bright Next Academy, CareerFoundry, Trevotech Academy, WSKZ University',
            'Tools: PowerPoint, Figma, interactive learning design',
        ],
        cta: { text: 'Discuss a Project', url: 'mailto:tripleaceme@gmail.com' }
    }
};

window.openModal = function(service) {
    const data = modalData[service];
    if (!data) return;
    const overlay = document.getElementById('modalOverlay');
    const body = document.getElementById('modalBody');
    if (!overlay || !body) return;
    body.innerHTML = `
        <div class="modal-icon">${data.icon}</div>
        <h3 class="modal-title">${data.title}</h3>
        <ul class="modal-list">
            ${data.details.map(d => `<li>${d}</li>`).join('')}
        </ul>
        <a href="${data.cta.url}" target="_blank" class="btn btn-primary modal-cta">${data.cta.text}</a>
    `;
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
};

window.closeModal = function() {
    const overlay = document.getElementById('modalOverlay');
    if (overlay) {
        overlay.classList.remove('active');
        document.body.style.overflow = '';
    }
};

const modalOverlay = document.getElementById('modalOverlay');
if (modalOverlay) {
    modalOverlay.addEventListener('click', function(e) {
        if (e.target === this) closeModal();
    });
}
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeModal();
});

// ---- Intersection Observer (fade-in on scroll) ----
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) entry.target.classList.add('visible');
    });
}, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll([
    '.service-card', '.repo-card', '.timeline-item', '.contact-card',
    '.community-badge', '.stat', '.info-card', '.exp-card',
    '.speaking-card', '.edition-card', '.mentorship-preview-card',
    '.oss-featured-card', '.writing-card', '.testimonial-card'
].join(',')).forEach(el => {
    el.classList.add('fade-in');
    observer.observe(el);
});
