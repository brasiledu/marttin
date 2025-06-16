# Configuração CSS - Landing Page

## Variáveis CSS (Custom Properties)

### Cores Principais
```css
:root {
    /* Cores de marca */
    --primary-gold: #fbbf24;
    --secondary-gold: #f59e0b;
    --tertiary-gold: #d97706;
    --dark-gold: #b45309;
    
    /* Tons de azul para contraste */
    --primary-blue: #1e3a8a;
    --secondary-blue: #3b82f6;
    
    /* Escala de cinza para texto */
    --text-light: #e2e8f0;
    --text-muted: #94a3b8;
    --text-dark: #1f2937;
    
    /* Backgrounds */
    --bg-dark-1: #0f172a;
    --bg-dark-2: #1e293b;
    --bg-dark-3: #334155;
    --bg-dark-4: #475569;
    
    /* Surfaces e overlays */
    --surface-glass: rgba(255,255,255,0.08);
    --surface-glass-hover: rgba(255,255,255,0.12);
    --border-glass: rgba(255,255,255,0.1);
    --overlay-pattern: rgba(251, 191, 36, 0.04);
}
```

### Gradientes
```css
:root {
    /* Gradiente principal do background */
    --bg-gradient: linear-gradient(135deg, 
        var(--bg-dark-1) 0%, 
        var(--bg-dark-2) 25%, 
        var(--bg-dark-3) 50%, 
        var(--bg-dark-4) 75%, 
        var(--bg-dark-2) 100%
    );
    
    /* Gradiente dos botões */
    --button-gradient: linear-gradient(135deg, 
        var(--primary-gold), 
        var(--secondary-gold)
    );
    
    /* Gradiente dos ícones */
    --icon-gradient: linear-gradient(135deg, 
        var(--primary-gold), 
        var(--secondary-gold)
    );
}
```

## Typography Scale

### Font Families
```css
:root {
    --font-primary: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    --font-weights: {
        light: 300,
        normal: 400,
        medium: 500,
        semibold: 600,
        bold: 700
    };
}
```

### Font Sizes (Desktop)
```css
:root {
    /* Headings */
    --font-size-h1: 3rem;       /* 48px */
    --font-size-h2: 2.5rem;     /* 40px */
    --font-size-h3: 1.8rem;     /* 28.8px */
    
    /* Body text */
    --font-size-large: 1.25rem; /* 20px */
    --font-size-base: 1rem;     /* 16px */
    --font-size-small: 0.95rem; /* 15.2px */
    --font-size-xs: 0.85rem;    /* 13.6px */
}
```

### Font Sizes (Mobile)
```css
@media (max-width: 768px) {
    :root {
        --font-size-h1: 2rem;       /* 32px */
        --font-size-h2: 2rem;       /* 32px */
        --font-size-h3: 1.5rem;     /* 24px */
        --font-size-large: 1.1rem;  /* 17.6px */
    }
}
```

## Spacing System

### Base Units
```css
:root {
    /* Base spacing unit */
    --space-unit: 1rem; /* 16px */
    
    /* Spacing scale */
    --space-xs: calc(var(--space-unit) * 0.25);   /* 4px */
    --space-sm: calc(var(--space-unit) * 0.5);    /* 8px */
    --space-md: calc(var(--space-unit) * 1);      /* 16px */
    --space-lg: calc(var(--space-unit) * 1.5);    /* 24px */
    --space-xl: calc(var(--space-unit) * 2);      /* 32px */
    --space-2xl: calc(var(--space-unit) * 3);     /* 48px */
    --space-3xl: calc(var(--space-unit) * 4);     /* 64px */
    --space-4xl: calc(var(--space-unit) * 6);     /* 96px */
}
```

### Section Padding
```css
:root {
    --section-padding-desktop: 6rem 2rem;
    --section-padding-mobile: 4rem 1rem;
    --container-max-width: 1200px;
}
```

## Layout System

### Grid Configurations
```css
/* Features grid */
.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: var(--space-2xl);
}

/* Benefits grid */
.benefits-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: var(--space-4xl);
    align-items: center;
}

/* Pricing grid */
.pricing-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: var(--space-xl);
}

/* Mobile adjustments */
@media (max-width: 768px) {
    .benefits-grid,
    .strategic-grid {
        grid-template-columns: 1fr;
        text-align: center;
    }
}
```

### Flexbox Patterns
```css
/* Timeline horizontal */
.process-timeline {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: var(--space-xl);
}

/* Card content vertical */
.pricing-card {
    display: flex;
    flex-direction: column;
    min-height: 600px;
}

.plan-features {
    flex-grow: 1;
}

.plan-button {
    margin-top: auto;
}
```

## Animation System

