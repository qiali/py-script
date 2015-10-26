from scipy import stats
import scipy 
import numpy 
import matplotlib as mpl
from matplotlib import pyplot as plt
import random
import psycopg2
import pandas as pd
import plotly.plotly as py
from plotly.graph_objs import *

data_141x = pd.read_csv('/Users/qiaoli/Downloads/intrvw14/interview14/fmli141x.csv')
data_142 = pd.read_csv('/Users/qiaoli/Downloads/intrvw14/interview14/fmli142.csv')
data_143 = pd.read_csv('/Users/qiaoli/Downloads/intrvw14/interview14/fmli143.csv')
data_144 = pd.read_csv('/Users/qiaoli/Downloads/intrvw14/interview14/fmli144.csv')
data_151 = pd.read_csv('/Users/qiaoli/Downloads/intrvw14/interview14/fmli151.csv')

df_new = pd.concat([data_141x[['NEWID','AS_COMP3']], data_142[['NEWID','AS_COMP3']]
                    , data_143[['NEWID','AS_COMP3']], data_144[['NEWID','AS_COMP3']],
                    data_151[['NEWID','AS_COMP3']]])
df_new.drop_duplicates(subset='NEWID',inplace=True)

cex = []
cex_1 = []
for i in df_new['AS_COMP3']:
    if i == 0:
        cex.append(0)
    else:
        cex.append(1)
        cex_1.append(1)

'''df = pd.DataFrame()
df = df.append(cex)
print df.describe()'''

conn_string = "host='db.urban4m.com' dbname='dev' user='etl' password='etl'"
print "Connecting to database\n ->%s"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

cursor.execute("select b01001_003+b01001_004+b01001_005 from acs5yr_census_2013._e201350002000;")
records = cursor.fetchall()
acs = []
for i in records:
    acs.append(i[0])

'''i = 0
while i<5:
    gradient, intercept, r_value, p_value, std_err = stats.linregress(cex,random.sample(acs,len(cex)))
    print "Gradient and intercept", gradient, intercept
    print "R-squared", r_value**2
    print "p-value", p_value
    i = i + 1
'''                                                                  
break_list = sorted(acs, key=int)[:(len(acs)*len(cex_1)/len(cex))]
print max(break_list)

'''acs_dummy = []
for i in acs:
    if i>max(break_list):
        acs_dummy.append(1)
    else:
        acs_dummy.append(0)

coefficient = []
p_value = []
i = 0
while i<101:
    TT = scipy.stats.mstats.ks_twosamp(random.sample(cex,100),random.sample(acs,100))
    coefficient.append(TT[0])
    p_value.append(TT[1])
    i=i+1
    

trace0 = Scatter(x=range(1,101),
                 y=coefficient)
trace1 = Scatter(x=range(1,101),
                 y=p_value)
data = Data([trace0, trace1])
plot_url = py.plot(data, filename='basic-line')

print sum(coefficient)/float(len(coefficient))
print sum(p_value)/float(len(p_value))'''


