import asyncio
import time
from predict import models
from openpyxl import load_workbook
import pandas as pd

def predict_data(job_id):    
    # open excel file
    d = models.DataFile.objects.get(id=job_id)
    wb = load_workbook(d.filepath)
    # convert to pandas dataframe
    ws = wb.worksheets[0]
    data = ws.values
    columns = next(data)[0:]
    df = pd.DataFrame(data, columns=columns)
    print(df)

    models.RunningJobs.objects.filter(datafile_id=job_id).delete()
    return 0