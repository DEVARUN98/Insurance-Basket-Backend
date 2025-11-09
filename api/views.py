from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from calculations.serializers import CalculationSerializer, NewCalculationSerializer,CalculationDropSerializer,CompanyDetailsSerializer
from calculations.models import CalculationNew ,CalculationNewForDrop,Companydetails
from calculations.models import Calculation

# Create your views here.

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

            return Response(final_result, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class NewCalculationView(viewsets.ModelViewSet):

    queryset = Calculation.objects.all()
    serializer_class = CalculationSerializer

class CalculationNewView(viewsets.ModelViewSet):

    queryset = CalculationNew.objects.all()
    serializer_class = NewCalculationSerializer
    filter_backends = [SearchFilter]
    search_fields = ['regno','dueDate','year','idv','ncb','totalPremium','payableAmount','company','institute']

    
class CalculationNewDropView(viewsets.ModelViewSet):

    queryset = CalculationNewForDrop.objects.all()
    serializer_class = CalculationDropSerializer
    filter_backends = [SearchFilter]
    # search_fields = ['regno','dueDate','year','idv','ncb','totalPremium','payableAmount','company']
    search_fields = ['idvnew','ratenew','companyName','sAddnew']

class CompanydetailsView(viewsets.ModelViewSet):
    queryset = Companydetails.objects.all()
    serializer_class = CompanyDetailsSerializer
