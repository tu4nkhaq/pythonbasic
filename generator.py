import time
import random
lisst=range(100)

def s(lisst):
    for x in lisst:
        yield x*x 
print(list(s(lisst)))

def a(lisst):
    for x in lisst:
        yield x*x 
gene=a(lisst)
print(next(gene))
print(next(gene))
print(next(gene))
print(next(gene))
print(next(gene))
print(next(gene))
branchs = ['BMW', 'VinFast', 'Toyota', 'Mez', 'Lexus', 'Lambogini']
engines=['2.0', '1.6', '3.0', 'V6', 'V8'] 
def car_generator (num_people):
    for i in range(num_people):
         car={
                    'id': i,
                    'name': random.choice(branchs),
                    'engine': random.choice(engines)
                  }
         yield car
if __name__== "__main__":
    t1=time.time()
    people=car_generator(1000000)
    t2=time.time()
    