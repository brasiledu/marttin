from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    BUSINESS_TYPE_CHOICES = [
        ('ecommerce', 'E-commerce'),
        ('services', 'Serviços'),
        ('saas', 'SaaS / Software'),
        ('retail', 'Varejo Físico'),
        ('restaurant', 'Restaurante / Food'),
        ('health', 'Saúde / Wellness'),
        ('education', 'Educação'),
        ('consulting', 'Consultoria'),
        ('other', 'Outro'),
    ]

    YEARS_ACTIVE_CHOICES = [
        ('lt1', '< 1 ano'),
        ('1-3', '1-3 anos'),
        ('gt3', '+3 anos'),
    ]

    ANNUAL_REVENUE_CHOICES = [
        ('mei', 'MEI (até R$ 81k)'),
        ('me', 'ME (R$ 81k - R$ 360k)'),
        ('epp', 'EPP (R$ 360k - R$ 4.8M)'),
        ('other', 'Outro / Não sei informar'),
    ]

    EMPLOYEES_CHOICES = [
        ('solo', 'Eu sozinho'),
        ('1-5', '1-5'),
        ('6-20', '6-20'),
        ('20+', '+20'),
    ]

    PRIMARY_GOAL_CHOICES = [
        ('increase_sales', 'Aumentar minhas vendas'),
        ('reduce_costs', 'Reduzir meus custos'),
        ('organize_finances', 'Organizar minhas finanças'),
        ('improve_marketing', 'Melhorar meu marketing'),
        ('exploring', 'Apenas explorando'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    business_name = models.CharField(max_length=200, verbose_name='Nome da Empresa')
    business_type = models.CharField(max_length=50, choices=BUSINESS_TYPE_CHOICES, verbose_name='Setor de Atuação')

    # Seção 2: Identidade
    years_active = models.CharField(max_length=8, choices=YEARS_ACTIVE_CHOICES, blank=True, null=True, verbose_name='Tempo de Atividade')
    annual_revenue = models.CharField(max_length=8, choices=ANNUAL_REVENUE_CHOICES, blank=True, null=True, verbose_name='Porte/Faturamento Anual')
    employees = models.CharField(max_length=8, choices=EMPLOYEES_CHOICES, blank=True, null=True, verbose_name='Número de Funcionários')

    # Seção 3: Coração do Negócio
    short_description = models.TextField(blank=True, null=True, verbose_name='Descrição Curta')
    target_audience = models.TextField(verbose_name='Público-Alvo (ICP)')
    competitive_advantage = models.TextField(blank=True, null=True, verbose_name='Diferencial Competitivo')
    competitors = models.TextField(blank=True, null=True, verbose_name='Principais Concorrentes')

    # Seção 4: Objetivos e Desafios
    primary_goal = models.CharField(max_length=32, choices=PRIMARY_GOAL_CHOICES, blank=True, null=True, verbose_name='Meu Principal Objetivo')
    main_challenge = models.TextField(blank=True, null=True, verbose_name='Meu Maior Desafio')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
    
    def __str__(self):
        return self.business_name

class MarketingAnalysis(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='analyses')
    current_strategy = models.TextField(verbose_name='Estratégia Atual')
    goals = models.TextField(verbose_name='Objetivos de Marketing')
    analysis_result = models.JSONField(verbose_name='Resultado da Análise', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Análise de Marketing'
        verbose_name_plural = 'Análises de Marketing'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Análise - {self.company.business_name} - {self.created_at.strftime("%d/%m/%Y")}'

class FileUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='file_uploads')
    file_name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = 'Arquivo Enviado'
        verbose_name_plural = 'Arquivos Enviados'

    def __str__(self):
        return self.file_name
