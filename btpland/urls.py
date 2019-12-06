
from django.contrib import admin
from django.urls import path, include
from btp_land import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('blog/', views.Blog, name='blog'),
    path('forum/<id_model>', views.Forum, name='forum'),
    path('login/', views.Login, name='login'),
    path('administrator/', views.Admin, name='admin'),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)