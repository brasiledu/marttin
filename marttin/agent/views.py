import random
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.dateparse import parse_date
from django.utils import timezone
from django.conf import settings
import os
from .models import Company, MarketingAnalysis, FileUpload
from .ai_service import ai_service
# Adiciona utilitário para renderização Markdown segura
from .utils.markdown_utils import render_markdown

# View principal (homepage)
def index(request):
    """Homepage da aplicação - redireciona usuários logados para dashboard"""
    # Se o usuário já está logado, redireciona para o dashboard
    if request.user.is_authenticated:
        return redirect('agent:dashboard')
    
    return render(request, 'agent/index.html')

# View de cadastro
def signup_view(request):
    """View para cadastro de novos usuários"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# View de login customizada
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return '/dashboard/'

# View de logout
def logout_view(request):
    """View para logout"""
    logout(request)
    messages.info(request, 'Você saiu da sua conta.')
    return redirect('agent:index')

# Dashboard (requer login)
@login_required
def dashboard_view(request):
    """Dashboard principal do usuário"""
    context = {
        'stats': {
            'conversations': 0,
            'analyses': 0,
            'content_ideas': 0,
        },
        'recent_activities': []
    }
    return render(request, 'agent/dashboard.html', context)

# Chat (acesso liberado para demo)
def chat_view(request):
    """Interface de chat com IA - Demo para usuários não logados, completo para logados"""
    context = {
        'conversation_history': [],
        'is_demo': not request.user.is_authenticated,
        'user_authenticated': request.user.is_authenticated
    }
    return render(request, 'agent/chat.html', context)

# API do Chat (demo para não logados, completo para logados)
@csrf_exempt
def chat_api(request):
    """API para enviar mensagens para o chat - Demo limitada para usuários não logados"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message', '').strip()
            arquivo = data.get('file_path')  # opcional
            pergunta_arquivo = data.get('file_question')  # opcional

            if not message:
                return JsonResponse({
                    'success': False,
                    'error': 'Mensagem não pode estar vazia'
                })

            if request.user.is_authenticated:
                try:
                    result = ai_service.run_ai_consultor(message, arquivo, pergunta_arquivo)
                    response = result.get('resposta_final') or 'Sem resposta.'
                except Exception as e:
                    response = f"Erro ao processar a solicitação de IA: {e}"
                html = render_markdown(response or '')
                return JsonResponse({
                    'success': True,
                    'response': response,
                    'response_html': html,
                    'is_demo': False
                })
            else:
                demo_responses = [
                    f"🎯 **Demo Marttin AI**\n\nSua pergunta: '{message}'\n\n💡 **Resposta demonstrativa:**\nEssa é uma funcionalidade incrível! O Marttin AI pode ajudar você com:\n• Consultoria empresarial instantânea\n• Análise de mercado personalizada\n• Geração de conteúdo para redes sociais\n• Estratégias de marketing\n\n🔒 **Crie sua conta gratuita** para ter acesso completo e salvar suas conversas!",
                    
                    f"📊 **Marttin AI Demo**\n\nAnalisando: '{message}'\n\n🚀 **Sugestão estratégica:**\nCom base na sua pergunta, recomendo focar em:\n• Definição clara de objetivos\n• Análise do público-alvo\n• Planejamento de ações práticas\n\n⚡ **Quer mais?** Usuários cadastrados têm acesso a análises detalhadas, templates profissionais e histórico completo!",
                    
                    f"💼 **Consultoria Marttin AI**\n\nSua consulta: '{message}'\n\n✨ **Dica profissional:**\nIsso é fundamental para o sucesso do seu negócio! O Marttin pode te ajudar com estratégias personalizadas.\n\n🎁 **Teste completo grátis:**\n• Faça seu cadastro em 30 segundos\n• Acesse todas as ferramentas\n• Sem compromisso inicial"
                ]
                
                import random
                response = random.choice(demo_responses)
                html = render_markdown(response or '')
                return JsonResponse({
                    'success': True,
                    'response': response,
                    'response_html': html,
                    'is_demo': True
                })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })

    return JsonResponse({'success': False, 'error': 'Método não permitido'})

