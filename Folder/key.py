BCA={"1":"Chinchana" ,
     "2":"Deeksha" ,
     "3":"Sumedha"}
     
#adding new element
BCA["4"]="Preethi"
print(BCA.values())
print(BCA.keys())
print(BCA.items())


#for key, values in BCA.items():
 
#print(key,values)

if "1" in BCA:
    print("Yes,'1' is a key in BCA dictionary")
