"""TEDx URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path("maintenance-mode/", include("maintenance_mode.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
    path("us/", admin.site.urls, name="Admin_Dashboard"),
]
urlpatterns += i18n_patterns(
    path("", include("apps.base.urls")),
    path("", include("apps.payment.urls")),
    path("", include("apps.products.urls")),
    path("", include("apps.users.urls")),
    path("", include("apps.dashboard.urls")),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = "apps.base.views.error_404_view"