# Análise de Marketing (requer login)
@login_required
def marketing_analysis_view(request):
    """View para análise de marketing"""
    if request.method == 'POST':
        # Simular análise de marketing
        analysis = """
        **Análise de Marketing Personalizada**
        
        Com base nas informações fornecidas:
        
        • **Pontos Fortes**: Seu negócio tem potencial para crescimento digital
        • **Oportunidades**: Foco em redes sociais e content marketing
        • **Recomendações**: 
          - Investir em Instagram e Facebook
          - Criar conteúdo educativo
          - Implementar email marketing
          - Monitorar métricas de engajamento
        
        Esta é uma análise simulada. Para análises completas, configure a integração com IA.
        """
        
        return JsonResponse({
            'success': True,
            'analysis': analysis
        })
    
    return render(request, 'agent/marketing_analysis.html')

# Geração de Conteúdo (requer login)
@login_required
def content_ideas_view(request):
    """View para geração de ideias de conteúdo"""
    if request.method == 'POST':
        # Simular geração de ideias
        ideas = [
            "💡 5 dicas para aumentar o engajamento nas redes sociais",
            "🚀 Como usar storytelling no seu marketing digital",
            "📊 Métricas que todo empreendedor deve acompanhar",
            "🎯 Estratégias de segmentação de público-alvo",
            "💰 ROI no marketing digital: como calcular e otimizar"
        ]
        
        return JsonResponse({
            'success': True,
            'ideas': ideas
        })
    
    return render(request, 'agent/content_ideas.html')

# Teste de conexão com IA
@login_required
def test_ai_connection(request):
    """Teste de conexão com a IA"""
    return JsonResponse({
        'success': True,
        'message': 'Conexão simulada OK. Configure a API do Google Gemini para funcionalidade completa.',
        'status': 'simulated'
    })

# Views para gerenciamento de empresas
@login_required
@csrf_exempt
def check_company(request):
    """API para verificar se o usuário tem empresa cadastrada"""
    try:
        company = Company.objects.get(user=request.user)
        return JsonResponse({
            'status': 'success',
            'company': {
                'id': company.id,
                'business_name': company.business_name,
                'business_type': company.business_type,
                'target_audience': company.target_audience
            }
        })
    except Company.DoesNotExist:
        return JsonResponse({
            'status': 'no_company'
        })

