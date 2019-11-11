from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    @classmethod
    def delete_location(cls,location):
        cls.objects.filter(location=location).delete()

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    @classmethod
    def get_all_categories(cls):
        categ = cls.objects.all()
        return categ

    @classmethod
    def delete_category(cls,name):
        cls.objects.filter(name=name).delete()


class Image(models.Model):
    title =models.CharField(max_length =60)
    post_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=60,default='DEFAULT VALUE')
    location= models.ForeignKey(Location)
    category= models.ForeignKey(Category)
    image = models.ImageField(upload_to ='images/' ,default='DEFAULT VALUE')

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    @classmethod    
    def all_images(cls):
        images = cls.objects.all()
        return images
 
    @classmethod 
    def search_by_category(cls,search_term):
        images= cls.objects.filter(category__name__icontains=search_term)

        return images