from django.urls import path
from .views import show

urlpatterns = [
    # path('show/', v.site.urls),
    path('show/', show),

]