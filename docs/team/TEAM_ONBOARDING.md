# 🎯 MARTTIN AI - Primeiro Dia da Equipe

## 📋 Checklist de Onboarding

### Antes de Começar
- [ ] Git instalado e configurado
- [ ] Python 3.8+ instalado
- [ ] VSCode ou IDE de preferência
- [ ] Acesso ao repositório do projeto

### Setup do Ambiente (15 minutos)
1. **Clone o projeto**
   ```bash
   git clone <repository-url>
   cd marttin
   ```

2. **Execute o setup automático**
   ```bash
   ./setup.sh
   ```

3. **Configure sua chave da OpenAI**
   ```bash
   # Edite o arquivo .env
   nano .env
   # Adicione: OPENAI_API_KEY=sua-chave-aqui
   ```

4. **Teste o ambiente**
   ```bash
   cd marttin
   python manage.py runserver
   ```

5. **Acesse a aplicação**
   - http://localhost:8000 (aplicação)
   - http://localhost:8000/admin (admin)

### Primeira Exploração (30 minutos)

#### 1. Entenda a Estrutura
- [ ] Navegue pelos arquivos principais
- [ ] Leia `README.md` e `PROJECT_OVERVIEW.md`
- [ ] Explore a pasta `docs/` para documentação detalhada

#### 2. Teste as Funcionalidades
- [ ] Crie uma conta de usuário
- [ ] Acesse o dashboard
- [ ] Teste o sistema de análise de marketing
- [ ] Experimente a geração de conteúdo
- [ ] Use o chat com IA

#### 3. Examine o Código
- [ ] `marttin/agent/models.py` - Modelos de dados
- [ ] `marttin/agent/views.py` - Lógica de negócio
- [ ] `marttin/agent/templates/` - Interface do usuário
- [ ] `marttin/agent/static/` - CSS e JavaScript

## 🎨 Design System

### Padrões Visuais
- **Tema**: Escuro com gradientes
- **Efeitos**: Glassmorphism (backdrop-blur)
- **Tipografia**: Inter (Google Fonts)
- **Layout**: Grid 60/40 para formulários

### Cores Principais
```css
/* Primárias */
--primary-blue: #007bff;
--primary-green: #28a745;
--primary-gray: #6c757d;

/* Background */
--bg-dark: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
--glass-bg: rgba(255, 255, 255, 0.1);
```

## 🧩 Arquitetura do Sistema

### Fluxo de Dados
1. **User** → **Authentication** → **Dashboard**
2. **Company Registration** → **Marketing Analysis** → **AI Processing**
3. **Content Generation** → **Template Selection** → **AI Output**
4. **Chat** → **Real-time AI** → **Response**

### Modelos Principais
```python
# User (Django built-in)
# ↓
# Company (one-to-one)
# ↓
# MarketingAnalysis (many-to-one)
```

## 🛠️ Tarefas para Primeiros Dias

### Dia 1: Familiarização
- [ ] Setup completo do ambiente
- [ ] Exploração das funcionalidades
- [ ] Leitura da documentação
- [ ] Primeiro commit (fix ou melhoria simples)

### Dia 2-3: Código
- [ ] Análise profunda do código
- [ ] Identificação de melhorias
- [ ] Testes das funcionalidades
- [ ] Contribuição com bug fixes

### Semana 1: Contribuição
- [ ] Implementação de feature pequena
- [ ] Adição de testes
- [ ] Melhoria na documentação
- [ ] Otimização de performance

## 🎯 Areas de Foco

### Frontend
- **Responsividade**: Melhorar experiência mobile
- **Acessibilidade**: Implementar ARIA labels
- **Performance**: Otimizar CSS/JS
- **UX**: Aprimorar fluxos de usuário

### Backend
- **APIs**: Expandir endpoints
- **Testes**: Aumentar cobertura
- **Security**: Implementar rate limiting
- **Performance**: Otimizar queries

### DevOps
- **CI/CD**: Setup de pipeline
- **Monitoring**: Implementar métricas
- **Deploy**: Automatizar processo
- **Backup**: Estratégia de dados

## 📚 Recursos de Aprendizado

### Django
- [Documentação Oficial](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django Security](https://docs.djangoproject.com/en/stable/topics/security/)

### Frontend
- [MDN Web Docs](https://developer.mozilla.org/)
- [CSS Grid Guide](https://css-tricks.com/snippets/css/complete-guide-grid/)
- [JavaScript ES6+](https://javascript.info/)

### AI Integration
- [OpenAI API Docs](https://platform.openai.com/docs)
- [Python OpenAI Library](https://github.com/openai/openai-python)

## 🤝 Comunicação

### Canais de Comunicação
- **Issues**: Para bugs e features
- **Discussions**: Para dúvidas gerais
- **Pull Requests**: Para code review
- **Wiki**: Para documentação colaborativa

### Padrões de Commit
```bash
# Tipos: feat, fix, docs, style, refactor, test, chore
git commit -m "feat: adiciona validação de formulário"
git commit -m "fix: corrige erro na autenticação"
git commit -m "docs: atualiza README com novas instruções"
```

### Code Review
- **Obrigatório**: Para todas as mudanças
- **Checklist**: Funcionalidade, testes, documentação
- **Aprovação**: Necessária antes do merge

## 🚨 Troubleshooting Comum

### Erro: ModuleNotFoundError
```bash
# Certifique-se de que o venv está ativo
source venv/bin/activate
pip install -r requirements.txt
```

### Erro: Database
```bash
# Reset do banco (desenvolvimento)
rm marttin/db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Erro: Static Files
```bash
# Coletar arquivos estáticos
python manage.py collectstatic
```

### Erro: OpenAI API
```bash
# Verificar se a chave está configurada
grep OPENAI_API_KEY .env
```

## 📞 Suporte

### Dúvidas Técnicas
1. **Documentação**: Consulte `/docs/`
2. **Issues**: Procure por problemas similares
3. **Discussions**: Faça perguntas gerais
4. **Code**: Analise implementações existentes

### Emergências
- **Bugs Críticos**: Abra issue com label `urgent`
- **Deploy Issues**: Verifique logs em `logs/`
- **Performance**: Use Django Debug Toolbar

---

**🎉 Bem-vindos à equipe MARTTIN AI!**

Lembrem-se: este é um projeto colaborativo. Não hesitem em fazer perguntas, sugerir melhorias e contribuir com ideias. Cada membro da equipe é importante para o sucesso do projeto.

**Objetivo**: Criar a melhor plataforma de consultoria empresarial com IA do Brasil! 🚀
