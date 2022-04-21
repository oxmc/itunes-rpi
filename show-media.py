import json

input_file = open('media.json').read()
json_array = json.loads(input_file)
json_array = json_array['media']

#print(json_array)

for item in json_array:
    print(item)
    # To get something without keyerror
    print(item.get('key'))
