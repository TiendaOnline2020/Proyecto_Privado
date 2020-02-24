"""ProyectoPersonal URL Configuration

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
from Afiliados.views import descargar_pdf
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = 'Administrador'
admin.site.site_title = 'Administrador'
admin.site.index_title = 'Administrador'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('descargar/<dni>', descargar_pdf, name="Descarga_PDF"),
    path('chaining/', include('smart_selects.urls')),
    path('', include('Afiliados.urls', namespace='afiliados')),
    path('registrar/',include('responsable.urls', namespace='registrar')),
    path('admin/chaining/',include('smart_selects.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
