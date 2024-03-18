from person import *
from bag import *

#--------------------------------------------------Part1-submission--------------------------------------------------------
Billybob = Person("Billybob", "Jones", "Male", 160, 65, 17)
print(Billybob)
Billybob.set_middlename("Harry")
print(Billybob)

Katie = Person("Katie", "Jones", "Male", 155, 60, 17, "Louise")
print(Katie)

Billybob.greeting()
Katie.greeting()

print(Billybob.getBMI())
print(Katie.getBMI())
print("\n")

#--------------------------------------------------Part2-submission--------------------------------------------------------

Billybob.writeToFile()
Katie.writeToFile()

Matilda = Person("Matilda", "Street", "Female", 170, 70, 18)
Matilda.writeToFile()

#--------------------------------------------------Part3-submission--------------------------------------------------------
Josh, James = Person("Josh", "Seddon", "Male", 181, "65", 17), Person("James", "Angiolini", "Male", 167, "65", 16)
Soma, Daniel = Person("Soma", "Benfell", "Male", 176, "65", 18), Person("Daniel", "Holmes", "Male", 178, "65", 16)
Thomas, Harrison = Person("Thomas", "Housego", "Male", "5'7", "65", 17), Person("Harrison", "Smith", "Male", "5'11", "65", 17)
Alex = Person("Alex", "Lamb", "Male", "??", "65", 17)

names_list = [Josh, James, Soma, Daniel, Thomas, Harrison, Alex]

for person_object in names_list:
    try:
        person_object.writeToFile()
        print(f"Person {person_object} written to file successfully")
        
    except Exception as e:
        print(f"Error: {e}")

print("\n")
#--------------------------------------------------Part4-submission--------------------------------------------------------
print(Person.howManyPeople())
print(Person.shout("Boo"))

print("\n")
#--------------------------------------------------Part5-submission--------------------------------------------------------
print(Matilda.isTallerThan(Billybob))
print(Katie.isTallerThan(Matilda))

print("\n")
#--------------------------------------------------Part6-submission--------------------------------------------------------
MobilePhone = Item("Mobile Phone", 3, "call someone")
Wallet = Item("Wallet", 1, "contain cards and money")
PencilCase = Item("Pencil case", 4, "store stationary")

print(f"{MobilePhone}, {Wallet}, {PencilCase}")

Billybob.getBag().add(PencilCase)
Billybob.getBag().add(PencilCase)
Billybob.getBag().add(PencilCase)
Billybob.getBag().add(PencilCase)
Billybob.getBag().add(PencilCase)

Billybob.getBag().add(MobilePhone)

Billybob.getBag().add(Wallet)
Billybob.getBag().add(Wallet)
Billybob.getBag().add(Wallet)
Billybob.getBag().add(Wallet)
Billybob.getBag().add(Wallet)

Billybob.getBag().checkContents()

Billybob.getBag().remove(MobilePhone)

Billybob.getBag().checkContents()

#--------------------------------------------------Part7-submission--------------------------------------------------------
'''
See Person file for additional classes and methods
'''

#--------------------------------------------------Part8a-submission--------------------------------------------------------
'''
See Student and Teacher file for additional classes and methods
'''

#--------------------------------------------------Part8b-submission--------------------------------------------------------
'''
See Bag file for additional classes and methods
'''