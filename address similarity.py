import psycopg2
import sys
       
str1 = " str1"
str2 = "str2 "
def mismatches(str1, str2):
	s1 = str1.strip().lower()
	s2 = str2.strip().lower()
	mis = 0
	for i in range(min(len(s1), len(s2))):
		if s1[i] != s2[i]:
			mis += 1

	mis += ( max(len(str1), len(str2)) - min(len(str1), len(str2)) )
	return mis

def scoreStreet(st1, st2):
	partition1, partition2 = st1.split(' '), st2.split()
	number1, number2 = partition1[0], partition2[0]
	typest1, typest2 = partition1[-1], partition2[-1]
	name1, name2 = " ".join(partition1[1:len(partition1)-1]), " ".join(partition2[1:len(partition2)-1])
	streetScore = mismatches(number1, number2) + mismatches(typest1, typest2) + mismatches(name1, name2)
	return streetScore 

def scoreCity(st1, st2):
	return mismatches(st1, st2)

def scoreCodes(st1, st2):
	partition1, partition2 = st1.split(' '), st2.split()
	state1, state2 = partition1[0], partition2[0]
	zipcode1, zipcode2 = partition1[1], partition2[1]
	codeScore = mismatches(state1, state2) + mismatches(zipcode1, zipcode2)
	return codeScore


def scoreAddrs(addr1, addr2):
	score = 0
	(street1, state1, codes1) = tuple(addr1.split(','))
	(street2, state2, codes2) = tuple(addr2.split(','))

	score += scoreStreet(street1, street2)
	score += scoreCity(state1, state2)
	score += scoreCodes(codes1, codes2)

	return score

def main():
    conn_string = "host='db.urban4m.com' dbname='dev' user='geo' password='geo'"
    print "Connecting to database\n ->%s" % (conn_string)
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("SELECT regexp_replace(lower(client_address),', (unit|apt)[^,]*,',',') client_address,\
                    lower(housing_address) FROM qiao.superfan_final")
    records = cursor.fetchall()
    for row in records:
        cursor.execute("update qiao.superfan_final set similarity_score="+str(scoreAddrs(row[0],row[1])))
    conn.commit()
        
        
if __name__=="__main__":
    main()
    print "done"
