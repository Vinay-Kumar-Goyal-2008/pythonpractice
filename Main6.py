import json
data={
    'name':'John',
    'age':30,
    'city':'New York',
    'hobbies':['reading','painting'],
    'address':{
        'street':'123 Main St',
        'city':'New York',
        'state':'NY',
        'country':'USA'}
}
with open('file.json','r') as f:
    data1 = json.load(f)
with open('file.json','w') as f:
    json.dump(data1+[data],f)