import pandas as pd
import io

data=""
with open("goog_flutends.csv",'r') as rf:
    data = rf.read().replace("\"","")

df=pd.read_csv(io.StringIO(data), index_col=0)
print(df)
