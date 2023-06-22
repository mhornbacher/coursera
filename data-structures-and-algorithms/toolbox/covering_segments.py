# Uses python3
import sys
import random
from collections import namedtuple
from operator import itemgetter

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments = sorted(segments, key=itemgetter(Segment._fields.index('end')))
    current_point = segments[0].start - 1;
    for s in segments:
        if s.start <= current_point <= s.end:
            continue
        else:
            current_point = s.end
            points.append(current_point)
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
