from django.contrib import admin
from .models import Professor, Curso


class DetCursos(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'datainicio', 'mostrar')
    list_editable = ('mostrar',)
    list_display_links = ('titulo', )
    search_fields = ('titulo', )


admin.site.register(Professor)
admin.site.register(Curso, DetCursos)
