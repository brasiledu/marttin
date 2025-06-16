# Troubleshooting Guide - Landing Page

## Problemas Comuns e Soluções

### 1. Layout e CSS

#### Problema: Seção não aparece na tela
**Sintomas:**
- Seção existe no HTML mas não é visível
- Conteúdo "cortado" ou escondido

**Possíveis Causas:**
```css
/* 1. Display property incorreto */
.section { display: none; } /* ❌ */
.section { display: block; } /* ✅ */

/* 2. Z-index conflicts */
.section { z-index: -1; } /* ❌ */
.section { z-index: 2; } /* ✅ */

/* 3. Overflow hidden em parent */
.parent { overflow: hidden; height: 100px; } /* ❌ */
.parent { overflow: visible; } /* ✅ */

/* 4. Position absolute sem coordenadas */
.section { position: absolute; } /* ❌ */
.section { position: absolute; top: 0; left: 0; } /* ✅ */
```

**Como debugar:**
```javascript
// No console do navegador
const element = document.querySelector('.problematic-section');
console.log('Element:', element);
console.log('Computed styles:', getComputedStyle(element));
console.log('Bounding rect:', element.getBoundingClientRect());
console.log('Offset parent:', element.offsetParent);
```

#### Problema: Cards não alinhados (pricing section)
**Sintomas:**
- Botões em alturas diferentes
- Cards com tamanhos desiguais

**Solução:**
```css
.pricing-card {
    display: flex;
    flex-direction: column;
    min-height: 600px; /* Altura mínima fixa */
}

.plan-features {
    flex-grow: 1; /* Cresce para preencher espaço */
}

.plan-button {
    margin-top: auto; /* Empurra para o final */
}
```

#### Problema: Timeline (Como Funciona) com alturas diferentes
**Sintomas:**
- Containers de tamanhos desiguais
- Layout inconsistente

**Solução:**
```css
.process-step {
    min-height: 360px; /* Altura mínima fixa */
    height: 360px; /* Altura fixa */
}

.step-content {
    min-height: 240px; /* Altura mínima do conteúdo */
    display: flex;
    flex-direction: column;
    justify-content: center;
}
```

### 2. Responsividade

#### Problema: Layout quebrado no mobile
**Sintomas:**
- Elementos sobrepostos
- Texto muito pequeno
- Scroll horizontal

**Verificações:**
```html
<!-- 1. Viewport meta tag obrigatória -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

```css
/* 2. Box-sizing global */
* {
    box-sizing: border-box; /* Obrigatório */
}

/* 3. Max-width em containers */
.container {
    max-width: 100%;
    overflow-x: hidden;
}

/* 4. Media queries corretas */
@media (max-width: 768px) {
    .grid-2-cols {
        grid-template-columns: 1fr; /* 2 cols → 1 col */
    }
}
```

#### Problema: Dashboard mockup muito pequeno no mobile
**Solução:**
```css
@media (max-width: 768px) {
    .dashboard-mockup {
        max-width: 100%;
        height: 350px; /* Altura reduzida para mobile */
    }
    
    .chat-message {
        font-size: 0.7rem; /* Texto menor */
        padding: 8px 10px;
    }
}
```

### 3. Performance

#### Problema: Animações lentas ou travando
**Sintomas:**
- FPS baixo durante animações
- Delay perceptível em hover effects
- Scroll não suave

**Soluções:**
```css
/* 1. Hardware acceleration */
.animated-element {
    transform: translate3d(0, 0, 0);
    backface-visibility: hidden;
    will-change: transform; /* Durante animação */
}

/* 2. Evitar animações custosas */
/* ❌ Evitar */
.element {
    transition: width 0.3s, height 0.3s, box-shadow 0.3s;
}

/* ✅ Preferir */
.element {
    transition: transform 0.3s, opacity 0.3s;
}

/* 3. Layout containment */
.component {
    contain: layout style paint;
}
```

**JavaScript optimizations:**
```javascript
// ❌ Evitar direct DOM updates
element.style.left = '100px';

// ✅ Usar requestAnimationFrame
requestAnimationFrame(() => {
    element.style.transform = 'translateX(100px)';
});

// ❌ Evitar scroll listeners diretos
window.addEventListener('scroll', handleScroll);

// ✅ Usar debounced scroll
const debouncedScroll = debounce(handleScroll, 16);
window.addEventListener('scroll', debouncedScroll, { passive: true });
```

#### Problema: Console errors durante animações
**Erro comum:**
```
Cannot read property 'style' of null
```

**Solução:**
```javascript
// ❌ Sem verificação
element.style.transform = 'translateY(0)';

// ✅ Com verificação
if (element && element.style) {
    element.style.transform = 'translateY(0)';
}

// ✅ Ainda melhor - function utilitária
function safeSetStyle(element, property, value) {
    if (element && element.style && property in element.style) {
        element.style[property] = value;
        return true;
    }
    return false;
}
```

### 4. JavaScript

#### Problema: Carousel não funciona
**Sintomas:**
- Dots não respondem a clicks
- Auto-rotate não funciona
- Dashboard views não mudam

**Debug steps:**
```javascript
// 1. Verificar se elementos existem
console.log('Dots:', document.querySelectorAll('.carousel-dot'));
console.log('Views:', document.querySelectorAll('.dashboard-view'));

// 2. Verificar event listeners
document.addEventListener('click', function(e) {
    console.log('Clicked:', e.target);
    const dot = e.target.closest('.carousel-dot');
    console.log('Is dot:', !!dot);
});

