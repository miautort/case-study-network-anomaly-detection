# ## Network Anomaly Detection

import numpy as np # numpy is THE toolbox for scientific computing with python
import pandas as pd # pandas provides THE data structure and data analysis tools for data scientists 

# To plot pretty figures
#  %matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)  #ma-ta 

# seaborn plotting 
import seaborn as sns



# Settings
pd.set_option('display.max_columns', None)
sns.set_theme(style="darkgrid")
print("it read ddata?")
data = pd.read_csv("C:/Users/Anto/Documents/case-study-network-anomaly-detection/Train-datas.csv")

print("it should display the rows")

print(data.head())


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


df = pd.DataFrame(data,columns=columns_names)
df.sample(4)


df.head(4)


df.shape

df['attack'].loc[df['attack']!='normal']='attack'

# Normal Connections vs Intrusion Detections: the frequency of normal connections is compared to the frequency of detected intrusions.


df.attack.value_counts()

# ## Data Understanding

from ydata_profiling import ProfileReport

profile = ProfileReport(df, title="Pandas Profiling Report")
profile


