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
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    business_name = models.CharField(max_length=200, verbose_name='Nome do Negócio')
    business_type = models.CharField(max_length=50, choices=BUSINESS_TYPE_CHOICES, verbose_name='Tipo de Negócio')
    target_audience = models.TextField(verbose_name='Público-Alvo')
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

# Create your models here.
