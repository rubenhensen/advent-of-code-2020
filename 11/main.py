import copy
filename = '11/input.txt'

class Hall:
    seats = []

    def __init__(self, seats): 
        self.seats = seats

    def __eq__(self, other):
        for indx, row in enumerate(self.seats):
            for indx2, seat in enumerate(row):
                other_seat = other.seats[indx][indx2]
                if seat != other_seat:
                    return False
        return True  

    def __iter__(self):
        self.row = 0
        self.col = 0
        return self

    def __next__(self):
        if self.col == len(self.seats[0]):
            self.col = 0
            self.row += 1
        if self.row < len(self.seats):
            col = self.col
            self.col += 1
            return self.seats[self.row][col]
        else:
            raise StopIteration

    def __str__(self):
        string = ""
        for row in self.seats:
            for seat in row:
                string += str(seat)
            string += "\n"
        return string

    def get_seat(self, row, col):
        return self.seats[row][col]

    def makeEmpty(self, seat):
        row = seat.row
        col = seat.col
        self.seats[row][col].makeEmpty()

    def makeTaken(self, seat):
        row = seat.row
        col = seat.col
        self.seats[row][col].makeTaken()

    def check_adjacent(self, seat):
        row = seat.row
        col = seat.col
        full_adjacent = 0
        col_length = len(self.seats[0]) - 1
        row_length = len(self.seats) - 1
        # check up
        if row > 0:
            seat = self.seats[row - 1][col]
            if not seat.isFloor and not seat.isEmpty:
                full_adjacent += 1

        # check up_right
        if row > 0 and col < col_length:
            seat = self.seats[row - 1][col + 1]
            if not seat.isFloor and not seat.isEmpty:
                full_adjacent += 1

        # check right
        if col < col_length:
            seat = self.seats[row][col + 1]
            if not seat.isFloor and not seat.isEmpty:
                full_adjacent += 1

        # check down_right
        if row < row_length and col < col_length:
            seat = self.seats[row + 1][col + 1]
            if not seat.isFloor and not seat.isEmpty:
                full_adjacent += 1

        # check down
        if row < row_length:
            seat = self.seats[row + 1][col]
            if not seat.isFloor and not seat.isEmpty:
                full_adjacent += 1

        # check down_left
        if row < row_length and col > 0:
            seat = self.seats[row + 1][col - 1]
            if not seat.isFloor and not seat.isEmpty:
                full_adjacent += 1
        
        # check left
        if col > 0:
            seat = self.seats[row][col - 1]
            if not seat.isFloor and not seat.isEmpty:
                full_adjacent += 1
        
        # check up_left
        if row > 0 and col > 0:
            seat = self.seats[row - 1][col - 1]
            if not seat.isFloor and not seat.isEmpty:
                full_adjacent += 1
        
        return full_adjacent

class Seat:
    row = None
    col = None
    isEmpty = True
    isFloor = False
      
    def __init__(self, row, col, isFloor): 
        self.row = row
        self.col = col
        self.isFloor = isFloor
    
    def __repr__(self):
        if self.isFloor:
            return "Floor: \nrow: " + str(self.row) + "\ncol: " + str(self.col)
        elif self.isEmpty:
            return "Empty seat: \nrow: " + str(self.row) + "\ncol: " + str(self.col)
        else: 
            return "Taken seat: \nrow: " + str(self.row) + "\ncol: " + str(self.col)

    def __str__(self):
        if self.isFloor:
            return "."
        elif self.isEmpty:
            return "L"
        else: 
            return "#"
    
    def __eq__(self, other):
        if self.row != other.row:
            return False
        if self.col != other.col:
            return False
        if self.isEmpty != other.isEmpty:
            return False
        if self.isFloor != other.isFloor:
            return False
        return True
    
    def makeEmpty(self):
        if self.isFloor:
            raise AssertionError("Cannot make floor empty")
        self.isEmpty = True

    def makeTaken(self):
        if self.isFloor:
            raise AssertionError("Cannot sit on floor")
        self.isEmpty = False
    

def read_file():
    with open(filename) as file:
        input =  file.readlines()
        seats = []
        for line_index, line in enumerate(input):
            row = []
            for letter_index, letter in enumerate(line):
                if letter == '\n':
                    pass
                elif letter == 'L':
                    seat = Seat(line_index, letter_index, False)
                    row.append(seat)
                elif letter == '.':
                    seat = Seat(line_index, letter_index, True)
                    row.append(seat)
                else:
                    print('error')
                
            seats.append(row)
        return Hall(seats)


            
# seats[row][col]
if __name__ == "__main__":
    hall = read_file()
    # print(hall)

    # seat = hall.get_seat(9,4)
    # print(hall.check_adjacent(seat))
    # print(hall)
    # hall.makeTaken(hall.get_seat(8,3))
    # print(hall.check_adjacent(seat))
    # print(hall)
    # hall.makeTaken(hall.get_seat(8,4))
    # print(hall.check_adjacent(seat))
    # print(hall)
    # hall.makeTaken(hall.get_seat(8,5))
    # print(hall.check_adjacent(seat))
    # print(hall)
    # hall.makeTaken(hall.get_seat(9,3))
    # print(hall.check_adjacent(seat))
    # print(hall)
    # hall.makeTaken(hall.get_seat(9,5))
    # print(hall.check_adjacent(seat))
    # print(hall)
    # hall.makeTaken(hall.get_seat(10,3))
    # print(hall.check_adjacent(seat))
    # print(hall)
    # hall.makeTaken(hall.get_seat(10,4))
    # print(hall.check_adjacent(seat))
    # print(hall)
    # hall.makeTaken(hall.get_seat(10,5))
    # print(hall.check_adjacent(seat))
    # print(hall)

    # for seat in hall:
    #     print(hall.check_adjacent(seat))



    while True:
        # print(hall)
        hall_copy = copy.deepcopy(hall)
        for seat in hall:
            taken = -1
            if not seat.isFloor:
                taken = hall.check_adjacent(seat)
            if taken == 0 and seat.isEmpty:
                hall_copy.makeTaken(seat)
            elif taken >= 4 and not seat.isEmpty:
                hall_copy.makeEmpty(seat)
            
        if hall == hall_copy:
            break
        else:
            hall = hall_copy

    occupied = 0
    for seat in hall_copy:
        if not seat.isFloor and not seat.isEmpty:
            occupied += 1
    print('There are ' + str(occupied) + ' occupied seats.')
    print('Final:')
    print(hall_copy)


    
    
