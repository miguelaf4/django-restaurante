"""webrestaurante URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views as views_core
from Services import views as views_services



from django.conf import settings
from recipe.urls import recipe_patterns
from blog.urls import blog_patterns
from pages.urls import page_patterns

urlpatterns = [
    path('', include('core.urls')),
    path('page/', include(page_patterns)),
    path('', include('Services.urls')),
    path('blog/', include(blog_patterns)),
    path('admin/', admin.site.urls),
    #path('recipe/',include('recipe.urls')),
    path('recipe/',include(recipe_patterns)),
    path('contact/', include('contact.urls')),


]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
