from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from chatauth.core.views import frontpage, signup, ProfilePage

urlpatterns = (
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('profile/<int:pk>/', ProfilePage.as_view(), name='profile'),

)