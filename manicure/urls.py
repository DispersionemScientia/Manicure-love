from django.contrib import admin
from django.urls import path, include

from records.views import RecordAPIView, RecordUpdateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('records.urls')),
    path('api/v1/recordlist/', RecordAPIView.as_view()),
    path('api/v1/recordlist/<int:pk>/', RecordUpdateAPIView.as_view()),
    path('api/v1/auth/', include('rest_framework.urls')),
]
