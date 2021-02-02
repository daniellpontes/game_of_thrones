"""game_of_thrones URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index
from casas import urls as casas_urls
from livros import urls as livros_urls
from personagens import urls as personagens_urls


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login_url'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_url'),
    path('', auth_views.LoginView.as_view()),
    path('accounts/', include('allauth.urls')),
    path('index/', index, name='principal_url'),
    path('admin/', admin.site.urls),
    path('casas/', include(casas_urls)),
    path('livros/', include(livros_urls)),
    path('personagens/', include(personagens_urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
