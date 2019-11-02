from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField('Person\'s Name', max_length=120)
    DOB = models.DateTimeField('Date Of Birth')
    phone = models.CharField('Phone number', max_length=16)

class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    pub_date = models.DateTimeField('date published')
    event_date = models.DateTimeField('Event Date')
    venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    guest_list = []

    def add_guest(self, name):
        guest = models.ForeignKey(Person, on_delete=models.CASCADE)
        self.guest_list.append(guest)

    def __str__(self):
        return self.name

    #def get_by_id(self, _id):
    #    self.objects.get(id= _id)


