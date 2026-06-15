from django.db import models


class CompanyInfo(models.Model):
    name = models.CharField(max_length=200, default='Trip Manager')
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    logo = models.ImageField(upload_to='company/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Company Info'

    def __str__(self):
        return self.name
