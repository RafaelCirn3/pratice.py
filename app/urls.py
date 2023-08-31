from rest_framework import routers 
from .views import TodoListViewset, FerramentaViewSet

router = routers.DefaultRouter()
router.register(r"Todo",TodoListViewset)
router.register(r"Ferramenta",FerramentaViewSet )
urlpatterns = router.urls