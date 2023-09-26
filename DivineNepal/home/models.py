from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length= 300)
    email = models.EmailField(max_length= 300)
    subject = models.TextField()
    message = models.TextField()


    def __str__(self):
        return self.name


class Information(models.Model):
    address= models.CharField(max_length = 400)
    phone = models.CharField(max_length= 50)
    email = models.EmailField(max_length = 500)

    def __str__(self):
        return self.address
        
        
class About(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    description_1 = models.TextField()
    description_2 = models.TextField()

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=300)
    icon = models.CharField(max_length=50)
    description = models.TextField()

    def str(self):
        return self.title


class Destination(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    description_1 = models.TextField()
    description_2 = models.TextField()

    def __str__(self):
        return self.title


class Team (models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    designation = models.CharField(max_length=300)

    def str(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    address= models.CharField(max_length = 400)
    description = models.TextField()

    def str(self):
        return self.name



class Booking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.CharField(max_length=20)
    destination = models.CharField(max_length=255)
    special_request = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class PackageDetail(models.Model):
    place = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    person = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    detail = models.TextField()
    image = models.ImageField(upload_to='package_images/')

    def __str__(self):
        return self.place

class AboutBooking(models.Model):
    title = models.CharField(max_length=300)
    description_1 = models.TextField()
    description_2 = models.TextField()