from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('home/', views.index, name='home'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu-items/', views.MenuItemsViewSet.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemViewSet.as_view()),
    path('booking/', include(router.urls)),
    # path('secret/', views.secret)
    path('api-token-auth/', obtain_auth_token)
]
