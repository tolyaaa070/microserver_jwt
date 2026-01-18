from .views import UserProfileViewSet , CurrentUserView,CustomLoginView , LogoutView , RegisterView
from rest_framework import routers
from django.urls import path , include

router = routers.SimpleRouter()
router.register(r'user' , UserProfileViewSet , basename='user')

urlpatterns = [
    path('' , include(router.urls)),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path("api/users/me/", CurrentUserView.as_view(), name="current-user"),
]