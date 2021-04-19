# challenge = 'thirty days of python'
# print(challenge.index('y',10)) 

# 1-2
a = "Thirty "
b = 'Days '
c = "Of "
d = "Python"
code = a + b + c + d
print(code)
e = "Coding "
f = "For "
g = "All"
letter = e + f + g
print(letter)

# 3-8
company = letter
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company.capitalize().title().swapcase())

# 9-14
cut = company[7:]
print(cut)
print(company.index("Coding"))

letter2 = "Python For Everyone"
print(letter2.replace("Everyone", "All"))

print(company.split(" "))

letter3 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(letter3.split(", "))

# 15-17
test = company[0]
print(test)
test2 = company[-1]
print(test2)
test3 = letter[10]
print(test3)

# 18-19
print ("".join(e[0] for e in letter2.split()))
print ("".join(e[0] for e in company.split()))

# 20-22
print(company.index("C"))
print(company.index("F"))
print(company.rfind("I"))

# 23-27
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.rindex('because'))
print(sentence.replace("because","").replace("   ", ""))
print(sentence.find('because'))

# 28-29
# Does ''Coding For All' start with a substring Coding? 
# Does 'Coding For All' end with a substring coding?

# 30-34
sentence2 = '   Coding For All      '
print(sentence2.strip())

sentence3 = '30DaysOfPython'
sentene4 = 'trihty_days_of_python'
print(sentence3.isidentifier())
print(sentene4.isidentifier())

join1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
res = '# '.join(join1)
print(res)

print("I am enjoying this challenge. \nI just wonder what is next.")

name = "Name\tAge\tCountry \nAsabeneh\t250\tFinland"
print(name.expandtabs(10))

# 35-end
radius = 10
area = 3.14 * radius ** 2
formatletter = "The area of a cricle with radius {} is {} meters square.".format(radius, area)
print(str(formatletter))

a = 8
b = 6
print("{} + {} = {}".format(a, b, a+b))
print("{} - {} = {}".format(a, b, a-b))
print("{} * {} = {}".format(a, b, a*b))
print("{} / {} = {:.2f}".format(a, b, a/b))
print("{} % {} = {}".format(a, b, a%b))
print("{} // {} = {}".format(a, b, a//b))
print("{} ** {} = {}".format(a, b, a**b))