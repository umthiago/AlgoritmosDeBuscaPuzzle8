import heapq

resultado = [1,2,3,4,5,6,7,8,0]


def heuristica(a):
    # Manhattan simples
    dist = 0
    for i, v in enumerate(a):
        if v == 0:
            continue
        x1, y1 = i % 3, i // 3
        x2, y2 = (v-1) % 3, (v-1) // 3
        dist += abs(x1-x2) + abs(y1-y2)
    return dist


def vizinhos(estado):
    i = estado.index(0)
    moves = []

    adj = {
        0:[1,3],1:[0,2,4],2:[1,5],
        3:[0,4,6],4:[1,3,5,7],5:[2,4,8],
        6:[3,7],7:[4,6,8],8:[7,5]
    }

    for j in adj[i]:
        novo = estado[:]
        novo[i], novo[j] = novo[j], novo[i]
        moves.append(novo)

    return moves


# ---------------- A* ----------------
def astar(start):
    open_list = []
    heapq.heappush(open_list, (0, start, []))

    visitados = 0
    expandidos = 0

    while open_list:

        f, estado, path = heapq.heappop(open_list)
        visitados += 1

        if estado == resultado:
            return {
                "custo": len(path),
                "visitados": visitados,
                "expandidos": expandidos,
                "solucao": path + [estado]
            }

        expandidos += 1

        for v in vizinhos(estado):
            heapq.heappush(open_list, (
                len(path)+1 + heuristica(v),
                v,
                path + [estado]
            ))

    return {"erro": "sem solução"}


# ---------------- GREEDY ----------------
def greedy(start):
    open_list = []
    heapq.heappush(open_list, (heuristica(start), start, []))

    visitados = 0
    expandidos = 0

    while open_list:

        h, estado, path = heapq.heappop(open_list)
        visitados += 1

        if estado == resultado:
            return {
                "custo": len(path),
                "visitados": visitados,
                "expandidos": expandidos,
                "solucao": path + [estado]
            }

        expandidos += 1

        for v in vizinhos(estado):
            heapq.heappush(open_list, (
                heuristica(v),
                v,
                path + [estado]
            ))

    return {"erro": "sem solução"}