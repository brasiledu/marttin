# 🚀 MARTTIN AI - Quickstart Guide

Este guia permite que sua equipe configure o projeto em menos de 5 minutos.

## ⚡ Setup Rápido (macOS/Linux)

### 1. Clone e Entre no Diretório
```bash
git clone <repository-url>
cd marttin
```

### 2. Setup Automático com Script
```bash
# Crie e execute o script de setup
cat > setup.sh << 'EOF'
#!/bin/bash
echo "🚀 Configurando MARTTIN AI..."

# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Configurar ambiente
cp .env.example .env
echo "✏️  Edite o arquivo .env com suas configurações (especialmente OPENAI_API_KEY)"

# Configurar banco de dados
cd marttin
python manage.py makemigrations
python manage.py migrate

# Criar superusuário
echo "👤 Criando superusuário..."
python manage.py createsuperuser

echo "✅ Setup concluído!"
echo "🌐 Execute: python manage.py runserver"
echo "📂 Acesse: http://localhost:8000"
EOF

chmod +x setup.sh
./setup.sh
```

### 3. Executar o Projeto
```bash
cd marttin
source ../venv/bin/activate  # Se não estiver ativo
python manage.py runserver
```

## 🔧 Comandos Úteis

### Desenvolvimento Diário
```bash
# Ativar ambiente virtual
source venv/bin/activate

# Executar servidor
cd marttin && python manage.py runserver

# Executar testes
python manage.py test

# Criar nova migração
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Coletar arquivos estáticos
python manage.py collectstatic

# Shell Django
python manage.py shell
```

### Git Workflow
```bash
# Atualizar develop
git checkout develop
git pull origin develop

# Criar feature branch
git checkout -b feature/nome-da-feature

# Commit com padrão
git add .
git commit -m "feat: descrição da funcionalidade"
git push origin feature/nome-da-feature

# Voltar para develop
git checkout develop
```

### Debugging
```bash
# Ver logs em tempo real
tail -f logs/marttin.log

# Logs específicos
tail -f logs/ai_agent.log
tail -f logs/errors.log

# Limpar cache
find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} +
```

## 🧪 Testes Rápidos

### Testar Componentes Principais
```bash
# Testar autenticação
python manage.py test agent.tests.test_auth

# Testar APIs
python manage.py test agent.tests.test_api

# Testar modelos
python manage.py test agent.tests.test_models

# Testar views
python manage.py test agent.tests.test_views
```

### Testar Manualmente
1. **Login**: `http://localhost:8000/login/`
2. **Dashboard**: `http://localhost:8000/dashboard/`
3. **Chat**: `http://localhost:8000/chat/`
4. **Marketing**: `http://localhost:8000/marketing-analysis/`
5. **Conteúdo**: `http://localhost:8000/content-ideas/`

## 🔍 Troubleshooting Rápido

### Problema: Erro de Migração
```bash
# Reset do banco (desenvolvimento)
rm marttin/db.sqlite3
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Problema: Dependências
```bash
# Reinstalar dependências
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Problema: Porta em Uso
```bash
# Usar porta diferente
python manage.py runserver 8001

# Ou matar processo na porta 8000
lsof -ti:8000 | xargs kill -9
```

### Problema: Static Files
```bash
# Debug de arquivos estáticos
python manage.py findstatic css/style.css
python manage.py collectstatic --clear
```

## 🚀 Deploy Rápido

### Para Staging
```bash
# Preparar para deploy
git checkout main
git pull origin main
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
```

### Checklist Pré-Deploy
- [ ] Testes passando: `python manage.py test`
- [ ] Migrações aplicadas: `python manage.py showmigrations`
- [ ] Variáveis de ambiente configuradas
- [ ] `DEBUG=False` em produção
- [ ] `SECRET_KEY` única e segura
- [ ] Backup do banco de dados feito

## 📱 URLs Importantes

### Desenvolvimento
- **Aplicação**: http://localhost:8000
- **Admin**: http://localhost:8000/admin
- **API Status**: http://localhost:8000/api/health

### Arquivos de Configuração
- **Settings**: `marttin/marttin/settings.py`
- **URLs**: `marttin/marttin/urls.py`
- **Models**: `marttin/agent/models.py`
- **Views**: `marttin/agent/views.py`

## 💡 Dicas da Equipe

1. **Use o VSCode** com extensões Python e Django
2. **Configure o Black** para formatação automática
3. **Instale o Django Debug Toolbar** para desenvolvimento
4. **Use o Django Shell** para testar código rapidamente
5. **Sempre teste localmente** antes do commit

## 📞 Suporte

- **Issues**: Para bugs e melhorias
- **Discussions**: Para dúvidas gerais
- **Documentation**: Pasta `/docs/` com guias detalhados

---

**⏱️ Tempo estimado de setup**: 3-5 minutos
**📋 Pré-requisitos**: Python 3.8+, Git
**🎯 Resultado**: Ambiente local funcionando
