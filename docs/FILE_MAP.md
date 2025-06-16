# 📂 MARTTIN AI - Mapa de Arquivos

Este documento serve como um guia de navegação pelos arquivos principais do projeto MARTTIN AI.

## 📋 Arquivos de Configuração na Raiz

### Essenciais
- **`README.md`** - Documentação principal do projeto
- **`CHANGELOG.md`** - Histórico de versões e mudanças
- **`DOCS_INDEX.md`** - Índice rápido da documentação
- **`requirements.txt`** - Dependências Python
- **`setup.sh`** - Script de instalação automática

### Docker & Deploy
- **`Dockerfile`** - Configuração do container
- **`docker-compose.yml`** - Orquestração de containers
- **`.env.example`** - Exemplo de variáveis de ambiente

## 📚 Documentação (`docs/`)

### Principais
- **`docs/README.md`** - Índice geral da documentação
- **`docs/PROJECT_OVERVIEW.md`** - Visão geral executiva
- **`docs/QUICK_REFERENCE.md`** - Comandos e referências rápidas
- **`docs/TESTING.md`** - Guia de testes

### Por Categoria
```
docs/
├── setup/
│   └── QUICKSTART.md          # Setup em 5 minutos
├── team/
│   └── TEAM_ONBOARDING.md     # Onboarding da equipe
├── development/
│   └── CONTRIBUTING.md        # Guia de contribuição
├── architecture/
│   ├── SYSTEM_ARCHITECTURE.md # Arquitetura do sistema
│   └── DETAILED_ARCHITECTURE.md # Detalhes técnicos
├── api/
│   └── openapi.yaml          # Especificação da API
└── deployment/
    └── DEPLOYMENT.md         # Guia de deploy
```

## 🏗️ Código Principal (`marttin/`)

### Django Core
- **`marttin/manage.py`** - CLI do Django
- **`marttin/marttin/settings.py`** - Configurações principais
- **`marttin/marttin/urls.py`** - URLs principais
- **`marttin/marttin/wsgi.py`** - WSGI para produção

### App Principal (`marttin/agent/`)

#### Backend
- **`models.py`** - Modelos de dados (User, Company, MarketingAnalysis)
- **`views.py`** - Lógica de negócio e views
- **`urls.py`** - URLs do app
- **`admin.py`** - Interface administrativa
- **`ai_agent.py`** - Integração com IA
- **`ai_service.py`** - Serviços de IA

#### Frontend Templates (`marttin/agent/templates/`)
- **`base.html`** - Template base com header/footer
- **`base_landing.html`** - Template para landing page
- **`agent/dashboard.html`** - Dashboard principal
- **`agent/marketing_analysis.html`** - Página de análise
- **`agent/content_ideas.html`** - Geração de conteúdo
- **`agent/chat.html`** - Interface de chat
- **`agent/index.html`** - Página inicial
- **`registration/login.html`** - Página de login
- **`registration/signup.html`** - Página de cadastro

#### Assets (`marttin/agent/static/agent/`)
- **`css/style.css`** - Estilos principais
- **`js/`** - Scripts JavaScript
- **`images/`** - Imagens e ícones

### Middleware & Utilitários
- **`middleware/rate_limiting.py`** - Rate limiting
- **`middleware/prometheus_metrics.py`** - Métricas
- **`management/commands/generate_api_docs.py`** - Geração de docs

### Testes
- **`tests.py`** - Testes unitários
- **`tests/test_e2e_selenium.py`** - Testes end-to-end

### Migrações
- **`migrations/0001_initial.py`** - Migração inicial
- **`migrations/__init__.py`** - Inicialização do módulo

## 📊 Logs (`marttin/logs/`)

- **`marttin.log`** - Logs gerais da aplicação
- **`errors.log`** - Logs de erro
- **`ai_agent.log`** - Logs específicos da IA
- **`performance.log`** - Métricas de performance
- **`security.log`** - Logs de segurança

