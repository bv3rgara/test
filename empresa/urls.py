from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/', login,
        {'template_name': 'login.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^api/', include('api.urls')),
    url(r'^web/', include('web.urls')),
]
