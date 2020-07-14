from util import Queue




def earliest_ancestor(ancestors, starting_node):
    pass
    # start with making a Queue
    q = Queue()
    # Enqueue list with starting node
    q .enqueue([starting_node])
    # start with empty list of ancestors
    longest_path = []
    # make empty visited set
    visited = set()

    # while queue is not empty
    while q.size() > 0:
        # dequeue list in
        path  =  q.dequeue()
        # look at the parent(1st element) in dequque' d tuple
        v = path [-1]
        
        # see if parent has been visited
        if v not in visited:
            # mark as visited
            visited.add(v)


        # check if one is longer than the rest
        if (len(path) > len(longest_path)):
            longest_path = path

        for i in range(len(ancestors)):
            if ancestors[i][1] is v:
                new_path = path.copy()
                # print(new_path)
                new_path.append(ancestors[i][0])
                q.enqueue(new_path)
        print('longest_path', longest_path)


        earliest = longest_path.pop()

        if earliest is starting_node:
            earliest = -1
        return earliest

           