from django.urls import path
from . import views

app_name = 'agent'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # Rotas do Agente IA
    path('chat/', views.chat_view, name='chat'),
    path('api/chat/', views.chat_api, name='chat_api'),
    path('marketing-analysis/', views.marketing_analysis_view, name='marketing_analysis'),
    path('api/marketing-analysis/', views.marketing_analysis_api, name='marketing_analysis_api'),
    path('content-ideas/', views.content_ideas_view, name='content_ideas'),
    path('api/content-ideas/', views.content_ideas_api, name='content_ideas_api'),
    path('test-ai/', views.test_ai_connection, name='test_ai'),
    
    # Rotas para gerenciamento de empresas
    path('api/check-company/', views.check_company, name='check_company'),
    path('api/register-company/', views.register_company, name='register_company'),
    path('api/get-company/', views.get_company, name='get_company'),
    path('api/dashboard-data/', views.dashboard_data_api, name='dashboard_data_api'),
    path('perfil/', views.profile_view, name='profile'),

    # Minhas Análises (Caixa de Entrada) e Detalhe
    path('analises/', views.analyses_list_view, name='analyses'),
    path('analises/<int:analysis_id>/', views.analysis_detail_view, name='analysis_detail'),
]