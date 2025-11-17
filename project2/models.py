from django.db import models
from django.utils import timezone

# Create your models here.
class ProjectDetail(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='project_images/')
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True)
    project_type = [("df","default"),("cf","custom")]
    type = models.CharField(max_length=2, choices=project_type)
    cost = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)

    def __str__(self):
        return self.title