# specs/urls.py
from django.urls import path
from . import views

# API URL patterns
urlpatterns = [
    # API Endpoints
    path('api/spec/', views.ProjectSpecListCreateAPIView.as_view(), name='spec-list-create'),
    path('api/spec/<int:pk>/', views.ProjectSpecRetrieveAPIView.as_view(), name='spec-detail'),
    path('api/spec/<int:pk>/download/', views.download_json, name='spec-download'),
    
    # Additional API endpoints
    # path('api/spec/<int:pk>/json/', views.spec_detail_view, name='spec-json'),
    
    # Health check endpoint
#     path('api/health/', views.health_check, name='health-check'),
]

# Optional: Add URL patterns with namespace
app_name = 'specs'