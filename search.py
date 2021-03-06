# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


# –your name: Liam Gordon
# –your Emory email address/user: lsgord2@emory.edu
# ID–the statement: 2310396
# THIS  CODE  WAS MY OWN WORK , IT WAS  WRITTEN  WITHOUT  CONSULTING  ANY# SOURCES  OUTSIDE  OF THOSE  APPROVED  BY THE  INSTRUCTOR. Liam Gordon

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
from util import Stack, manhattanDistance

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    check = []
    visited = []
    actions = []
    print(problem)
    s = util.Stack()
    s.push(problem.getStartState())
    while (s.isEmpty != True):
        p = s.pop()
        if problem.isGoalState(p):
            #print(actions)
            break
        if p not in visited:
            visited.append(p)
        for x in problem.getSuccessors(p):
            if x[0] not in visited:
                check.append([[p],[x[0]],[x[1]]])
                s.push(x[0])
    count = 0
    for x in reversed(check):
        count+=1
        if count == 1:
            look = x[0]
            actions.append(x[2])
        if count != 1 and x[1] == look:
            look = x[0]
            actions.append(x[2])
    result = []
    for x in reversed(actions):
        result.append(x[0])
    return result
    
    util.raiseNotDefined()
    
                

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    check = []
    visited = []
    actions = []
    print(problem)
    s = util.Queue()
    s.push(problem.getStartState())
    while (s.isEmpty != True):
        p = s.pop()
        if problem.isGoalState(p):
            #print(actions)
            goal = p
            break
        if p not in visited:
            visited.append(p)
        for x in problem.getSuccessors(p):
            if x[0] not in visited:
                visited.append(x[0])
                check.append([[p],[x[0]],[x[1]]])
                s.push(x[0])
                if problem.isGoalState(x[0]):
                    #print(actions)
                    break
    count = 0
    for x in reversed(check):
        count+=1
        if x[1][0] != goal and count == 1:
            count = 0
            continue
        if count == 1:
            look = x[0]
            actions.append(x[2])
        if count != 1 and x[1] == look:
            look = x[0]
            actions.append(x[2])
    result = []
    for x in reversed(actions):
        result.append(x[0])
    return result
    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"

    actions = []
    track = {}
    check = []
    visited = []
    goal = None
    s = util.PriorityQueue()
    s.push(problem.getStartState(), 0)
    track[problem.getStartState()] = 0
    while (s.isEmpty != True):
        p = s.pop()
        if problem.isGoalState(p):
            goal = p
            break
        if p not in visited:
            visited.append(p)
        for x in problem.getSuccessors(p):
            if x[0] not in visited or problem.isGoalState(x[0]) == True:
                visited.append(x[0])
                check.append([[p],[x[0]],[x[1]]])
                track[x[0]] = x[2] + track[p]
                s.push(x[0], track[x[0]])
    count = 0
    for x in reversed(check):
        count+=1
        if x[1][0] != goal and count == 1:
            count = 0
            continue
        if count == 1:
            look = x[0]
            actions.append(x[2])
        if count != 1 and x[1] == look:
            look = x[0]
            actions.append(x[2])
    result = []
    for x in reversed(actions):
        result.append(x[0])
    return result
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    actions = []
    track = {}
    check = []
    visited = []
    goal = None
    s = util.PriorityQueue()
    s.push(problem.getStartState(), 0 + heuristic(problem.getStartState(), problem))
    track[problem.getStartState()] = 0 + heuristic(problem.getStartState(), problem)
    while (s.isEmpty != True):
        p = s.pop()
        if problem.isGoalState(p):
            goal = p
            break
        if p not in visited:
            visited.append(p)
        for x in problem.getSuccessors(p):
            if x[0] not in visited or problem.isGoalState(x[0]) == True:
                #print(heuristic(x[0], problem))
                visited.append(x[0])
                check.append([[p],[x[0]],[x[1]]])
                track[x[0]] = x[2] + track[p] + heuristic(x[0], problem) - heuristic(p, problem)
                s.push(x[0], track[x[0]])
    count = 0
    for x in reversed(check):
        count+=1
        if x[1][0] != goal and count == 1:
            count = 0
            continue
        if count == 1:
            look = x[0]
            actions.append(x[2])
        if count != 1 and x[1] == look:
            look = x[0]
            actions.append(x[2])
    result = []
    for x in reversed(actions):
        result.append(x[0])
    return result
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
