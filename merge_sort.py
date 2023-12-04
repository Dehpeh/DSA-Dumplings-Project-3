def merge_sort(data, sort_parameter) -> set:
    # Dictionary to map sort parameters to their corresponding indices
    param_dict = {"title": 0,
                  "rank": 1,
                  "date": 2,
                  "artist": 3,
                  "url": 4,
                  "region": 5,
                  "chart": 6,
                  "trend": 7,
                  "stream": 8}

    # if data has one element or is empty, it is already sorted
    if len(data) <= 1:
        return {tuple(entry["title"], entry["artist"], entry["url"]) for entry in data}

    # stack for iterative recursion
    stack = [(0, len(data))]
    sorted_tuples = set()

    while stack:
        start, end = stack.pop()
        size = end - start

        # if subarray has 1 element, add it to result
        if size <= 1:
            sorted_tuples.add(tuple(data[start]["title"], data[start]["artist"], data[start]["url"]))
        else:
            mid = start + size // 2
            stack.append((mid, end))
            stack.append((start, mid))

            # extract left and right halves
            left = data[start:mid]
            right = data[mid:end]
            merged = []
            i = j = 0

            # merge the two halves
            while i < len(left) and j < len(right):
                if left[i][param_dict[sort_parameter]] < right[j][param_dict[sort_parameter]]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            # add any elements left
            merged.extend(left[i:])
            merged.extend(right[j:])

            # update the original data with the merged result
            data[start:end] = merged

    # select the top 10 songs
    ten_songs = set()
    i = 0
    while len(ten_songs) < 10 and i < len(sorted_tuples):
        ten_songs.add(sorted_tuples[i])
        i += 1

    return ten_songs

def template_merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the list
        left_half = arr[:mid]  # Divide the list into two halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Recursively sort the left half
        merge_sort(right_half)  # Recursively sort the right half

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements in both halves
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
