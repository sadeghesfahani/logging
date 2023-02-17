from django.urls import path
from .views import message

urlpatterns = [
    # path('show/', v.site.urls),
    path('message/', message , name='message'),

]