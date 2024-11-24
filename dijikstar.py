import heapq
def dijikstar(source,graph):
    distances={node:float("infinity") for node in graph}
    distances[source]=0
    priority_queue=[(0,source)]
    while priority_queue:
        current_distance,current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbour,distance in graph[current_node]:
            d=current_distance + distance
            if d<distances[neighbour]:
                distances[neighbour]=d
                heapq.heappush(priority_queue, (distance, neighbour))
    return distances
gp={'A':[('B',2),('C',4)],
   'B':[('C',1),('D',6)],
   'C':[('D',3)],
   'D':[]}
re=dijikstar('A',gp)
for i in re:
    print(i,":",re[i])

