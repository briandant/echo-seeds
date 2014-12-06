from django.conf.urls import patterns, url

from seedbank import views

urlpatterns = patterns('',

    url(r'^$', views.ListSeedView.as_view(),
        name='seeds-list',),
    url(r'^new$', views.CreateSeedView.as_view(),
        name='seeds-new',),
    url(r'^edit/(?P<pk>\d+)/$', views.UpdateSeedView.as_view(),
        name='seeds-edit',),
    url(r'^delete/(?P<pk>\d+)/$', views.DeleteSeedView.as_view(),
        name='seeds-delete',),
    url(r'^(?P<pk>\d+)/$', views.SeedView.as_view(),
        name='seeds-view',),
    # url(r'^edit/(?P<pk>\d+)/locations$', views.EditSeedLocationView.as_view(),
    #     name='seeds-edit-locations',),
)
