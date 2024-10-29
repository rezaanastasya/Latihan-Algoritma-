foo = ["Belajar", "Python", "di", "Duniasasha"]
bar = [100, 200, 300, 400]
baz = ["Python", 200, 6.99, True]
  
print(foo)
print(bar)
print(baz) 
foo = ["Python", 200, 6.99, True, 'Duniasasha', 99j]
  
print(foo[0])
print(foo[1])
print(foo[2])
print(foo[3])
print(foo[4])
print(foo[5])
foo = ["Python", 200, 6.99, True, 'Duniasasha', 99j]
print(foo)
  
foo[0] = 'Belajar'
foo[3] = False
print(foo)
foo = ["Python", 200, 6.99, True, 'Duniasasha', 99j]
print(foo[2:5])
print(foo[:3])
print(foo[3:])
print(foo[:])