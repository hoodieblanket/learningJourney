# Towers of Hanoi
# Moving disks between 3 pillars without a Larger disk ever going on top of a smaller disk.

def print_move(fr, to):
    print('Move from ' + str(fr) + ' to ' + str(to))

def towers(number, fr, to, spare_disk):
    if number == 1:
        print_move(fr,to)
    else:
        towers(number-1, fr, spare_disk, to)
        towers(1, fr, to, spare_disk)
        towers(number-1, spare_disk, to, fr)

print(towers(4, 'left_pile', 'middle_pile', 'right_pile'))