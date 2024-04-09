from django.contrib.sitemaps import Sitemap
from patagonia.models import portfolo, blog
from django.urls import reverse
from django.contrib.sites.models import Site

class BlogSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return blog.objects.all()

    def lastmod(self, obj):
        return obj.last_modified

class PortfolioSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7
    custome_domain = 'www.webstooone.com'
    
    def items(self):
        return portfolo.objects.all()

    def lastmod(self, obj):
        return obj.last_modified
    
    def get_urls(self, site=None, **kwargs):
        custome_site = Site(domain='webstooone.com', name='webstooone.com')  # Specify your custom domain here
        return super(PortfolioSitemap, self).get_urls(site=custome_site, **kwargs)
    
class StaticPagesSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    custom_domain = 'www.webstooone.com'

    def items(self):
        return ['/', '/contact/', '/blog/', '/portfolio/', '/robots.txt/']
    
    def get_urls(self, site=None, protocol='https', **kwargs):
        custom_site = Site(domain='webstooone.com', name='webstooone.com')  # Specify your custom domain here
        return super(StaticPagesSitemap, self).get_urls(site=custom_site, protocol=protocol, **kwargs)
    

    def location(self, obj):

        url = obj  # Assuming obj is the URL string
        
        if url.startswith('http://'):
            url = url.replace('http://', 'https://', 1)
        return url
