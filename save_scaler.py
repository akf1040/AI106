import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

df = pd.read_csv('star_classification.csv')
columns_to_drop= ['obj_ID', 'run_ID', 'rerun_ID', 'cam_col', 'field_ID', 'spec_obj_ID', 'plate', 'MJD', 'fiber_ID', 'class']
df = df.drop(columns=columns_to_drop)
scaler = MinMaxScaler()
scaler.fit(df.values)
joblib.dump(scaler, 'scaler.pkl')
print('Scaler kaydedildi: scaler.pkl') 