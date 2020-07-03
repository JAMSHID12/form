import random
names = ["jamshid", "gopika", "alen", "amal"]
rand = random.choice(names)
print(rand)   
print(random.randint(1001, 9999))
print(random.randrange(100, 9999,8))

upper_char = ["A", "B", "C", "D", "E"]
lower_char = ["a", "b", "c", "d", "e"]
num = ["1", "2", "3", "4", "5"]
special_char = ["@", "#", "$", "&"]

passw = random.choice(upper_char) + random.choice(lower_char) + random.choice(lower_char) + random.choice(lower_char) +  random.choice(special_char) + random.choice(num) + random.choice(num)
print(passw)