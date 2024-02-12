family = ['bob', 'lty', 'ked', 'der']
print(family)
print(family[0])
print(f"My second cousin name is {family[0].title()}")
family[0] = "Teddi"
print(family)
family.append("bobby") # add at the end
print(family)
family.append("grey, red, yellow")
print(family)
#insert with sertain index
family.insert(2, "jeremy")
print(family)

del family[0]
print(family)

poped_family = family.pop()
print(family)
print(poped_family)
poped_first_elem = family.pop(0)
print(family)
print(poped_first_elem)

family.remove("ked")
print(family)