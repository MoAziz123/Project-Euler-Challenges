list = [1, 2]
sum = 0
found = False
i=0
while not found:
    if list[len(list)-1] >= 4000000:
        found = True
    if list[i] % 2 == 0:
        sum+=list[i] 
    list.append(list[i] + list[i+1])
    i += 1

print(sum)
print(list)