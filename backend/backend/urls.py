from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
<<<<<<< HEAD
#it is git fetch comment
=======
#it is url pattern.
>>>>>>> 489e89dc70d321d7808f67f0b1c59ae700acc375
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('AUTH.urls')),
    path('api/account/', include('ACCOUNT.urls')),
    path('api/attendance/',include('ATTENDANCE.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
