from django.contrib import admin
from .models import Empleado, TipoDeDocumento


admin.site.site_header = 'Empresa'
admin.site.site_url = '/web/inicio/'
admin.site.site_title = 'Administrador'
admin.site.index_title = ''

admin.site.register(Empleado)
admin.site.register(TipoDeDocumento)
