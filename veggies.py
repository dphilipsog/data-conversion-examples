vegetables = [
 {"name": "eggplant"},
 {"name": "tomato"},
 {"name": "corn"},
 {"name": "squash"},
 {"name": "kale"},
 {"name": "carrot"},
]

import csv

with open('veggies.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'length'])
	for veggie in vegetables:
		#I want the name of the vegetable
		vegetable_name = veggie['name']
		#I want the lenfth of that word
		vegetable_name_length = len(vegetable_name)
		#Write to csv
		row = [vegetable_name, vegetable_name_length]
		writer.writerow(row)