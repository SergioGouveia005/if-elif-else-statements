import math
def is_complete(peg_c, number_of_disks):
    if len(peg_c) != number_of_disks:
        return False
    for i in range(0,number_of_disks):
        if peg_c[i] != number_of_disks - i:
            return False
    return True

def solve_tower_of_hanoi(number_of_disks):
    complete = False
    move_smallest_piece = True
    moves = 0
    while(complete == False):
        smallest_value = math.inf
        movable_piece_index = 0
        if move_smallest_piece:
            for i in range(len(peg_list)):
                if len(peg_list[i]) != 0 and peg_list[i][-1] == 1:
                    moves += 1
                    move_smallest_piece = False
                    print(f"{moves}.",peg_list, end=" => ") #Display before move
                    if number_of_disks % 2 == 0: peg_list[(i+1)%3].append(peg_list[i].pop())
                    else:  peg_list[(i-1)%3].append(peg_list[i].pop())
                    print(peg_list) #Display after move
                    if is_complete(peg_c, number_of_disks): return
                    break
        else:
            for i in range(len(peg_list)):
                if len(peg_list[i]) != 0 and peg_list[i][-1] != 1:
                    if peg_list[i][-1] < smallest_value:
                        smallest_value = peg_list[i][-1]
                        movable_piece_index = i
            for i in range(len(peg_list)):
                if len(peg_list[i]) == 0:
                    moves += 1
                    move_smallest_piece = True
                    print(f"{moves}.",peg_list, end=" => ") #Display before move
                    peg_list[i].append(peg_list[movable_piece_index].pop())
                    print(peg_list) #Display after move
                    if is_complete(peg_c, number_of_disks): return
                    break
                elif len(peg_list[i]) != 0 and peg_list[i][-1] > peg_list[movable_piece_index][-1]:
                    moves += 1
                    move_smallest_piece = True
                    print(f"{moves}.",peg_list, end=" => ") #Display before move
                    peg_list[i].append(peg_list[movable_piece_index].pop())
                    print(peg_list) #Display after move
                    if is_complete(peg_c, number_of_disks): return
                    break

    
    return

#Setting up the pegs
number_of_disks = int(input("Enter the number of disks: "))
peg_a = []
peg_b = []
peg_c = []
peg_list = [peg_a,peg_b,peg_c]
for i in range(0,number_of_disks):
    peg_a.append(number_of_disks - i)

#Solving it
solve_tower_of_hanoi(number_of_disks)