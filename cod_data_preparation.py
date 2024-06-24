import numpy as np # numpy is THE toolbox for scientific computing with python
import pandas as pd # pandas provides THE data structure and data analysis tools for data scientists 

import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

import seaborn as sns

# Settings
pd.set_option('display.max_columns', None)
sns.set_theme(style="darkgrid")

from sklearn.preprocessing import LabelEncoder, StandardScaler

from pycaret.classification import setup, compare_models

data = pd.read_csv("Train-datas.csv")

columns_names = ["duration","protocol_type","service","flag","src_bytes","dst_bytes","land",
"wrong_fragment","urgent","hot","num_failed_logins","logged_in",
"num_compromised","root_shell","su_attempted","num_root","num_file_creations",
"num_shells","num_access_files","num_outbound_cmds","is_host_login",
"is_guest_login","count","srv_count","serror_rate", "srv_serror_rate",
"rerror_rate","srv_rerror_rate","same_srv_rate", "diff_srv_rate", "srv_diff_host_rate","dst_host_count","dst_host_srv_count","dst_host_same_srv_rate",
"dst_host_diff_srv_rate","dst_host_same_src_port_rate",
"dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate",
"dst_host_rerror_rate","dst_host_srv_rerror_rate","attack", "last_flag"]

data = np.array(data)
#columns datas
df = pd.DataFrame(data,columns=columns_names)

df.drop(['land','urgent','num_failed_logins','num_outbound_cmds'],axis=1,inplace=True)

df['attack'].loc[df['attack']!='normal']='attack'

le=LabelEncoder()

df['protocol_type']=le.fit_transform(df['protocol_type'])
df['service']=le.fit_transform(df['service'])
df['flag']=le.fit_transform(df['flag'])
df['attack']=le.fit_transform(df['attack'])

from pycaret.classification import *
print("Setting up PyCaret...")
s= setup(df, target = 'attack', session_id = 42, data_split_stratify=True)
print("Comparing models...")
best_model = compare_models(sort = 'AUC')


print("Creating plot for src_bytes vs dst_bytes...")
plt.figure(figsize=(10, 6))
plt.scatter(data['src_bytes'], data['dst_bytes'], alpha=0.5)
plt.xlabel('Source Bytes')
plt.ylabel('Destination Bytes')
plt.title('Source Bytes vs. Destination Bytes')
plt.show()