## 📱 Dados (`marttin/`)

- **`db.sqlite3`** - Banco de dados SQLite (desenvolvimento)
- **`static/`** - Arquivos estáticos coletados

## 🎯 Navegação por Funcionalidade

### Para Trabalhar com Autenticação
- **Models**: `marttin/agent/models.py`
- **Views**: `marttin/agent/views.py` (auth_views)
- **Templates**: `marttin/agent/templates/registration/`
- **URLs**: `marttin/agent/urls.py`

### Para Trabalhar com Dashboard
- **View**: `marttin/agent/views.py` (dashboard_view)
- **Template**: `marttin/agent/templates/agent/dashboard.html`
- **CSS**: `marttin/agent/static/agent/css/style.css`

### Para Trabalhar com Análise de Marketing
- **Models**: `marttin/agent/models.py` (Company, MarketingAnalysis)
- **Views**: `marttin/agent/views.py` (marketing_analysis_view)
- **Template**: `marttin/agent/templates/agent/marketing_analysis.html`
- **AI Service**: `marttin/agent/ai_service.py`

### Para Trabalhar com Geração de Conteúdo
- **View**: `marttin/agent/views.py` (content_ideas_view)
- **Template**: `marttin/agent/templates/agent/content_ideas.html`
- **AI Integration**: `marttin/agent/ai_agent.py`

### Para Trabalhar com Chat
- **View**: `marttin/agent/views.py` (chat_view)
- **Template**: `marttin/agent/templates/agent/chat.html`
- **AI Service**: `marttin/agent/ai_service.py`

## 🔧 Configuração e Deploy

### Ambiente Local
- **Setup**: `setup.sh`
- **Env**: `.env.example` → `.env`
- **Requirements**: `requirements.txt`

### Docker
- **Build**: `Dockerfile`
- **Compose**: `docker-compose.yml`

### Produção
- **Settings**: `marttin/marttin/settings_production.py`
- **Deploy**: `docs/deployment/DEPLOYMENT.md`

## 📋 Checklist para Navegação

### Novo Desenvolvedor
1. **README.md** - Entender o projeto
2. **docs/setup/QUICKSTART.md** - Configurar ambiente
3. **docs/team/TEAM_ONBOARDING.md** - Onboarding
4. **marttin/agent/models.py** - Entender dados
5. **marttin/agent/views.py** - Entender lógica

### Trabalhar com Frontend
1. **marttin/agent/templates/base.html** - Layout base
2. **marttin/agent/static/agent/css/style.css** - Estilos
3. **marttin/agent/templates/agent/** - Páginas específicas

### Trabalhar com Backend
1. **marttin/agent/models.py** - Estrutura de dados
2. **marttin/agent/views.py** - Lógica de negócio
3. **marttin/agent/urls.py** - Roteamento
4. **marttin/agent/ai_service.py** - Integração IA

### Debug e Testes
1. **marttin/logs/** - Arquivos de log
2. **marttin/agent/tests.py** - Testes unitários
3. **marttin/agent/tests/** - Testes específicos

## 🔍 Dicas de Navegação

### VSCode
- Use Ctrl+P para busca rápida de arquivos
- Use Ctrl+Shift+F para busca em todo o projeto
- Configure workspace settings para o Django

### Terminal
```bash
# Buscar arquivos por nome
find . -name "*.py" -path "*/views*"

# Buscar conteúdo em arquivos
grep -r "function_name" marttin/agent/

# Ver estrutura de diretórios
ls -la marttin/agent/
```

### Git
```bash
# Ver arquivos modificados
git status

# Ver diferenças
git diff filename

# Histórico de um arquivo
git log --follow filename
```

---

**📍 Este mapa de arquivos é seu guia de navegação pelo projeto MARTTIN AI.**

Mantenha este documento atualizado conforme o projeto evolui!

**📅 Última atualização**: 16 de junho de 2025
