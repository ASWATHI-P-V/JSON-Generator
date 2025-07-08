# # specs/urls.py
# from django.urls import path
# from . import views

# # API URL patterns
# urlpatterns = [
#     # API Endpoints
#     # This path handles both GET (list) and POST (create) requests.
#     # The ProjectSpecListCreateAPIView correctly uses ProjectSpecCreateSerializer for POST
#     # and ProjectSpecSerializer for GET, as per your setup.
#     path('api/spec/', views.ProjectSpecListCreateAPIView.as_view(), name='spec-list-create'),
    
#     # This path handles GET (retrieve) requests for a single project spec.
#     # It uses ProjectSpecSerializer for output.
#     path('api/spec/<int:pk>/', views.ProjectSpecRetrieveAPIView.as_view(), name='spec-detail'),
    
#     # This path handles the custom JSON download view.
#     path('api/spec/<int:pk>/download/', views.download_json, name='spec-download'),
    
#     # Additional API endpoints (currently commented out, no changes needed based on your request)
#     # path('api/spec/<int:pk>/json/', views.spec_detail_view, name='spec-json'),
    
#     # Health check endpoint (currently commented out, no changes needed based on your request)
#     # path('api/health/', views.health_check, name='health-check'),
# ]

# # Optional: Add URL patterns with namespace
# app_name = 'specs'

# # If you also have the web views defined in views.py, you would add them here.
# # Assuming your web views are separate and might use a different URL structure.
# # Example if you want to include them:
# urlpatterns += [
#     path('specs/create/', views.spec_create_view, name='spec-create-web'),
#     path('specs/', views.spec_list_view, name='spec-list-web'),
#     path('specs/<int:pk>/', views.spec_detail_view, name='spec-detail-web'),
# ]

# specs/urls.py
# from django.urls import path
# from . import views

# # API URL patterns
# urlpatterns = [
#     # API Endpoints
#     path('api/spec/', views.ProjectSpecListCreateAPIView.as_view(), name='spec-list-create'),
#     path('api/spec/<int:pk>/', views.ProjectSpecRetrieveAPIView.as_view(), name='spec-detail'),
#     path('api/spec/<int:pk>/download/', views.download_json, name='spec-download'),
    
#     # Additional API endpoints
#     # path('api/spec/<int:pk>/json/', views.spec_detail_view, name='spec-json'),
    
#     # Health check endpoint
# #     path('api/health/', views.health_check, name='health-check'),
# ]

# # Optional: Add URL patterns with namespace
# app_name = 'specs'

from django.urls import path
from . import views

# API URL patterns
urlpatterns = [
    # API Endpoints
    path('api/spec/', views.ProjectSpecListCreateAPIView.as_view(), name='spec-list-create'),
    path('api/spec/<int:pk>/', views.ProjectSpecRetrieveAPIView.as_view(), name='spec-detail'),
    path('api/spec/<int:pk>/download/', views.download_json, name='spec-download'),
    
    # Optional Web UI routes if you keep them
    path('spec/create/', views.spec_create_view, name='spec-create'),
    path('spec/list/', views.spec_list_view, name='spec-list'),
    path('spec/<int:pk>/detail/', views.spec_detail_view, name='spec-detail-web'), # Added a specific name for web detail
]

# Optional: Add URL patterns with namespace
app_name = 'specs'