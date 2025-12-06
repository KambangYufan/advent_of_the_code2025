# Getting the sequence file and making it usable
with open("Sequence") as rotations_file:
    rotations = [int(line.strip().replace("L", "-").replace("R", ""))
        for line in rotations_file]


#setting the dial start and a passes variable
start = 50
passes = 0


# Iterating through each number in the sequence, dividing full rotations of 100 it has then leaving the rest as a remainder and adding the div to passes whilst leaving behind a remainder
for rotation in rotations:
    if rotation < 0:
        div, mod = divmod(rotation, -100)
        passes += div
        if start != 0 and start + mod <= 0:
            passes += 1
    else:
        div, mod = divmod(rotation, 100)
        passes += div
        if start + mod >= 100:
            passes += 1

    #Wrapping the number back down to between 0-99 then restarting the sequence
    start = (start + rotation) % 100

print(passes)
#5831

