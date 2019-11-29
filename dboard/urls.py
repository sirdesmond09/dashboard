from django.urls import path, include
from .views import *
from .api import LawyerList, LawyerDetail

urlpatterns = [
    path('', index, name='home'),
    path('add-lawyer/', add_lawyer , name='add_lawyer'),
    path('add-user/', add_user , name='add_user'),
    path('lawyers/', lawyers_profile, name= 'lawyers_profile'),
    path('users/', user_profile, name= 'user_profile'),
    path('profile/', profile, name = 'profile'), 

    #api Url
    path('api/lawyerslist/', LawyerList.as_view(), name = 'lawyer_api' ),
    path('api/lawyerslist/<int:lawyer_id>', LawyerDetail.as_view(), name = 'lawyer_api' )
]
