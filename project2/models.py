from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    


# one to many
class ProjectReview(models.Model):
    project = models.ForeignKey(ProjectDetail, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review by {self.user.username} for {self.project.title} - Rating: {self.rating}"
    
# many to many
class ProjectShop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=50)

    project = models.ManyToManyField(ProjectDetail, related_name='shops')
    

    def __str__(self):
        return self.name
    
# one to one
class ProjectCertificate(models.Model):
    project = models.OneToOneField(ProjectDetail, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateField(default=timezone.now)
    valid_until = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Certificate for {self.project.title}: {self.certificate_name}"