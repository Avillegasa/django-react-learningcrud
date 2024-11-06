from django.urls import path, include
from tasks import views
from rest_framework import routers


#api versioning
router = routers.DefaultRouter()
router.register(r'tasks', views.TaskView, 'tasks' )
urlpatterns = [
    path('api/v1/', include(router.urls))
]