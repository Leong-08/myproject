
# cofig/urls.py
# import settins
from os import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

# urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    # Main app
    path('', include('photoapp.urls')),
    path('photoapp/', include('photoapp.urls', namespace='photos')),
    # Auth app
    path('users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
