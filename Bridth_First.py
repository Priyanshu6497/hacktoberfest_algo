def depth_first_search(graph, start_node):
  """Performs a depth-first search on the given graph, starting at the given node.

  Args:
    graph: The graph to search.
    start_node: The node to start the search from.

  Returns:
    A list of nodes that were visited during the search.
  """

  # Initialize a stack to track the nodes that have been visited.
  stack = [start_node]

  # Initialize a set to track the nodes that have been visited.
  visited = set()

  # While the stack is not empty:
  while stack:

    # Pop the top node from the stack.
    current_node = stack.pop()

    # Add the current node to the set of visited nodes.
    visited.add(current_node)

    # For each neighbor of the current node:
    for neighbor in graph[current_node]:

      # If the neighbor has not been visited:
      if neighbor not in visited:

        # Add the neighbor to the stack.
        stack.append(neighbor)

  # Return the set of visited nodes.
  return visited
