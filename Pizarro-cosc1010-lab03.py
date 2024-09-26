#Angel Pizarro
#UWYO COSC 1010
#09/26/2024
#Lab 03
#Lab Section 18
#Sources,COSC1010_lec6-WorkingWithLists.pptx.pdf

states=["Wyoming","Colorado","Montana"]
print(states)
print(states[0])
print(states[-1])
print(f"{states[1].upper()} is south of {states[0].upper()}")



states.append("Washington")
states.append("Oregon")
states.append("California")
print(states)
states.insert(5,"Maine")
print(states)
states.insert(2,"Texas")
print(states)
states.__delitem__(3)
print(states)
states.__delitem__(2)
print(states)


print(sorted(states))
print(states)
print(states)
states.sort(reverse=True)
print(states)
print(reversed(states))
