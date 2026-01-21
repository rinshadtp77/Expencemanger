def write_expences(data):
    fp=open("expences_data","w")
    for item in data:
        fp.write(item[0]+"-"+item[1]+"-"+item[2]+"-"+item[3]+"\n")
def read_expences():
    expences = []
    
    fp = open("expences_data", "r")
    for line in fp:
        line = line.strip()          # remove newline
        parts = line.split("-")      # split by '-'
        expences.append(tuple(parts))
    fp.close()
    
    return expences
