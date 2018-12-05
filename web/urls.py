from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

from . import views


urlpatterns = [
    url(r'^inicio/$', login_required(views.vista_inicio), name='inicio'),
    url(r'^nuevo/$', views.vista_empleado, name='crear_empleado'),
    url(r'^registrar/', views.vista_registrar.as_view(), name='registrar'),
    # url(r"^reportes/(?P<id>\d+)/$", views.vista_reportes, name='reportes'),
    # url(r"^excel/(?P<id>\d+)/(?P<fecha>\d\d/\d\)/$", views.el, name='excel'),
    url(r'^password_reset/', password_reset,
        {'template_name': 'password_reset_form.html', 'email_template_name':
         'password_reset_email.html'},
        name='password_reset'),
    url(r'^password_reset_done/', password_reset_done,
        {'template_name': 'password_reset_done.html'},
        name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        password_reset_confirm, {'template_name':
                                 'password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^done/', password_reset_complete,
        {'template_name': 'password_reset_complete.html'},
        name='password_reset_complete'),
]