@login_required
@csrf_exempt
def register_company(request):
    """API para cadastrar/atualizar empresa do usuário"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Validar dados obrigatórios
            required_fields = ['business_name', 'business_type', 'target_audience']
            for field in required_fields:
                if not data.get(field, '').strip():
                    return JsonResponse({
                        'status': 'error',
                        'message': f'Campo {field} é obrigatório'
                    })
            
            # Criar ou atualizar empresa
            company, created = Company.objects.update_or_create(
                user=request.user,
                defaults={
                    'business_name': data['business_name'].strip(),
                    'business_type': data['business_type'],
                    'target_audience': data['target_audience'].strip()
                }
            )
            
            action = 'cadastrada' if created else 'atualizada'
            
            return JsonResponse({
                'status': 'success',
                'message': f'Empresa {action} com sucesso!',
                'company': {
                    'id': company.id,
                    'business_name': company.business_name,
                    'business_type': company.business_type,
                    'target_audience': company.target_audience
                }
            })
            
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': f'Erro ao cadastrar empresa: {str(e)}'
            })
    
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'})

@login_required
@csrf_exempt
def get_company(request):
    """API para obter dados da empresa do usuário"""
    try:
        company = Company.objects.get(user=request.user)
        return JsonResponse({
            'status': 'success',
            'company': {
                'id': company.id,
                'business_name': company.business_name,
                'business_type': company.business_type,
                'target_audience': company.target_audience
            }
        })
    except Company.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'Empresa não encontrada'
        })

# API de Análise de Marketing atualizada
@login_required
@csrf_exempt
def marketing_analysis_api(request):
    """API aprimorada para análise de marketing"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Validar dados obrigatórios
            company_id = data.get('company_id')
            current_strategy = data.get('current_strategy', '').strip()
            goals = data.get('goals', '').strip()
            
            if not all([company_id, current_strategy, goals]):
                return JsonResponse({
                    'status': 'error',
                    'message': 'Todos os campos são obrigatórios'
                })
            
            # Verificar se a empresa pertence ao usuário
            try:
                company = Company.objects.get(id=company_id, user=request.user)
            except Company.DoesNotExist:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Empresa não encontrada'
                })
            
            # Gerar análise simulada personalizada
            analysis_data = {
                'insights': f"""
Com base nas informações da {company.business_name} ({company.get_business_type_display()}):

🎯 **Público-Alvo Identificado:**
{company.target_audience[:200]}...

📊 **Análise da Estratégia Atual:**
Sua estratégia atual mostra foco em: {current_strategy[:100]}...

✨ **Insights Principais:**
• Seu tipo de negócio ({company.get_business_type_display()}) tem grande potencial de crescimento digital
• O público-alvo definido está alinhado com as tendências de mercado
• Oportunidades de expansão em canais digitais
""",
                
                'recommendations': f"""
🚀 **Recomendações Personalizadas para {company.business_name}:**

• **Digital Marketing**: Invista em presença digital forte
• **Content Marketing**: Crie conteúdo relevante para seu público
• **Social Media**: Foque nas redes onde seu público está presente
• **Email Marketing**: Desenvolva relacionamento com leads
• **SEO**: Otimize para ser encontrado organicamente

**Específico para {company.get_business_type_display()}:**
• Estratégias segmentadas para seu setor
• Benchmarking com concorrentes do ramo
• Métricas específicas da indústria
""",
                
                'growth_strategies': f"""
📈 **Estratégias de Crescimento:**

**Curto Prazo (1-3 meses):**
• Otimizar perfis em redes sociais
• Criar calendário de conteúdo
• Implementar sistema de captação de leads

**Médio Prazo (3-6 meses):**
• Lançar campanhas pagas segmentadas
• Desenvolver funil de vendas
• Automatizar processos de marketing

**Longo Prazo (6-12 meses):**
• Expansão para novos mercados
• Desenvolvimento de produtos/serviços
• Parcerias estratégicas
""",
                
                'next_steps': f"""
✅ **Próximos Passos Recomendados:**

**Imediato:**
1. Definir KPIs específicos baseados em: {goals[:100]}...
2. Configurar ferramentas de analytics
3. Criar identidade visual consistente

**Esta Semana:**
• Auditar presença digital atual
• Mapear jornada do cliente
• Definir orçamento de marketing

**Este Mês:**
• Implementar primeiras campanhas
• Monitorar resultados iniciais
• Ajustar estratégia conforme dados

💡 **Dica:** Foque em métricas que importam para seus objetivos específicos.
"""
            }
            
            # Salvar análise no banco
            analysis = MarketingAnalysis.objects.create(
                company=company,
                current_strategy=current_strategy,
                goals=goals,
                analysis_result=analysis_data
            )
            
            return JsonResponse({
                'status': 'success',
                'analysis': analysis_data,
                'analysis_id': analysis.id
            })
            
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': f'Erro ao processar análise: {str(e)}'
            })
    
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'})

