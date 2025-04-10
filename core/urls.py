from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from core.swagger.schema import swagger_urlpatterns

urlpatterns = [
    path('m/', include("apps.main.urls")),
    path('<path:path>', RedirectView.as_view(url='/m/countdown/', permanent=False)),
    # path('admin/', admin.site.urls),
    # path('api/v1/common/', include("apps.users.urls"))
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

