from django.db import models
from users.models import CustomUser
from PIL import Image as Img
import io
from django.core.files.uploadhandler import InMemoryUploadedFile


class Category(models.Model):
    url = models.SlugField(max_length=130, unique=True)
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"


class Brand(models.Model):
    name = models.CharField(max_length=200, unique=True)
    url = models.SlugField(max_length=130, unique=True)
    description = models.TextField(max_length=200)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Brands"
        verbose_name_plural = "Brands"


class ProductPhoto(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Photos"
        verbose_name_plural = "ProductPhoto"

    def save(self, **kwargs):
        if self.image:
            img = Img.open(io.BytesIO(self.image.read()))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.thumbnail((150, 160), Img.ANTIALIAS)  # (width,height)
            output = io.BytesIO()
            img.save(output, format='JPEG')
            output.seek(0)
            self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg"
                                              % self.image.name.split('.')[0], 'image/jpeg',
                                              "Content-Type: charset=utf-8", None)
            super(ProductPhoto, self).save()


class Review(models.Model):
    email = models.EmailField()
    name = models.CharField("Ism", max_length=200)
    text = models.TextField("Messages", max_length=5000)
    product = models.ForeignKey('Product', verbose_name="Product", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Messages"
        verbose_name_plural = "Messages"


class Product(models.Model):
    url = models.SlugField(max_length=150, unique=True)
    name = models.CharField(max_length=200, db_index=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)


class Order(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class Xususiyatlari(models.Model):
    vazni = models.CharField(max_length=100, null=True, blank=True)
    razmeri = models.CharField(max_length=100, null=True, blank=True)
    os_versiyasi = models.CharField(max_length=200, null=True, blank=True)
    wi_fi_standarti = models.CharField(max_length=100, null=True, blank=True)
    SIM_karta_turi = models.CharField(max_length=200, null=True, blank=True)
    aloqa_standarti = models.CharField(max_length=120, null=True, blank=True)
    kafolat_muddati = models.CharField(max_length=30, null=True, blank=True)
    old_kamera_olchamlari = models.CharField(max_length=50, null=True, blank=True)
    eshitish_vositasi = models.CharField(max_length=50, null=True, blank=True)
    ornatilgan_xotira = models.CharField(max_length=50, null=True, blank=True)
    operativ_xotira = models.CharField(max_length=50, null=True, blank=True)
    protsessor = models.CharField(max_length=50, null=True, blank=True)
    korpus_materiali = models.CharField(max_length=100, null=True, blank=True)
    registratsiya = models.CharField(max_length=50, null=True, blank=True)
    max_vedio_olchami = models.CharField(max_length=50, null=True, blank=True)
    orqa_kamera_soni = models.CharField(max_length=50, null=True, blank=True)
    xotira_kartasi_uyasi = models.CharField(max_length=50, null=True, blank=True)
    simsiz_interfeyslar = models.CharField(max_length=50, null=True, blank=True)
    batareya_quvvati = models.CharField(max_length=100, null=True, blank=True)
    asosiy_kamera = models.CharField(max_length=50, null=True, blank=True)
    vedio_tezligi = models.CharField(max_length=50, null=True, blank=True)
    max_kadr_tezligi = models.CharField(max_length=50, null=True, blank=True)
    prosessor_yadrolari_soni = models.CharField(max_length=50, null=True, blank=True)
    fullhd_vedio_tezligi = models.CharField(max_length=60, null=True, blank=True)
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, blank=True, related_name='xususiyatlar')

