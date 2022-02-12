import time
a=0
b=0
c=0
d=0

print("What character are you in star wars?")
time.sleep(0.3)
print("What is your weapon of choice?")
time.sleep(0.3)
print("a) Lightsaber")
time.sleep(0.3)
print("b) Blaster")
time.sleep(0.3)
print("c) Amban rifle")
time.sleep(0.3)
print("d) Electornic baton")
answer=input()
if answer=="a":
  a+=1
elif answer=="b":
  b+=1
elif answer=="c":
  c+=1
else:
  d+=1

print("What is your favourite spaceship?")
time.sleep(0.3)
print("a) X-wing")
time.sleep(0.3)
print("b) Millenium falcon")
time.sleep(0.3)
print("c) Razor crest")
time.sleep(0.3)
print("d) Tie fighter")
answer=input()
if answer=="a":
  a+=1
elif answer=="b":
  b+=1
elif answer=="c":
  c+=1
else:
  d+=1

print("What is your favourite world in star wars?")
time.sleep(0.3)
print("a) Tattooine")
time.sleep(0.3)
print("b) Naboo")
time.sleep(0.3)
print("c) Coruscant")
time.sleep(0.3)
print("d) Bespin")
answer=input()
if answer=="a":
  a+=1
elif answer=="b":
  b+=1
elif answer=="c":
  c+=1
else:
  d+=1

print("What is your favourite droid in star wars?")
time.sleep(0.3)
print("a) R2-D2")
time.sleep(0.3)
print("b) BB-8")
time.sleep(0.3)
print("c) IG-11")
time.sleep(0.3)
print("d) R2-Q5")
answer=input()
if answer=="a":
  a+=1
elif answer=="b":
  b+=1
elif answer=="c":
  c+=1
else:
  d+=1

if a>b and a>c and a>d:
  print("You are Luke Skywalker!")
elif b>a and b>c and b>d:
  print("You are Han Solo!")
elif c>a and c>b and c>d:
  print("You are the Mandalorian!")
elif d>a and d>b and d>c:
  print("You are a Stormtrooper!")

