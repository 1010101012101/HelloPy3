import numpy as np
import pandas as pd
from tempfile import NamedTemporaryFile
from os.path import getsize

np.random.seed(42)
a = np.random.randn(365, 4)

tmpf = NamedTemporaryFile()
np.savetxt(tmpf, a, delimiter=",")
print("HHHA:0===>name=", tmpf.name)
print("Size CSV file", getsize(tmpf.name))

tmpf = NamedTemporaryFile()
np.save(tmpf, a)
tmpf.seek(0)
loaded = np.load(tmpf)
print("HHHA:1===>name=", tmpf.name)
print("Size .npy  file", getsize(tmpf.name))

df = pd.DataFrame(a)
tmpf = NamedTemporaryFile()
this_name = "./aaa"
print("HHHA:2===>name=", tmpf.name)
df.to_pickle(this_name)
print("Size pickled dataframe", getsize(this_name))
print("DF from pickled\n", pd.read_pickle(this_name))