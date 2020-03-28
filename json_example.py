import json


class Person:
    def __init__(self, first_name, surname, age):
        self._first_name = first_name
        self._surname = surname
        self._age = age



person = {
    'first_name': "Math",
    'surname': 'Daemon',
    'age': 30,
    'interests': ('football', 'math')

}
with open('my.json', 'w') as file:
    json.dump(person, file)  # to file

print(person)
person_serialized = json.dumps(person, indent=4)
print(person_serialized)
person_des = json.loads(person_serialized)
print(person_des)
