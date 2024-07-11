"""
URL configuration for smpproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from smpapp1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Signuppage, name='signup'),
    path('index/', views.index, name='index'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('search/', views.search, name='search'),
    path('predict/<str:ticker_value>/<str:number_of_days>/', views.predict, name='predict'),
    path('ticker/', views.ticker, name='ticker'),
    path('login/', views.Loginpage, name='login'),
    path('homepage/', views.Homepage, name='homepage'),
    path('logout/', views.Logoutpage, name='logout'),
    path('uploadProfile/', views.uploadProfile, name='uploadProfile'),
    path('plotingData/', views.PlotingData, name='PlotingData'),
    path('news/', views.news, name='news'),
    path('settings/', views.settings, name='settings'),
    path('aboutus/', views.aboutus, name='aboutus')
]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)