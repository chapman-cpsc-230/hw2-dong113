"""
File: cooling2.py

Copyright (c) 2016 Lisa Dong

License: MIT

<brief description of the code>

"""    



tea = raw_input("temperature of tea: ")
t_tea = float(tea)

ambient = raw_input("temperature of room: ")
t_air = float (ambient)

m = raw_input("how many minutes passed? ")
min = float (m)

k = .055
ks = .055/60 #convert 1/min to 1/seconds

print "Temperature of the air: %d\nNumber of minutes: %d\nMinute Temperature" % (t_air, min)

i = 0 #min counter
s = 0 #seconds counter
while i <= min:

    print "%3.1d      %4.1f" % (i, t_tea)

    while s <60:

        t_tea = t_tea - ks*(t_tea-t_air)

        s +=1
    
    i+= 1
    s= 0 # resets the seconds counter
