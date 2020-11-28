from typing import List, Tuple

X = 0
Y = 1
TYPE = 2
# #
# ##
TYPE_1 = 0
# ##
# #
TYPE_2 = 1
# ##
#  #
TYPE_3 = 2
#  #
# ##
TYPE_4 = 3

FIRST_TWO = {TYPE_1, TYPE_2}
ONE_OR_FOUR = {TYPE_1, TYPE_4}
ODD = {TYPE_1, TYPE_2}

class Tree:

    def __init__(self, goal_x: int, goal_y: int, goal_type: int) -> None:
        self.start = (0, 0, TYPE_1)
        self.goal = (goal_x, goal_y, goal_type)

    def BFS(self) -> int:
        if self.start == self.goal:
            return 0

        queue = [self.start]
        visited = {self.start}
        step = 0
        while True:
            step += 1
            queue_len = len(queue)
            # self.debug(queue)
            for i in range(queue_len):
                now = queue[i]
                moves = self.move(now)
                for m in moves:
                    if m == self.goal:
                        return step

                    if m not in visited:
                        queue.append(m)
                        visited.add(m)
            queue = queue[queue_len:]

    def move(self, now: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
        dx = 1 if now[TYPE] in FIRST_TWO else -1
        dy = 1 if now[TYPE] in ONE_OR_FOUR else -1
        move1 = (now[X] + dx, now[Y] + dy, (now[TYPE]+2)%4)
        move2 = (now[X], now[Y], (now[TYPE]+1)%4)
        move3 = (now[X], now[Y], (now[TYPE]+3)%4)
        move4 = (
            now[X] if now[TYPE] in ODD else now[X] + dx,
            now[Y] + dy if now[TYPE] in ODD else now[Y],
            (now[TYPE]+2)%4,
        )
        move5 = (
            now[X] + dx if now[TYPE] in ODD else now[X],
            now[Y] if now[TYPE] in ODD else now[Y] + dy,
            (now[TYPE]+2)%4,
        )
        move6 = (
            now[X] + dx if now[TYPE] in ODD else now[X],
            now[Y] if now[TYPE] in ODD else now[Y] + dy,
            (now[TYPE]+3)%4,
        )
        move7 = (
            now[X] if now[TYPE] in ODD else now[X] + dx,
            now[Y] + dy if now[TYPE] in ODD else now[Y],
            (now[TYPE]+1)%4,
        )
        return [move1, move2, move3, move4, move5, move6, move7]

    def debug(self, dots: List[Tuple[int, int, int]]) -> None:
        positive_x = abs(self.goal[X])
        positive_y = abs(self.goal[Y])
        max_range = max(positive_x, positive_y)
        def create_field(dot):
            field = {x: {y: '.' for y in range(-max_range-1, max_range+2)} for x in range(-max_range-1, max_range+2)}
            for i in range(-max_range-1, max_range+2):
                field[0][i] = '|'
                field[i][0] = '-'
            field[0][0] = '+'
            def print_ku(x: int, y: int, t: int) -> None:
                if t == TYPE_1:
                    field[x][y] = str(TYPE_1+1)
                    field[x+1][y] = str(TYPE_1+1)
                    field[x][y+1] = str(TYPE_1+1)
                if t == TYPE_2:
                    field[x][y] = str(TYPE_2+1)
                    field[x+1][y] = str(TYPE_2+1)
                    field[x][y-1] = str(TYPE_2+1)
                if t == TYPE_3:
                    field[x][y] = str(TYPE_3+1)
                    field[x-1][y] = str(TYPE_3+1)
                    field[x][y-1] = str(TYPE_3+1)
                if t == TYPE_4:
                    field[x][y] = str(TYPE_4+1)
                    field[x-1][y] = str(TYPE_4+1)
                    field[x][y+1] = str(TYPE_4+1)
            print_ku(dot[X], dot[Y], dot[TYPE])
            print_ku(self.goal[X], self.goal[Y], self.goal[TYPE])
            return field

        print(''.join('=' for _ in range(2 * positive_x+3)))
        fields = [create_field(d) for d in dots]
        num = len(dots) // 5
        remain = len(dots) % 5
        for i in range(num):
            col = remain if i == num - 1 else 5
            for y in reversed(range(-max_range-1, max_range+2)):
                for j in range(col):
                    for x in range(-max_range-1, max_range+2):
                        print(fields[i*5+j][x][y], end='')
                    print(' ', end='')
                print()
            print()
        print(''.join('-=' for _ in range(2 * positive_x+3)))

def solve(ax, ay, bx, by, cx, cy) -> int:
    largest_x = max(ax, bx, cx)
    largest_y = max(ay, by, cy)
    points = [(ax, ay), (bx, by), (cx, cy)]
    if (largest_x, largest_y) not in points:
        goal_x = largest_x-1
        goal_y = largest_y-1
        goal_type = TYPE_1
    elif (largest_x, largest_y-1) not in points:
        goal_x = largest_x-1
        goal_y = largest_y
        goal_type = TYPE_2
    elif (largest_x-1, largest_y-1) not in points:
        goal_x = largest_x
        goal_y = largest_y
        goal_type = TYPE_3
    elif (largest_x-1, largest_y) not in points:
        goal_x = largest_x
        goal_y = largest_y-1
        goal_type = TYPE_4
    else:
        raise Exception()

    tree = Tree(goal_x, goal_y, goal_type)
    return tree.BFS()

def main():
    T = int(input())
    for _ in range(T):
        ax, ay, bx, by, cx, cy = map(int, input().split())
        print(solve(ax, ay, bx, by, cx, cy))

if __name__ == '__main__':
    main()
