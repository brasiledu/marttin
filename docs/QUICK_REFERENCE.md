# ⚡ MARTTIN AI - Referência Rápida

## 🚀 Comandos Essenciais

### Setup Inicial
```bash
./setup.sh                    # Setup automático completo
```

### Desenvolvimento Diário
```bash
source venv/bin/activate      # Ativar ambiente virtual
cd marttin                    # Entrar no projeto Django
python manage.py runserver    # Executar servidor (porta 8000)
python manage.py test         # Executar todos os testes
```

### Git Workflow
```bash
git checkout develop          # Mudar para branch develop
git pull origin develop       # Atualizar develop
git checkout -b feature/nome   # Criar nova feature branch
git add . && git commit -m "feat: descrição"  # Commit
git push origin feature/nome   # Push da branch
```

### Banco de Dados
```bash
python manage.py makemigrations  # Criar migrações
python manage.py migrate         # Aplicar migrações
python manage.py shell          # Shell do Django
python manage.py createsuperuser # Criar admin
```

## 🔗 URLs Importantes

### Desenvolvimento
- **App**: http://localhost:8000
- **Admin**: http://localhost:8000/admin
- **API Health**: http://localhost:8000/api/health

### Páginas Principais
- **Dashboard**: http://localhost:8000/dashboard
- **Chat**: http://localhost:8000/chat
- **Marketing**: http://localhost:8000/marketing-analysis
- **Conteúdo**: http://localhost:8000/content-ideas

## 📁 Estrutura de Arquivos

### Principais
```
marttin/
├── manage.py                 # Django CLI
├── agent/
│   ├── models.py            # Modelos de dados
│   ├── views.py             # Lógica de negócio
│   ├── urls.py              # URLs do app
│   ├── templates/           # Templates HTML
│   └── static/              # CSS, JS, imagens
└── marttin/
    └── settings.py          # Configurações
```

### Documentação
```
docs/
├── README.md                # Índice da documentação
├── PROJECT_OVERVIEW.md      # Visão geral
├── setup/QUICKSTART.md      # Setup rápido
├── team/TEAM_ONBOARDING.md  # Onboarding
└── development/CONTRIBUTING.md # Contribuição
```

## 🛠️ Troubleshooting Rápido

### Problemas Comuns
```bash
# Ambiente virtual não ativo
source venv/bin/activate

# Dependências desatualizadas
pip install -r requirements.txt

# Banco de dados corrompido (DEV)
rm marttin/db.sqlite3
python manage.py migrate

# Porta 8000 ocupada
python manage.py runserver 8001
```

### Logs
```bash
tail -f logs/marttin.log      # Logs gerais
tail -f logs/errors.log       # Logs de erro
tail -f logs/ai_agent.log     # Logs da IA
```

## 🎯 Fluxos Principais

### Novo Desenvolvedor
1. Clone → `./setup.sh` → Configure `.env` → Execute

### Nova Feature
1. `git checkout develop` → Criar branch → Desenvolver → Testar → PR

### Deploy
1. Testar → Merge → Deploy → Verificar

## 📋 Checklist de Desenvolvimento

### Antes de Commitar
- [ ] Código testado localmente
- [ ] Testes passando: `python manage.py test`
- [ ] Lint/formato OK
- [ ] Commit message segue padrão

### Antes de PR
- [ ] Branch atualizada com develop
- [ ] Descrição clara do PR
- [ ] Testes incluídos (se necessário)
- [ ] Documentação atualizada

### Antes de Deploy
- [ ] Todos os testes passando
- [ ] Code review aprovado
- [ ] Migrações aplicadas
- [ ] Variáveis de ambiente configuradas

## 🔑 Variáveis de Ambiente Importantes

```bash
# .env
SECRET_KEY=                   # Chave secreta Django
DEBUG=True                    # Debug mode (False em prod)
OPENAI_API_KEY=              # Chave da OpenAI (obrigatória)
DATABASE_URL=                # URL do banco (opcional)
```

## 📞 Links de Ajuda

### Documentação
- **[Completa](docs/README.md)** - Toda a documentação
- **[Setup](docs/setup/QUICKSTART.md)** - Configuração rápida
- **[Contribuir](docs/development/CONTRIBUTING.md)** - Como contribuir

### Suporte
- **Issues** - Para bugs
- **Discussions** - Para dúvidas
- **Code Review** - Para melhorias

---

**💡 Dica**: Salve este arquivo nos favoritos para acesso rápido!
