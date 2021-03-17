from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.category

class Currency(models.Model):
    name = models.CharField(max_length=10, null=True)
    nation = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name

class Account(models.Model):
    name = models.CharField(max_length=50, null=True)
    nick = models.CharField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name


class Cashflowcategory(models.Model):
    name = models.CharField(max_length=20, null=True)
    constant = models.IntegerField(default=1, null=True)

    def __str__(self):
        return self.name

class Stocktradecategory(models.Model):
    name = models.CharField(max_length=20, null=True)
    constant = models.IntegerField(default=1, null=True)

    def __str__(self):
        return self.name

class Stock(models.Model):
    name = models.CharField(max_length=30, null=True)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, null=True)
    split_cons = models.IntegerField(default=1, null=True)
    memo = models.TextField(default='-', null=True)

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Cashflow(models.Model):
    date = models.DateField(null=True)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, null=True)
    io = models.ForeignKey(Cashflowcategory, on_delete=models.PROTECT, null=True)
    cash_krw = models.IntegerField(default=0, null=True)
    cash_usd = models.DecimalField(max_digits=15, decimal_places=2, default=0, null=True)



class Stocktrade(models.Model):
    date = models.DateField(null=True)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, null=True)
    io = models.ForeignKey(Stocktradecategory, on_delete=models.PROTECT, null=True)
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, null=True)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)

    objects=models.Manager()


    @property
    def price_total(self):
        return self.unit_price * self.amount * self.io.constant


class Asset(models.Model):
    date = models.DateField(unique=True, null=True)
    title = models.CharField(max_length=100, null=True)
    title_photo = models.ImageField(upload_to='img/blog_rich', default='img/blog/no_pic.jpg', null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    written_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    # current assets & prices
    deposit_krw = models.IntegerField(null=True)
    deposit_usd = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a1_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a1', default=1)
    a1_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a2_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a2', default=2)
    a2_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    """
    a3_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a3')
    a3_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a4_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a4')
    a4_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a5_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a5')
    a5_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a6_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a6')
    a6_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a7_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a7')
    a7_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a8_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a8')
    a8_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a9_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a9')
    a9_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a10_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a10')
    a10_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a11_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a11')
    a11_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a12_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a12')
    a12_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a13_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a13')
    a13_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a14_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a14')
    a14_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a15_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a15')
    a15_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a16_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a16')
    a16_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a17_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a17')
    a17_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a18_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a18')
    a18_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a19_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a19')
    a19_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a20_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a20')
    a20_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a21_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a21')
    a21_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a22_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a22')
    a22_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a23_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a23')
    a23_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a24_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a24')
    a24_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a25_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a25')
    a25_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a26_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a26')
    a26_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a27_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a27')
    a27_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a28_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a28')
    a28_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a29_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a29')
    a29_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a30_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a30')
    a30_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a31_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a31')
    a31_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a32_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a32')
    a32_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a33_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a33')
    a33_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a34_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a34')
    a34_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a35_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a35')
    a35_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a36_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a36')
    a36_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a37_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a37')
    a37_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a38_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a38')
    a38_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a39_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a39')
    a39_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a40_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a40')
    a40_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a41_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a41')
    a41_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a42_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a42')
    a42_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a43_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a43')
    a43_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a44_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a44')
    a44_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a45_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a45')
    a45_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a46_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a46')
    a46_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a47_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a47')
    a47_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a48_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a48')
    a48_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a49_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a49')
    a49_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    a50_name = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, related_name='a50')
    a50_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    """
    class Meta:
        ordering = ['-date']

    # objects = models.Manager()