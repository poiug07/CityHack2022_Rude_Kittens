from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class DataFile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.CharField(max_length=300, default="Some default description of the project")
    name = models.CharField(max_length=200)
    filepath = models.FileField(upload_to='files/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.filepath)

class DataPrediction(models.Model):
    datafile_id = models.ForeignKey(DataFile, on_delete=models.CASCADE)
    predictionsJSON = models.TextField()

class RunningJobs(models.Model):
    datafile = models.OneToOneField(
        DataFile,
        on_delete=models.CASCADE,
        primary_key=True,
    )

class AccessRequest(models.Model):
    companyName = models.CharField(max_length=300)
    representativeName = models.CharField(max_length=300)
    email = models.EmailField(max_length=300) 