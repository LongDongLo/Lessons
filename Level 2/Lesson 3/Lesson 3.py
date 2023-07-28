'''
Dictionaries have no order
They are the last data type
In lists index is used to access values
In dictionaries keys are used to access them
Dictionaries are made with {}
Key first : Value ,
Keys and indexes are accessed with ["Pee"]
Use print dict.keys to return all keys
Use print dict.values to return all values
Use x = dict.copy to get a copy
Use dict.clear to clear
To add a pair use dict[key] = value
Dict.update is used to add if keys not present and to change if keys are present
Use like dict.update({key : value})
Make conditional dicts with newDict = {k:v for (k,v) in dict.items() if v % 2 = 0 if v > 3}
'''

original_dict = {"jack":38, "Michael":48, "Guido":57, "John":33}

new_dict = {k:v for (k,v) in original_dict.items() if v < 50}

print(new_dict)

new_dict2 = {k:v for (k,v) in original_dict.items() if len(k) > 4}

print(new_dict2)
