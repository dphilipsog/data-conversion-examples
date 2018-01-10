#Read superheros.json
import json
from pprint import pprint

with open('superhero.json') as f:
    data = json.load(f)
#Create list of powers 
powers = []
#Loop over members
members = data['members']
for member in members:
#For each member, loop over powers
	member_powers = member['powers']
	for power in member_powers:
		#Add to our list of powers
		powers.append(power)
#Get unique list of powers
unique_powers = list(set(powers))
#Print unique members
pprint(unique_powers)