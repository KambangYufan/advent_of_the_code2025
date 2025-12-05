#Working out howmany times a padlock goes to and past zero to create a password

#Grabbing the numbers from sequence and sorting them
with open("Sequence") as rotations:
    sequence = [line.strip() for line in rotations]

#with open("dummysequence") as rotations:
    #sequence = [line.strip() for line in rotations]

#Setting a start point, being the number 50, including the previously found password and a variable for the newly created sequence
start = 50
password = 1031
passes = 0
hundredpasses = 0
wrapped_sequence = []
zeros = 0
#Changing the property of R to addition and L to subtraction and turning it into an integer
second_sequence = [int(s.replace("R", "+").replace("L", "-")) for s in sequence]
#print(second_sequence)

for number in second_sequence:
    
    hundredpasses += abs(number) // 100


# Start at 50 then iterating through each number adding them up until it exceeds 100 or -100 and add the abs(number) // 100?

for number in second_sequence:
    sign = -1 if number < 0 else 1
    mag = abs(number)
    wrapped_mag = mag % 100
    wrapped_number = sign * wrapped_mag
    wrapped_sequence.append(wrapped_number)

for number in wrapped_sequence:
    #print(start)
    #print(number)
    previous = start
    #print(previous)
    start += number
    #print (previous)
    #print(previous, "+", number, "=", start )
    #if start == 0:
        #zeros += 1
        #print("start is 0")
    if start < 0:
        start = start + 100
        #print("start was less that 0")
        passes += 1
    if start > 99:
        #print("start was greater than 100")
        start = start - 100
        passes += 1

    #print(passes)
    #print(zeros)

#print(passes + zeros + hundredpasses + password)
#print(password + passes + hundredpasses + zeros)
#print(zeros)
#print(hundredpasses)
#print(passes)
#print(wrapped_sequence)




