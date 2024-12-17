from django.db import models

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    api_token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "companies" 



class Document(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    class Meta:
        db_table = "documents"

class Signer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    document = models.ForeignKey('Document', on_delete=models.CASCADE)

    class Meta:
        db_table = "signers"

