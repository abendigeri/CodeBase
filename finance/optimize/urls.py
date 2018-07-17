from django.conf.urls import url
from optimize import views


urlpatterns = [

    url(r'^$',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name),

    url(r'^investment/$',
        views.InvestmentList.as_view(),
        name=views.InvestmentList.name),

    url(r'^investment/(?P<pk>[0-9]+)$',
        views.InvestmentDetail.as_view(),
        name=views.InvestmentDetail.name),


    url(r'^test/$',
        views.investment_list,
        name='test-api')


]
