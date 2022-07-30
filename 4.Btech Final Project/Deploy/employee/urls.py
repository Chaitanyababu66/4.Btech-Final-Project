from django.conf.urls import url
from employee import views

urlpatterns = [
    url('diabetic', views.diabetic, name='diabetic'),
]
