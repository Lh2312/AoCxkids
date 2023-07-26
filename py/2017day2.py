filename=open("C:\\...\\2017day2.txt", "r") 
spreadsheet = filename.read().splitlines()
spreadsheet = [row.split("\t") for row in spreadsheet]
spreadsheet = [list(map(int, row)) for row in spreadsheet]

# part 1
checksum = 0

for row in spreadsheet:
    checksum += max(row) - min(row)
    
print("Checksum:", checksum)# part 2 
checksum = 0

for row in spreadsheet:
    for i in row:
        for j in row:
            if i%j == 0 and i!=j:
                checksum += i / j
                
print("Checksum:", checksum)
