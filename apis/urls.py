from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'manager', views.ManagerViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'salesperson', views.SalespersonViewSet)
router.register(r'item', views.ItemViewSet)
router.register(r'inventory', views.InventoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("SignIn", views.SignIn, name="SignIn"),
    # path('VerifyChangePassword/<slug:timestamp/<slug:username>/',views.VerifyChangePassword,name='VerifyChangePassword'),
    path("ChangePassword", views.ChangePassword, name="ChangePassword"),
    path("Logout", views.Logout, name="Logout"),
    # path("accept", views.accept, name="accept"),
]


