#Working out how many times a padlock goes to 0 to work out a password


#Grabbing the numbers from sequence and sorting them
with open("Sequence") as rotations:
    sequence = [line.strip() for line in rotations]

#Setting a start point, being the number 50
Start = 50
Password = 0
Passes =  0

#Changing the property of R to addition and L to subtraction
sequence = [s.replace("R", "+").replace("L", "-") for s in sequence]

#Checking the numbers are sorted
#print (sequence)

#Creating the numbers that the sequence would progress through
#for number in sequence:
    #Start += int(number)
    #print (Start)

# Only allowing the numbers to go between 0-99
for number in sequence:
    Start += int(number)
    Start %= 100
    if Start == 0:
        Password += 1

    #print(Start)

print("The password is", Password)











