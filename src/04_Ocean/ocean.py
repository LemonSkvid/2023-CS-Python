import sys
from typing import List


class Ocean:
    state: List[List[str]]
    
    def __init__(self, init_state: List[List[str]]):
        self.state = init_state

    def __str__(self) -> str:
        return "\n".join(["".join(el for el in row) for row in self.state])
        
    def gen_next_quantum(self) -> "Ocean":
        new_state = []
        fisch = 2
        srimp = 3
        for i in range(len(self.state)):
            next_row = []
            for j in range(len(self.state[i])):
                if self.state[i][j] == 1:
                    next_row.append(1)
                else:
                    n_fisch = 0
                    n_srimp = 0
                    neighbours = [
                        (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                        (i, j - 1), (i, j + 1),
                        (i + 1, j - 1), (i + 1, j), (i + 1, j + 1),
                    ]
                    for ni, nj in neighbours:
                        if ni < 0 or nj < 0 or ni >= len(self.state) or nj >= len(self.state[i]):
                            continue
                        if self.state[ni][nj] == fisch:
                            n_fisch += 1
                        elif self.state[ni][nj] == srimp:
                            n_srimp += 1
                
                    if self.state[i][j] == fisch:
                            
                        if n_fisch < 2 or n_fisch > 3:
                            next_row.append(0)
                        else:
                            next_row.append(2)

                    elif self.state[i][j] == srimp:
                        if n_srimp < 2 or n_srimp > 3:
                            next_row.append(0)
                        else:
                            next_row.append(3)

                    elif n_fisch == fisch and n_srimp == srimp:
                        next_row.append(2)
                    elif n_fisch == 3:
                        next_row.append(2)
                    else:
                        next_row.append(0)
                        
            new_state.append(next_row)

        return Ocean(init_state=new_state)

if __name__ == "__main__":
    n_quantums = int(sys.stdin.readline())
    n_rows, n_clms = (int(i) for i in sys.stdin.readline().split())
    init_state = []
    for i in range(n_rows):
        line = [int(i) for i in sys.stdin.readline().split()]
        init_state.append(line)

    ocean = Ocean(init_state=init_state)
    for _ in range(n_quantums):
        ocean = ocean.gen_next_quantum()
    print(ocean)
