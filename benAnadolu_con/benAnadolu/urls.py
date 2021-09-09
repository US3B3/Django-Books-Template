from django.contrib import admin, sitemaps
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from benAnadolu.sitemaps import MakaleSitemap
from django.contrib.sitemaps.views import sitemap
from makale import views as makale_views


sitemaps = {
    'makaleler' : MakaleSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
    path('post/<str:isim>', makale_views.post, name='post'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('sayfalar.urls')),
    path('blog/', include('makale.urls')),
    path('videoders/', include('videoders.urls')),
    path('galeri/', include('galeri.urls')),
    path('vitrin/', include('vitrin.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
