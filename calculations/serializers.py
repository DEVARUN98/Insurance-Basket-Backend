from .models import Calculation,CalculationNew,CalculationNewForDrop,Companydetails
from rest_framework import serializers

# from rest_framework import serializers
class CalculationSerializer(serializers.Serializer):
    idv = serializers.FloatField()
    rate = serializers.FloatField()
    sAdd = serializers.FloatField()
    ncb = serializers.FloatField()
    discount = serializers.FloatField()
    seatingCapacity = serializers.IntegerField()
    legalLiability = serializers.FloatField()
    poAmoun = serializers.FloatField()
    regno = serializers.CharField(required=False, allow_blank=True)  # Optional, string field
    year = serializers.DateField(required=False)  # Optional date
    dueDate = serializers.DateField(required=False)  # Optional date


    def create(self, validated_data):
        print("i am here")
        # Create and save a new Calculation instance
        return Calculation.objects.create(**validated_data)

    # Calculation.objects.create(**data, field=value)

# main serailizer for CalculationNew model
class NewCalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculationNew
        fields = '__all__'
        read_only_fields = ['odpremium','odMinusNCB','netPremium','tpPremium','totalPremium','netPremiumAmount','poAmount','payableAmount','created_at','policyType']

    def create(self, validated_data):
        # data = serializer.validated_data
        idv = validated_data.get('idv', 0)
        rate = validated_data.get('rate', 0)
        sAdd = validated_data.get('sAdd', 0)
        ncb = validated_data.get('ncb', 0)
        discount = validated_data.get('discount', 0)
        seatingCapacity = validated_data.get('seatingCapacity', 0)
        legalLiability = validated_data.get('legalLiability', 0)
        po = validated_data.get('po', 0)
        company = validated_data.get('company',None)

        print('fffffffffffffffffffffffffffffffff',company)

        # rateValue = rate / 100

        odPremiumbefore = (idv * rate / 100) + sAdd
        odPremium = odPremiumbefore * 1.15 
        odMinusNCB = odPremium * (100 - ncb) / 100
        netPremium = odMinusNCB * (100 - discount) / 100
        tpPremium = 12192 + 745 * seatingCapacity + legalLiability * 50
        totalPremium = (netPremium + tpPremium) * 1.18
        netPremiumAmount = totalPremium/1.18
        poAmount = netPremiumAmount * po / 100

       
        payableAmount = totalPremium - poAmount
        if(company):
            if (company== "Reliance"):
                payableAmount+= 590
        print("final result payableAmount", payableAmount)


        # final_result = {
        #         'odPremium' : odPremium,
        #         'odMinusNCB' : odMinusNCB,
        #         'netPremium' : netPremium,
        #         'tpPremium' : tpPremium,
        #         'totalPremium' : totalPremium,
        #         'netPremiumAmount' : netPremiumAmount,
        #         'poAmount' : poAmount,
        #         'payableAmount' : payableAmount
        #     }
        
        validated_data['odPremium'] = odPremium
        validated_data['odMinusNCB'] = odMinusNCB
        validated_data['netPremium'] = netPremium
        validated_data['tpPremium'] = tpPremium
        validated_data['totalPremium'] = totalPremium
        validated_data['poAmount'] = poAmount
        validated_data['payableAmount'] = payableAmount
        print("validated_data after update", validated_data['payableAmount'])
        # validated_data.update(final_result)

        return super().create(validated_data)
    

# need to create serializer for CalculationNewForDrop model 


class CalculationDropSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculationNewForDrop
        fields = '__all__'
        # read_only_fields = 


        def create(self,validated_data):
            idvnew = validated_data.get('idvnew',0)
            ratenew = validated_data.get('ratenew',0)
            companyName = validated_data.get('companyName',0)
            sAddnew = validated_data.get('sAddnew',0)

            odPremiumnew = idvnew + ratenew + sAddnew

            validated_data['odPremiumnew'] = odPremiumnew

            return super().create(validated_data)
        
class CompanyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companydetails
        fields = '__all__'


