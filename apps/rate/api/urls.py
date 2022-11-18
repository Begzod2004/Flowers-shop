from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.rate.api.v1.urls'))
]
