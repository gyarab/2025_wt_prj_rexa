from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path('', views.render_homepage, name="homepage"),
    path('about/', views.render_about, name="about"),

    # API playground stránka
    path('api-playground/', views.render_api_playground, name='api_playground'),

    # API endpoint
    path('api/taktiky/', views.taktiky_api, name='taktiky_api'),
]
