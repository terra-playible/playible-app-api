from django.db import models
from core.models import BaseInfo


class Account(BaseInfo):
    username = models.CharField(max_length=155)
    wallet_addr = models.CharField(max_length=155, unique=True)
    image_url = models.CharField(max_length=155, null=True, blank=True)

    def __str__(self):
        return self.wallet_addr
        
    class Meta:
        ordering = ['-created_at', '-updated_at']


class Collection(BaseInfo):
    contract_addr = models.CharField(max_length=155, unique=True)
    
    def __str__(self):
        return self.contract_addr
        
    class Meta:
        ordering = ['-created_at', '-updated_at']


class Asset(BaseInfo):
    token_id = models.CharField(max_length=155) #Token ID
    owner = models.ForeignKey("Account", on_delete=models.CASCADE)
    collection = models.ForeignKey("Collection", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.token_id + ' ' + self.collection.contract_addr
      
    class Meta:
        ordering = ['-created_at', '-updated_at']
        constraints = [
            models.UniqueConstraint(fields=['token_id','collection'], name='unique_asset'),
        ]


class AssetProperties(BaseInfo):
    class DataType(models.TextChoices):
        NUMBER = 'NUMBER'
        STRING = 'STRING'
    name = models.CharField(max_length=155)
    value = models.CharField(max_length=155)
    data_type = models.CharField(max_length=30, choices=DataType.choices, default=DataType.STRING)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at', '-updated_at']


class PrelaunchEmail(BaseInfo):
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ['-created_at', '-updated_at']


class SalesOrder(BaseInfo):
    asset = models.OneToOneField("Asset", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=19, decimal_places=10)
    signed_message = models.CharField(max_length=155)
    message = models.CharField(max_length=155)
    
    def __str__(self):
        return self.asset.token_id + ' ' + self.asset.collection.contract_addr + '-' + str(self.price)
      
    class Meta:
        ordering = ['-created_at', '-updated_at']
