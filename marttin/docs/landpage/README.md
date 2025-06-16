# Documentação da Landing Page - Marttin AI

## Visão Geral

A landing page do Marttin AI é uma página moderna e responsiva construída em Django que apresenta o produto de consultoria empresarial por IA. Foi desenvolvida com foco em conversão, experiência do usuário e performance.

## Arquitetura da Página

### Sistema de Autenticação Diferencial
- **Usuários não logados**: Acesso apenas ao chat demo limitado
- **Usuários logados**: Redirecionamento automático para dashboard completo
- **Lógica implementada**: Template tags condicionais `{% if user.is_authenticated %}`

### Estrutura de Seções

1. **Hero Section** - Apresentação principal
2. **Features Section** - Benefícios e funcionalidades
3. **Como Funciona** - Processo em 3 etapas
4. **Documentos Inteligentes** - Demonstração visual
5. **Objetivos Estratégicos** - Dashboard interativo com carousel
6. **Planos** - Estrutura de preços
7. **CTA Final** - Chamada para ação

## Sistema de Cores e Design

### Paleta de Cores Principal
```css
/* Gradiente de fundo */
background: linear-gradient(135deg, #0f172a 0%, #1e293b 25%, #334155 50%, #475569 75%, #1e293b 100%);

/* Cores de destaque */
--primary-gold: #fbbf24;
--secondary-gold: #f59e0b;
--text-light: #e2e8f0;
--text-muted: #94a3b8;
--dark-surface: rgba(255,255,255,0.08);
```

### Efeitos Visuais
- **Glassmorphism**: `backdrop-filter: blur(8px)`
- **Animações suaves**: Transform 3D para performance
- **Sombras profundas**: Box-shadow múltiplas camadas
- **Gradientes**: Linear e conic para elementos visuais

## Componentes Interativos

### 1. Dashboard Mockup (Seção Documentos)
- **Localização**: `.dashboard-mockup`
- **Tamanho**: 620px x 480px (aumentado para melhor visualização)
- **Características**: Chat simulation em tempo real
- **Ícone removido**: Robot icon removido conforme solicitação

### 2. Carousel de Dashboard (Objetivos Estratégicos)
- **Slides**: 4 dashboards diferentes (Vendas, Marketing, Financeiro, Objetivos)
- **Auto-rotação**: 5 segundos entre slides
- **Interatividade**: Click nos dots para navegação manual
- **Transições**: Smooth transform animations

### 3. Timeline de Processo (Como Funciona)
- **Layout**: 3 steps horizontais com linha conectora
- **Responsive**: Empilhamento vertical em mobile
- **Animação**: Entrada sequencial com delay
- **Altura uniforme**: Todos containers com mesma altura (240px)

## Sistema Responsivo

### Breakpoints
```css
@media (max-width: 768px) {
    /* Mobile adjustments */
}
```

### Ajustes Principais
- **Grid Layout**: 2 colunas → 1 coluna
- **Font Sizes**: Redução proporcional
- **Containers**: Max-width 100% e height ajustado
- **Timeline**: Flex-direction column
- **Pricing Cards**: Grid de 3 → 1 coluna

## Performance e Otimizações

### JavaScript Otimizado
- **Event Delegation**: Reduz listeners
- **RequestAnimationFrame**: Animações suaves
- **Intersection Observer**: Lazy loading de animações
- **Debounced Scroll**: Performance em scroll
- **Prefers-reduced-motion**: Acessibilidade

### CSS Performance
- **Transform 3D**: Hardware acceleration
- **Will-change**: Otimização de compositing
- **Contain**: Layout containment
- **Passive Event Listeners**: Scroll performance

## Estrutura de Arquivos

```
agent/templates/agent/
├── index.html          # Landing page principal
├── base.html           # Template base
└── chat.html           # Interface de chat demo

agent/static/agent/
└── css/
    └── style.css       # Estilos auxiliares (se necessário)
```

## Configurações do Django

### URLs
```python
# agent/urls.py
urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat_view, name='chat'),
    # ... outras rotas
]
```

### Views
```python
# agent/views.py
def index(request):
    return render(request, 'agent/index.html')

def chat_view(request):
    # Sem @login_required para permitir demo
    return render(request, 'agent/chat.html')
```

## Funcionalidades Especiais

### Chat Demo para Não-Logados
- **Banner informativo**: Indica limitações da demo
- **Respostas limitadas**: 3-4 respostas pré-definidas
- **CTA para upgrade**: Incentiva cadastro

### Sistema de Pricing Cards
- **Flexbox alignment**: Botões alinhados no final
- **Featured card**: Destaque visual com badge
- **Hover effects**: Transformações suaves

## Manutenção e Atualizações

### Para adicionar nova seção:
1. Criar HTML na estrutura apropriada
2. Adicionar CSS seguindo padrão de nomenclatura
3. Implementar animações com Intersection Observer
4. Testar responsividade em mobile

### Para modificar cores:
1. Atualizar variáveis CSS no início do style
2. Verificar contraste de acessibilidade
3. Testar em modo escuro/claro

### Para otimizar performance:
1. Usar transform 3D para animações
2. Implementar lazy loading para imagens
3. Minificar CSS em produção
4. Comprimir imagens

## Métricas de Performance

### Objetivos:
- **First Contentful Paint**: < 1.5s
- **Largest Contentful Paint**: < 2.5s
- **Cumulative Layout Shift**: < 0.1
- **Time to Interactive**: < 3s

### Ferramentas de Monitoramento:
- Google PageSpeed Insights
- Chrome DevTools Lighthouse
- WebPageTest

## Acessibilidade

### Implementado:
- Semantic HTML structure
- Alt text para imagens decorativas
- Focus states para interatividade
- Prefers-reduced-motion support
- Contraste adequado de cores

### Para melhorar:
- ARIA labels em elementos interativos
- Keyboard navigation completa
- Screen reader testing
- Color-blind friendly palette

## SEO e Meta Tags

### Implementado no base.html:
```html
<title>Marttin AI - Consultoria Empresarial por IA</title>
<meta name="description" content="...">
<meta property="og:title" content="...">
<meta property="og:description" content="...">
```

### Estrutura para SEO:
- Heading hierarchy (H1 → H2 → H3)
- Semantic HTML tags
- Internal linking structure
- Fast loading times
