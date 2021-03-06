from django.urls import path
from .import views

urlpatterns = [
    path('/', views.index),
    path('/st_patty_page', views.st_patty_page),
    path('/gov_quiz_page', views.gov_quiz),
    path('/white_house_quiz_page', views.white_house),
    path('/declaration_quiz_page', views.declaration),
    path('/earth_quiz_page', views.earth_page),
    path('/social_studies', views.history),
    path('/student_info', views.student_info),
    path('/add_student/<int:user_id>', views.add_student),
    path('/account_info', views.account_info),
    path('/hands_on', views.hands_on),
    path('/delete_student/<int:student_id>', views.delete_student),
    path('/success', views.success),
    # OUR GENERIC VALIDATOR
    path('/validate', views.generic_validator)
]
