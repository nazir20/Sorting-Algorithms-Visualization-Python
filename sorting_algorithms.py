import time


class SortingAlgorithms:

    def __init__(self):
        self.comparisons_count = 0

    def set_comparisons_count(self, value):
        self.comparisons_count = value

    def get_comparisons_count(self):
        return self.comparisons_count

    # Bubble Sort Implementation
    def bubble_sort(self, dataset, draw_data, speed, stop_flag):
        # comparisons counter
        self.set_comparisons_count(0)
        i = 0
        while i < len(dataset):
            j = 0
            while j < len(dataset) - i - 1:
                if stop_flag:
                    time.sleep(0.1)  # Sleep for a short duration to reduce CPU usage
                    continue  # Skip the current iteration and check stop_flag again
                comparisons = self.get_comparisons_count() + 1
                self.set_comparisons_count(comparisons)
                if dataset[j] > dataset[j + 1]:
                    # swap elements
                    dataset[j], dataset[j + 1] = dataset[j + 1], dataset[j]
                    draw_data(dataset, ['#019267' if c == j or c == j + 1 else 'red' for c in range(len(dataset))])
                    time.sleep(speed)
                j += 1
            i += 1

        draw_data(dataset, ['#019267' for i in range(len(dataset))])

    # Quick Sort Implementation
    def quick_sort(self, dataset, start, end, draw_data, speed):
        comparisons = 0  # Counter for comparisons
        self.set_comparisons_count(0)
        if start < end:
            pi, comparisons = self.partition(dataset, start, end, draw_data, speed, comparisons)
            left_comparisons = self.quick_sort(dataset, start, pi - 1, draw_data, speed)
            right_comparisons = self.quick_sort(dataset, pi + 1, end, draw_data, speed)
            comparisons += left_comparisons + right_comparisons
            self.set_comparisons_count(comparisons)
        return self.get_comparisons_count()

    def partition(self, dataset, start, end, draw_data, speed, comparisons):
        pivot = dataset[end]

        draw_data(dataset, self.get_colors(len(dataset), start, end, start, start))
        time.sleep(speed)

        for i in range(start, end):
            comparisons += 1  # Increment the counter
            self.set_comparisons_count(comparisons + self.get_comparisons_count())

            if dataset[i] < pivot:
                draw_data(dataset, self.get_colors(len(dataset), start, end, start, i, True))
                time.sleep(speed)

                dataset[i], dataset[start] = dataset[start], dataset[i]
                start += 1
            draw_data(dataset, self.get_colors(len(dataset), start, end, start, i))
            time.sleep(speed)

        draw_data(dataset, self.get_colors(len(dataset), start, end, start, end, True))
        time.sleep(speed)
        dataset[end], dataset[start] = dataset[start], dataset[end]

        return start, self.get_comparisons_count()

    def get_colors(self, n, start, end, s, ci, is_swap=False):
        colors = []
        for i in range(n):
            if start <= i <= end:
                colors.append('gray')
            else:
                colors.append('orange')
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
    def selection_sort(self, dataset, draw_data, speed):
        self.set_comparisons_count(0)
        for i in range(len(dataset)):
            mini = i
            for j in range(i + 1, len(dataset)):
                comparisons = self.get_comparisons_count() + 1  # Increment the counter
                self.set_comparisons_count(comparisons)
                if dataset[mini] > dataset[j]:
                    mini = j
                    draw_data(dataset, ['blue' if c == mini or c == i else 'red' for c in range(len(dataset))])
                    time.sleep(speed)
            dataset[i], dataset[mini] = dataset[mini], dataset[i]
            draw_data(dataset, ['green' if c == i or c == mini else 'red' for c in range(len(dataset))])
            time.sleep(speed)
        draw_data(dataset, ['green' for i in range(len(dataset))])

    # Merge Sort Implementation
    def merge_sort(self, dataset, draw_data, speed):
        self.set_comparisons_count(0)
        self.merge_sort_(dataset, 0, len(dataset) - 1, draw_data, speed)

    def merge_sort_(self, dataset, left, right, draw_data, speed):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort_(dataset, left, mid, draw_data, speed)
            self.merge_sort_(dataset, mid + 1, right, draw_data, speed)
            self.merge(dataset, left, mid, right, draw_data, speed)

    def merge(self, dataset, left, mid, right, draw_data, speed):
        draw_data(dataset, self.color_arr(len(dataset), left, mid, right))
        time.sleep(speed)
        left_data = dataset[left:mid + 1]
        right_data = dataset[mid + 1:right + 1]

        li = ri = 0
        for i in range(left, right + 1):
            if li < len(left_data) and ri < len(right_data):
                comparisons = self.get_comparisons_count() + 1
                self.set_comparisons_count(comparisons)
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

        draw_data(dataset, ['green' if left <= c <= right else 'silver' for c in range(len(dataset))])
        time.sleep(speed)

    def color_arr(self, n, left, mid, right):
        colors = []
        for i in range(n):
            if left <= i <= right:
                if left <= i <= mid:
                    colors.append('yellow')
                else:
                    colors.append('blue')
            else:
                colors.append('silver')

        return colors

    # Insertion Sort Implementation
    def insertion_sort(self, dataset, draw_data, speed):
        self.set_comparisons_count(0)
        for i in range(1, len(dataset)):
            key = dataset[i]
            j = i - 1
            while j >= 0 and dataset[j] > key:
                dataset[j + 1] = dataset[j]
                j -= 1
                draw_data(dataset, ['green' if x == j + 1 else 'red' for x in range(len(dataset))])
                time.sleep(speed)
                comparisons = self.get_comparisons_count() + 1  # Increment the counter
                self.set_comparisons_count(comparisons)
            dataset[j + 1] = key
            draw_data(dataset, ['green' if x == j + 1 else 'red' for x in range(len(dataset))])
            time.sleep(speed)

        draw_data(dataset, ['green' for x in range(len(dataset))])
