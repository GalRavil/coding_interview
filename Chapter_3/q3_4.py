"""
In the classic problem of the Towers of Hanoi, you have 3 rods and N disks
of different sizes which can side onto any tower. The puzzle starts with disks
sorted in ascending order of size from top to bottom (e.g. each disk sits on
top of an even larger one). 

You have the following constraints:
(A) Only one disk can be moved at a time.
(B) A disk is slid off the top of one rod onto the next rod.
(C) A disk can only be placed on top of a larger disk.

Write a program to move the disks from the first rod to the last using Stacks.
"""

class TowersOfHanoi:
    def __init__(self, height):
        self.towers = [[], [], []]
        self.height = height
        self.towers[0] = [x for x in range(height, 0, -1)]
    
    def play(self):
        self.print_towers()
        self.move_disk(self.height, 1, 2, 3)
        self.print_towers()
    
    def move_disk(self, height, from_, helper, to):
        if height == 1:
            data = self.towers[from_-1].pop()
            self.towers[to-1].append(data)
            print('Disk {}: Tower {} -> {}'.format(data, from_, to))
        else:
            self.move_disk(height-1, from_, to, helper)
            self.move_disk(1, from_, helper, to)
            self.move_disk(height-1, helper, from_, to)
    
    def print_towers(self):
        for i in self.towers:
            print(i, end='')
        print()

hanoi = TowersOfHanoi(3)
hanoi.play()
