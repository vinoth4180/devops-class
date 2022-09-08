import cx_Oracle
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dsn_tns=cx_Oracle.makedsn('LAPTOP-NOIBARN8','1521', service_name='XE')
conn=cx_Oracle.connect(user=r'hr',password=r'hr',dsn=dsn_tns)

sql='select * from countries'
query = pd.read_sql_query(sql, conn)
df = pd.DataFrame(query)
print(df.to_string())
print('-----------------------')
df.plot(x = 'COUNTRY_NAME', y = 'REGION_ID',kind='scatter')
plt.show()
