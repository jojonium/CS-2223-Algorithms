# Joseph Petitti
# Project 2
from time import perf_counter
import sys
import getopt


def distance(a, b):
    # Finds the Euclidean distance between two points a and b in the Cartesian plane
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** (1 / 2)


def brute_force(points):
    # Solves the closest-pair problem by brute force
    # Input: An array of n >= 2 points in the Cartesian plane
    # Output: Euclidean distance between the closest pair of points
    num_points = len(points)
    return min(((distance(points[i], points[j]))
                for i in range(num_points - 1)
                for j in range(i + 1, num_points)))


def efficient_closest_pair(p, q):
    # Solves the closest-pair problem by divide-and-conquer
    # Input: An array p of n >= 2 points in the Cartesian plane sorted in
    #       non-decreasing order of their x coordinates and an array q of the
    #       same points sorted in non-decreasing order of the y coordinates
    # Output: Euclidean distance between the closest pair of points
    if len(p) <= 3:
        return brute_force(p)
    else:
        mid = len(p) // 2
        p_l = p[:mid]
        q_l, q_r = [], []
        for q_point in q:
            if q_point in p_l:
                q_l.append(q_point)
            else:
                q_r.append(q_point)
        p_r = p[mid:]
        d_l = efficient_closest_pair(p_l, q_l)
        d_r = efficient_closest_pair(p_r, q_r)
        d = min(d_l, d_r)
        m = p[mid - 1][0]
        s = []
        for q_point in q:
            if abs(q_point[0] - m) < d:
                s.append(q_point)
        dminsq = d ** 2
        num = len(s)
        for i in range(num - 1):
            k = i + 1
            while k <= num - 1 and (s[k][1] - s[i][1]) ** 2 < dminsq:
                dminsq = min((s[k][0] - s[i][0]) ** 2 + (s[k][1] - s[i][1]) ** 2, dminsq)
                k = k + 1
    return dminsq ** (1 / 2)


def eff_rec(p, q):
    t0 = perf_counter()
    result = efficient_closest_pair(p, q)
    t1 = perf_counter()
    elapsed = t1 - t0
    print("Efficient Closest Pair:\nAnswer: " + str(result) + "\nTime Elapsed: " + str(elapsed))


def eff_bf(p):
    t0 = perf_counter()
    result = brute_force(p)
    t1 = perf_counter()
    elapsed = t1 - t0
    print("\nBrute Force:\nAnswer: " + str(result) + "\nTime Elapsed: " + str(elapsed))


def main(argv):
    try:
        opts, args = getopt.getopt(argv, ":")
    except getopt.GetoptError:
        print("Project_2.py <input filename>")
        sys.exit(2)
    try:
        file = open(args[1], "r")
    except IndexError:
        file = open("input.txt", "r")
    except IOError:  # Illegal filename
        print("File \"" + argv[1] + "\" not found. Defaulting to \"input.txt\"")
        file = open("input.txt", "r")
    point_string = file.read()
    point_string = point_string.replace("[(", "")
    point_string = point_string.replace(")]", "")
    point_string = point_string.replace("),(", " ")
    string_set = point_string.split()
    point_set = []
    for i in string_set:
        temp = i.split(',')
        point_set.append((float(temp[0]), float(temp[1])))
    # print(point_set)
    p = sorted(point_set, key=lambda point: point[0])
    q = sorted(point_set, key=lambda point: point[1])
    eff_rec(p, q)
    eff_bf(p)


main(sys.argv)
