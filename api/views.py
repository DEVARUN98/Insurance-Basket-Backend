from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .serializers import CompanySerializer
from companies.models import Companies
from rest_framework.response import Response
from rest_framework import status,mixins,generics,viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.filters import SearchFilter,OrderingFilter
from calculations.serializers import CalculationSerializer, NewCalculationSerializer,CalculationDropSerializer,CompanyDetailsSerializer
from calculations.models import CalculationNew ,CalculationNewForDrop,Companydetails
from calculations.models import Calculation
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
@api_view(['GET','POST'])
def companiesView(request):
    if request.method == 'GET':
        cmpny = Companies.objects.all()
        serializer = CompanySerializer(cmpny,many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer= CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # print(cmpny_list)

@api_view(['GET','PUT','DELETE'])
def companyDetailView(request,pk):

    try:
        cmpny = Companies.objects.get(pk=pk)
    except Companies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # to find an item from all data
    if request.method == 'GET':
        serializer = CompanySerializer(cmpny)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = CompanySerializer(cmpny,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        cmpny.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# class Employee(APIView):
#     def get(self,request):
#         employees = Employees.objects.all()
#         seralizer = EmployeeSerilaizer(employees,many=True)
#         return Response(seralizer.data,status=status.HTTP_200_OK)

#     def post(self,request):
#         serializer = EmployeeSerilaizer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# class EmployeeDetails(APIView):
#     def get_object(self,pk):
#         try:
#             return Employees.objects.get(pk=pk)
#         except Employees.DoesNotExist:
#             # return Response(status=status.HTTP_404_NOT_FOUND)
#             raise Http404
        
#     def get(self,request,pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerilaizer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)

#     def put(self,request,pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerilaizer(employee,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
        
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


"""

# Mixins
class Employee(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerilaizer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
# Mixins

class EmployeeDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerilaizer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)

"""

"""
# Generics

class Employee(generics.ListCreateAPIView):
    queryset=Employees.objects.all()
    serializer_class = EmployeeSerilaizer

class EmployeeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerilaizer
    lookup_field = "pk"

"""

"""

# viewsets.ViewSet

class EmployeeViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Employees.objects.all()
        serializer = EmployeeSerilaizer(queryset,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = EmployeeSerilaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors)
    
    def update(self,request,pk=None):
        employee = get_object_or_404(Employees,pk=pk)
        serializer = EmployeeSerilaizer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_204_NO_CONTENT)
    
    def delete(self,request,pk=None):
        emploee = get_object_or_404(Employees,pk=pk)
        emploee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def retrieve(self,request,pk=None):
        employee = get_object_or_404(Employees,pk=pk)
        serializer = EmployeeSerilaizer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)

"""



from rest_framework.views import APIView
from rest_framework.response import Response
from calculations.models import Calculation

class MyAPIView(APIView):

    # def get(self, request):
    #     calculation = Calculation.objects.all()
    #     serializer = CalculationSerializer(calculation, many=True)
    #     return Response(serializer.data)
    



    def post(self, request):
        userInputData = request.data
        print("Received data:", userInputData)

        serializer = CalculationSerializer(data=userInputData)
        if serializer.is_valid():
            
            data = serializer.validated_data
            idv = data.get('idv', 0)
            rate = data.get('rate', 0)
            sAdd = data.get('sAdd', 0)
            ncb = data.get('ncb', 0)
            discount = data.get('discount', 0)
            seatingCapacity = data.get('seatingCapacity', 0)
            legalLiability = data.get('legalLiability', 0)
            poAmoun = data.get('poAmoun', 0)

            # rateValue = rate / 100

            odPremiumbefore = (idv * rate / 100) + sAdd
            odPremium = odPremiumbefore * 1.15 
            odMinusNCB = odPremium * (100 - ncb) / 100
            netPremium = odMinusNCB * (100 - discount) / 100
            tpPremium = 12192 + 745 * seatingCapacity + legalLiability * 50
            totalPremium = (netPremium + tpPremium) * 1.18
            netPremiumAmount = totalPremium/1.18
            poAmount = netPremiumAmount * poAmoun / 100
            payableAmount = totalPremium - poAmount

            final_result = {
                'odPremium': odPremium,
                'odMinusNCB': odMinusNCB,
                'netPremium': netPremium,
                'tpPremium': tpPremium,
                'totalPremium': totalPremium,
                'poAmount': poAmount,
                'netPremiumAmount': netPremiumAmount,
                'payableAmount': payableAmount
            }
            print("Final Result:", final_result)
            serializer.save()

            return Response(final_result, status=status.HTTP_201_CREATED)

        else:
            print("Serializer is invalid:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class CalculationApiView(APIView):
    def post(self,request):
        userInputData = request.data

        serializer = CalculationSerializer(data = userInputData)

        if serializer.is_valid():
            data = serializer.validated_data
            idv = data.get('idv',0)
            rate = data.get('rate',0)
            sAdd = data.get('sAdd',0)
            ncb = data.get('ncb',0)
            discount = data.get('discount',0)
            seatingCapacity = data.get('seatingCapacity',0)
            legalLiability = data.get('legalLiability',0)
            po = data.get('po',0)
            # idv = data.get('idv',0)
            # idv = data.get('idv',0)
            # idv = data.get('idv',0)
            

            # calculation

            odPremiumbefore = (idv * rate / 100) + sAdd
            odPremium = odPremiumbefore * 1.15 
            odMinusNCB = odPremium * (100 - ncb) / 100
            netPremium = odMinusNCB * (100 - discount) / 100
            tpPremium = 12192 + 745 * seatingCapacity + legalLiability * 50
            totalPremium = (netPremium + tpPremium) * 1.18
            netPremiumAmount = totalPremium/1.18
            poAmount = netPremiumAmount * po / 100
            payableAmount = totalPremium - poAmount
            print("final result payableAmount", payableAmount)


            final_result = {
                'odPremium' : odPremium,
                'odMinusNCB' : odMinusNCB,
                'netPremium' : netPremium,
                'tpPremium' : tpPremium,
                'totalPremium' : totalPremium,
                'netPremiumAmount' : netPremiumAmount,
                'poAmount' : poAmount,
                'payableAmount' : payableAmount
            }
            # final_serializer = CalculationSerializer(data=final_result)
            # print("final_serializer", final_serializer)
            # if final_serializer.is_valid():
            
            # data[odPremium] = odPremium
            # data[odMinusNCB] = odMinusNCB
            # data[netPremium] = netPremium
            # data[tpPremium] = tpPremium
            # data[totalPremium] = totalPremium
            # data[poAmount] = poAmount
            # data[payableAmount] = payableAmount
            # print("final result validated_data", data)
            # # validated_data.update(final_result)

            # return super().create(data)
            return Response(final_result, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class NewCalculationView(viewsets.ModelViewSet):

    queryset = Calculation.objects.all()
    serializer_class = CalculationSerializer

class CalculationNewView(viewsets.ModelViewSet):

    queryset = CalculationNew.objects.all()
    serializer_class = NewCalculationSerializer
    filter_backends = [SearchFilter]
    search_fields = ['regno','dueDate','year','idv','ncb','totalPremium','payableAmount','company']

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     # can add further fields for searching if required
    #     company = self.request.query_params.get('company', None)

    #     if company:
    #         queryset = queryset.filter(company__iexact = company)

    #     return queryset
    
class CalculationNewDropView(viewsets.ModelViewSet):

    queryset = CalculationNewForDrop.objects.all()
    serializer_class = CalculationDropSerializer
    filter_backends = [SearchFilter]
    # search_fields = ['regno','dueDate','year','idv','ncb','totalPremium','payableAmount','company']
    search_fields = ['idvnew','ratenew','companyName','sAddnew']

class CompanydetailsView(viewsets.ModelViewSet):
    queryset = Companydetails.objects.all()
    serializer_class = CompanyDetailsSerializer
