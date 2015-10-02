import psycopg2
import pandas as pd
import csv

df = pd.read_csv('/Users/qiaoli/Downloads/start_date.csv')
saved_column = df['client_id']

conn_string = "host='db.urban4m.com' dbname='dev' user='geo' password='geo'"
print "Connecting to database\n ->%s" % (conn_string)
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
list=[]
for i in range(0,len(saved_column)):
    cursor.execute("select unique_client_identifier::integer, \
                sum(regexp_replace(price,'[^0-9]*','')::double precision) \
                from qiao.ml_client_analysis\
                where unique_client_identifier::integer="+str(saved_column[i])
               +" and regexp_replace(price,'[^0-9]*','')<>'' \
                group by unique_client_identifier")
    records = cursor.fetchall()
    print records
    list.append(records)
with open('/Users/qiaoli/Downloads/transaction.csv','wb') as fp:
    csv_writer = csv.writer(fp)
    csv_writer.writerows(list)

print "done"
    
