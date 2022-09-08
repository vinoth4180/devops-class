import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

conn = sqlite3.connect('chinook.db')
sql='select * from company'
query = pd.read_sql_query(sql, conn)
df = pd.DataFrame(query)
print(df)
print('-----------------------')
df.plot(x = 'ADDRESS', y = 'SALARY')
plt.show()
print('-----------------------')
df.plot(x = 'ADDRESS', y = 'SALARY', kind = 'bar')
plt.show()
print('-----------------------')
group_address = df.groupby('ADDRESS')['SALARY'].count()
print(group_address)
group_address.plot(kind = 'bar')
plt.show()
print('-----------------------5')
conn = sqlite3.connect('chinook.db')
sql='select * from datatable'
query = pd.read_sql_query(sql, conn)
df = pd.DataFrame(query)
print(df)
group_name = df.groupby('Name')[['age','salary']].sum()
group_name.plot(kind = 'bar')
plt.show()
group_name = df.groupby('Name')[['age', 'salary']].sum()
group_name.plot.bar(subplots = True)
plt.show()
group_name = df.groupby('Name')[['age', 'salary']].sum()
group_name.plot.bar(title = 'Bar Plot', grid = True, fontsize = 7, position = 1)
plt.show()
group_name = df.groupby('Name')['salary'].sum()
group_name.plot.barh(x = 'Name', y = 'salary' )
plt.show()
group_name = df.groupby('Name')[['age','salary']].sum()
group_name.plot.barh(title = ['Age Graph','Salary Graph'], subplots = True, legend = False)
plt.show()
group_age = df.groupby('age')['salary'].sum()
group_age.plot(x = 'age', y = 'salary', kind = 'area' )
plt.show()
groupby_name = df.groupby('Name')[['age','salary']].sum()
groupby_name.plot.area(title = 'name vs age vs salary', legend = True, color = ['r', 'b'])
plt.show()

print('-----------------------')
# creating a dataframe
df = pd.DataFrame([('Bike', 'Kawasaki', 186),
                   ('Bike', 'Ducati Panigale', 202),
                   ('Car', 'Bugatti Chiron', 304),
                   ('Car', 'Jaguar XJ220', 210),
                   ('Bike', 'Lightning LS-218', 218),
                   ('Car', 'Hennessey Venom GT', 270),
                   ('Bike', 'BMW S1000RR', 188)],
                  columns=('Type', 'Name', 'top_speed(mph)'))

print(df)
result = df.groupby('Type').agg({'top_speed(mph)': ['mean', 'min', 'max']})

print("Mean, min, and max values of Top Speed grouped by Vehicle Type")
print(result)

# creating a dataframe
sales_data = pd.DataFrame({
    'customer_id': [3005, 3001, 3002, 3009, 3005, 3007,
                    3002, 3004, 3009, 3008, 3003, 3002],

    'salesman_id': [102, 105, 101, 103, 102, 101, 101,
                    106, 103, 102, 107, 101],

    'purchase_amt': [1500, 2700, 1525, 1100, 948, 2400,
                     5700, 2000, 1280, 2500, 750, 5050]})

print(sales_data)
result = sales_data.groupby('salesman_id').agg({'purchase_amt': ['mean', 'min', 'max']})

print("Mean, min, and max values of Purchase Amount grouped by Salesman id")
print(result)

df = pd.DataFrame({"Team": ["Radisson", "Radisson", "Gladiators",
                            "Blues", "Gladiators", "Blues",
                            "Gladiators", "Gladiators", "Blues",
                            "Blues", "Radisson", "Radisson"],

                   "Position": ["Player", "Extras", "Player", "Extras",
                                "Extras", "Player", "Player", "Player",
                                "Extras", "Player", "Player", "Extras"],

                   "Age": [22, 24, 21, 29, 32, 20, 21, 23, 30, 26, 20, 31]})


print(df)
result = df.groupby('Team').agg({'Age': ['mean', 'min', 'max']})

print("Mean, min, and max values of Age grouped by Team")
print(result)
# data of 2018 drivers world championship
dict1 = {'Driver': ['Hamilton', 'Vettel', 'Raikkonen',
                    'Verstappen', 'Bottas', 'Ricciardo',
                    'Hulkenberg', 'Perez', 'Magnussen',
                    'Sainz', 'Alonso', 'Ocon', 'Leclerc',
                    'Grosjean', 'Gasly', 'Vandoorne',
                    'Ericsson', 'Stroll', 'Hartley', 'Sirotkin'],

         'Points': [408, 320, 251, 249, 247, 170, 69, 62, 56,
                    53, 50, 49, 39, 37, 29, 12, 9, 6, 4, 1],

         'Age': [33, 31, 39, 21, 29, 29, 31, 28, 26, 24, 37,
                 22, 21, 32, 22, 26, 28, 20, 29, 23]}

# creating dataframe using DataFrame constructor
df = pd.DataFrame(dict1)
print(df)
# the result shows max on
# Driver, Points, Age columns.
print(df.max())
# Who scored more points ?
print(df[df.Points == df.Points.max()])
# what is the maximum age ?
print(df.Age.max())
# Which row has maximum age |
# who is the oldest driver ?
print(df[df.Age == df.Age.max()])


table = np.random.randn(50, 5)
print(table)
data = pd.DataFrame(table, columns = ['A', 'B', 'C', 'D', 'E'])
print(data)
data.plot(kind = 'bar')
plt.show()