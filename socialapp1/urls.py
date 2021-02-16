from django.urls import path
from .views import loginpage, registerpage, home, logoutpage

urlpatterns = [
    path('', loginpage, name="login"),
    path('register/', registerpage, name="register"),
    path('userhome/', home, name='home'),
    path('logout/', logoutpage, name='logout'),

]