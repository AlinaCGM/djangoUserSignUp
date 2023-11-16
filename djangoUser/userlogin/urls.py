from django.urls import path
from .views import home, login_view, signup, user_info

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('userinfo/', user_info, name='userinfo'),
]
 