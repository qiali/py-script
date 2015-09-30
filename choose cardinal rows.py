import csv
from itertools import islice

myreader = csv.DictReader(open('/Users/qiaoli/Downloads/allCustNumVisitsRangeLifecycle.csv'))
i=3
list=[]
with open('/Users/qiaoli/Downloads/allCustNumVisitsRangeLifecycle.csv') as inFH:
    csvReader = csv.reader(inFH)

    for row in csvReader:
        
        if csvReader.line_num ==i:
            list.append(row)
         
            
            i=i+2
with open('/Users/qiaoli/Downloads/end_date.csv','wb') as fp:
                csv_writer = csv.writer(fp)
                
                csv_writer.writerows(list)      
            
print "done"
