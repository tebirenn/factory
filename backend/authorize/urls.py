from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views

app_name = 'authorize'

urlpatterns = [
    path('', views.HomeAPIView.as_view(), name='user-home'),
    path('signin/', views.SignInUser.as_view(), name='user-signin'),
    path('signup/', views.SignUpUser.as_view(), name='user-signup'),
    path('signout/', views.signout_user, name='user-signout'),
    path('tgregister/', views.SetTgIdAPIView.as_view(), name='user-tg-register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/user/', views.UserViewSet.as_view({'get': 'retrieve', 'post': 'create'})),
    path('send/', views.SendMessageAPIView.as_view(), name='user-send-message'),
]