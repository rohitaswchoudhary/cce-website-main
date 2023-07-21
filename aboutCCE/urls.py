from django.urls import path
from aboutCCE import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('management', views.management_page, name='Management'),
    path('hod_desk', views.hod_desk_page, name='HOD_Desk'),
    path('principals_desk', views.principals_desk_page, name='Principals_Desk'),
    path('cec_in_media', views.cec_in_media_page, name='CEC_in_Media'),

]

if settings.DEBUG:     
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
