import time
from predict import models
from openpyxl import load_workbook
import numpy as np
import warnings
import pandas as pd
from statsmodels.tsa.api import VAR
from statsmodels.iolib.smpickle import load_pickle
warnings.filterwarnings(action="ignore")

nobs = 1
def test_model(df_diff, pred_diff, model, lag_order=24):
    cont_set = df_diff
    for i in range(0, len(pred_diff)):
        forecast_input = cont_set.values[-lag_order:]
        fc = model.forecast(y=forecast_input, steps=nobs)
        df_forecast = pd.DataFrame(fc, index=df_diff.index[-nobs:], columns=cont_set.columns)
        new_row = np.array(pred_diff)[i]
        new_row = np.append(new_row, list(df_forecast["Y"])[0])
        to_app = pd.DataFrame(new_row.reshape(1, 5),index = [len(df_diff)+i], columns = cont_set.columns)
        cont_set = cont_set.append(to_app)
    return list(cont_set["Y"][-len(pred_diff):])

def inv_diff(seq, init_val):
    seq = list(seq)
    res = [init_val]
    for i in range(len(seq)):
        res.append(seq[i]+res[i])
    return res

def predict_data(job_id):    
    # open excel file
    d = models.DataFile.objects.get(id=job_id)
    wb = load_workbook(d.filepath)
    # convert to pandas dataframe
    ws = wb.worksheets[0]
    data = ws.values
    columns = next(data)[0:]
    df = pd.DataFrame(data, columns=columns)
    
    newprediction = models.DataPrediction(datafile_id=d)
    to_predict = pd.read_excel(d.filepath, sheet_name="dataset", parse_dates=['DateTime'])
    to_predict["minute"] = to_predict["DateTime"].dt.minute
    to_predict = to_predict.loc[to_predict["minute"] == 0]
    to_predict = to_predict.set_index('DateTime')
    to_predict.drop("minute", inplace=True, axis=1)
    lag_points = to_predict[:25]
    to_predict = to_predict[24:]

    to_predict = to_predict.fillna(0)

    lag_diff = lag_points.diff().dropna()
    pred_diff = to_predict.diff().dropna().drop("Y", axis=1)

    model = load_pickle("predict/model/VAR_rmse_78336.pickle")
    res = test_model(lag_diff, pred_diff, model)
    res = inv_diff(res, lag_points["Y"][-1])
    to_predict['Y'] = res

    newprediction.predictionsJSON = to_predict.to_json()

    newprediction.save()

    models.RunningJobs.objects.filter(datafile_id=job_id).delete()
    return 0