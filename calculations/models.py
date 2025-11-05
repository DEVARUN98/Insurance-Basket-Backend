from django.db import models


class Company(models.Model):
    comp_name = models.CharField(max_length=100)
    restrictions = models.JSONField(default=list)
    extra_charges = models.FloatField()


    def __str__(self):
        return self.comp_name | self.restrictions | self.extra_charges


# Create your models here.
class Calculation(models.Model):
    idv = models.FloatField()
    rate = models.FloatField()
    sAdd = models.FloatField()
    odPremium = models.FloatField()
    odMinusNCB = models.FloatField()
    ncb = models.IntegerField()
    discount = models.FloatField()
    netPremium = models.FloatField()
    legalLiability = models.FloatField()
    seatingCapacity = models.IntegerField()
    tpPremium = models.FloatField()
    totalPremium = models.FloatField()
    po = models.FloatField()
    poAmount = models.FloatField()
    payableAmount = models.FloatField()
    regYear = models.IntegerField()
    company = models.CharField(max_length=100)
    dueDate = models.DateField()
    policyType = models.CharField(max_length=100)
    regno = models.CharField(max_length=20,default='0')
    year = models.DateField(default='2000-01-01')
    poAmoun = models.FloatField(default=0.0)

# class CalculationNew(models.Model):
#     idv = models.FloatField()
#     rate = models.FloatField()
#     sAdd = models.FloatField()
#     odPremium = models.FloatField(null=True,blank=True)
#     odMinusNCB = models.FloatField(null=True,blank=True)
#     ncb = models.IntegerField()
#     discount = models.FloatField()
#     netPremium = models.FloatField(null=True,blank=True)
#     legalLiability = models.FloatField()
#     seatingCapacity = models.IntegerField()
#     tpPremium = models.FloatField(null=True,blank=True)
#     totalPremium = models.FloatField(null=True,blank=True)
#     po = models.FloatField(default=0.0)
#     poAmount = models.FloatField(null=True,blank=True)
#     payableAmount = models.FloatField(null=True,blank=True)
#     regYear = models.IntegerField()
#     company = models.CharField(max_length=100)
#     dueDate = models.DateField()
#     policyType = models.CharField(max_length=100)
#     regno = models.CharField(max_length=20,default='0')
#     year = models.DateField(default='2000-01-01')
#     # poAmoun = models.FloatField(default=0.0)
#     created_at = models.DateTimeField(auto_now_add=True)


# class FinalCalculationNew(models.Model):
#     # company = models.ForeignKey(Company,max_length=100,on_delete=models.CASCADE)   need to change to foreign key
#     company = models.CharField()
#     idv = models.FloatField()
#     rate = models.FloatField()
#     sAdd = models.FloatField()
#     odPremium = models.FloatField(null=True,blank=True)
#     odMinusNCB = models.FloatField(null=True,blank=True)
#     ncb = models.IntegerField()
#     discount = models.FloatField()
#     netPremium = models.FloatField(null=True,blank=True)
#     legalLiability = models.FloatField()
#     seatingCapacity = models.IntegerField()
#     tpPremium = models.FloatField(null=True,blank=True)
#     totalPremium = models.FloatField(null=True,blank=True)
#     po = models.FloatField(default=0.0)
#     poAmount = models.FloatField(null=True,blank=True)
#     payableAmount = models.FloatField(null=True,blank=True)
#     regYear = models.IntegerField()
#     # company = models.CharField(max_length=100)
#     dueDate = models.DateField()
#     policyType = models.CharField(max_length=100)
#     regno = models.CharField(max_length=20,default='0')
#     year = models.DateField(default='2000-01-01')
#     institute = models.CharField(max_length=100,null=True,blank=True)
#     # poAmoun = models.FloatField(default=0.0)
#     created_at = models.DateTimeField(auto_now_add=True)

#  main running calculation model
class CalculationNew(models.Model):
    # company = models.ForeignKey(Company,max_length=100,on_delete=models.CASCADE)   need to change to foreign key
    company = models.CharField()
    idv = models.FloatField()
    rate = models.FloatField()
    sAdd = models.FloatField()
    odPremium = models.FloatField(null=True,blank=True)
    odMinusNCB = models.FloatField(null=True,blank=True)
    ncb = models.IntegerField()
    discount = models.FloatField()
    netPremium = models.FloatField(null=True,blank=True)
    legalLiability = models.FloatField()
    seatingCapacity = models.IntegerField()
    tpPremium = models.FloatField(null=True,blank=True)
    totalPremium = models.FloatField(null=True,blank=True)
    po = models.FloatField(default=0.0)
    poAmount = models.FloatField(null=True,blank=True)
    payableAmount = models.FloatField(null=True,blank=True)
    regYear = models.IntegerField()
    # company = models.CharField(max_length=100)
    dueDate = models.DateField()
    policyType = models.CharField(max_length=100)
    regno = models.CharField(max_length=20,default='0')
    year = models.DateField(default='2000-01-01')
    institute = models.CharField(max_length=100,null=True,blank=True)
    # poAmoun = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)


# for dropdown companies

class Companydetails(models.Model):
    comp_name = models.CharField(max_length=100)
    restrictions = models.CharField(default=list)
    vehicle_type = models.CharField(max_length=100)
    extra_charges = models.FloatField()

    def __str__(self):
        return self.comp_name
    
class CalculationNewForDrop(models.Model):
    companyName = models.ForeignKey(Companydetails,on_delete=models.CASCADE)
    idvnew = models.FloatField()
    ratenew = models.FloatField()
    sAddnew = models.FloatField()
    odPremiumnew = models.FloatField(null=True,blank=True)
    # odMinusNCBnew = models.FloatField(null=True,blank=True)
    # ncbnew = models.IntegerField()
    # discountnew = models.FloatField()
    # netPremiumnew = models.FloatField(null=True,blank=True)
    # legalLiabilitynew = models.FloatField()
    # seatingCapacitynew = models.IntegerField()
    # tpPremiumnew = models.FloatField(null=True,blank=True)
    # totalPremiumnew = models.FloatField(null=True,blank=True)
    # ponew = models.FloatField(default=0.0)
    # poAmountnew = models.FloatField(null=True,blank=True)
    # payableAmountnew = models.FloatField(null=True,blank=True)
    # regYearnew = models.IntegerField()
    # # company = models.CharField(max_length=100)
    # dueDatenew = models.DateField()
    # policyTypenew = models.CharField(max_length=100)
    # regnonew = models.CharField(max_length=20,default='0')
    # yearnew = models.DateField(default='2000-01-01')
    # institutenew = models.CharField(max_length=100,null=True,blank=True)
    # # poAmoun = models.FloatField(default=0.0)
    # created_atnew = models.DateTimeField(auto_now_add=True)