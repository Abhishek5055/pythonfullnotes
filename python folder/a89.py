# import requests 
# from bs4 import BeautifulSoup
# url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
# r = requests.get(url)
# # print(r.text)


# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
# for heading in soup.find_all("h2"):
#   print(heading.text)
# # url = "https://jsonplaceholder.typicode.com/posts"

# # data = {
# #     "title": 'harry',
# #     "body": 'bhai',
# #     "userId": 12,
# #   }
# # headers =  {
# #     'Content-type': 'application/json; charset=UTF-8',
# #   }
# # response = requests.post(url, headers=headers, json=data)

# # print(response.text)

#91 lecture
#Generators
def my_generator():
    for i in range(5):
        yield i
gen = my_generator()

print(next(gen))
print(next(gen))


#Example 2
def my_generator():
    for i in range(5):
        yield i
gen = my_generator()

for j in gen:
    print(j)
    
#Example 3
def my_generator():
    for i in range(5):
        i=i*i
        yield i
gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))

#92 lecture
#Function Caching
from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("Done for 20")
print(fx(30))
print("Done for 30")
print(fx(40))
print("Done for 40")

print(fx(20))
print("Done for 20")
print(fx(30))
print("Done for 30")
print(fx(40))
print("Done for 40")

print(fx(60))
print("Done for 60")


#Example 2
def fib(n):
    if n<2:
        return n
    return fib(n-1)+fib(n-2)
print(fib(10))
