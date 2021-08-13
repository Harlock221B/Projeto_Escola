from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='home'),
    path('curso/<int:idbusca>', views.mostrar, name='cursos'),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
