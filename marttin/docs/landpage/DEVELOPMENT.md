# Guia de Desenvolvimento - Landing Page

## Setup do Ambiente

### Pré-requisitos
- Python 3.12+
- Django 4.2+
- Node.js (para ferramentas de build, se necessário)

### Estrutura de Arquivos
```
marttin/
├── agent/
│   ├── templates/
│   │   ├── base.html
│   │   └── agent/
│   │       └── index.html      # Landing page principal
│   ├── static/
│   │   └── agent/
│   │       ├── css/
│   │       ├── js/
│   │       └── images/
│   ├── views.py
│   └── urls.py
└── docs/
    └── landpage/               # Esta documentação
```

## Padrões de Código

### CSS Architecture

#### 1. Nomenclatura BEM-like
```css
/* Block */
.hero { }

/* Block + Element */
.hero-content { }
.hero-text { }
.hero-visual { }

/* Block + Modifier */
.pricing-card { }
.pricing-card.featured { }
```

#### 2. Organização de CSS
```css
/* 1. Reset e Base */
* { margin: 0; padding: 0; box-sizing: border-box; }

/* 2. Variáveis (Custom Properties) */
:root {
    --primary-gold: #fbbf24;
    --text-light: #e2e8f0;
}

/* 3. Layout Sections */
.hero { }
.features { }
.benefits { }

/* 4. Components */
.feature-card { }
.pricing-card { }

/* 5. Utilities */
.highlight { color: var(--primary-gold); }

/* 6. Responsive */
@media (max-width: 768px) { }
```

#### 3. Performance CSS
```css
/* Hardware Acceleration */
.animated-element {
    transform: translate3d(0, 0, 0);
    backface-visibility: hidden;
    will-change: transform;
}

/* Layout Containment */
.component {
    contain: layout style paint;
}
```

### JavaScript Patterns

#### 1. Event Delegation
```javascript
// ❌ Não fazer - Múltiplos listeners
buttons.forEach(btn => btn.addEventListener('click', handler));

// ✅ Fazer - Event delegation
document.addEventListener('click', function(e) {
    const button = e.target.closest('.target-class');
    if (button) {
        handler(e);
    }
});
```

#### 2. Performance Optimization
```javascript
// RequestAnimationFrame para animações
function smoothAnimation() {
    requestAnimationFrame(() => {
        element.style.transform = 'translateY(-10px)';
    });
}

// Intersection Observer para lazy loading
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate');
            observer.unobserve(entry.target);
        }
    });
});
```

#### 3. Clean Up
```javascript
// Sempre limpar listeners
window.addEventListener('beforeunload', () => {
    if (rafId) cancelAnimationFrame(rafId);
    if (timer) clearTimeout(timer);
    observer.disconnect();
});
```

## Workflow de Desenvolvimento

### 1. Adicionando Nova Seção

#### Passo 1: HTML Structure
```html
<section class="new-section" id="nova-secao">
    <div class="new-section-container">
        <div class="new-section-header">
            <h2>Título da <span class="highlight">Seção</span></h2>
        </div>
        <div class="new-section-content">
            <!-- Conteúdo -->
        </div>
    </div>
</section>
```

#### Passo 2: CSS Styling
```css
/* Container principal */
.new-section {
    padding: 6rem 2rem;
    background: transparent;
    position: relative;
}

.new-section-container {
    max-width: 1200px;
    margin: 0 auto;
    position: relative;
    z-index: 2;
}

/* Responsive */
@media (max-width: 768px) {
    .new-section {
        padding: 4rem 1rem;
    }
}
```

#### Passo 3: JavaScript Interaction
```javascript
// Adicionar ao observer para animações
const newElements = document.querySelectorAll('.new-section-element');
newElements.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(50px)';
    animationObserver.observe(el);
});
```

### 2. Modificando Componentes Existentes

#### Carousel Example
```javascript
// Para adicionar novo slide ao carousel
function addCarouselSlide(content, index) {
    const newSlide = document.createElement('div');
    newSlide.className = 'dashboard-view';
    newSlide.setAttribute('data-view', index);
    newSlide.innerHTML = content;
    
    dashboardContainer.appendChild(newSlide);
    
    // Adicionar dot
    const newDot = document.createElement('span');
    newDot.className = 'carousel-dot';
    dotsContainer.appendChild(newDot);
}
```

