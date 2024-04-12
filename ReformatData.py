import json

f1 = open("data/Neighborhood_poverty.csv", "r")
lines = f1.readlines()
data_dict = {}

# Iterate through each line in the CSV file
lines_list=[]
for individual in lines:
    new=individual.split(',') #sepparating each my comma
    lines_list.append(new)

for individual_line in lines_list:
    if individual_line[4] not in data_dict:
        data_dict[individual_line[4]]={}
    poverty_val=individual_line[5].strip()
    data_dict[individual_line[4]]["value"]=poverty_val
    percent_val=individual_line[6].strip()
    data_dict[individual_line[4]]["percent"]=percent_val

f1.close()

# Save the json object to a file
with open("Neighberhood_poverty.json", "w") as f2:
    json.dump(data_dict, f2, indent=4)