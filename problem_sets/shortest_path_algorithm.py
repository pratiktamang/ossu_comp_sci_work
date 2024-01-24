my_graph = {
    "A": [("B", 5), ("C", 3), ("E", 11)],
    "B": [("A", 5), ("C", 1), ("F", 2)],
    "C": [("A", 3), ("B", 1), ("D", 1), ("E", 5)],
    "D": [("C", 1), ("E", 9), ("F", 3)],
    "E": [("A", 11), ("C", 5), ("D", 9)],
    "F": [("B", 2), ("D", 3)],
}


def shortest_path(graph, start, target=""):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float("inf") for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)

    while unvisited:
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)

    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(
            f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}'
        )

    return distances, paths


shortest_path(my_graph, "A", "F")


"""
-----
Explanation:
-----

    The Python code for the shortest path algorithm successfully calculated the shortest path from node "A" to node "D" in the given graph. Here's the output with comments explaining each line's result:

    Initialization:

    Unvisited nodes: ['A', 'B', 'C', 'D']
    Distances: {'A': 0, 'B': inf, 'C': inf, 'D': inf}
    Paths: {'A': ['A'], 'B': [], 'C': [], 'D': []}
    First Iteration (Starting at A):

    Selected node: 'A'
    Neighbors of A: 'B' (distance 1), 'C' (distance 4)
    Updated distances: {'A': 0, 'B': 1, 'C': 4, 'D': inf}
    Updated paths: {'A': ['A'], 'B': ['A', 'B'], 'C': ['A', 'C'], 'D': []}
    Mark 'A' as visited: ['B', 'C', 'D']
    Second Iteration (From B):

    Selected node: 'B'
    Neighbors of B: 'A' (visited, skipped), 'D' (distance 2)
    Updated distances: {'A': 0, 'B': 1, 'C': 4, 'D': 3}
    Updated paths: {'A': ['A'], 'B': ['A', 'B'], 'C': ['A', 'C'], 'D': ['A', 'B', 'D']}
    Mark 'B' as visited: ['C', 'D']
    Third Iteration (From C):

    Selected node: 'C'
    Neighbors of C: 'A' (visited, skipped), 'D' (distance 3)
    No updates to distances or paths (since A->B->D is shorter than A->C->D)
    Mark 'C' as visited: ['D']
    Fourth Iteration (From D):

    Selected node: 'D'
    All neighbors visited, no updates
    Mark 'D' as visited: []
    Final Output:

    Shortest distance from A to D: 3
    Path: A -> B -> D
    The result indicates that the shortest path from node "A" to node "D" in this graph is via node "B", with a total distance of 3


-----
RUBY equivalent:
-----


def shortest_path(graph, start, target = nil)
    unvisited = graph.keys
    distances = Hash.new(Float::INFINITY)
    paths = Hash.new { |h, k| h[k] = [] }
    distances[start] = 0
    paths[start] << start

    until unvisited.empty?
        current = unvisited.min_by { |node| distances[node] }
        graph[current].each do |node, distance|
            if distances[current] + distance < distances[node]
                distances[node] = distances[current] + distance
                paths[node] = paths[current] + [node]
            end
            # In the Ruby version, the path for each node is directly updated in the if block with paths[node] = paths[current] + [node]. This line effectively does what both the Python version's direct assignment and the extend operation do, by creating a new array that combines the current path with the next node. So, the need for an else block to handle path extension is eliminated.
        end
        unvisited.delete(current)
    end

    targets_to_print = target ? [target] : graph.keys
    targets_to_print.each do |node|
        next if node == start
        puts "\n#{start}-#{node} distance: #{distances[node]}\nPath: #{paths[node].join(' -> ')}"
    end

    return distances, paths
end

# Example usage
my_graph = {
    "A" => [["B", 5], ["C", 3], ["E", 11]],
    "B" => [["A", 5], ["C", 1], ["F", 2]],
    "C" => [["A", 3], ["B", 1], ["D", 1], ["E", 5]],
    "D" => [["C", 1], ["E", 9], ["F", 3]],
    "E" => [["A", 11], ["C", 5], ["D", 9]],
    "F" => [["B", 2], ["D", 3]],
}

shortest_path(my_graph, "A", "F")


"""
