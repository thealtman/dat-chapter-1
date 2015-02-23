# What are the top 20 songs by playcount
import csv

csvfile = open( 'rock.csv' )
reader  = csv.DictReader( csvfile ) 
cols    = [row for row in reader] 


sorted_pc = sorted( cols, 
                            key = lambda row: int( row['PlayCount'] ), 
                            )
top_20 = sorted_pc[0:19]
print top_20