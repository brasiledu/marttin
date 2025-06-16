# MARTTIN AI - Assistente de Marketing Digital

![MARTTIN AI](https://img.shields.io/badge/MARTTIN-AI%20Marketing%20Assistant-blue)
![Django](https://img.shields.io/badge/Django-5.2.3-green)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-Private-red)

## 📖 Sobre o Projeto

**MARTTIN AI** é uma plataforma de consultoria empresarial baseada em inteligência artificial, desenvolvida especificamente para empreendedores brasileiros. A plataforma oferece análise de estratégias de marketing, geração de conteúdo e chat interativo com IA para otimizar campanhas e estratégias digitais.

### 🎯 Funcionalidades Principais

- **Dashboard Intuitivo**: Visão geral das métricas e atividades
- **Análise de Marketing**: Sistema de análise inteligente com cadastro de empresa
- **Geração de Conteúdo**: Criação automática de ideias de conteúdo com templates
- **Chat com IA**: Assistente inteligente para consultas em tempo real
- **Autenticação Completa**: Sistema de login, registro e gerenciamento de usuários

## 🏗️ Arquitetura do Sistema

### Estrutura do Projeto

```
marttin/
├── marttin/                    # Configurações do Django
│   ├── settings.py            # Configurações principais
│   ├── urls.py               # URLs principais
│   └── wsgi.py               # WSGI config
├── agent/                     # App principal
│   ├── models.py             # Modelos de dados
│   ├── views.py              # Lógica de negócio
│   ├── urls.py               # URLs do app
│   ├── ai_agent.py           # Integração com IA
│   ├── ai_service.py         # Serviços de IA
│   ├── templates/            # Templates HTML
│   │   ├── base.html         # Template base
│   │   └── agent/            # Templates específicos
│   └── static/               # Arquivos estáticos
├── docs/                      # Documentação
├── logs/                      # Logs da aplicação
└── manage.py                 # Django CLI
```

### 🗄️ Modelos de Dados

#### Company (Empresa)
```python
- user: OneToOneField(User) - Relacionamento com usuário
- business_name: CharField - Nome do negócio
- business_type: CharField - Tipo de negócio (e-commerce, serviços, etc.)
- target_audience: TextField - Público-alvo
- created_at/updated_at: DateTimeField - Timestamps
```

#### MarketingAnalysis (Análise de Marketing)
```python
- company: ForeignKey(Company) - Relacionamento com empresa
- current_strategy: TextField - Estratégia atual
- goals: TextField - Objetivos de marketing
- analysis_result: JSONField - Resultado da análise
- created_at: DateTimeField - Data de criação
```

## 🚀 Configuração do Ambiente

### Pré-requisitos

- Python 3.8+
- Django 5.2.3
- SQLite (desenvolvimento) / PostgreSQL (produção)
- Git

### Instalação

1. **Clone o repositório**
```bash
git clone <repository-url>
cd marttin
```

2. **Crie um ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# ou
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Configure o banco de dados**
```bash
cd marttin
python manage.py makemigrations
python manage.py migrate
```

5. **Crie um superusuário**
```bash
python manage.py createsuperuser
```

6. **Execute o servidor de desenvolvimento**
```bash
python manage.py runserver
```

7. **Acesse a aplicação**
- Aplicação: `http://localhost:8000`
- Admin: `http://localhost:8000/admin`

## 🎨 Design System

### Padrão de Design Unificado

O projeto utiliza um design system consistente baseado em:

- **Tema Escuro**: Background gradiente escuro (#0a0a0a → #1a1a1a)
- **Glassmorphism**: Efeitos de vidro com backdrop-blur
- **Tipografia**: Inter (Google Fonts)
- **Cores Primárias**: 
  - Azul: #007bff
  - Verde: #28a745
  - Cinza: #6c757d
- **Layout**: Sistema de grid responsivo 60/40

### Componentes Principais

- **Header**: Navegação com logo e menu responsivo
- **Forms**: Estilização consistente com focus effects
- **Cards**: Layout glassmorphism para conteúdo
- **Botões**: Estados hover e active bem definidos

## 🔧 APIs e Endpoints

### Autenticação
- `POST /login/` - Login de usuário
- `POST /signup/` - Registro de usuário
- `POST /logout/` - Logout

### Dashboard
- `GET /dashboard/` - Página principal do usuário

### Gestão de Empresas
- `GET /api/company/check/` - Verificar se empresa existe
- `POST /api/company/register/` - Registrar nova empresa
- `GET /api/company/data/` - Obter dados da empresa

### Marketing
- `GET /marketing-analysis/` - Página de análise
- `POST /api/marketing-analysis/` - Processar análise

### Conteúdo
- `GET /content-ideas/` - Página de geração de conteúdo
- `POST /api/content-ideas/` - Gerar ideias de conteúdo

### Chat
- `GET /chat/` - Interface de chat
- `POST /api/chat/` - Enviar mensagem para IA

## 🧪 Testes

### Estrutura de Testes

```bash
agent/tests/
├── test_e2e_selenium.py      # Testes end-to-end
└── __pycache__/              # Cache de testes
```

### Executar Testes

```bash
# Todos os testes
python manage.py test

# Testes específicos
python manage.py test agent.tests.test_e2e_selenium

# Com coverage
coverage run --source='.' manage.py test
coverage report
```

## 📊 Logging e Monitoramento

### Sistema de Logs

```bash
logs/
├── ai_agent.log             # Logs da IA
├── errors.log              # Logs de erro
├── marttin.log             # Logs gerais
├── performance.log         # Métricas de performance
└── security.log            # Logs de segurança
```

### Configuração de Logs

- **Level**: INFO (desenvolvimento), WARNING (produção)
- **Rotation**: Diária com retenção de 30 dias
- **Format**: JSON estruturado para análise

## 🔒 Segurança

### Configurações de Segurança

- **CSRF Protection**: Habilitado em todos os forms
- **XSS Protection**: Escape automático nos templates
- **Rate Limiting**: Middleware personalizado
- **Authentication**: Sistema Django + sessões
- **HTTPS**: Obrigatório em produção

### Variáveis de Ambiente

```bash
# .env (não commitado)
SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=postgresql://...
OPENAI_API_KEY=your-openai-key
```

## 🚀 Deploy

### Ambientes

- **Desenvolvimento**: SQLite + DEBUG=True
- **Staging**: PostgreSQL + DEBUG=False
- **Produção**: PostgreSQL + Cache + CDN

### Checklist de Deploy

- [ ] Variáveis de ambiente configuradas
- [ ] Banco de dados migrado
- [ ] Arquivos estáticos coletados
- [ ] SSL/HTTPS configurado
- [ ] Logs configurados
- [ ] Backup automatizado

## 🤝 Contribuição

### Fluxo de Desenvolvimento

1. **Feature Branch**: Crie branch a partir de `main`
2. **Development**: Desenvolva e teste localmente
3. **Pull Request**: Abra PR com descrição detalhada
4. **Code Review**: Aguarde aprovação
5. **Merge**: Merge após aprovação

### Padrões de Código

- **Python**: PEP 8 + Black formatting
- **HTML/CSS**: Prettier + consistência com design system
- **JavaScript**: ES6+ com consistência
- **Commits**: Conventional Commits

### Estrutura de Branch

```
main                    # Produção
├── develop            # Desenvolvimento
├── feature/user-auth  # Features
├── hotfix/login-bug   # Correções urgentes
└── release/v1.0.0     # Releases
```

## 📚 Documentação Completa

📖 **[Acesse a Documentação Completa](docs/README.md)**

### Documentos Principais
- **[Visão Geral do Projeto](docs/PROJECT_OVERVIEW.md)** - Resumo executivo
- **[Setup Rápido](docs/setup/QUICKSTART.md)** - Configuração em 5 minutos
- **[Onboarding da Equipe](docs/team/TEAM_ONBOARDING.md)** - Guia para novos desenvolvedores
- **[Guia de Contribuição](docs/development/CONTRIBUTING.md)** - Como contribuir

### Documentação Técnica
- **[Arquitetura](docs/architecture/)** - Documentação técnica detalhada
- **[APIs](docs/api/)** - Documentação das APIs
- **[Deploy](docs/deployment/)** - Guias de implantação
- **[Testes](docs/TESTING.md)** - Estratégias de teste

## 🐛 Issues e Suporte

### Relatando Bugs

1. Verifique se o bug já foi reportado
2. Use o template de issue apropriado
3. Inclua passos para reproduzir
4. Adicione logs/screenshots relevantes

### Suporte

- **Issues**: Para bugs e melhorias
- **Discussions**: Para dúvidas gerais
- **Wiki**: Documentação colaborativa

## 📄 Licença

Este projeto é propriedade privada. Todos os direitos reservados.

## 👥 Equipe

- **Arquitetura**: Sistema modular Django
- **Frontend**: Design system unificado
- **Backend**: APIs RESTful + IA integration
- **DevOps**: Deploy automatizado

---

**Última atualização**: 16 de junho de 2025

Para mais informações, consulte a documentação completa em `/docs/` ou entre em contato com a equipe de desenvolvimento.
