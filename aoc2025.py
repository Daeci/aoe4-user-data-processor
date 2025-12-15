from aoc2025_helper import EdgeCase, Positions, UniqueCoordsQueue


class Day1:
    @staticmethod
    def Part1() -> int:
        start_val = 50
        total_zero_hit = 0
        with open('day1_input.txt', 'r') as input:
            for line in input:
                mover = int(line[1:])

                if line[0] == 'L':
                    start_val -= mover
                elif line[0] == 'R':
                    start_val += mover

                if start_val == 0 or start_val % 100 == 0:
                    total_zero_hit += 1
        
        return total_zero_hit
    
    @staticmethod
    def Part2() -> int:
        start_val = 50
        total_zero_hit = 0
        with open('day1_input.txt', 'r') as input:
            for line in input:
                mover = int(line[1:])

                if line[0] == 'L':
                    for _ in range(mover):
                        start_val -= 1
                        if start_val == 0 or start_val % 100 == 0:
                            total_zero_hit += 1
                elif line[0] == 'R':
                    for _ in range(mover):
                        start_val += 1
                        if start_val == 0 or start_val % 100 == 0:
                            total_zero_hit += 1

        return total_zero_hit
    
class Day2:
    @staticmethod
    def Part1() -> int:
        total_sum = 0
        with open('day2_input.txt', 'r') as input:
            data_line = input.read()
            lines = data_line.split(',')
            for item in lines:
                numbers = item.split('-')
                for num in range(int(numbers[0]), int(numbers[1]) + 1):
                    num_str = str(num)
                    num_len = len(num_str)
                    if num_len % 2 == 0:
                        mid = num_len // 2
                        if num_str[:mid] == num_str[mid:]:
                            total_sum += num
        
        return total_sum
    
    @staticmethod
    def Part2() -> int:
        #helpers
        def IsValid(total_len, len, num_str) -> bool:
            is_valid = False
            div = total_len // len
            first = num_str[:div]
            for i in range(1, len):
                if first != num_str[div*i:div*(i+1)]:
                    is_valid = True
                    break
                first = num_str[div*i:div*(i+1)]
            
            return is_valid
        #end helpers

        total_sum = 0
        with open('day2_input.txt', 'r') as input:
            data_line = input.read()
            lines = data_line.split(',')
            for item in lines:
                numbers = item.split('-')
                for num in range(int(numbers[0]), int(numbers[1]) + 1):
                    added = False
                    num_str = str(num)
                    num_len = len(num_str)
                    if num_len % 2 == 0:
                        if IsValid(num_len, 2, num_str) == False:
                            total_sum += num
                            added = True
                    if num_len % 3 == 0 and added == False:
                        if IsValid(num_len, 3, num_str) == False:
                            total_sum += num
                            added = True
                    if num_len % 5 == 0 and added == False:
                        if IsValid(num_len, 5, num_str) == False:
                            total_sum += num
                            added = True
                    if num_len % 7 == 0 and added == False:
                        if IsValid(num_len, 7, num_str) == False:
                            total_sum += num

        
        
        return total_sum
    
class Day3:
    @staticmethod
    def Part1() -> int:
        total_joltage = 0
        with open('day3_input.txt', 'r') as input:
            for line in input:
                line_strip = line.strip()
                num1_str = line_strip[len(line_strip)-2]
                num2_str = line_strip[len(line_strip)-1]
                for i in range(len(line_strip) - 3, -1, -1):
                    if int(line_strip[i]) >= int(num1_str):
                        if int(num1_str) > int(num2_str):
                            temp = num1_str
                            num2_str = temp
                        num1_str = line_strip[i]
                
                #print(f'{line_strip} -> first:{line_strip[len(line_strip)-2]}{line_strip[len(line_strip)-1]} second:{int(num1_str + num2_str)}')
                total_joltage += int(num1_str + num2_str)
        return total_joltage
    
    @staticmethod
    def Part2() -> int:
        # get last 12 digits (len - 13)
        # check back to x[0] that 1st digit is highest
        # get last 11
        # check back to x[0] that 1st digit is highest
        
        total_joltage = 0
        with open('day3_input.txt', 'r') as input:
            for line in input:
                line_strip = line.strip()
                #init_line = line_strip
                final_num_str = ""
                for length_checker in range(12, 0, -1):
                    if length_checker == len(line_strip):
                        final_num_str += line_strip
                        break
                    head_position = len(line_strip) - length_checker
                    head = line_strip[head_position]
                    for i in range(len(line_strip) - 1 - length_checker, -1, -1):
                        if int(line_strip[i]) >= int(head):
                            head_position = i
                            head = line_strip[i]
                    final_num_str += head
                    line_strip = line_strip[head_position+1:]
                #print(f'{init_line} -> {final_num_str}')
                total_joltage += int(final_num_str)
        
        return total_joltage
    
