import dataset
from pandas.io.sql import read_sql
from pandas.io.sql import to_sql
import statsmodels.api as sm


db = dataset.connect('sqlite:///:memory:')
table = db['books']
table.insert(dict(title="NumPy Beginner's Guide", author='Ivan Idris'))
table.insert(dict(title="NumPy Cookbook", author='Ivan Idris'))
table.insert(dict(title="Learning NumPy", author='Ivan Idris'))
print(read_sql('SELECT * FROM books', db.executable.raw_connection()))  #运行出错

data_loader = sm.datasets.sunspots.load_pandas()
df = data_loader.data
to_sql(df, "sunspots", db.executable.raw_connection())
table = db['sunspots']

for row in table.find(_limit=5):
    print(5)


print("Tables", db.tables)