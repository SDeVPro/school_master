from django.urls import path #url adressni qaysi appdan qayerga murojaat qilishi va qayerga olib chiqishini ta'minlaydi
from home import views

urlpatterns = [
    path('',views.index,name='index'),
    path('post/',views.post,name='post'),
    path('student/',views.student,name='student'),
    path('teacher/',views.teacher,name='teacher'),
]
