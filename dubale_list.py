a=[2,4,6,8,]
p={}
for i in range(len(a)):
    p.update({a[i]:a[i]})
print(p)