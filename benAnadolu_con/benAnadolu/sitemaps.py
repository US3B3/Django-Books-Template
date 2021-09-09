from django.contrib.sitemaps import Sitemap
from makale.models import Makale

class MakaleSitemap(Sitemap):
    def items(self):
        return Makale.objects.all()