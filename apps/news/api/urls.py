from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.news.api.v1.urls'))
]
