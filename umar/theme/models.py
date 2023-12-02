from django.db import models

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    image = models.ImageField(upload_to='img/teacher', null=True, blank=True)

    class_choices = (
        ('Menggambar dan Mewarnai', 'Menggambar dan Mewarnai'),
        ('Melukis', 'Melukis'),
        ('Kaligrafi', 'Kaligrafi'),
    )

    teach = models.CharField(max_length=50, choices=class_choices)

    def __str__(self):
        return self.name


class Testimoni(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=20)
    says = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='img/gallery')
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.caption

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    time = models.DateField(auto_now=True)

    meta = models.CharField(max_length=300)

    image = models.ImageField(upload_to='img/news')
    caption = models.CharField(max_length=50)

    content = models.TextField()

    def __str__(self):
        return self.title
