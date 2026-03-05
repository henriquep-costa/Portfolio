from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.views import ApplicationViewSet

# Router cria rotas automáticas para API
router = DefaultRouter()

# registra viewset
router.register(r'applications', ApplicationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # inclui rotas da API
    path('', include(router.urls)),
]