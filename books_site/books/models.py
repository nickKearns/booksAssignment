from django.db import models

# Create your models here.




class Author(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField()

    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    num_pages = models.IntegerField(default=0)
    date_published = models.DateField()
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title



