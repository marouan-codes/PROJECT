from django.urls import path
from django.conf.urls import handler404
from . import views
from django.contrib.sitemaps.views import sitemap
from patagonia.sitemaps import BlogSitemap, PortfolioSitemap, StaticPagesSitemap



sitemaps = {
    'blog': BlogSitemap,
    'portfolio': PortfolioSitemap,
    'staticpages': StaticPagesSitemap,
}

urlpatterns = [
    path("", views.index, name="index"),
    path("portfolio/", views.work, name= "portfolio"),
    path("contact/", views.contact, name= "contact"),
    path("portfolio/<slug:slug>/", views.portfoliopage, name= "portfoliopage"),
    path("blog/", views.blogs, name= "blog"),
    path("adawat/", views.adawat, name= "adat"),
    path("blog/<slug:slug>/", views.blogpage, name= "blogpage"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # path("success/", views.success, name='success'),
]  
