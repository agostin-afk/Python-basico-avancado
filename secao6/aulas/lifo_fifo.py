from collections import deque

fila: deque[int] = deque()
fila.appendleft(2)  # Adiciona no começo
fila.appendleft(1)  # Adiciona no começo
fila.appendleft(0)
fila.popleft()