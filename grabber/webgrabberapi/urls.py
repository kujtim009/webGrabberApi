"""ticketsManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
# router.register('graburl', views.UrlGrabberView.as_veiw(), basename="graburl")
# router.register('reshtat', views.ReshtatView)
# router.register('ulset', views.UlsetView)
# router.register('cmimet', views.CmimetView)
# router.register('llojiindeshjeve', views.LlojiIndeshjeveView)
# router.register('ndeshjet', views.NdeshjetView)
# router.register('ndeshjetcurrent', views.NdeshjetCurrentView)
# router.register('ulsetezena', views.UlsetEzenaView)

# router.register('updateulset', views.UpdateUlsetView)

# router.register('shitja', views.ShitjaView)
# router.register('ulsetregjion', views.UlsetRegjionView.as_view())

urlpatterns = [
    path('',include(router.urls)),
    path('graburl/', views.UrlGrabberView.as_view(), name="ulsetupdate"),
    path('getlinkedindata/', views.linkedinCompanyGrabber.as_view(), name="ulsetupdate")
    # path('graburl/', views.UrlGrabberView.as_view(), basename="graburl")
    # path('ulsetupdate/', views.UlsetUpdateStatus.as_view(), name="ulsetupdate"),
    # path('inserttickets/', views.ShitjaInsertView.as_view(), name="ulsetupdate"),
    # path('ulsetupdateall/', views.UpdateUlsetView.as_view(), name="ulsetupdateall"),
    # path('cmimetgroup/', views.CmimetGroupView.as_view(), name="cmimetgroup"),
    # path('auth/', obtain_auth_token, name='auth')
]
