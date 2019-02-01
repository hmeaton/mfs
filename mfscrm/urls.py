from django.contrib import admin
from django.conf.urls import  include,url
from django.urls import path
from django.contrib.auth import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm.urls')),
    path('account/', include('account.urls')),
    #url('accounts/login/$', views.login, name='login'),
    #url('accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),

    url(r'^accounts/login/$', LoginView.as_view(template_name='registration/login.html'), name="login"),
    url(r'^accounts/logout/$', LogoutView.as_view(), LogoutView.next_page, name="logout"),
]
