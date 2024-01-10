import sys
from typing import List


class Ocean:
    state: List[List[str]]
    rows: int
    cols: int

    def __init__(self, init_state: List[List[str]]):
        self.state = init_state
        self.rows = len(init_state)
        self.cols = len(init_state[0])

    def __str__(self) -> str:
        return "\n".join(["".join(el for el in row) for row in self.state])

    def count_neighbors(self, row: int, col: int, species: str) -> int:
        count = 0
        for i in range(max(0, row - 1), min(row + 2, self.rows)):
            for j in range(max(0, col - 1), min(col + 2, self.cols)):
                if self.state[i][j] == species:
                    count += 1
        return count

    def gen_next_quantum(self) -> "Ocean":
        new_state = [[''] * self.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                if self.state[i][j] in ('2', '3'): 
                    species = self.state[i][j]
                    neighbors = self.count_neighbors(i, j, species)
                    if neighbors >= 4 or neighbors <= 1:
                        new_state[i][j] = ''  # Die
                    else:
                        new_state[i][j] = species
                elif self.state[i][j] == '0':
                    fish_neighbors = self.count_neighbors(i, j, '2') 
                    shrimp_neighbors = self.count_neighbors(i, j, '3')
                    if fish_neighbors == 3 and shrimp_neighbors == 3:
                        new_state[i][j] = '2'
                    else:
                        new_state[i][j] = self.state[i][j]
        return Ocean(new_state)


if __name__ == "__main__":
    n_quantums = int(sys.stdin.readline())
    n_rows, n_cols = (int(i) for i in sys.stdin.readline().split())
    init_state = []
    for _ in range(n_rows):
        line = [str(i) for i in sys.stdin.readline().split()]
        init_state.append(line)

    ocean = Ocean(init_state=init_state)
    for _ in range(n_quantums):
        ocean = ocean.gen_next_quantum()
    print(ocean)
