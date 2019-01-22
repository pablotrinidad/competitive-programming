import copy


class Solution:
    """Problem solution."""

    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        rows = len(A)
        cols = len(A[0])
        base_dict = {'dir': 1, 'start': 0, 'limit': 0, 'val': 0}
        axes = {'x': copy.deepcopy(base_dict), 'y': copy.deepcopy(base_dict)}
        axes['x']['limit'] = cols - 1
        axes['y']['limit'] = rows - 1

        direction = 'x'
        result = []
        for _ in range(rows * cols):
            axis = axes[direction]
            result.append(A[axes['y']['val']][axes['x']['val']])
            if axis['val'] == axis['limit']:
                opp = 'y' if direction == 'x' else 'x'
                # Next
                axes[opp]['val'] += axes[opp]['dir']
                axes[opp]['start'] = axes[opp]['val']

                # Current
                cur_start = axis['start']
                axis['dir'] *= -1
                axis['start'] = axis['limit'] + axis['dir']
                axis['limit'] = cur_start

                direction = opp

            else:
                axis['val'] += axis['dir']
            axis = axes[direction]
        return result
