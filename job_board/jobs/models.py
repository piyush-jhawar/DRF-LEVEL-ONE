from django.db import models

# Create your models here.


class JobOffer(models.Model):
    company_name = models.CharField(max_length=10)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=10)
    job_description = models.TextField()
    salary = models.PositiveIntegerField()
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
