import sys
import rushhour

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as rushhour_file:
        r = rushhour.load_file(rushhour_file)

    results = rushhour.breadth_first_search(r, max_depth=100)
    solutions = results['solutions']
    num_solutions = len(solutions)

    if num_solutions == 0:
        print 'Impossible'
        sys.exit(1)

    solutions.sort(key=lambda x: len(x))
    shortest_solution = len(solutions[0])

    if shortest_solution < 20 or num_solutions > 200:
        print 'Easy'
    elif shortest_solution > 50 or num_solutions < 20:
        print 'Hard'
    else:
        print 'Moderate'
