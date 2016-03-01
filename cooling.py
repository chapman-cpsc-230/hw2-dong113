
"""
File: cooling.py

Copyright (c) 2016 Lisa Dong

License: MIT

-asks user for tea temperature, room temperature, and how many minutes passed.
-prints how tea changes temperature after each minute that passes

"""    



tea = raw_input("temperature of tea: ")
t_tea = float(tea)

ambient = raw_input("temperature of room: ")
t_air = float (ambient)

m = raw_input("how many minutes passed? ")
min = float (m)

k = .055

print "Temperature of the air: %d\nNumber of minutes: %d\nMinute Temperature" % (t_air, min)

i =0

while i <= min:

    print "%3.1d      %4.1f" % (i, t_tea)

    t_tea = t_tea - k*(t_tea-t_air)

    i+= 1
