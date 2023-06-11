from django.db import models


# Create your models here.
CHATOGORY_CHOICES=(
    ('CR','curd'),
    ('ML','Milk'),
    ('LS','Lassi'),
    ('MS','Milkshake'),
    ('PN','Panner'),
    ('GH','Ghee'),
    ('CZ','cheesse'),
    ('IC','Icecreams'),

)

class product(models.Model):
    title = models.CharField(max_length=100)
    selling_price =models.FloatField()
    discount_price =models.FloatField()
    discription =models.TextField()
    composiotion =models.TextField()
    prodapp =models.TextField()
    category =models.CharField(choices=CHATOGORY_CHOICES,max_length=2)
    product_image =models.ImageField(upload_to="product")

    def __str__(self):
        return self.title
0