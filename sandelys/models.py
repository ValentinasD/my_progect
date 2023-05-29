from django.db import models
from django.forms import ModelForm

#
# class BaseModel(models.Model):
#     objects = models.Model()
#
#     class Meta:
#         abstract = True




CONDITION_VALUE = [('nau', 'nauja'),
                   ('nuk','nukainuota'),
                   ]

MANUFACTURER_VALUE=[('AEG','AEG'),
                    ('SIM', 'SIMENS'),
                    ('BOS', 'BOSCH'),
                    ('BEK', 'BEKO'),
                    ]


class NewSupplier(models.Model):
        supplier_name = models.CharField(blank=False, null=False, max_length=50)
        company_code = models.CharField(blank=False, null=False, max_length=30)
        company_address_country = models.CharField(blank=False, null=False, max_length=30)
        company_address_city = models.CharField(blank=False, null=False, max_length=30)
        company_address_street = models.CharField(blank=False, null=False, max_length=30)
        company_bank_account = models.CharField
        company_vat_code = models.CharField


class EnterNewProduct(models.Model):
    date_of_purchase = models.DateField(auto_now=True, blank=False, null=False)
    supplier_of_goods = models.CharField(blank=False, null=False, max_length=50)
    invoice_number = models.CharField(blank=False, null=False, max_length=15)
    manufacturer = models.CharField(choices=MANUFACTURER_VALUE, blank=False, null=False, max_length=20)
    product_category = models.CharField(blank=False, null=False, max_length=20)
    product_model = models.CharField(blank=False, null=False, max_length=20)
    quantity = models.CharField(blank=False, null=False, max_length=4)
    condition = models.CharField(choices=CONDITION_VALUE, max_length=15)
    product_price = models.FloatField(blank=False, null=False, max_length=15)

    def __repr__(self):
        return self.date_of_purchase, self.supplier_of_goods, self.invoice_number, self.manufacturer, \
               self.product_category, self.product_model, self.quantity, self.condition, self.product_price