// 3. Verificar CSS classes
const activeView = document.querySelector('.dashboard-view.active');
console.log('Active view:', activeView);
```

**Soluções comuns:**
```javascript
// Garantir que DOM está carregado
document.addEventListener('DOMContentLoaded', function() {
    initCarousel();
});

// Event delegation correta
document.addEventListener('click', function(e) {
    const dot = e.target.closest('.carousel-dot');
    if (dot) {
        const index = Array.from(document.querySelectorAll('.carousel-dot')).indexOf(dot);
        switchDashboard(index);
    }
});
```

#### Problema: Intersection Observer não funciona
**Sintomas:**
- Animações não disparam
- Elementos permanecem invisíveis

**Verificações:**
```javascript
// 1. Verificar suporte do browser
if ('IntersectionObserver' in window) {
    console.log('IntersectionObserver supported');
} else {
    console.log('IntersectionObserver NOT supported - implement fallback');
}

// 2. Debug observer
const observer = new IntersectionObserver(function(entries) {
    console.log('Observer triggered:', entries);
    entries.forEach(entry => {
        console.log('Element:', entry.target);
        console.log('Is intersecting:', entry.isIntersecting);
        console.log('Intersection ratio:', entry.intersectionRatio);
    });
});

// 3. Verificar threshold e rootMargin
const observerOptions = {
    threshold: [0, 0.1], // Trigger at 0% and 10% visibility
    rootMargin: '0px 0px -50px 0px' // 50px antes do bottom
};
```

### 5. Browser Compatibility

#### Problema: Glassmorphism não funciona
**Sintomas:**
- backdrop-filter não aplicado
- Cards aparecem opacas

**Fallback:**
```css
.glass-card {
    background: rgba(255,255,255,0.08);
    
    /* Fallback para browsers sem backdrop-filter */
    background: rgba(255,255,255,0.15);
    
    /* Aplicar backdrop-filter se suportado */
    backdrop-filter: blur(8px);
}

/* Detectar suporte via CSS */
@supports (backdrop-filter: blur(8px)) {
    .glass-card {
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(8px);
    }
}
```

#### Problema: CSS Grid não funciona
**Fallback para Flexbox:**
```css
/* Fallback com flexbox */
.features-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 2rem;
}

.feature-card {
    flex: 1 1 300px;
}

/* Override com Grid se suportado */
@supports (display: grid) {
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    }
    
    .feature-card {
        flex: none;
    }
}
```

### 6. Debug Tools

#### CSS Debug Outline
```css
/* Adicionar temporariamente para debug */
.debug * {
    outline: 1px solid red !important;
}

.debug .grid-container {
    outline: 2px solid blue !important;
}

.debug .flex-container {
    outline: 2px solid green !important;
}
```

#### JavaScript Debug Functions
```javascript
// Função para debug de performance
function debugPerformance(name, fn) {
    const start = performance.now();
    const result = fn();
    const end = performance.now();
    console.log(`⏱️ ${name}: ${(end - start).toFixed(2)}ms`);
    return result;
}

// Função para debug de elementos
function debugElement(selector) {
    const element = document.querySelector(selector);
    if (!element) {
        console.error(`❌ Element not found: ${selector}`);
        return;
    }
    
    console.group(`🔍 Debug: ${selector}`);
    console.log('Element:', element);
    console.log('Computed styles:', getComputedStyle(element));
    console.log('Bounding rect:', element.getBoundingClientRect());
    console.log('Offset parent:', element.offsetParent);
    console.log('Classes:', Array.from(element.classList));
    console.groupEnd();
}

// Função para debug de observers
function debugIntersectionObserver() {
    const elements = document.querySelectorAll('[data-animate]');
    console.log(`📊 Found ${elements.length} elements to observe`);
    
    elements.forEach((el, index) => {
        const rect = el.getBoundingClientRect();
        console.log(`Element ${index}:`, {
            element: el,
            isVisible: rect.top < window.innerHeight && rect.bottom > 0,
            rect: rect
        });
    });
}
```

### 7. Checklist de Troubleshooting

#### Quando algo não funciona:

1. **Verificar Console Errors**
   ```javascript
   // Abrir DevTools → Console
   // Verificar erros em vermelho
   ```

2. **Verificar Network Tab**
   ```
   // DevTools → Network
   // Verificar se todos os recursos carregaram
   // Status 404, 500, etc.
   ```

3. **Verificar Elements/DOM**
   ```
   // DevTools → Elements
   // Verificar se HTML está correto
   // Verificar CSS aplicado
   ```

4. **Testar sem JavaScript**
   ```
   // DevTools → Settings → Debugger → Disable JavaScript
   // Verificar se layout funciona sem JS
   ```

5. **Verificar Responsive**
   ```
   // DevTools → Toggle Device Toolbar
   // Testar diferentes resoluções
   ```

#### Quick Fixes Comuns:

```javascript
// 1. Forçar reflow se layout está quebrado
element.offsetHeight;

// 2. Limpar cache de estilos
document.documentElement.style.display = 'none';
document.documentElement.offsetHeight;
document.documentElement.style.display = '';

// 3. Reinicializar observers
observer.disconnect();
elements.forEach(el => observer.observe(el));

// 4. Reset de animações
element.style.animation = 'none';
element.offsetHeight;
element.style.animation = null;
```
