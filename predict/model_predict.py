import asyncio
import time
from predict import models

def predict_data(job_id):
    # Run model here
    # open excel file

    # convert to pandas dataframe
    
    models.RunningJobs.objects.filter(datafile_id=job_id).delete()
    return 0