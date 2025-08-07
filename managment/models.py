from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):
    usuario = models.OneToOneField(
        User, on_delete=models.PROTECT, verbose_name="usuário")
    name = models.CharField(max_length=100, verbose_name="nome")
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Admin"
        ordering = ["name"]

class Client(models.Model):
    usuario = models.OneToOneField(
        User, on_delete=models.PROTECT, verbose_name="usuário")
    name = models.CharField(max_length=255, verbose_name="nome")
    phone = models.CharField(max_length=15, verbose_name="telefone")
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Cliente"
        ordering = ["name"]

class Clothing(models.Model):
    name = models.CharField(max_length=255, verbose_name="nome")
    description = models.CharField(max_length=150, verbose_name="descrição", null=True, blank=True)
    size = models.CharField(max_length=10, verbose_name="tamanho")
    color = models.CharField(max_length=20, verbose_name="cor")
    value = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="valor")
    
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="categoria")
    admin = models.ForeignKey('Admin', on_delete=models.PROTECT, verbose_name="autor")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Roupas"
        ordering = ["category", "name"]

class ClothingImages(models.Model):
    clothing = models.ForeignKey('Clothing', on_delete=models.CASCADE, related_name='images', null=True, blank=True, verbose_name="roupa")
    # image = models.ImageField( upload_to='media', verbose_name="imagem", blank=True, null=True)
    image_url = models.URLField(null=False, blank=False, default="https://cdn3.iconfinder.com/data/icons/fashion-16/1000/fashion_dress-1024.png")
    def __str__(self):
            return self.image_url
    class Meta:
        verbose_name = "Imagens"
        ordering = ["image_url"]

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="nome")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Categoria"
        ordering = ["name"]