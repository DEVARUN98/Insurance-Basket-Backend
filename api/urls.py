from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


#  for viewsets router is used and also need to register the viewset
router = DefaultRouter()
# eg for employee viewset registration
# router.register('employees',views.EmployeeViewSet,basename='employee')
router.register('calculation',views.NewCalculationView,basename='calculation')
router.register('calculationnew',views.CalculationNewView,basename='calculationnew')
router.register('calculationnewfordrop',views.CalculationNewDropView,basename='calculationnewfordrop')
router.register('companydetails',views.CompanydetailsView,basename='companydetails')

urlpatterns =[
    path('companies/',views.companiesView),
    path('companies/<int:pk>/',views.companyDetailView),

    path('',include(router.urls)),

    path('frontend/',views.CalculationApiView.as_view()),
    # path('frontend/',views.NewCalculationView.as_view({'post': 'create'})),
    # path('calculations/',views.CommentDetailView.as_view()),
    # path('calculationsNew/',views.CalculationNew.as_view()),


]