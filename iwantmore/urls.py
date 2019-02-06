"""iwantmore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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


from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.conf.urls import url

from main import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^(?P<child_id>\d+)/$', views.child_detail, name='child-detail'),
    # url(r'^admin/', admin.site.urls),
    path('', include('main.urls')),
    # url(r'^$', views.home, name='home'),
    url(r'^auth/login/$', auth_view.LoginView.as_view(template_name='auth/login.html'), name='auth-login'),
    url(r'^auth/logout/$', auth_view.LogoutView.as_view(next_page='/'), name='auth-logout'),
    url(r'^auth/registration/$', views.auth_registration, name='auth-registration')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
