"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static #추가
from django.conf import settings #추가

from mysite.views import HomeView, MainView, ManualView, DoneeView, DonorView
from mysite.views import UserCreateView, UserCreateDoneTV

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='videopage_ex'),
    url(r'^main/$', MainView.as_view(), name='mainpage_ex'),
    url(r'^manual/$', ManualView.as_view(), name='manual_home'),
    url(r'^donee/$', DoneeView.as_view(), name='manual_donee'),
    url(r'^donor/$', DonorView.as_view(), name='manual_donor'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),

    url(r'^photo/', include('photo.urls', namespace='photo')), #추가

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #추가