### 3. Testing Guidelines

#### Visual Testing
```bash
# Testar em diferentes resoluções
# Desktop: 1920x1080, 1366x768
# Tablet: 768x1024
# Mobile: 375x667, 414x896

# Browsers suportados
# Chrome 90+
# Firefox 88+
# Safari 14+
# Edge 90+
```

#### Performance Testing
```javascript
// Lighthouse metrics targets
const performanceTargets = {
    'First Contentful Paint': '< 1.5s',
    'Largest Contentful Paint': '< 2.5s',
    'Cumulative Layout Shift': '< 0.1',
    'Time to Interactive': '< 3s'
};
```

## Debugging Common Issues

### 1. Layout Quebrado
```css
/* Debug grid/flexbox */
.debug * {
    outline: 1px solid red;
}

/* Check box-sizing */
* {
    box-sizing: border-box; /* Sempre incluir */
}
```

### 2. Animações Lentas
```css
/* Verificar will-change */
.animated-element {
    will-change: transform; /* Durante animação */
    will-change: auto;      /* Após animação */
}

/* Usar transform em vez de position */
/* ❌ */ left: 100px;
/* ✅ */ transform: translateX(100px);
```

### 3. JavaScript Errors
```javascript
// Verificar se elementos existem
const element = document.querySelector('.target');
if (element) {
    // Código seguro
}

// Event delegation para elementos dinâmicos
document.addEventListener('click', function(e) {
    const target = e.target.closest('.dynamic-element');
    if (target) {
        // Handle click
    }
});
```

## Deployment Checklist

### Antes do Deploy
- [ ] Minificar CSS (se usando build process)
- [ ] Otimizar imagens (WebP, tamanhos corretos)
- [ ] Testar em múltiplos browsers
- [ ] Validar HTML (W3C Validator)
- [ ] Verificar console errors
- [ ] Testar performance (Lighthouse)
- [ ] Verificar responsive design
- [ ] Testar carregamento lento
- [ ] Verificar acessibilidade básica

### Pós Deploy
- [ ] Verificar todas as seções carregam
- [ ] Testar interações (carousel, buttons)
- [ ] Verificar analytics tracking
- [ ] Monitorar Core Web Vitals
- [ ] Testar formulários (se houver)

## Manutenção

### Updates de Conteúdo
```html
<!-- Para alterar textos, buscar por: -->
<h1>Controle seu negócio e <span class="highlight">economize tempo</span></h1>
<p class="subtitle">Consultoria empresarial por IA...</p>
```

### Updates de Estilo
```css
/* Para alterar cores, modificar variáveis: */
:root {
    --primary-gold: #fbbf24;    /* Cor principal */
    --secondary-gold: #f59e0b;  /* Cor secundária */
    --text-light: #e2e8f0;     /* Texto claro */
}
```

### Performance Monitoring
```javascript
// Monitorar métricas importantes
const observer = new PerformanceObserver((list) => {
    for (const entry of list.getEntries()) {
        console.log(`${entry.name}: ${entry.value}ms`);
    }
});

observer.observe({ entryTypes: ['largest-contentful-paint'] });
```

## Troubleshooting

### Issue: Seção não aparece
1. Verificar CSS `display` property
2. Verificar `z-index` conflicts
3. Verificar `overflow: hidden` em parents
4. Verificar JavaScript errors no console

### Issue: Animações não funcionam
1. Verificar `will-change` property
2. Verificar browser support para CSS properties
3. Verificar JavaScript animation triggers
4. Verificar `prefers-reduced-motion`

### Issue: Performance ruim
1. Verificar heavy CSS properties (box-shadow, filter)
2. Verificar JavaScript loops em scroll events
3. Verificar image optimization
4. Verificar número de DOM elements

### Issue: Mobile quebrado
1. Verificar viewport meta tag
2. Verificar media queries
3. Verificar touch event handling
4. Verificar font sizes mínimos
