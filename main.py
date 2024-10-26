import math
import time
num = 1

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
    
while True:
  time.sleep(0.1)
  num += 1
  if is_prime(num) == True:
      file1 = open("numbers.txt", "a")  # append mode
      file1.write(str(num) + "/n")
      file1.close()
