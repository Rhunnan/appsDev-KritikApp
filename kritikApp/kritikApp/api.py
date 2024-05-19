from rest_framework import routers
from kritikApps import views as kritikApps_views

router = routers.DefaultRouter()
router.register(r'user', kritikApps_views.UserViewSet)
router.register(r'establishment', kritikApps_views.EstablishmentViewSet)
router.register(r'review', kritikApps_views.ReviewViewSet)