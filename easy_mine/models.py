
# Create your models here.

from django.db import models


class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=100)
    account_description = models.TextField()

    def __str__(self):
        return self.account_name
    

class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=100)
    status_description = models.TextField()
    account_id = models.ForeignKey(
                                    Account,
                                    on_delete=models.CASCADE,
                                    verbose_name="related account",
                                  )
    
    def __str__(self):
        return self.status_name


class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.type_name


class Project(models.Model):
    project_id = models.AutoField(primary_key=True) 
    project_name = models.CharField(max_length=100)
    project_details = models.TextField()
    account_id = models.ForeignKey(
                                    Account,
                                    on_delete=models.CASCADE,
                                    verbose_name="related account",
                                  )

    def __str__(self):
        return self.project_name


class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True) 
    ticket_title = models.CharField(max_length=100)
    ticket_details = models.TextField()
    project_id = models.ForeignKey(
                                    Project,
                                    on_delete=models.CASCADE,
                                    verbose_name="related project",
                                  )
    status_id = models.ForeignKey(
                                    Status,
                                    on_delete=models.CASCADE,
                                    verbose_name="project status",
                                  ) 
    type_id =  models.ForeignKey(
                                    Type,
                                    on_delete=models.CASCADE,
                                    verbose_name="project type",
                                  )                                                                  

    def __str__(self):
        return self.ticket_title