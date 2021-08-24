from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('sayfalar.urls')),
    path('blog/', include('makale.urls')),
    path('videoders/', include('videoders.urls')),
    path('galeri/', include('galeri.urls')),
    path('vitrin/', include('vitrin.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
