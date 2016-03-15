import psycopg2

try:
    conn = psycopg2.connect("dbname='metri_lokal' user='metri' host='localhost' password='<BrtrZg8'")
except:
    print "I am unable to connect to the database"
