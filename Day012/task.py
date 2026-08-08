enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()

print(f"enemies outside function: {enemies}")

#Global constants

PI = 3.14159
GOOGLE_URL = "https://www.google.com"


def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

print(is_prime(79))


