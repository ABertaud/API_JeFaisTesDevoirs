from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from . import views # import views so we can use them in urls.
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Documentation REST-API_JeFaisTesDevoirs",
        default_version='v1',
        description="",
        terms_of_service="",
        contact=openapi.Contact(email="arthur.bertaud44@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.SimpleRouter()
router.register(r'Subject', views.SubjectViewSet)
router.register(r'Answer', views.AnswerViewSet)
router.register(r'File', views.FileViewSet)
router.register(r'User', views.CustomUserViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
