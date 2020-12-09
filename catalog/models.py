from django.db import models
from django.utils import timezone


class Course(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    currency = models.TextField(max_length=10, default='₴')
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    start_date = models.DateField()
    end_date = models.DateField()
    photo = models.ImageField(upload_to="gallery")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def display_price(self):
        return str(self.price) + ' ' + self.currency



