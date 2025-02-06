
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

from Home import urls
import Home

import Events
from Events import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(Home.urls)),
    path("events",include(Events.urls)),
    
    
]
urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

