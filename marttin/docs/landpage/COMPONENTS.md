# Componentes da Landing Page

## 1. Hero Section

### Estrutura
```html
<section class="hero">
    <div class="hero-content">
        <div class="hero-text">
            <!-- Título, subtítulo e CTA -->
        </div>
        <div class="hero-visual">
            <!-- Phone mockup com chat demo -->
        </div>
    </div>
</section>
```

### Características
- **Layout**: Grid 2 colunas (1 coluna em mobile)
- **Background**: Gradiente diagonal com overlay patterns
- **Animações**: Phone mockup com float animation
- **CTA Dinâmico**: Muda baseado no status de login

### CSS Classes Principais
- `.hero` - Container principal
- `.hero-content` - Grid layout
- `.hero-text` - Conteúdo textual
- `.hero-visual` - Container do mockup
- `.phone-mockup` - Mockup do celular
- `.floating-elements` - Ícones flutuantes

---

## 2. Features Section

### Estrutura
```html
<section class="features" id="servicos">
    <div class="features-container">
        <div class="features-header">
            <!-- Título da seção -->
        </div>
        <div class="features-grid">
            <!-- 3 feature cards -->
        </div>
    </div>
</section>
```

### Características
- **Layout**: Grid auto-fit, minmax(300px, 1fr)
- **Cards**: Glassmorphism effect
- **Hover**: Transform translateY(-10px)
- **Icons**: Gradient background circles

### CSS Classes Principais
- `.features` - Section container
- `.features-grid` - Auto-fit grid
- `.feature-card` - Individual cards
- `.feature-icon` - Circular icon containers
- `.feature-card::before` - Top gradient line

---

## 3. Process Timeline (Como Funciona)

### Estrutura
```html
<section class="process-section" id="como-funciona">
    <div class="process-container">
        <div class="process-header">
            <!-- Título e descrição -->
        </div>
        <div class="process-timeline">
            <!-- 3 process steps -->
        </div>
    </div>
</section>
```

### Características
- **Layout**: Flex horizontal (vertical em mobile)
- **Conectores**: Linha CSS pseudo-element
- **Animação**: Sequential slide-up entrance
- **Altura uniforme**: 240px para todos os containers

### CSS Classes Principais
- `.process-timeline` - Flex container
- `.process-step` - Individual steps
- `.step-number` - Circular numbered badges
- `.step-content` - Content containers
- `.process-timeline::before` - Connecting line

### Animações
```css
@keyframes slideUpIn {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
```

---

## 4. Dashboard Mockup (Documentos Inteligentes)

### Estrutura
```html
<section class="benefits">
    <div class="benefits-container">
        <div class="benefits-grid">
            <div class="benefits-content">
                <!-- Texto explicativo -->
            </div>
            <div class="benefits-visual">
                <div class="dashboard-mockup">
                    <!-- Chat simulation -->
                </div>
            </div>
        </div>
    </div>
</section>
```

### Características
- **Tamanho**: 620px x 480px (responsivo)
- **Efeito**: Shimmer animation
- **Conteúdo**: Chat messages simulados
- **Interação**: Hover scale effect
- **Remoção**: Robot icon removido do header

### CSS Classes Principais
- `.dashboard-mockup` - Container principal
- `.dashboard-content` - Conteúdo interno
- `.dashboard-header` - Header com status
- `.chat-simulation` - Container das mensagens
- `.chat-message` - Mensagens individuais
- `.processing-indicator` - Indicador de processamento

---

## 5. Strategic Objectives Carousel

### Estrutura
```html
<section class="strategic-objectives" id="objetivos-estrategicos">
    <div class="strategic-container">
        <div class="strategic-grid">
            <!-- Content + Visual -->
        </div>
        <div class="carousel-dots">
            <!-- Navigation dots -->
        </div>
    </div>
</section>
```

### Características
- **Slides**: 4 dashboard views diferentes
- **Auto-rotate**: 5 segundos
- **Navegação**: Click nos dots
- **Transições**: Opacity + translateX
- **Charts**: Different types per dashboard

### Dashboard Views
1. **Sales Dashboard**: Green theme, bar chart
2. **Marketing Dashboard**: Purple theme, pattern chart  
3. **Financial Dashboard**: Yellow theme, pie chart
4. **Goals Dashboard**: Red theme, progress circles

### CSS Classes Principais
- `.laptop-mockup` - Laptop container
- `.laptop-screen` - Screen area
- `.dashboard-view` - Individual dashboard
- `.carousel-dots` - Navigation
- `.carousel-dot` - Individual dot

### JavaScript Functionality
```javascript
function switchDashboard(index) {
    // Remove active classes
    // Add active to selected
    // Update current slide
}
```

---

## 6. Pricing Section

### Estrutura
```html
<section class="pricing" id="planos">
    <div class="pricing-container">
        <div class="pricing-header">
            <!-- Section title -->
        </div>
        <div class="pricing-grid">
            <!-- 3 pricing cards -->
        </div>
    </div>
</section>
```

### Características
- **Layout**: Auto-fit grid, minmax(320px, 1fr)
- **Featured Card**: Scale(1.05) + special styling
- **Alignment**: Flexbox para botões alinhados
- **Height**: min-height: 600px
- **Buttons**: margin-top: auto para alinhamento

### Pricing Plans
1. **Essencial**: R$ 29,90/mês
2. **Profissional**: R$ 59,90/mês (Featured)
3. **Performance**: R$ 99,90/mês

### CSS Classes Principais
- `.pricing-grid` - Grid container
- `.pricing-card` - Individual cards
- `.pricing-card.featured` - Highlighted card
- `.popular-badge` - "Mais Popular" badge
- `.plan-features` - Features list
- `.plan-button` - CTA buttons

---

## 7. CTA Section

### Estrutura
```html
<section class="cta-section">
    <div class="cta-content">
        <!-- Final call to action -->
    </div>
</section>
```

### Características
- **Layout**: Centered content
- **Background**: Transparent com overlay
- **Button**: Conditional baseado em auth status
- **Typography**: Large, impactful text

---

## Componentes Comuns

### Glassmorphism Cards
```css
.glass-card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 20px;
    box-shadow: 0 25px 50px rgba(0,0,0,0.25);
}
```

### Gradient Buttons
```css
.cta-button {
    background: #fbbf24;
    color: #1e3a8a;
    border-radius: 30px;
    transition: all 0.3s ease;
}

.cta-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(251, 191, 36, 0.3);
}
```

### Animated Elements
- **Float Animation**: Phone mockup
- **Bounce Animation**: Floating icons
- **Pulse Animation**: Status indicators
- **Shimmer Animation**: Dashboard overlay
- **Grow Animation**: Metric bars

### Performance Optimizations
- **Transform 3D**: Hardware acceleration
- **Will-change**: Compositing hints
- **Contain**: Layout containment
- **RequestAnimationFrame**: Smooth animations
- **Event Delegation**: Reduced event listeners
