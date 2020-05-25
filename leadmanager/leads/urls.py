from rest_framework import routers
from .api import LeadApiViewSet


router = routers.DefaultRouter()
router.register('api/leads',LeadApiViewSet, 'leads')
urlpatterns = router.urls
