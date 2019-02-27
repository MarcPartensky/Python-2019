import json

a=dict()
a["chat"]=True
a["chien"]=False
a["combien"]=2

b=json.dumps(a)
print(a)
print(b)

c=json.loads(b)

print(c)


print(json.dumps(c,indent=2))

with open("test.json","w") as file:
    json.dump(b,file)


with open("test.json","r") as file:
    d=json.load(file)

print(d)

e=json.loads(d)

print(e)
