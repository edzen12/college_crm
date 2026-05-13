from django.contrib import admin
from django.urls import path, include
from college_crm.api_router import router
from apps.accounts.views import MeAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import (
    SpectacularAPIView, SpectacularSwaggerView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/', include(router.urls)), 

    path('api/me/', MeAPIView.as_view()), 
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema')), 
]
