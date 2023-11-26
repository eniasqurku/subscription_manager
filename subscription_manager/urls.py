from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

import customer.urls as customer_urls
import service.urls as service_urls
import subscription.urls as subscription_urls

schema_view = get_schema_view(
    openapi.Info(
        title="Subscription Manager API",
        default_version='v1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += service_urls.urlpatterns
urlpatterns += subscription_urls.urlpatterns
urlpatterns += customer_urls.urlpatterns
