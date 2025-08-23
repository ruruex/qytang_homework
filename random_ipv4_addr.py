import random
def random_ipv4_addr():
    for i in range(4):
        if i < 3:
            print(random.randint(0, 255), end='.')
        else:
            print(random.randint(0, 255))
    print()

random_ipv4_addr()





