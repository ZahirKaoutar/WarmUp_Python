
litst=[("a",1),("c",1)]
def tuple_to_dict(l):
    d={}
    for i in range(len(l)):
        
            d[l[i][0]]=l[i][1]
print(tuple_to_dict(litst))


