import numpy as np
import pandas as pd
from tempfile import NamedTemporaryFile

np.random.seed(42)
a = np.random.randn(365, 4)

tmpf = NamedTemporaryFile(suffix=".xlsx",dir="./data/temp/",delete=False)
df = pd.DataFrame(a)
print(tmpf.name)
df.to_excel(tmpf.name, sheet_name="Random Data1")
df.to_excel(tmpf.name, sheet_name="Random Data2")
print("Means\n", pd.read_excel(tmpf.name, "Random Data2").mean())
df.to_html("./data/hello.html")
df.to_csv("./data/hello.csv",float_format="%.3f")