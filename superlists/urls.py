from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'lists.views.home_page', name='home_page'),
    url(r'^lists/the-only-list-in-the-world/$', 'lists.views.view_list',
        name='view_list'),
]
