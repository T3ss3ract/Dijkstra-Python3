import heapq


def dijkstra(graph, start, end):
    """
    graph: a dictionary of dictionary
    start: starting node
    end: ending node
    """
    # initialize
    distance = {}
    previous = {}
    for node in graph:
        distance[node] = float("inf")
        previous[node] = None
    distance[start] = 0
    # create a priority queue
    queue = []
    for node in graph:
        heapq.heappush(queue, (distance[node], node))
    # loop
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distance[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance_candidate = current_distance + weight
            if distance_candidate < distance[neighbor]:
                distance[neighbor] = distance_candidate
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance[neighbor], neighbor))
    # return
    path = [end]
    while previous[end]:
        path.append(previous[end])
        end = previous[end]
    return path[::-1]


if __name__ == "__main__":
    graph = {
        "A": {"B": 5, "C": 1},
        "B": {"A": 5, "C": 2, "D": 1},
        "C": {"A": 1, "B": 2, "D": 4, "E": 8},
        "D": {"B": 1, "C": 4, "E": 3, "F": 6},
        "E": {"C": 8, "D": 3},
        "F": {"D": 6},
    }
    print(dijkstra(graph, "A", "F"))
