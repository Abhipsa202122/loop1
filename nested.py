l1 = ['S001', 'S002', 'S003', 'S004']
l2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
l3 = [85, 98, 89, 92]
l5 =[]
l6 = []
for i in range(len(l2)):
    d2 = {}
for j in range(len(l3)):
    if i == j:
       d2.setdefault(l2[i],l3[j])
       l5.append(d2)
       print(l5)
for x in range(len(l1)):
    d3 = {}
    d3.setdefault(l1[x],l5[x])
    l6.append(d3)
    print(l6)

