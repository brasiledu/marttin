#!/bin/bash

# MARTTIN AI - Script de Setup Automático
# Compatível com macOS/Linux

set -e  # Parar se houver erro

echo "🚀 MARTTIN AI - Setup Automático"
echo "=================================="
echo ""

# Verificar se Python 3 está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Instale Python 3.8+ antes de continuar."
    exit 1
fi

# Verificar versão do Python
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "🐍 Python detectado: $PYTHON_VERSION"

# Criar ambiente virtual
echo "📦 Criando ambiente virtual..."
python3 -m venv venv

# Ativar ambiente virtual
echo "⚡ Ativando ambiente virtual..."
source venv/bin/activate

# Upgrade pip
echo "📋 Atualizando pip..."
pip install --upgrade pip

# Instalar dependências
echo "📚 Instalando dependências..."
pip install -r requirements.txt

# Configurar arquivo de ambiente
if [ ! -f .env ]; then
    echo "⚙️  Criando arquivo de configuração..."
    cp .env.example .env
    echo "✏️  IMPORTANTE: Configure o arquivo .env com suas credenciais!"
    echo "   - Especialmente o OPENAI_API_KEY"
else
    echo "✅ Arquivo .env já existe"
fi

# Navegar para o diretório do Django
cd marttin

# Fazer migrações
echo "🗄️  Configurando banco de dados..."
python manage.py makemigrations

# Aplicar migrações
echo "🔄 Aplicando migrações..."
python manage.py migrate

# Verificar se já existe superusuário
echo "👤 Configurando superusuário..."
echo "Se já existe um superusuário, pode pular esta etapa (Ctrl+C)"
read -p "Deseja criar um superusuário? (y/n): " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    python manage.py createsuperuser
fi

# Coletar arquivos estáticos (se necessário)
echo "📁 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput || echo "⚠️  Collectstatic pode ser executado depois"

echo ""
echo "✅ Setup concluído com sucesso!"
echo ""
echo "🚀 Para executar o projeto:"
echo "   cd marttin"
echo "   source ../venv/bin/activate"
echo "   python manage.py runserver"
echo ""
echo "🌐 Depois acesse: http://localhost:8000"
echo "🔧 Admin: http://localhost:8000/admin"
echo ""
echo "📝 Não esqueça de configurar o arquivo .env!"
echo "   - OPENAI_API_KEY é obrigatório para IA"
echo ""
echo "📚 Consulte QUICKSTART.md para mais comandos úteis"
