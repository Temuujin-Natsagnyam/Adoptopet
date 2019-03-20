import csv
import re

with open('static/test.csv','r') as csvinput:
    with open('static/test_out.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)

        for row in reader:
            if row[2] =="Cat":
                new_col = '0'
                if re.search("^Black", row[5]):
                    new_col += '0'
                elif re.search("^White", row[5]):
                    new_col += '1'
                elif re.search("^Brown", row[5]):
                    new_col += '2'
                else:
                    new_col = 'x'
        
            elif row[2] == "Dog":
                new_col = '1'
                if re.search("^Black", row[5]):
                    new_col += '0'
                elif re.search("^White", row[5]):
                    new_col += '1'
                elif re.search("Blue", row[5]):
                    new_col += '2'
                elif re.search("^Brown", row[5]):
                    new_col += '3'
                elif re.search("^Chocolate", row[5]):
                    new_col += '4'
                elif re.search("Yellow", row[5]):
                    new_col += '5'
                else:
                    new_col = 'x'
            
            elif row[2] == "Bird":
                new_col = '2'
                if re.search("White", row[5]):
                    new_col += '0'
                elif re.search("Red", row[5]):
                    new_col += '1'
                else:
                    new_col = 'x' 

            elif row[2] == "Rabbit":
                new_col = '30'  
            
            else: new_col = 'x'

            row.append(new_col)
            row.append('0')
            all.append(row)
        writer.writerows(all)

        # 00 Cat Black 
        # 01 Cat White
        # 02 Cat Brown 
        #  
        # 10 Dog Black 
        # 11 Dog White 
        # 12 Dog Blue 
        # 13 Dog Brown 
        # 14 Dog Chocolate
        # 15 Dog yellow 
        
        # 20 Bird White
        # 21 Bird Red 

        # 30 Rabbit       
