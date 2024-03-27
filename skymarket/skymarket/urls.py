from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from djoser.views import UserViewSet
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import SimpleRouter

# TODO здесь необходимо подклюючит нужные нам urls к проекту
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Callboard description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

user_router = SimpleRouter()
user_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", include(user_router.urls)),
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
    path('api/ads/', include('ads.urls', namespace='ads')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
