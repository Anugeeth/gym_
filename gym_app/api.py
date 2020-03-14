from rest_framework import routers
from gym import views as api

router = routers.DefaultRouter()
router.register(r'members', api.MemberViewset)
router.register(r'log', api.SubscriptionViewset)