server1 ={
    "type":"micro",
    "storage":9,
    "active":True
}
server2 ={
    "type":"mediumo",
    "storage":20,
    "active":False
}
print("my name")
list=[server1,server2]
for env in list:
    for key,value in env.items():
       if key=="active" and value =="True":
        print("your server is active")