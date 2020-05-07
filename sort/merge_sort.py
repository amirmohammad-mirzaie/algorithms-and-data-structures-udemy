def merge_sort(nums):
    # base case
    if len(nums) == 1:
        return
    # finding the middle index of the array
    mid_index = len(nums)//2

    # creating left and right arrays
    left_half = nums[:mid_index]
    right_half = nums[mid_index:]

    # sort the left and right sub-arrays
    merge_sort(left_half)
    merge_sort(right_half)

    # merging begins here:

    # initializing some indices for tracking the pointer in each array
    i = 0 # index used in in left sub array
    j = 0 # index used in the right sub array
    k = 0 # index used in the main array

    # while we have items in one of the left and right arrays
    # that are not visited yet
    while i < len(left_half) and j < len(right_half):
        # if i-th element of the left array is bigger than the j-th element
        # of the right array
        if left_half[i] < right_half[j]:
            # add this value to the k-th item in the main array
            nums[k] = left_half[i]
            i += 1
        else:
            # add j-th element of the right array to the k-th element of the main array
            nums[k] = right_half[j]
            j += 1

        k += 1
    # while we have some remaining items in the left array
    while i < len(left_half):
        nums[k] = left_half[i]
        i += 1
        k += 1
    # while we have some remaining items in the right array
    while j < len(right_half):
        nums[k] = right_half[j]
        j += 1
        k += 1
    return nums


if __name__ == '__main__':
    a = [5, 3, 0, 1, -2, 10,4]
    print(merge_sort(a))