# API de Geração de Ideias de Conteúdo
@login_required
@csrf_exempt
def content_ideas_api(request):
    """API para geração de ideias de conteúdo"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Extrair dados do formulário
            business_description = data.get('business_description', '').strip()
            content_type = data.get('content_type', '').strip()
            platform = data.get('platform', '').strip()
            target_audience = data.get('target_audience', '').strip()
            tone = data.get('tone', '').strip()
            keywords = data.get('keywords', '').strip()
            quantity = int(data.get('quantity', 5))
            
            # Validar campos obrigatórios
            if not all([business_description, content_type, platform, target_audience, tone]):
                return JsonResponse({
                    'success': False,
                    'error': 'Todos os campos obrigatórios devem ser preenchidos'
                })
            
            # Gerar ideias baseadas no tipo de conteúdo e plataforma
            ideas = generate_content_ideas(
                business_description=business_description,
                content_type=content_type,
                platform=platform,
                target_audience=target_audience,
                tone=tone,
                keywords=keywords,
                quantity=quantity
            )
            
            return JsonResponse({
                'success': True,
                'ideas': ideas,
                'content_type': content_type,
                'platform': platform,
                'tone': tone
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': f'Erro no processamento: {str(e)}'
            })
    
    return JsonResponse({'success': False, 'error': 'Método não permitido'})

def generate_content_ideas(business_description, content_type, platform, target_audience, tone, keywords, quantity):
    """Gera ideias de conteúdo personalizadas"""
    
    # Base de ideias por tipo de conteúdo
    content_templates = {
        'social_media': [
            "🚀 {quantidade} maneiras de {negocio} pode transformar a vida do seu {publico}",
            "💡 Dica rápida: Como {negocio} resolve {problema} em minutos",
            "📊 Estatística surpreendente sobre {setor} que vai impressionar você",
            "🎯 Por que {publico} deve escolher {negocio} em 2025",
            "🔥 Tendência: O futuro de {setor} já chegou",
            "⚡ Transformação: Antes e depois com {negocio}",
            "🌟 Cliente satisfeito: Depoimento real sobre {negocio}",
            "📱 Tutorial: Como aproveitar ao máximo {servico}",
            "💰 Investimento inteligente: Por que {negocio} vale a pena",
            "🎉 Celebrando: Marco importante para {negocio}"
        ],
        'blog_posts': [
            "📝 Guia Completo: Tudo sobre {setor} que {publico} precisa saber",
            "🔍 Análise Profunda: Como {negocio} está revolucionando o mercado",
            "📈 Estudo de Caso: {quantidade} empresas que cresceram com {estrategia}",
            "🎯 Estratégia Detalhada: Como {publico} pode alcançar {objetivo}",
            "💡 Inovação: As tecnologias que estão mudando {setor}",
            "📊 Pesquisa Exclusiva: O que {publico} realmente quer",
            "🏆 Melhores Práticas: Lições aprendidas em {setor}",
            "🔮 Futuro: Previsões para {setor} nos próximos 5 anos",
            "⚠️ Evite Estes Erros: Armadilhas comuns em {setor}",
            "🚀 Transformação Digital: Como {negocio} pode ajudar"
        ],
        'email_campaigns': [
            "✉️ Bem-vindo(a)! Sua jornada com {negocio} começa aqui",
            "🎁 Oferta Especial: Desconto exclusivo para {publico}",
            "📢 Novidade: {negocio} tem algo incrível para você",
            "⏰ Última Chance: Oferta termina em breve",
            "💡 Dica Semanal: Como melhorar {area} com {negocio}",
            "🏆 Conquista Desbloqueada: Seu progresso com {negocio}",
            "📊 Relatório Mensal: Seus resultados com {negocio}",
            "🎯 Personalizado: Sugestões baseadas no seu perfil",
            "🔔 Lembrete: Não perca esta oportunidade",
            "💝 Agradecimento: Por escolher {negocio}"
        ],
        'ad_copy': [
            "🎯 {negocio}: A solução que {publico} estava procurando!",
            "💰 Pare de gastar dinheiro à toa. Descubra {negocio}",
            "⚡ Resultados em {tempo}! {negocio} funciona de verdade",
            "🏆 Nº1 em {setor}: {negocio} é referência no mercado",
            "🔥 Oferta Limitada: {desconto} OFF em {negocio}",
            "✅ Garantido: Satisfação ou seu dinheiro de volta",
            "🚀 Transforme sua {area} com {negocio} hoje mesmo",
            "💎 Exclusivo: Acesso VIP para {publico}",
            "⏰ Promoção Relâmpago: {negocio} com preço especial",
            "🎁 Bônus Grátis: Ganhe {bonus} ao escolher {negocio}"
        ],
        'video_scripts': [
            "🎬 Abertura: Por que {publico} precisa conhecer {negocio}",
            "📹 Tutorial: Passo a passo para usar {servico}",
            "🎥 Depoimento: Cliente real conta sua experiência",
            "🎞️ Bastidores: Como {negocio} funciona por dentro",
            "📺 Comparação: {negocio} vs. concorrência",
            "🎪 Demonstração: Veja {negocio} em ação",
            "🎨 Storytelling: A história por trás de {negocio}",
            "🎯 FAQ: Respostas para as dúvidas mais comuns",
            "🎪 Evento: Lançamento especial de {produto}",
            "🎬 Série: Episódio sobre {topico} em {setor}"
        ],
        'product_descriptions': [
            "🏷️ {produto}: A escolha inteligente para {publico}",
            "💎 Premium: {produto} com qualidade superior",
            "🔧 Funcional: {produto} que resolve {problema}",
            "🎯 Específico: {produto} feito sob medida para {necessidade}",
            "⚡ Rápido: {produto} com resultados imediatos",
            "🛡️ Confiável: {produto} com garantia de qualidade",
            "💰 Econômico: {produto} com melhor custo-benefício",
            "🌿 Sustentável: {produto} eco-friendly para o futuro",
            "🏆 Premiado: {produto} reconhecido pelo mercado",
            "🔄 Versátil: {produto} para múltiplas aplicações"
        ]
    }
    
    # Selecionar templates apropriados
    templates = content_templates.get(content_type, content_templates['social_media'])
    
    # Preparar variáveis para substituição
    variables = {
        'negocio': business_description.split('.')[0].strip(),
        'publico': target_audience.lower(),
        'setor': extract_sector_from_description(business_description),
        'problema': 'seus desafios',
        'servico': 'nossos serviços',
        'quantidade': random.choice(['5', '7', '10']),
        'estrategia': 'nossa metodologia',
        'objetivo': 'sucesso',
        'area': 'seus resultados',
        'tempo': random.choice(['24h', '7 dias', '30 dias']),
        'desconto': random.choice(['20%', '30%', '50%']),
        'bonus': 'material exclusivo',
        'produto': 'nossa solução',
        'topico': keywords.split(',')[0].strip() if keywords else 'inovação',
        'necessidade': 'suas demandas'
    }
    
    # Gerar ideias personalizadas
    selected_templates = random.sample(templates, min(quantity, len(templates)))
    
    ideas = []
    for template in selected_templates:
        idea = template
        for var, value in variables.items():
            idea = idea.replace(f'{{{var}}}', value)
        
        # Ajustar tom de voz
        idea = adjust_tone(idea, tone)
        
        # Adicionar keywords se especificadas
        if keywords and random.choice([True, False]):
            keyword = random.choice(keywords.split(',')).strip()
            idea += f" #{keyword.replace(' ', '')}"
        
        ideas.append(idea)
    
    return ideas

def extract_sector_from_description(description):
    """Extrai o setor do negócio da descrição"""
    sectors = {
        'tecnologia': ['tech', 'software', 'app', 'digital', 'sistema'],
        'saúde': ['saúde', 'médico', 'clínica', 'hospital', 'wellness'],
        'educação': ['educação', 'curso', 'escola', 'ensino', 'formação'],
        'varejo': ['loja', 'venda', 'produto', 'varejo', 'comércio'],
        'serviços': ['consultoria', 'assessoria', 'atendimento', 'serviço'],
        'alimentação': ['restaurante', 'comida', 'alimentação', 'culinária']
    }
    
    description_lower = description.lower()
    for sector, keywords in sectors.items():
        if any(keyword in description_lower for keyword in keywords):
            return sector
    
    return 'negócios'

def adjust_tone(idea, tone):
    """Ajusta o tom de voz da ideia"""
    if tone == 'professional':
        idea = idea.replace('🔥', '📊').replace('💰', '💼')
    elif tone == 'casual':
        idea = idea.replace('📊', '😊').replace('💼', '👍')
    elif tone == 'humorous':
        if not any(emoji in idea for emoji in ['😂', '🤣', '😄']):
            idea += ' 😄'
    elif tone == 'inspirational':
        idea = idea.replace('📊', '🌟').replace('💼', '✨')
    
    return idea

@login_required
@csrf_exempt
def dashboard_data_api(request):
    """API que fornece dados do dashboard via agente (Estrategista/Data Analyst).
    Aceita opcionalmente ?file_path= para direcionar análise de planilha.
    """
    try:
        file_path = request.GET.get('file_path')
        prompt = (
            "Você é o Estrategista do Marttin. Gere SOMENTE um JSON válido (sem texto extra) com este formato: "
            "{"
            "\"kpis\": {\"faturamento_mes\": number, \"novos_clientes\": number, \"cac\": number},"
            " \"cashflow\": {\"labels\": string[], \"entradas\": number[], \"saidas\": number[]},"
            " \"channels\": {\"labels\": string[], \"values\": number[]},"
            " \"latest_sales\": [{\"id\": number, \"data\": string, \"cliente\": string, \"canal\": string, \"valor\": number, \"status\": string}],"
            " \"insights\": [{\"icon\": string, \"title\": string, \"text\": string}]"
            "}"
            " Se uma planilha for fornecida, calcule KPIs a partir dela; caso contrário, use valores plausíveis."
        )
        result = ai_service.run_ai_consultor(prompt, arquivo=file_path, pergunta_sobre_arquivo=(
            "Calcule faturamento do mês, novos clientes e CAC; gere séries de fluxo de caixa 30 dias e divisão por canal. "
            "Retorne somente JSON no formato especificado."
        ) if file_path else None)

        raw = None
        if result:
            raw = result.get('resposta_final') or ''
        data = None
        if raw:
            try:
                data = json.loads(raw)
            except Exception:
                # Tenta extrair JSON entre chaves
                try:
                    start = raw.find('{')
                    end = raw.rfind('}')
                    if start != -1 and end != -1:
                        data = json.loads(raw[start:end+1])
                except Exception:
                    data = None
        if not data:
            # Fallback demo seguro
            data = {
                "kpis": {"faturamento_mes": 125430, "novos_clientes": 87, "cac": 62.5},
                "cashflow": {
                    "labels": [f"D{i}" for i in range(1, 13)],
                    "entradas": [12,9,14,11,16,13,18,14,17,15,19,18],
                    "saidas":   [9,8,11,10,12,12,13,12,14,13,15,14]
                },
                "channels": {"labels": ["Loja Online","Marketplace","Instagram","WhatsApp"], "values": [46,28,17,9]},
                "latest_sales": [
                    {"id":1,"data":"2025-10-25","cliente":"Maria Oliveira","canal":"Loja Online","valor":1290.00,"status":"Pago"},
                    {"id":2,"data":"2025-10-25","cliente":"João Lima","canal":"Marketplace","valor":349.90,"status":"Pago"},
                    {"id":3,"data":"2025-10-24","cliente":"Aline Souza","canal":"Instagram","valor":179.00,"status":"Pendente"},
                ],
                "insights": [
                    {"icon":"lightbulb","title":"Campanhas com melhor ROI","text":"Direcione mais orçamento para Instagram Ads (CAC -15%)."},
                    {"icon":"graph-up","title":"Fluxo de caixa","text":"Previsão de pico de despesas nos próximos 10 dias; considere antecipar recebíveis."}
                ]
            }
        return JsonResponse({"success": True, "data": data})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)

@login_required
def profile_view(request):
    """Tela de Perfil para configurar dados padrão da empresa (base de contexto dos agentes)."""
    company = None
    try:
        company = Company.objects.get(user=request.user)
    except Company.DoesNotExist:
        company = None

    if request.method == 'POST':
        # Fluxo: apagar conta
        if request.POST.get('delete_account') == '1':
            # Placeholder: apagar conta e dados (LGPD)
            u = request.user
            from django.contrib.auth import logout
            logout(request)
            u.delete()
            messages.success(request, 'Sua conta e dados foram removidos.')
            return redirect('agent:index')

        # Fluxo: upload de dados (form separado)
        if request.POST.get('upload_file') == '1':
            data_file = request.FILES.get('data_file')
            if not data_file:
                messages.error(request, 'Selecione um arquivo para enviar.')
                return redirect('agent:profile')
            # Persistir arquivo em diretório local "uploads"
            try:
                upload_dir = settings.BASE_DIR / 'uploads'
                os.makedirs(upload_dir, exist_ok=True)
                timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
                safe_name = f"user{request.user.id}_{timestamp}_" + data_file.name
                dest_path = upload_dir / safe_name
                with open(dest_path, 'wb+') as destination:
                    for chunk in data_file.chunks():
                        destination.write(chunk)
                # Registrar histórico (exibimos nome original para o usuário)
                FileUpload.objects.create(user=request.user, file_name=data_file.name)
                messages.success(request, 'Arquivo enviado com sucesso.')
            except Exception as e:
                messages.error(request, f'Falha no upload: {e}')
            return redirect('agent:profile')

        # Fluxo: salvar perfil (form principal)
        business_name = request.POST.get('business_name', '').strip()
        business_type = request.POST.get('business_type', '').strip()
        target_audience = request.POST.get('target_audience', '').strip()

        # Novos campos
        years_active = request.POST.get('years_active', '').strip()
        annual_revenue = request.POST.get('annual_revenue', '').strip()
        employees = request.POST.get('employees', '').strip()
        short_description = request.POST.get('short_description', '').strip()
        competitive_advantage = request.POST.get('competitive_advantage', '').strip()
        competitors = request.POST.get('competitors', '').strip()
        primary_goal = request.POST.get('primary_goal', '').strip()
        main_challenge = request.POST.get('main_challenge', '').strip()

        if not business_name or not business_type or not target_audience:
            messages.error(request, 'Preencha todos os campos obrigatórios.')
        else:
            Company.objects.update_or_create(
                user=request.user,
                defaults={
                    'business_name': business_name,
                    'business_type': business_type,
                    'target_audience': target_audience,
                    'years_active': years_active,
                    'annual_revenue': annual_revenue,
                    'employees': employees,
                    'short_description': short_description,
                    'competitive_advantage': competitive_advantage,
                    'competitors': competitors,
                    'primary_goal': primary_goal,
                    'main_challenge': main_challenge,
                }
            )
            messages.success(request, 'Perfil salvo com sucesso. Os agentes usarão essas informações como contexto.')
            return redirect('agent:profile')

    context = {
        'company': company,
        'business_type_choices': Company.BUSINESS_TYPE_CHOICES,
    }
    return render(request, 'agent/profile.html', context)

@login_required
def analyses_list_view(request):
    """Lista de análises do usuário (Caixa de Entrada)."""
    company = None
    analyses = []
    try:
        company = Company.objects.get(user=request.user)
        analyses = MarketingAnalysis.objects.filter(company=company).order_by('-created_at')
    except Company.DoesNotExist:
        company = None
        analyses = []
    return render(request, 'agent/analyses.html', {
        'analyses': analyses,
        'company': company,
    })

@login_required
def analysis_detail_view(request, analysis_id: int):
    """Tela de detalhe da análise com abas e gráficos/KPIs."""
    try:
        analysis = MarketingAnalysis.objects.select_related('company').get(id=analysis_id, company__user=request.user)
    except MarketingAnalysis.DoesNotExist:
        messages.error(request, 'Análise não encontrada.')
        return redirect('agent:analyses')

    # Dados estruturados para as abas
    result = analysis.analysis_result or {}
    insights_text = result.get('insights', '')
    recommendations = result.get('recommendations', '')
    growth = result.get('growth_strategies', '')
    next_steps = result.get('next_steps', '')

    context = {
        'analysis': analysis,
        'insights_text': insights_text,
        'recommendations': recommendations,
        'growth': growth,
        'next_steps': next_steps,
    }
    return render(request, 'agent/analysis_detail.html', context)
