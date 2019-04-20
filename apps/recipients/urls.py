from __future__ import unicode_literals

from rest_framework.routers import SimpleRouter

from apps.recipients import views as recipients_views

router = SimpleRouter()
router.register(r'recipient', recipients_views.RecipientViewset)
router.register(r'social-activity', recipients_views.SocialActivityViewset)


urlpatterns = router.urls