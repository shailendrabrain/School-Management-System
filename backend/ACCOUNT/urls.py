from django.urls import path
from . import views

urlpatterns = [
            path('profile/student/',views.RegisterView.as_view(),name='student_profile'),
]
