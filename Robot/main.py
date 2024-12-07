# Define class here
class RobotPirate:
    def __init__(self, name, width, height):
        self.name = name 
        self.width = width 
        self.height = height
        self.num_treasures = 5
        self.row = 0
        self.col = 0
        self.direction = 'S'
        self.treasure_locations = set()

    def drop_treasure(self):
        if self.num_treasures>0 and (self.row, self.col) not in self.treasure_locations:
            self.num_treasures -=1
            self.treasure_locations.add((self.row, self.col))
            return True
        return False

    def move(self, places):
        if self.direction == 'S':
            new_pos = self.row + places
            self.row = min(new_pos, self.height - 1)
        elif self.direction == 'E':
            new_pos = self.col + places
            self.col = min(new_pos, self.width - 1)
        elif self.direction == 'N':
            new_pos = self.row - places
            self.row = max(new_pos, 0)
        elif self.direction == 'W':
            new_pos = self.col - places
            self.col = max(new_pos, 0)
        if (self.row, self.col) in self.treasure_locations:
            self.num_treasures +=1
            self.treasure_locations.remove((self.row, self.col))
    
    def turn_left(self):
        direction_map = {
            'N' : 'W',
            'W' : 'S',
            'S' : 'E',
            'E' : 'N'
        }

        self.direction = direction_map[self.direction]

    def turn_right(self):

        direction_map = {
            'N' : 'E',
            'E' : 'S',
            'S' : 'W',
            'W' : 'N'
        }

        self.direction = direction_map[self.direction]


    def __str__(self):
        room = ''
        room_height = self.height
        room_width = self.width
        current_location = (self.row, self.col)
        for r in range(room_height):
            for c in range(room_width):
                if (r,c) == current_location:
                    room += self.name[0].upper()
                elif (r,c) in self.treasure_locations:
                    room += 'x'
                else:
                    room += '-'
            room += "\n"
        return room.strip()
            
    
    def __eq__(self, other):
        position_self = (self.row, self.col)
        position_other = (other.row, other.col)
        return position_other == position_self and self.direction == other.direction



# No need to touch code below this line unless you
# would like to play with different settings. It allows
# you to interact with an instance of your class.
def run_program():
    robot = RobotPirate("Pirate Jake", 5, 3)
    keep_playing = 'y'
    while keep_playing == 'y':
        question = "What would you like to do: "
        m = "Options:\n  m: move forward"
        d = "  d: drop treasure"
        l = "  l: turn left"
        r = "  r: turn right"
        q = "  q: quit"
        prompt = "{}\n{}\n{}\n{}\n{}\n{}".format(m, d, l, r, q, question)
        action = input(prompt)
        if action == 'm':
            how_many = int(input('How many spots? '))
            robot.move(how_many)
        elif action == 'd':
            robot.drop_treasure()
        elif action == 'l':
            robot.turn_left()
        elif action == 'r':
            robot.turn_right()
        elif action == 'q':
            keep_playing = 'n'
        print(robot)
    print('All done!')

if __name__ == "__main__":
    run_program()

