from django.conf.urls import url, include

from apps.accounts import views as accounts_views

urlpatterns = [
url(r'^auth/login/$', accounts_views.MembersLoginView.as_view(), name="login"),
    url(r'^auth/', include('rest_auth.urls')),
]
