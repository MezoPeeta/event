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
    path('', include('pwa.urls'))
]
urlpatterns += i18n_patterns(
    path("", include("base.urls")),
    path("", include("payment.urls")),
    path("", include("products.urls")),
    path("", include("users.urls")),
    path("", include("dashboard.urls")),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path(r"__debug__/", include('debug_toolbar.urls'))]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



handler404 = "base.views.error_404_view"
