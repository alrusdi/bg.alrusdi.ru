"""gamechooser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from django.contrib.staticfiles import views as static_views

from chooser import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', login_required(views.Index.as_view())),
    path('games/', login_required(views.GamesList.as_view())),
    path('choose-game/', csrf_exempt(login_required(views.ChooseGame.as_view()))),
    path('register-play/', csrf_exempt(login_required(views.RegisterPlay.as_view()))),
    path('reject-play/', csrf_exempt(login_required(views.RejectPlay.as_view()))),
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', static_views.serve),
    ]
