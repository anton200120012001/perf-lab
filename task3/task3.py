import json
import sys

def fill_values(tests, values):
    for test in tests:
        if 'id' in test:
            test['value'] = values.get(test['id'], None)
        
        if 'values' in test:
            fill_values(test['values'], values)

if len(sys.argv) != 4:
        print("ERROR. How to run: python task3.py PATH_TO_VALUES PATH_TO_TESTS PATH_TO_REPORT")
        sys.exit(1)

with open(sys.argv[1], 'r') as file:
    values_data = json.load(file)
values = {item['id']: item['value'] for item in values_data['values']}

with open(sys.argv[2], 'r') as file:
    tests = json.load(file)

fill_values(tests['tests'], values)

with open(sys.argv[3], 'w') as file:
    json.dump(tests, file, indent=4)
print('Task3 successfully completed!')