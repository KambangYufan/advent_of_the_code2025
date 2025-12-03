file_path = "input_1.txt"
with open(file_path, "r") as file:
    lines = file.readlines()


lock_number = 50
zero_counter = 0
for line in lines:
    direction = line[:1]
    quantity = int(line[1:])
    current_sum = lock_number
    if direction == "R":
        current_sum += quantity
        lock_number = current_sum%100
        if lock_number == 0:
            zero_counter += 1
    else:
        current_sum -= quantity
        lock_number = current_sum%100
        if lock_number == 0:
            zero_counter += 1
        

print("lock number is :" + str(lock_number))
print("Zero passes are:"+ str(zero_counter))

print(-10//-3)