from django.db import models

# Create your models here.


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.URLField()
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return f"{self.id}, {self.name}, {self.price}, {self.image}, {self.image}," \
               f" {self.release_date}, {self.lte_exists}, {self.slug}"
