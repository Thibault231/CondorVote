"""condorVote_project URL Configuration

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
from django.conf import settings
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from common import views


urlpatterns = [
    # urls for APPs
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path(
        'common/',
        include(('common.urls', 'app_name'), namespace='common')),
    path(
        'desk/',
        include(('desk.urls', 'app_name'), namespace='desk')),
    path(
        'account/',
        include(('account.urls', 'app_name'), namespace='account')),
    path(
        'account/',
        include(('django.contrib.auth.urls', 'app_name'), namespace='author')),
    
    # urls for changing password
    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='registration/password_change_done.html'),
        name='password_change_done'),
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name='registration/password_change.html'),
        name='password_change'),

    # urls for reseting password
    path(
        'account/password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset.html'),
        name="password_reset"),
    path(
        'account/password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'),
        name="password_reset_done"),
    path(
        'account/reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'),
        name="password_reset_confirm"),
    path(
        'account/reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'),
        name="password_reset_complete")
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(
            r'^__debug__/',
            include(
                debug_toolbar.urls,
                namespace='debug_toolbar')),
    ] + urlpatterns
