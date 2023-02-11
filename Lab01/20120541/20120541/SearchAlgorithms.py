from heapq import heappush
from Space import *
from Constants import *
import math
from queue import PriorityQueue


def re_Path(g,sc, father, curr):
    g.start.set_color(orange)
    node = father[curr.value]
    if  curr.value == g.start.value:
        return
    if father[curr.value] ==-1:
        return
    curr.set_color(grey)
    if g.is_goal(curr):
        curr.set_color(purple)
    pygame.draw.line(sc, green,  (curr.x,curr.y), (node.x,node.y))
    g.draw(sc)
    re_Path(g,sc, father, node)
    
def DFS(g:Graph, sc:pygame.Surface):
    print('Implement DFS algorithm')

    open_set = [g.start]
    closed_set = []
    father = [-1]*g.get_len()

    while len(open_set) > 0:
        curr = open_set.pop()
        curr.set_color(yellow)
        curr.draw(sc)

        if len(closed_set) !=0:
            father[curr.value] = closed_set[len(closed_set)-1]
        if curr not in closed_set:
            closed_set.append(curr)

            if g.is_goal(curr):
                curr.set_color(yellow)
                g.draw(sc)
                re_Path(g,sc, father, curr)
                return

            for item in g.get_neighbors(curr):
                if  item not in closed_set:
                    open_set.append(item)
                    item.set_color(red)
            g.draw(sc)
        closed_set[len(closed_set)-1].set_color(blue)
        
        

    #TODO: Implement DFS algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')

def BFS(g:Graph, sc:pygame.Surface):
    print('Implement BFS algorithm')

    open_set = [g.start]
    closed_set = set([])
    father = [-1]*g.get_len()

    while len(open_set) > 0:
        curr = open_set.pop(0)
        curr.set_color(yellow)
        curr.draw(sc)

        if g.is_goal(curr):
            curr.set_color(yellow)
            g.draw(sc)
            re_Path(g,sc, father, curr)
            return
        
        for item in g.get_neighbors(curr):
            if item not in open_set and item not in closed_set :
                open_set.append(item)
                item.set_color(red)
                father[item.value] = curr
            
                
        g.draw(sc)
            
        closed_set.add(curr)
        curr.set_color(blue)
        
    #TODO: Implement BFS algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')
   
def UCS(g:Graph, sc:pygame.Surface):
    print('Implement UCS algorithm')

    open_set = [g.start]
    closed_set = set([])
    father = [-1]*g.get_len()
    cost = {} 
    cost[g.start] = 0

    while len(open_set) > 0 :
        curr = None
        for tmp in open_set :
            if curr==None or cost[tmp] < cost[curr]  :
                curr = tmp
        
        if curr==None:
            return

        curr.set_color(yellow)
        curr.draw(sc)
        if g.is_goal(curr):
            curr.set_color(yellow)
            g.draw(sc)
            re_Path(g, sc, father,curr)
            return
        
        else :
            for item in g.get_neighbors(curr):
                if item not in open_set and item not in closed_set:
                    father[item.value] = curr
                    cost[item] = cost[curr] + 1 
                    open_set.append(item) 
                    item.set_color(red)
                    
                else:
                    if cost[item] > cost[curr] +1 :
                        print("hi")
                        cost[item] = cost[curr] +1
                        father[item.value] = curr
                        if item in closed_set:
                            closed_set.remove(item)
                            open_set.append(item)
                        
            g.draw(sc)
            open_set.remove(curr) 
            closed_set.add(curr) 
            curr.set_color(blue)
    #TODO: Implement A* algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')

def h(v, g):
    return math.sqrt((v.x - g.goal.x)*(v.x - g.goal.x) + (v.y - g.goal.y)*(v.y - g.goal.y))

def AStar(g:Graph, sc:pygame.Surface):
    print('Implement A* algorithm')

    open_set = [g.start]
    closed_set = []
    father = [-1]*g.get_len()
    cost = {}
    cost[g.start] = 0

    while len(open_set) > 0 :
        curr = None

        for tmpNode in open_set :
            if curr==None or cost[tmpNode] + h(tmpNode,g)  < cost[curr] + h(curr,g) :
                curr = tmpNode
        if curr==None:
            return
        curr.set_color(yellow) 

        if g.is_goal(curr):
            curr.set_color(yellow)
            g.draw(sc)
            re_Path(g, sc, father,curr)
            return
        else :
            for item in g.get_neighbors(curr):
                if item not in open_set and item not in closed_set:
                    open_set.append(item)
                    father[item.value] = curr
                    cost[item] = cost[curr] + 1
                    item.set_color(red)
                else:
                    if cost[item] > cost[curr] +1:
                        cost[item] = cost[curr] +1
                        father[item.value] = curr

                        if item in closed_set:
                            closed_set.remove(item)
                            open_set.append(item)
                g.draw(sc)
                
            open_set.remove(curr)
            closed_set.append(curr)
            curr.set_color(blue)
            g.draw(sc)
    #TODO: Implement A* algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')

def Greedy(g:Graph, sc:pygame.Surface):
    print('Implement A* algorithm')

    open_set = [g.start]
    closed_set = []
    father = [-1]*g.get_len()
    cost = {}
    cost[g.start] = 0

    while len(open_set) > 0 :
        curr = None

        for tmpNode in open_set :
            if curr==None or  h(tmpNode,g)  <  h(curr,g) :
                curr = tmpNode
        if curr==None:
            return
        curr.set_color(yellow)        
        if g.is_goal(curr):
            curr.set_color(yellow)
            g.draw(sc)
            re_Path(g, sc, father,curr)
            return
        else :
            for item in g.get_neighbors(curr):
                if item not in open_set and item not in closed_set:
                    open_set.append(item)
                    father[item.value] = curr
                    cost[item] = cost[curr] + 1
                    item.set_color(red)
                else:
                    if cost[item] > cost[curr] +1:
                        cost[item] = cost[curr] +1
                        father[item.value] = curr

                        if item in closed_set:
                            closed_set.remove(item)
                            open_set.append(item)
                g.draw(sc)
                
            open_set.remove(curr)
            closed_set.append(curr)
            curr.set_color(blue)
    #TODO: Implement A* algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')