### Timing Functions
```css
:root {
    --easing-smooth: cubic-bezier(0.4, 0, 0.2, 1);
    --easing-bounce: cubic-bezier(0.68, -0.55, 0.265, 1.55);
    --easing-ease-out: ease-out;
    
    --duration-fast: 0.2s;
    --duration-normal: 0.3s;
    --duration-slow: 0.6s;
    --duration-extra-slow: 0.8s;
}
```

### Common Animations
```css
/* Hover lift effect */
.hover-lift {
    transition: transform var(--duration-normal) var(--easing-smooth);
}

.hover-lift:hover {
    transform: translateY(-10px);
}

/* Scale effect */
.hover-scale {
    transition: transform var(--duration-normal) var(--easing-smooth);
}

.hover-scale:hover {
    transform: scale(1.05);
}

/* Float animation */
@keyframes float {
    0%, 100% { 
        transform: rotate(-5deg) translate3d(0, 0, 0); 
    }
    50% { 
        transform: rotate(-5deg) translate3d(0, -20px, 0); 
    }
}

.float-animation {
    animation: float 6s ease-in-out infinite;
}
```

### Performance Optimizations
```css
/* Hardware acceleration */
.gpu-accelerated {
    transform: translate3d(0, 0, 0);
    backface-visibility: hidden;
    perspective: 1000px;
    will-change: transform;
}

/* Layout containment */
.contained {
    contain: layout style paint;
}
```

## Component Styles

### Glass Cards
```css
.glass-card {
    background: var(--surface-glass);
    backdrop-filter: blur(8px);
    border: 1px solid var(--border-glass);
    border-radius: 20px;
    box-shadow: 0 25px 50px rgba(0,0,0,0.25);
    transition: all var(--duration-normal) var(--easing-smooth);
}

.glass-card:hover {
    background: var(--surface-glass-hover);
    transform: translateY(-10px);
    box-shadow: 0 35px 70px rgba(0,0,0,0.3);
}
```

### Buttons
```css
.btn-primary {
    background: var(--primary-gold);
    color: var(--primary-blue);
    padding: 1rem 2rem;
    border: none;
    border-radius: 30px;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all var(--duration-normal) var(--easing-smooth);
    text-decoration: none;
    display: inline-block;
}

.btn-primary:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(251, 191, 36, 0.3);
    color: var(--primary-blue);
    text-decoration: none;
}

.btn-outline {
    background: transparent;
    color: var(--primary-gold);
    border: 2px solid var(--primary-gold);
    padding: 1rem 2rem;
    border-radius: 30px;
    font-weight: 600;
    font-size: 1.1rem;
    cursor: pointer;
    transition: all var(--duration-normal) var(--easing-smooth);
}

.btn-outline:hover {
    background: var(--primary-gold);
    color: var(--primary-blue);
    transform: translateY(-2px);
}
```

### Icons
```css
.icon-circle {
    width: 80px;
    height: 80px;
    background: var(--icon-gradient);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    color: var(--primary-blue);
    box-shadow: 0 10px 30px rgba(251, 191, 36, 0.3);
    margin: 0 auto 2rem;
}
```

## Responsive Design

### Breakpoints
```css
/* Mobile first approach */
:root {
    --breakpoint-sm: 576px;
    --breakpoint-md: 768px;
    --breakpoint-lg: 992px;
    --breakpoint-xl: 1200px;
}

/* Usage */
@media (max-width: 768px) {
    /* Mobile styles */
}

@media (min-width: 769px) and (max-width: 992px) {
    /* Tablet styles */
}

@media (min-width: 993px) {
    /* Desktop styles */
}
```

### Container Queries (Future)
```css
/* Para quando container queries tiver melhor suporte */
@container (max-width: 600px) {
    .pricing-card {
        grid-template-columns: 1fr;
    }
}
```

## Dark Mode Support

### CSS Variables Override
```css
@media (prefers-color-scheme: dark) {
    :root {
        /* Já está em dark mode por padrão */
        /* Manter valores atuais */
    }
}

@media (prefers-color-scheme: light) {
    :root {
        /* Override para light mode se necessário */
        --bg-dark-1: #ffffff;
        --bg-dark-2: #f8fafc;
        --text-light: #1f2937;
        --text-muted: #6b7280;
    }
}
```

## Accessibility

### Focus States
```css
.focusable {
    outline: none;
    transition: box-shadow var(--duration-fast) var(--easing-smooth);
}

.focusable:focus-visible {
    box-shadow: 0 0 0 3px rgba(251, 191, 36, 0.5);
    outline: 2px solid var(--primary-gold);
    outline-offset: 2px;
}
```

### Reduced Motion
```css
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}
```

### High Contrast
```css
@media (prefers-contrast: high) {
    :root {
        --primary-gold: #ffdc00;
        --text-light: #ffffff;
        --border-glass: rgba(255,255,255,0.5);
    }
}
```
