# Guia de Contribuição - MARTTIN AI

## 🚀 Como Começar

### Configuração do Ambiente Local

1. **Clone o repositório**
```bash
git clone <repository-url>
cd marttin
```

2. **Configure o ambiente virtual**
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

4. **Configure as variáveis de ambiente**
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

5. **Execute as migrações**
```bash
cd marttin
python manage.py makemigrations
python manage.py migrate
```

6. **Crie um superusuário**
```bash
python manage.py createsuperuser
```

7. **Execute o servidor**
```bash
python manage.py runserver
```

## 🔄 Fluxo de Desenvolvimento

### Branches

- **`main`**: Código em produção (protegida)
- **`develop`**: Branch de desenvolvimento principal
- **`feature/*`**: Novas funcionalidades
- **`hotfix/*`**: Correções urgentes
- **`release/*`**: Preparação para release

### Workflow

1. **Crie uma branch** a partir de `develop`
```bash
git checkout develop
git pull origin develop
git checkout -b feature/nome-da-feature
```

2. **Desenvolva e teste** sua funcionalidade
```bash
# Faça suas alterações
git add .
git commit -m "feat: adiciona funcionalidade X"
```

3. **Execute os testes**
```bash
python manage.py test
```

4. **Push e crie Pull Request**
```bash
git push origin feature/nome-da-feature
# Crie PR no GitHub/GitLab
```

## 📝 Padrões de Código

### Python (Backend)

- **PEP 8**: Siga as convenções do Python
- **Docstrings**: Use docstrings para funções e classes
- **Type hints**: Use quando possível
- **Imports**: Organize os imports (stdlib, third-party, local)

```python
from typing import Dict, List
from django.db import models
from .models import Company

def process_analysis(data: Dict[str, str]) -> Dict[str, any]:
    """
    Processa análise de marketing.
    
    Args:
        data: Dados da análise
        
    Returns:
        Resultado processado
    """
    pass
```

### HTML/CSS (Frontend)

- **Indentação**: 2 ou 4 espaços consistentes
- **Classes**: Use classes CSS semânticas
- **Responsividade**: Mobile-first approach
- **Acessibilidade**: Atributos alt, aria-* quando necessário

```html
<div class="marketing-form-container">
    <form class="marketing-form" method="post">
        {% csrf_token %}
        <div class="form-group">
            <label for="business_name">Nome do Negócio</label>
            <input type="text" id="business_name" name="business_name" required>
        </div>
    </form>
</div>
```

### JavaScript

- **ES6+**: Use features modernas do JavaScript
- **Async/Await**: Para operações assíncronas
- **Nomenclatura**: camelCase para variáveis e funções

```javascript
async function submitAnalysis(formData) {
    try {
        const response = await fetch('/api/marketing-analysis/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify(formData)
        });
        
        return await response.json();
    } catch (error) {
        console.error('Erro na análise:', error);
        throw error;
    }
}
```

## 🧪 Testes

### Tipos de Teste

1. **Unit Tests**: Testam componentes isolados
2. **Integration Tests**: Testam integração entre componentes
3. **E2E Tests**: Testam fluxos completos do usuário

### Executando Testes

```bash
# Todos os testes
python manage.py test

# Testes com coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Gera relatório HTML

# Testes específicos
python manage.py test agent.tests.test_views
```

### Escrevendo Testes

```python
from django.test import TestCase, Client
from django.contrib.auth.models import User
from agent.models import Company

class CompanyModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
    def test_company_creation(self):
        company = Company.objects.create(
            user=self.user,
            business_name='Test Company',
            business_type='ecommerce',
            target_audience='Jovens 18-25 anos'
        )
        self.assertEqual(str(company), 'Test Company')
```

## 📋 Commits

### Conventional Commits

Use o padrão de Conventional Commits:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Tipos de Commit

- **feat**: Nova funcionalidade
- **fix**: Bug fix
- **docs**: Documentação
- **style**: Formatação, sem mudança de código
- **refactor**: Refatoração sem mudança de funcionalidade
- **test**: Adição ou correção de testes
- **chore**: Tarefas de build, configuração, etc.

### Exemplos

```bash
feat: adiciona sistema de cadastro de empresa
fix: corrige bug no login de usuário
docs: atualiza README com instruções de deploy
style: aplica formatação PEP 8
refactor: reorganiza estrutura de views
test: adiciona testes para model Company
chore: atualiza dependências do requirements.txt
```

## 🔍 Code Review

### Checklist do Revisor

- [ ] Código segue os padrões estabelecidos
- [ ] Funcionalidade está testada
- [ ] Não quebra funcionalidades existentes
- [ ] Documentação está atualizada
- [ ] Performance não foi impactada negativamente
- [ ] Segurança foi considerada

### Checklist do Autor

- [ ] Código foi testado localmente
- [ ] Testes passam
- [ ] Documentação foi atualizada
- [ ] Commit messages são claros
- [ ] Branch está atualizada com develop

## 🐛 Debugging

### Logs

Use o sistema de logging do Django:

```python
import logging

logger = logging.getLogger(__name__)

def my_view(request):
    logger.info('Processando requisição para my_view')
    try:
        # código
        logger.debug('Debug info específica')
    except Exception as e:
        logger.error(f'Erro em my_view: {str(e)}')
        raise
```

### Debug Toolbar (Desenvolvimento)

```bash
pip install django-debug-toolbar
# Adicione ao INSTALLED_APPS e MIDDLEWARE
```

## 🚀 Deploy

### Checklist de Deploy

- [ ] Testes passando
- [ ] Variáveis de ambiente configuradas
- [ ] Migrações aplicadas
- [ ] Arquivos estáticos coletados
- [ ] SSL configurado (produção)
- [ ] Backup do banco antes do deploy

### Ambientes

1. **Development**: Local com SQLite
2. **Staging**: Similar à produção para testes
3. **Production**: Ambiente live

## 📞 Suporte

### Canais de Comunicação

- **Issues**: Para bugs e melhorias
- **Discussions**: Para dúvidas gerais
- **Slack/Teams**: Comunicação rápida da equipe

### Reportando Bugs

1. **Verifique** se já foi reportado
2. **Reproduza** o erro
3. **Descreva** os passos para reproduzir
4. **Inclua** logs de erro
5. **Adicione** screenshots se relevante

### Template de Issue

```markdown
## Descrição
Descrição clara do problema

## Passos para Reproduzir
1. Vá para '...'
2. Clique em '....'
3. Role para baixo até '....'
4. Veja o erro

## Comportamento Esperado
O que deveria acontecer

## Screenshots
Se aplicável, adicione screenshots

## Ambiente
- OS: [e.g. iOS]
- Browser [e.g. chrome, safari]
- Version [e.g. 22]
```

## 🎯 Boas Práticas

### Segurança

- **Nunca** commite credenciais
- **Use** HTTPS em produção
- **Valide** todas as entradas do usuário
- **Implemente** rate limiting
- **Mantenha** dependências atualizadas

### Performance

- **Otimize** queries do banco
- **Use** cache quando apropriado
- **Minimize** requests HTTP
- **Comprima** arquivos estáticos
- **Monitor** performance em produção

### Manutenibilidade

- **Escreva** código limpo e legível
- **Documente** decisões complexas
- **Refatore** regularmente
- **Mantenha** testes atualizados
- **Siga** princípios SOLID

---

**Dúvidas?** Entre em contato com a equipe de desenvolvimento!
