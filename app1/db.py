from django.db import models
from django.utils import timezone
from django.urls import  reverse
# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category_detail',args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    author = models.ForeignKey('Author',related_name='authors',on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    image2 = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    image3 = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    publisher = models.CharField(max_length=100, db_index=True)
    release_date = models.DateTimeField(null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail',args=[str(self.slug)])


class Author(models.Model):
    first_name = models.CharField(max_length=200, db_index=True)
    last_name = models.CharField(max_length=200, db_index=True)
    created = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('-first_name',)
        index_together = (('id'),)
    
    def __str__(self):
        return self.first_name + " " + self.last_name 