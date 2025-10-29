import heapq
import time

def find_shortest_paths(graph, start):
    """Find the shortest paths from a starting node on a graph using Dijkstra's algorithm.
    
    Args:
        graph (dict): adjacency list
        start (str): starting node
        
    Returns:
        tuple[dict, dict]: (distances, predecessors)    
    """
    distances = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, previous    
    
def reconstruct_path(previous , start, end):
    """Reconstruct the path from start to end using the predecessor map.
    
    Args:
        graph (dict): adjacency list
        start (str): starting node
        end (str): destination node
        
    Returns:
        list[str]: the path between the starting node and the destination node
    """
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    
    return path if path[0] == start else []

if __name__ == "__main__":
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5, 'E': 3},
        'C': {'A': 2, 'B': 1, 'F': 4},
        'D': {'B': 5, 'E': 2, 'G': 6},
        'E': {'B': 3, 'D': 2, 'F': 3, 'H': 5},
        'F': {'C': 4, 'E': 3, 'I': 4},
        'G': {'D': 6, 'H': 2, 'J': 5},
        'H': {'E': 5, 'G': 2, 'I': 3},
        'I': {'F': 4, 'H': 3, 'J': 2},
        'J': {'G': 5, 'I': 2}
    }
    start = 'A'

    benchmark_start = time.perf_counter()

    distances, previous = find_shortest_paths(graph, start)

    for node in sorted(graph, key=lambda n: distances[n]):
        path = reconstruct_path(previous, start, node)
        if node == start or distances[node] == float('inf'):
            continue
        print(f"{start} to {node}\nDistance: {distances[node]}\nPath: {path}\n")
        

    benchmark_end = time.perf_counter()
    print(f"Execution time: {benchmark_end - benchmark_start:.6f}s")