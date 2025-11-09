from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


#  for viewsets router is used and also need to register the viewset
router = DefaultRouter()
router.register('calculation',views.NewCalculationView,basename='calculation')
router.register('calculationnew',views.CalculationNewView,basename='calculationnew')
router.register('calculationnewfordrop',views.CalculationNewDropView,basename='calculationnewfordrop')
router.register('companydetails',views.CompanydetailsView,basename='companydetails')

urlpatterns =[

    path('',include(router.urls)),
    path('frontend/',views.CalculationApiView.as_view()),
]