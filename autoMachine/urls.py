
from django.urls import path, include
from .views import *
app_name='autoMachine'

urlpatterns = [
    path('', mainview ),
    path('scrap/', scrap, name='scrap' ),
    path('submitScrap/', submitScrap, name='submitScrap'),
    path('chat/', include('chat.urls')),

]
