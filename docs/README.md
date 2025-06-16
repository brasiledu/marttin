# 📚 Documentação MARTTIN AI

Bem-vindo à documentação completa do projeto MARTTIN AI. Esta pasta contém todos os guias, manuais e recursos necessários para desenvolver, manter e implantar a aplicação.

## 📋 Índice da Documentação

### 🚀 Para Começar
- **[Visão Geral do Projeto](PROJECT_OVERVIEW.md)** - Resumo executivo e status do projeto
- **[Setup Rápido](setup/QUICKSTART.md)** - Como configurar o ambiente em 5 minutos
- **[Onboarding da Equipe](team/TEAM_ONBOARDING.md)** - Guia para novos desenvolvedores
- **[Referência Rápida](QUICK_REFERENCE.md)** - Comandos e links essenciais
- **[Mapa de Arquivos](FILE_MAP.md)** - Navegação pelos arquivos do projeto

### 🛠️ Desenvolvimento
- **[Guia de Contribuição](development/CONTRIBUTING.md)** - Como contribuir com o projeto
- **[Testes](TESTING.md)** - Estratégias e execução de testes
- **[Arquitetura](architecture/)** - Documentação técnica da arquitetura
  - [Arquitetura do Sistema](architecture/SYSTEM_ARCHITECTURE.md)
  - [Arquitetura Detalhada](architecture/DETAILED_ARCHITECTURE.md)

### 🌐 API e Integração
- **[APIs](api/)** - Documentação das APIs
  - [OpenAPI Specification](api/openapi.yaml)

### 🚀 Deploy e Produção
- **[Deploy](deployment/)** - Guias de implantação
  - [Guia de Deploy](deployment/DEPLOYMENT.md)

## 🎯 Navegação Rápida

### Para Desenvolvedores Novos
1. Leia [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) para entender o projeto
2. Siga [setup/QUICKSTART.md](setup/QUICKSTART.md) para configurar o ambiente
3. Complete [team/TEAM_ONBOARDING.md](team/TEAM_ONBOARDING.md) para onboarding
4. Consulte [development/CONTRIBUTING.md](development/CONTRIBUTING.md) antes de contribuir

### Para Desenvolvedores Experientes
- **Arquitetura**: [architecture/](architecture/)
- **APIs**: [api/](api/)
- **Deploy**: [deployment/](deployment/)
- **Testes**: [TESTING.md](TESTING.md)

### Para DevOps/SysAdmin
- **Deploy**: [deployment/DEPLOYMENT.md](deployment/DEPLOYMENT.md)
- **Arquitetura**: [architecture/SYSTEM_ARCHITECTURE.md](architecture/SYSTEM_ARCHITECTURE.md)
- **Monitoramento**: Logs em `/logs/`

## 📁 Estrutura da Documentação

```
docs/
├── README.md                    # Este arquivo (índice)
├── PROJECT_OVERVIEW.md          # Visão geral do projeto
├── TESTING.md                   # Guia de testes
│
├── setup/                       # Configuração e instalação
│   └── QUICKSTART.md           # Setup rápido
│
├── team/                        # Documentação para equipe
│   └── TEAM_ONBOARDING.md      # Onboarding de novos membros
│
├── development/                 # Desenvolvimento
│   └── CONTRIBUTING.md         # Guia de contribuição
│
├── architecture/                # Arquitetura técnica
│   ├── SYSTEM_ARCHITECTURE.md  # Arquitetura geral
│   └── DETAILED_ARCHITECTURE.md # Detalhes técnicos
│
├── api/                         # Documentação de APIs
│   └── openapi.yaml            # Especificação OpenAPI
│
└── deployment/                  # Deploy e produção
    └── DEPLOYMENT.md           # Guia de deploy
```

## 🔍 Como Encontrar Informações

### Por Tipo de Tarefa
- **Configurar ambiente**: [setup/QUICKSTART.md](setup/QUICKSTART.md)
- **Entender o projeto**: [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)
- **Contribuir código**: [development/CONTRIBUTING.md](development/CONTRIBUTING.md)
- **Executar testes**: [TESTING.md](TESTING.md)
- **Fazer deploy**: [deployment/DEPLOYMENT.md](deployment/DEPLOYMENT.md)
- **Integrar APIs**: [api/openapi.yaml](api/openapi.yaml)

### Por Papel na Equipe
- **Desenvolvedor Frontend**: Arquitetura → API → Contribuição
- **Desenvolvedor Backend**: Arquitetura → API → Testes → Contribuição
- **DevOps**: Deploy → Arquitetura → Monitoramento
- **QA**: Testes → Arquitetura → APIs
- **Tech Lead**: Visão Geral → Arquitetura → Todos os guias

## 📖 Convenções da Documentação

### Formatação
- **Markdown**: Todos os documentos em `.md`
- **Emojis**: Para melhor navegação visual
- **Links**: Relativos para navegação interna
- **Código**: Blocos com syntax highlighting

### Estrutura Padrão
1. **Título e Descrição**
2. **Índice** (se necessário)
3. **Conteúdo Principal**
4. **Exemplos Práticos**
5. **Links Relacionados**
6. **Última Atualização**

### Manutenção
- **Revisão**: A cada release
- **Atualização**: Quando há mudanças significativas
- **Validação**: Links e exemplos testados

## 🔗 Links Úteis

### Externos
- [Django Documentation](https://docs.djangoproject.com/)
- [OpenAI API](https://platform.openai.com/docs)
- [Bootstrap Icons](https://icons.getbootstrap.com/)

### Internos
- **Código Fonte**: `../marttin/agent/`
- **Templates**: `../marttin/agent/templates/`
- **Static Files**: `../marttin/agent/static/`
- **Logs**: `../logs/`

## 📞 Suporte

### Para Dúvidas sobre Documentação
- **Issues**: Para correções na documentação
- **Discussions**: Para sugestões de melhoria
- **PR**: Para contribuições diretas

### Contatos
- **Tech Lead**: Para questões arquiteturais
- **DevOps**: Para questões de deploy
- **QA**: Para questões de testes

---

**📅 Última atualização**: 16 de junho de 2025
**📝 Versão da documentação**: 1.0.0
**🚀 Status do projeto**: Em desenvolvimento ativo

> 💡 **Dica**: Use Ctrl+F para buscar rapidamente informações específicas nesta documentação.
