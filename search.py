# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def generalSearch(problem, structure):
    """ 
    Defines a general graph search algorithm. 
    Taking into the account the fact that, given the same search problem,search algorithms utimately differ 
    in the type of data structure associated with them  and how the cost function is calculated for each set of actions.
    Uninformed graph search algorithms are assumed to have a constant cost for each set of actions.

    Params:
    problem:    Search problem

    structure:  Data structure conforming to the (LIFO, FIFO, Priority) queueing policies. 
                Must support pop() and push() methods. Will store the paths for each node traversed.
                Where each path is a list of triples, each triple looking like this (state, action, cost)   
    """
    from game import Directions

    structure.push([(problem.getStartState(), Directions.STOP, 0)]) # Adds path of start node to structure

    visited = set() # Set to hold states already visited/traversed

    while not structure.isEmpty():
        
        # Gets the path of the most recent structure entry
        path_latest = structure.pop()

        # Gets current state
        curr_state, _, _ = path_latest[-1]

        if problem.isGoalState(curr_state): # Check if goal has been reached
            # Returns a sequence of actions leading up to the goal state, disregarding initial STOP action
            return [action for _, action,_ in path_latest][1:]

        visited.add(curr_state) # Adds current state to visited, if not already visited

        for newState, nxtAction, stepCost in problem.getSuccessors(curr_state): # For each of current state's successors
            if newState not in visited:
                path_succesor = path_latest.copy() # Copies parent state's path

                path_succesor.append((newState, nxtAction, stepCost)) # Succesor's path = Parent state's path + successor node triple 

                structure.push(path_succesor)

    return False # If search fails



def depthFirstSearch(problem):
    """ Searches the deepest nodes in the search tree first. Employs a stack-based implementation. """

    stack = util.Stack() # Initializes an empty stack

    return generalSearch(problem, structure=stack) 

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
