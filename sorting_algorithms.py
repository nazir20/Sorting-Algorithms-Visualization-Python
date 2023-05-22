import time


class SortingAlgorithms:

    # Bubble Sort
    @staticmethod
    def bubble_sort(data_set, draw_d, speed, stop_flag):
        for i in range(len(data_set) - 1):
            for j in range(len(data_set) - 1):
                if stop_flag:
                    return
                if data_set[j] > data_set[j + 1]:
                    # swap datas
                    data_set[j], data_set[j + 1] = data_set[j + 1], data_set[j]
                    draw_d(data_set, ['#019267' if c == j or c == j + 1 else 'red' for c in range(len(data_set))])
                    time.sleep(speed)

        draw_d(data_set, ['#019267' for i in range(len(data_set))])

    # this part will be updated...
