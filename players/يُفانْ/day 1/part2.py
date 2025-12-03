file_path = "input_1.txt"
with open(file_path, "r") as file:
    lines = file.readlines()

def nextLockNumber(current_numb, direction, quantity):
    if direc == "R":
        new_number = current_numb + quantity
        lock_num = new_number%100
        return(lock_num, new_number)
    if direc == "L":
        new_number = current_numb - quantity
        lock_num = new_number%100
        return(lock_num, new_number)
    else:
        return("error")

def zerosTouchPass(limbo_number, old_number):
    z_counter = 0
    if limbo_number == 0:
        z_counter += 1
    if (limbo_number > 0 and old_number < 0) or (limbo_number < 0 and old_number > 0):
        z_counter += 1
    if limbo_number <= -100:
        passes = abs(limbo_number//-100)
        z_counter += passes
    if limbo_number >= 100:
        passes = abs(limbo_number//100)
        z_counter += passes

    return(z_counter)

x = 50
zero = 0
number_on_lock = x
for line in lines:
    direc, quant = line[:1], int(line[1:])
    # print(direc, quant)
    lock2, limbo_num = nextLockNumber(number_on_lock, direc, quant)
    password = zerosTouchPass(limbo_num ,number_on_lock)
    zero += password
    number_on_lock = lock2
    # print(f"this is the limbo number: {limbo_num}")
    # print(f"this is the new lock number: {number_on_lock}")
    print(f"this number is wehn zero touched or passed: {zero}")