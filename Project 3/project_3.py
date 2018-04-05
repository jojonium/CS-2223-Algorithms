# Joseph Petitti
# Project 3
import sys
from getopt import getopt, GetoptError
from itertools import chain, combinations
from time import perf_counter


# Input: list l
# Output: a list that represents a set of all subsets of list l
def power_set(l):
    return chain.from_iterable(combinations(l, r) for r in range(len(l) + 1))


# Input: a list 'items' of tuples representing the weight and value, respectively,
#   of items, and an int 'cap', representing the maximum capacity of the knapsack
# Output: The total value of all items in 'items', if their total weight is less
#   than the capacity of the knapsack, or zero if they are too heavy
def conditional_value(items, max_weight):
    return sum([x[1] for x in items]) if sum([x[0] for x in items]) <= max_weight else 0


# Input: a list 'items' of tuples representing the weight and value, respectively,
#   of items; and an int, 'cap', representing the maximum capacity of the knapsack.
# Output: The optimal way to select items, maximizing the total value while keeping
#   the total weight below cap, found by exhaustively comparing every possibility.
#   The first variable returned is the optimal value, the second variable returned
#   is the optimal list of items.
def exhaustive_search(items, cap):
    best_value = 0
    best_set = []
    for candidate in power_set(items):
        v = conditional_value(candidate, cap)
        if v >= best_value:
            best_value = v
            best_set = candidate
    return best_value, best_set


# Input: a list 'items' of tuples representing the weight and value, respectively,
#   of items; and an int, 'cap', representing the maximum capacity of the knapsack.
# Output: The optimal way to select items, maximizing the total value while keeping
#   the total weight below cap, found by a dynamic programming method. The first
#   variable returned is the optimal value, the second variable returned is the
#   optimal list of items.
def dynamic(items, cap):    # Something is wrong here
    # Build the table
    n = len(items)
    c = [[0 for j in range(cap + 1)] for i in range(n + 1)]
    for w in range(cap + 1):
        c[0][w] = 0
    for i in range(1, n + 1):
        c[i][0] = 0
        for w in range(1, cap + 1):
            wi, vi = items[i - 1][0], items[i - 1][1]
            if items[i - 1][0] <= w:
                if vi + c[i - 1][w - wi] > c[i - 1][w]:
                    c[i][w] = vi + c[i - 1][w - wi]
                else:
                    c[i][w] = c[i - 1][w]
            else:
                c[i][w] = c[i - 1][w]

    # Trace the optimal path
    i, w, = n, cap
    best_set = []
    while i > 0 and w > 0:
        if c[i][w] != c[i - 1][w]:
            best_set.append(items[i - 1])
            w -= items[i - 1][0]
        i -= 1
    return c[n][cap], best_set


stored = {}


# Input: a list 'items' of tuples representing the weight and value, respectively,
#   of items; an int, 'cap', representing the maximum capacity of the knapsack; and
#   an int, 'n', representing the length maximum index of the list of items we are
#   considering.
# Output: The set of items to select, maximizing the total value while keeping
#   the total weight below cap, found by a greedy method.
def greedy(items, cap):
    sorted_by_ratio = sorted(items, key=lambda item: item[1]/item[0])
    sorted_by_ratio.reverse()
    used_items = []
    total_value = 0
    for item in sorted_by_ratio:
        if item[0] <= cap:
            used_items.append(item)
            cap -= item[0]
            total_value += item[1]
    return total_value, used_items


def eff_es(items, cap):
    t0 = perf_counter()
    result = exhaustive_search(items, cap)
    t1 = perf_counter()
    elapsed = t1 - t0
    print("\nExhaustive Search:\nBest value: " + str(result[0]) + "\nBest set: " + str(result[1]))
    print("Time Elapsed: " + str(elapsed))


def eff_dy(items, cap):
    t0 = perf_counter()
    result = dynamic(items, cap)
    t1 = perf_counter()
    elapsed = t1 - t0
    print("\nDynamic Programming Method:\nBest value: " + str(result[0]) + "\nBest set: " + str(result[1]))
    print("Time Elapsed: " + str(elapsed))


def eff_greedy(items, cap):
    t0 = perf_counter()
    result = greedy(items, cap)
    t1 = perf_counter()
    elapsed = t1 - t0
    print("\nGreedy Method:\nBest value: " + str(result[0]) + "\nBest set: " + str(result[1]))
    print("Time Elapsed: " + str(elapsed))


def main(argv):
    try:
        opts, args = getopt(argv, ":")
    except GetoptError:
        print("project_3.py <input filename>")
        sys.exit(2)
    try:
        file = open(args[1], "r")
    except IndexError:
        file = open("input.txt", "r")
    except IOError:     # Illegal filename
        print("File \"" + argv[1] + "\" not found. Defaulting to \:input.txt\"")
        file = open("input.txt", "r")
    raw_string = file.read()
    lines = raw_string.split('\n')
    capacity, l_weights, l_values = int(lines[0]), lines[1].split(','), lines[2].split(',')
    items = []      # List of tuples representing (weight, value) of items
    for i in range(len(l_weights)):
        items.append((int(l_weights[i]), int(l_values[i])))
    print("Capacity: " + str(capacity))
    print("Item\tWeight\tValue")
    for x in range(len(items)):
        print(str(x + 1) + "\t\t" + str(items[x][0]) + "\t\t" + str(items[x][1]))
    eff_dy(items, capacity)
    eff_greedy(items, capacity)
    eff_es(items, capacity)
    return 0


main(sys.argv)
