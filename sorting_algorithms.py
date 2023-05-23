import time


class SortingAlgorithms:

    # Bubble Sort Implementation
    @staticmethod
    # def bubble_sort(dataset, draw_data, speed, stop_flag):
    #     # comparisons counter
    #     comparisons = 0
    #     for i in range(len(dataset)):
    #         for j in range(len(dataset) - i - 1):
    #             if stop_flag():
    #                 return
    #             comparisons += 1
    #             if dataset[j] > dataset[j + 1]:
    #                 # swap elements
    #                 dataset[j], dataset[j + 1] = dataset[j + 1], dataset[j]
    #                 draw_data(dataset, ['#019267' if c == j or c == j + 1 else 'red' for c in range(len(dataset))])
    #                 time.sleep(speed)
    #
    #     draw_data(dataset, ['#019267' for i in range(len(dataset))])
    #     return comparisons
    def bubble_sort(dataset, draw_data, speed, stop_flag):
        # comparisons counter
        comparisons = 0
        i = 0
        while i < len(dataset):
            j = 0
            while j < len(dataset) - i - 1:
                if stop_flag:
                    time.sleep(0.1)  # Sleep for a short duration to reduce CPU usage
                    continue  # Skip the current iteration and check stop_flag again
                comparisons += 1
                if dataset[j] > dataset[j + 1]:
                    # swap elements
                    dataset[j], dataset[j + 1] = dataset[j + 1], dataset[j]
                    draw_data(dataset, ['#019267' if c == j or c == j + 1 else 'red' for c in range(len(dataset))])
                    time.sleep(speed)
                j += 1
            i += 1

        draw_data(dataset, ['#019267' for i in range(len(dataset))])
        return comparisons

    # Quick Sort Implementation
    @staticmethod
    def quick_sort(dataset, start, end, draw_data, speed):
        comparisons = 0  # Counter for comparisons
        if start < end:
            pi, comparisons = SortingAlgorithms.partition(dataset, start, end, draw_data, speed, comparisons)
            left_comparisons = SortingAlgorithms.quick_sort(dataset, start, pi - 1, draw_data, speed)
            right_comparisons = SortingAlgorithms.quick_sort(dataset, pi + 1, end, draw_data, speed)
            comparisons += left_comparisons + right_comparisons

        return comparisons

    @staticmethod
    def partition(dataset, start, end, draw_data, speed, comparisons):
        pivot = dataset[end]

        draw_data(dataset, SortingAlgorithms.get_colors(len(dataset), start, end, start, start))
        time.sleep(speed)

        for i in range(start, end):
            comparisons += 1  # Increment the counter

            if dataset[i] < pivot:
                draw_data(dataset, SortingAlgorithms.get_colors(len(dataset), start, end, start, i, True))
                time.sleep(speed)

                dataset[i], dataset[start] = dataset[start], dataset[i]
                start += 1
            draw_data(dataset, SortingAlgorithms.get_colors(len(dataset), start, end, start, i))
            time.sleep(speed)

        draw_data(dataset, SortingAlgorithms.get_colors(len(dataset), start, end, start, end, True))
        time.sleep(speed)
        dataset[end], dataset[start] = dataset[start], dataset[end]

        return start, comparisons

    @staticmethod
    def get_colors(n, start, end, s, ci, is_swap=False):
        colors = []
        for i in range(n):
            if start <= i <= end:
                colors.append('gray')
            else:
                colors.append('white')
            if i == end:
                colors[i] = 'blue'
            elif i == s:
                colors[i] = 'red'
            elif i == ci:
                colors[i] = 'yellow'
            if is_swap:
                if i == s or i == ci:
                    colors[i] = 'green'
        return colors

    # Selection Sort Implementation
    @staticmethod
    def selection_sort(dataset, draw_data, speed):
        comparisons = 0  # Counter for comparisons
        for i in range(len(dataset)):
            mini = i
            for j in range(i + 1, len(dataset)):
                comparisons += 1  # Increment the counter
                if dataset[mini] > dataset[j]:
                    mini = j
                    draw_data(dataset, ['blue' if c == mini or c == i else 'red' for c in range(len(dataset))])
                    time.sleep(speed)
            dataset[i], dataset[mini] = dataset[mini], dataset[i]
            draw_data(dataset, ['green' if c == i or c == mini else 'red' for c in range(len(dataset))])
            time.sleep(speed)
        draw_data(dataset, ['green' for i in range(len(dataset))])
        return comparisons

    # Merge Sort Implementation
    @staticmethod
    def merge_sort(dataset, draw_data, speed):
        SortingAlgorithms.merge_sort_(dataset, 0, len(dataset) - 1, draw_data, speed)
        # comparisons = SortingAlgorithms.merge_sort_(dataset, 0, len(dataset) - 1, draw_data, speed)
        # return comparisons

    @staticmethod
    def merge_sort_(dataset, left, right, draw_data, speed):
        comparisons = 0
        if left < right:
            mid = (left + right) // 2
            SortingAlgorithms.merge_sort_(dataset, left, mid, draw_data, speed)
            SortingAlgorithms.merge_sort_(dataset, mid + 1, right, draw_data, speed)
            SortingAlgorithms.merge(dataset, left, mid, right, draw_data, speed)
            # comparisons += SortingAlgorithms.merge(dataset, left, mid, right, draw_data, speed)
        # return comparisons

    @staticmethod
    def merge(dataset, left, mid, right, draw_data, speed):
        comparisons = 0
        draw_data(dataset, SortingAlgorithms.color_arr(len(dataset), left, mid, right))
        time.sleep(speed)
        left_data = dataset[left:mid + 1]
        right_data = dataset[mid + 1:right + 1]

        li = ri = 0
        for i in range(left, right + 1):
            if li < len(left_data) and ri < len(right_data):
                comparisons += 1
                if left_data[li] <= right_data[ri]:
                    dataset[i] = left_data[li]
                    li += 1
                else:
                    dataset[i] = right_data[ri]
                    ri += 1
            elif li < len(left_data):
                dataset[i] = left_data[li]
                li += 1
            else:
                dataset[i] = right_data[ri]
                ri += 1

        draw_data(dataset, ['green' if left <= c <= right else 'white' for c in range(len(dataset))])
        time.sleep(speed)
        # return comparisons

    @staticmethod
    def color_arr(n, left, mid, right):
        colors = []
        for i in range(n):
            if left <= i <= right:
                if left <= i <= mid:
                    colors.append('yellow')
                else:
                    colors.append('blue')
            else:
                colors.append('white')

        return colors

    # Insertion Sort Implementation
    @staticmethod
    def insertion_sort(dataset, draw_data, speed):
        comparisons = 0  # Counter for comparisons
        for i in range(1, len(dataset)):
            key = dataset[i]
            j = i - 1
            while j >= 0 and dataset[j] > key:
                dataset[j + 1] = dataset[j]
                j -= 1
                draw_data(dataset, ['green' if x == j + 1 else 'white' for x in range(len(dataset))])
                time.sleep(speed)
                comparisons += 1  # Increment the counter
            dataset[j + 1] = key
            draw_data(dataset, ['green' if x == j + 1 else 'white' for x in range(len(dataset))])
            time.sleep(speed)
        draw_data(dataset, ['green' for x in range(len(dataset))])

        return comparisons
