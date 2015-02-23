# How many songs were released in 1981?
import csv

f = open( 'rock.csv' )
reader  = csv.DictReader( f ) 
cols    = [row for row in reader] 

released_1981 = 0
for row in cols:
    if row['Release Year'] == '1981':
        released_1981 += 1

# WHY DOES THIS NEED 2 spaces or it will throw an error?
print released_1981
# 61 songs checked by  
#f = open("rock.csv")
#for row in csv.reader(f):
 #   if row[2] == "1981":
  #      print(row[2])