class Day4:
    #helper
    @staticmethod
    def GetAdjacentPositions(edge_case: EdgeCase) -> list[Positions]:
        positions = []
        match edge_case:
            case EdgeCase.NONE:
                positions = [Positions.TOP, 
                             Positions.TOP_RIGHT, 
                             Positions.RIGHT, 
                             Positions.BOTTOM_RIGHT, 
                             Positions.BOTTOM, 
                             Positions.BOTTOM_LEFT, 
                             Positions.LEFT, 
                             Positions.TOP_LEFT]
            case EdgeCase.TOP_EDGE:
                # left, bottom-left, bottom, bottom-right, right
                positions = [Positions.LEFT, 
                             Positions.BOTTOM_LEFT, 
                             Positions.BOTTOM, 
                             Positions.BOTTOM_RIGHT, 
                             Positions.RIGHT]
            case EdgeCase.BOTTOM_EDGE:
                # left, top-left, top, top-right, right
                positions = [Positions.LEFT, 
                             Positions.TOP_LEFT, 
                             Positions.TOP, 
                             Positions.TOP_RIGHT, 
                             Positions.RIGHT]
            case EdgeCase.LEFT_EDGE:
                # top, top-right, right, bottom-right, bottom
                positions = [Positions.TOP, 
                             Positions.TOP_RIGHT, 
                             Positions.RIGHT, 
                             Positions.BOTTOM_RIGHT, 
                             Positions.BOTTOM]
            case EdgeCase.RIGHT_EDGE:
                # top, top-left, left, bottom-left, bottom
                positions = [Positions.TOP, 
                             Positions.TOP_LEFT,
                             Positions.LEFT, 
                             Positions.BOTTOM_LEFT, 
                             Positions.BOTTOM]
            case EdgeCase.TOP_LEFT_CORNER:
                # right, bottom-right, bottom
                positions = [Positions.RIGHT,
                             Positions.BOTTOM_RIGHT,
                             Positions.BOTTOM]
            case EdgeCase.TOP_RIGHT_CORNER:
                # left, bottom-left, bottom
                positions = [Positions.LEFT,
                             Positions.BOTTOM_LEFT,
                             Positions.BOTTOM]
            case EdgeCase.BOTTOM_RIGHT_CORNER:
                # left, top-left, top
                positions = [Positions.LEFT,
                             Positions.TOP_LEFT,
                             Positions.TOP]
            case EdgeCase.BOTTOM_LEFT_CORNER:
                # top, top-right, right
                positions = [Positions.TOP,
                             Positions.TOP_RIGHT,
                             Positions.RIGHT]
                
        return positions
    
    @staticmethod
    def IsAdjacentARoll(position, input_list, x, y) -> bool:
        # top          -> [y-1][x]
        # top-right    -> [y-1][x+1]
        # right        -> [y][x+1]
        # bottom-right -> [y+1][x+1]
        # bottom       -> [y+1][x]
        # bottom-left  -> [y+1][x-1]
        # left         -> [y][x-1]
        # top-left     -> [y-1][x-1]

        match position:
            case Positions.TOP:
                return True if input_list[y-1][x] == "@" else False
            case Positions.TOP_RIGHT:
                return True if input_list[y-1][x+1] == "@" else False
            case Positions.RIGHT:
                return True if input_list[y][x+1] == "@" else False
            case Positions.BOTTOM_RIGHT:
                return True if input_list[y+1][x+1] == "@" else False
            case Positions.BOTTOM:
                return True if input_list[y+1][x] == "@" else False
            case Positions.BOTTOM_LEFT:
                return True if input_list[y+1][x-1] == "@" else False
            case Positions.LEFT:
                return True if input_list[y][x-1] == "@" else False
            case Positions.TOP_LEFT:
                return True if input_list[y-1][x-1] == "@" else False
        
        return False
    
    @staticmethod
    def GetPositionCoord(position: Positions, x: int, y: int) -> tuple[int, int]:
        match position:
            case Positions.TOP:
                return (x, y-1)
            case Positions.TOP_RIGHT:
                return (x+1, y-1)
            case Positions.RIGHT:
                return (x+1, y)
            case Positions.BOTTOM_RIGHT:
                return (x+1, y+1)
            case Positions.BOTTOM:
                return (x, y+1)
            case Positions.BOTTOM_LEFT:
                return (x-1, y+1)
            case Positions.LEFT:
                return (x-1, y)
            case Positions.TOP_LEFT:
                return (x-1, y-1)

    @staticmethod
    def IsAdjacentRollCountUnderFour(edge_case, input_list, x, y) -> bool:
        positions = Day4.GetAdjacentPositions(edge_case)
        roll_count = 0
        for position in positions:
            if Day4.IsAdjacentARoll(position, input_list, x, y):
                roll_count += 1
        return True if roll_count < 4 else False

    @staticmethod
    def EnqueueAdjacents(checking_queue: UniqueCoordsQueue, edge_case: EdgeCase, x: int, y: int, input_list: list[str]) -> None:
        # check if adjacents have "@" -> add to queue
        positions = Day4.GetAdjacentPositions(edge_case)
        for position in positions:
            if Day4.IsAdjacentARoll(position, input_list, x, y):
                x_new, y_new = Day4.GetPositionCoord(position, x, y)
                print(f'checking coords:{y},{x} char:{input_list[y][x]} enqueuing:{y_new},{x_new} char:{input_list[y_new][x_new]}')
                checking_queue.enqueue(Day4.GetPositionCoord(position, x, y))

    @staticmethod
    def GetNewLine(line: str, replace_index: int) -> str:
        if replace_index == 0:
            return "x" + line[1:]
        elif replace_index == len(line) - 1:
            return line[:len(line)-1] + "x"
        else:
            return line[:replace_index] + "x" + line[replace_index+1:]


    #end helper

    @staticmethod
    def Part1() -> int:
        input_list = []
        with open('day4_input.txt', 'r') as input:
            for line in input:
                input_list.append(line.strip())
        total_count = 0
        for i in range(len(input_list)): # horizontal movement
            for j in range(len(input_list[i])): # vertical movement
                if input_list[i][j] != "@":
                    continue
                if i == 0: # top edge
                    if j == 0 or j == len(input_list[i]) - 1: # left and right corners
                        total_count += 1 # since these corners can only have 3 max adjacent, as long as it is a paper roll it's valid
                    else:
                        if Day4.IsAdjacentRollCountUnderFour(EdgeCase.TOP_EDGE, input_list, j, i):
                            total_count += 1
                elif i == len(input_list) - 1: # bottom edge
                    if j == 0 or j == len(input_list[i]) - 1: # corners
                        total_count += 1
                    else:
                        if Day4.IsAdjacentRollCountUnderFour(EdgeCase.BOTTOM_EDGE, input_list, j, i):
                            total_count += 1
                elif j == 0: # left edge not including top and bottom corners
                    if Day4.IsAdjacentRollCountUnderFour(EdgeCase.LEFT_EDGE, input_list, j, i):
                        total_count += 1
                elif j == len(input_list[i]) - 1: # right edge not including top and bottom corners:
                    if Day4.IsAdjacentRollCountUnderFour(EdgeCase.RIGHT_EDGE, input_list, j, i):
                        total_count += 1
                else: # no edge case
                    if Day4.IsAdjacentRollCountUnderFour(EdgeCase.NONE, input_list, j, i):
                        total_count += 1
        
        return total_count
    
    @staticmethod
    def Part2() -> int:
        input_list = []
        with open('day4_input.txt', 'r') as input:
            for line in input:
                input_list.append(line.strip())
        total_count = 0
        checking_queue = UniqueCoordsQueue()
        line_len = len(input_list[0])
        for i in range(len(input_list)): # first pass to get initial checking queue coords
            for j in range(line_len):
                if input_list[i][j] != "@":
                    continue
                if i == 0: # top edge
                    if j == 0: # left corner
                        total_count += 1
                        input_list[i] = Day4.GetNewLine(input_list[i], j)
                        Day4.EnqueueAdjacents(checking_queue, EdgeCase.TOP_LEFT_CORNER, j, i, input_list)
                    elif j == len(input_list[i]) - 1: # right corner
                        total_count += 1
                        input_list[i] = Day4.GetNewLine(input_list[i], j)
                        Day4.EnqueueAdjacents(checking_queue, EdgeCase.TOP_RIGHT_CORNER, j, i, input_list)
                    else:
                        if Day4.IsAdjacentRollCountUnderFour(EdgeCase.TOP_EDGE, input_list, j, i):
                            total_count += 1
                            input_list[i] = Day4.GetNewLine(input_list[i], j)
                            Day4.EnqueueAdjacents(checking_queue, EdgeCase.TOP_EDGE, j, i, input_list)
                elif i == len(input_list) - 1: # bottom edge
                    if j == 0: # left corner
                        total_count += 1
                        input_list[i] = Day4.GetNewLine(input_list[i], j)
                        Day4.EnqueueAdjacents(checking_queue, EdgeCase.BOTTOM_LEFT_CORNER, j, i, input_list)
                    elif j == len(input_list[i]) - 1: # right corner
                        total_count += 1
                        input_list[i] = Day4.GetNewLine(input_list[i], j)
                        Day4.EnqueueAdjacents(checking_queue, EdgeCase.BOTTOM_RIGHT_CORNER, j, i, input_list)
                    else:
                        if Day4.IsAdjacentRollCountUnderFour(EdgeCase.BOTTOM_EDGE, input_list, j, i):
                            total_count += 1
                            input_list[i] = Day4.GetNewLine(input_list[i], j)
                            Day4.EnqueueAdjacents(checking_queue, EdgeCase.BOTTOM_EDGE, j, i, input_list)
                elif j == 0: # left edge not including top and bottom corners
                    if Day4.IsAdjacentRollCountUnderFour(EdgeCase.LEFT_EDGE, input_list, j, i):
                        total_count += 1
                        input_list[i] = Day4.GetNewLine(input_list[i], j)
                        Day4.EnqueueAdjacents(checking_queue, EdgeCase.LEFT_EDGE, j, i, input_list)
                elif j == len(input_list[i]) - 1: # right edge not including top and bottom corners:
                    if Day4.IsAdjacentRollCountUnderFour(EdgeCase.RIGHT_EDGE, input_list, j, i):
                        total_count += 1
                        input_list[i] = Day4.GetNewLine(input_list[i], j)
                        Day4.EnqueueAdjacents(checking_queue, EdgeCase.RIGHT_EDGE, j, i, input_list)
                else: # no edge case
                    if Day4.IsAdjacentRollCountUnderFour(EdgeCase.NONE, input_list, j, i):
                        total_count += 1
                        input_list[i] = Day4.GetNewLine(input_list[i], j)
                        Day4.EnqueueAdjacents(checking_queue, EdgeCase.NONE, j, i, input_list)
        
        # 10k too high, 4807 too low
        while checking_queue.is_empty() == False:
            j, i = checking_queue.dequeue()
            print(f'running coords:{i},{j} char:{input_list[i][j]}')
            if (j, i) != (-1, -1) and input_list[i][j] == "@": # sanity check
                if i == 0: # top edge
                    if j == 0: # left corner
                        total_count += 1
                        input_list[i] = Day4.GetNewLine(input_list[i], j)
                        Day4.EnqueueAdjacents(checking_queue, EdgeCase.TOP_LEFT_CORNER, j, i, input_list)
                    elif j == len(input_list[i]) - 1: # right corner
                        total_count += 1
                        input_list[i] = Day4.GetNewLine(input_list[i], j)
                        Day4.EnqueueAdjacents(checking_queue, EdgeCase.TOP_RIGHT_CORNER, j, i, input_list)
                    else:
                        if Day4.IsAdjacentRollCountUnderFour(EdgeCase.TOP_EDGE, input_list, j, i):
                            total_count += 1
                            input_list[i] = Day4.GetNewLine(input_list[i], j)
                            Day4.EnqueueAdjacents(checking_queue, EdgeCase.TOP_EDGE, j, i, input_list)
                elif i == len(input_list) - 1: # bottom edge
                    if j == 0: # left corner
                        total_count += 1
                        input_list[i] = Day4.GetNewLine(input_list[i], j)
                        Day4.EnqueueAdjacents(checking_queue, EdgeCase.BOTTOM_LEFT_CORNER, j, i, input_list)
                    elif j == len(input_list[i]) - 1: # right corner
                        total_count += 1
                        input_list[i] = Day4.GetNewLine(input_list[i], j)
                        Day4.EnqueueAdjacents(checking_queue, EdgeCase.BOTTOM_RIGHT_CORNER, j, i, input_list)
                    else:
                        if Day4.IsAdjacentRollCountUnderFour(EdgeCase.BOTTOM_EDGE, input_list, j, i):
                            total_count += 1
                            input_list[i] = Day4.GetNewLine(input_list[i], j)
                            Day4.EnqueueAdjacents(checking_queue, EdgeCase.BOTTOM_EDGE, j, i, input_list)
                elif j == 0: # left edge not including top and bottom corners
                    if Day4.IsAdjacentRollCountUnderFour(EdgeCase.LEFT_EDGE, input_list, j, i):
                        total_count += 1
                        input_list[i] = Day4.GetNewLine(input_list[i], j)
                        Day4.EnqueueAdjacents(checking_queue, EdgeCase.LEFT_EDGE, j, i, input_list)
                elif j == len(input_list[i]) - 1: # right edge not including top and bottom corners:
                    if Day4.IsAdjacentRollCountUnderFour(EdgeCase.RIGHT_EDGE, input_list, j, i):
                        total_count += 1
                        input_list[i] = Day4.GetNewLine(input_list[i], j)
                        Day4.EnqueueAdjacents(checking_queue, EdgeCase.RIGHT_EDGE, j, i, input_list)
                else: # no edge case
                    if Day4.IsAdjacentRollCountUnderFour(EdgeCase.NONE, input_list, j, i):
                        total_count += 1
                        input_list[i] = Day4.GetNewLine(input_list[i], j)
                        Day4.EnqueueAdjacents(checking_queue, EdgeCase.NONE, j, i, input_list)

        return total_count