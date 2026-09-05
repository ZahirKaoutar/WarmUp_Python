#challenge1:
First_dict = { "Appareil": "Laptop", "Marque": "IBM", "Carte mère": "MSI Z490", "Carte Graphique":"GeForce RTX 3070", "RAM": "16G", "Processeur": "Intel core i7-G11", "SSD": "1 To" }    
if First_dict["RAM"]=="16G":
    First_dict["RAM"]="16G"
print(First_dict)


for cle,val in First_dict.items():
    print(cle,val)
print(First_dict.keys())
print(First_dict.values())
First_dict["Carte Graphique"],First_dict["Processeur"]=First_dict["GeForce RTX 3070"],First_dict["Intel core i7-G11"]
for cle,val in First_dict.items():
    print(cle,val)
notes_eleves = { "Amine": 15.5, "Yassine": 19.0, "Reda": 14.2, "Malak": 8.7, "Manal": 20.0, "Ahmed": 7.5,"Saad": 11.3, "Hannae": 9.8 }
etudiantAdmis={}
etudiantNAdmis={}
for cle in notes_eleves:
    if notes_eleves[cle]>=10:
        etudiantAdmis.add(notes_eleves[cle]) 
    else:
        etudiantAdmis.add(notes_eleves[cle])
print(etudiantAdmis.values)
print(etudiantNAdmis.values)
#challenge2:
notes_eleves1 = { "Amine": 15.5, "Yassine": 19.0, "Reda": 14.2, "Malak": 8.7, "Manal": 20.0, "Ahmed": 7.5,"Saad": 11.3, "Hannae": 9.8 }
notes_eleves2 = { "salma": 15.5, "ali": 19.0, "mariem": 14.2, "pmp": 8.7, "M": 20.0, "Aed": 7.5,"Sa": 11.3, "Ha": 9.8 }
notes_eleves1.update(notes_eleves2)
for cle,val in notes_eleves1.items():
    print(cle,val)


#challenge4:
notesTRie=dict(sorted(notes_eleves1,key=lambda x:x[0]))
for cle,val in notes_eleves1.items():
    print(cle,val)
#challenge3:
l2=['a','b','c']
l1=[1,2,3]
l3=dict(zip(l2,l1))
for cle,val in notes_eleves1.items():
    print(cle,val)







#challenge5:
c=("Yasmine", 22,"Informatique",17.4)
l=("prenom","age","branche","note")
for  i in range(len(l)):
        print(l[i],":",c[i])
print(c[0:2])
c=("Yasmine", 22,"Informatique",17.4)
c1=("2024","T.Bien")
c3=c1+c
print(c3)


#challenge1av:

d1 = {'a': 1, 'b': 2}
d2 = {'a': 3, 'c': 4}
def  fusionner_dictionnaires(d1,d2,fadd):
    d3={}
    for cle,val in d1.items():
        if cle in d2:
            d3[cle]=fadd(val,d2[cle])

        else:
            d3[cle]=val
    for cle,val in d2.items():
        d3.setdefault(cle,val)
    return d3
            

addition = lambda x, y: x + y

resultat1 = fusionner_dictionnaires(d1, d2, addition)

print(resultat1)

#challenge 2:
def filtrer_dictionnaire(fc,d):
    d1={}
    # for cle,val in d.items:
    #     if fc(val):
    #         d1[cle]=val
    d1=dict(filter(fc,d.items()))
    return d1
d={'a': 5, 'b': 12, 'c': 8, 'd': 15}
fs=lambda x:x[1]>10 and x[1]%2==0
print(filtrer_dictionnaire(fs,d)) 

def filtrer_dictionnaire(fc,d):
    d1={}
    for cle,val in d.items():
        if fc(val):
            d1[cle]=val
    return d1
d={'a': 5, 'b': 12, 'c': 8, 'd': 15}
fs=lambda x:x>10 and x%2==0
print(filtrer_dictionnaire(fs,d))

#challenge3:
d3={'a': 10, 'b': 5, 'c': 15}
def dictionnaire_vers_tuples(d2,t1):
  
    t=()
    t=sorted(d2.items(),key=t1)
    return t
t1=lambda x:x[1]

print(dictionnaire_vers_tuples(d3,t1))
#challenge 4:
t4=[('a', 1), ('b', 2), ('a', 3), ('c', 4)] 
def regrouper_tuples(t4):
    d1={}
    for i in range(len(t4)):
        cle=t4[i][0]
        val=t4[i][1]
        if cle in d1:
            d1[cle].append(val)
        else:
            d1[cle] = [val]


    return d1
#challenge 5:
def transformer_tuples(L):
    p=list(map(lambda x:tuple(map(lambda y:y*2,x)),L))
    return p
a=[(2, 4), (6, 8)]
print(transformer_tuples(a))
#challenge6:

def aplatir_dictionnaire(d):
    result = []
    for k,v in d.items():
        if not isinstance(v,dict):
            result.append((k,v))
        else:
            for k2, v2 in v.items():
                result.append((f"{k}.{k2}", v2))

    return result


D = {'a': 1, 'b': {'c': 2, 'd': 3}}

print(aplatir_dictionnaire(D))

    



   