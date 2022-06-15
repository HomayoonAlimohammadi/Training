from enum import Enum 


class Days(Enum):
    SAT = 'Saturday'
    SUN = 'Sunday'
    MON = 'Monday'
    FRI = 'Friday'


sat = Days.SAT 
print(sat)
print(repr(sat))
print(sat.name)
print(sat.value)

days = Days 
for day in days:
    print(day)
    print(day.value)
    print()

for day in Days:
    print(day)

sat = Days['SAT']
print(Days['SAT'] == Days.SAT)

# enums are hashable and can be used for dictionary keys
d = {
    Days.SAT: 'good day',
    Days.SUN: 'not so good'
}

print(d)


#### 
#####
###### enums can be accessed via their values!!

print(Days('Saturday'))
print(Days('Monday'))