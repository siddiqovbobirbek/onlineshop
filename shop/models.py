from django.db import models


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
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Brands"
        verbose_name_plural = "Brands"


class ProductPhoto(models.Model):
    url = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(null=True, blank=True)
    text = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Photos"
        verbose_name_plural = "ProductPhoto"


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
    brand = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    item = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.item) + ": $" + str(self.price)

    class Meta:
        ordering = ('name',)


class Order(models.Model):
    name = models.CharField(max_length=200)
    url = models.SlugField(max_length=250, unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200)
    number = models.IntegerField(unique=True)
    datetime = models.DateTimeField(auto_now_add=True)
    total = models.PositiveSmallIntegerField("Jami summa", default=0)

    def __str__(self):
        return self.number


class OrderDetail(models.Model):
    url = models.SlugField(max_length=200, unique=True)
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Users(models.Model):

