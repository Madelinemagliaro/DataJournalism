import json

f1 = open("data/Neighborhood_poverty.csv", "r")
lines = f1.readlines() ##list of each line is csv(strings) 
data_dict = {}

# Iterate through each line in the CSV file
lines_list=[]
for individual in lines: ##each individual peice of data in each string 
    new=individual.split(',') #sepparating each by comma
    lines_list.append(new)## adding to the list 

for individual_line in lines_list:
    if individual_line[7] not in data_dict:
        data_dict[individual_line[7]]={}
    if individual_line[4] not in data_dict[individual_line[7]]:
      data_dict[individual_line[7]][individual_line[4]]={}

    poverty_val=individual_line[5].strip()
    data_dict[individual_line[7]][individual_line[4]]["value"]=poverty_val
    percent_val=individual_line[6].strip()
    data_dict[individual_line[7]][individual_line[4]]["percent"]=percent_val

f1.close()

# Save the json object to a file
with open("Neighberhood_poverty.json", "w") as f2:
    json.dump(data_dict, f2, indent=4)