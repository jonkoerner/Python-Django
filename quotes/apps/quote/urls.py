from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^quotes$', views.showquotes),
    url(r'^addquote$', views.addquote),
    url(r'^users/(?P<user_id>\d+)$', views.show_user),
    url(r'^addtoFav/(?P<quote_id>\d+)$', views.addtoFav),
    url(r'^removefromFav/(?P<quote_id>\d+)$', views.removefromFav)
]
