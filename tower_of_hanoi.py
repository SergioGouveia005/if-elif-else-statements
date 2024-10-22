def check_if_complete(peg_c, number_of_disks):
    if len(peg_c) == 0:
        return True
    for i in range(0,number_of_disks):
        if peg_c[i] != number_of_disks - i:
            return False

def solve_tower_of_hanoi(number_of_disks):
    #if even smallest goes right
    #if odd smallest goes left, wraps around
    print(peg_a)
    while(check_if_complete):
        disk = peg_a.pop()
        peg_b.append(disk)
        if check_if_complete(peg_c, number_of_disks):
            return
        disk = peg_a.pop()
        peg_c.append(disk)
        if check_if_complete(peg_c, number_of_disks):
            return
        disk = peg_b.pop()
        peg_c.append(disk)
        if check_if_complete(peg_c, number_of_disks):
            return
        disk = peg_a.pop()
        peg_b.append(disk)
        if check_if_complete(peg_c, number_of_disks):
            return
        disk = peg_c.pop()
        peg_a.append(disk)
        if check_if_complete(peg_c, number_of_disks):
            return
        disk = peg_c.pop()
        peg_b.append(disk)
        if check_if_complete(peg_c, number_of_disks):
            return
        solve_tower_of_hanoi(number_of_disks)
    else:
        disk = peg_a.pop()
    
    print(peg_a)
    print(disk)
    return

number_of_disks = 4
moves = 0
peg_a = []
peg_b = []
peg_c = []
for i in range(0,number_of_disks):
    peg_a.append(number_of_disks - i)
solve_tower_of_hanoi(number_of_disks)

# when even
# a - b #
# a - c
# b - c #
# a - b
# c - a #
# c - b
# loop


# when odd
# a - c #
# a - b
# c - b #
# a - c
# b - a #
# b - c
# loop