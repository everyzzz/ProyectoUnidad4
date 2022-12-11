from django.db import models

class FormData(models.Model):
    url_photo = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    url_github = models.CharField(max_length=100)

    class Meta:
        db_table = "formulario_proyecto"

class ip(models.Model):
    ip = models.CharField(max_length=20)
    last_connection = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "ip_table"