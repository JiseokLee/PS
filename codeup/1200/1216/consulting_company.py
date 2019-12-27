
no_advertise, advertise, advertise_cost = input().split()
no_advertise = int(no_advertise)
advertise = int(advertise)
advertise_cost = int(advertise_cost)

if(advertise - advertise_cost == no_advertise):
    print('does not matter')
elif(advertise - advertise_cost > no_advertise):
    print('advertise')
else:
    print('do not advertise')
