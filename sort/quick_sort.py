class QuickSort(object):

    def __init__(self, nums):
        self.nums = nums # input array
        self.low = 0 # lower index
        self.high = len(self.nums) - 1 # upper index

    # main method
    def quick_sort(self):
        self.helper_sort(self.nums, self.low, self.high)
        return self.nums
    # helper method
    def helper_sort(self, nums, low, high):
        # base case
        if low >= high:
            return
        # finding a pivot and it's true location in the array
        pivot_index = self.partition(nums, low, high)
        # using recursion to sort left part
        self.helper_sort(nums, low, pivot_index-1)
        # using recursion to sort right part
        self.helper_sort(nums, pivot_index+1, high)

        return nums
    # method to find and stabilize the location of a pivot
    def partition(self, nums, low, high):
        # finding the pivot
        pivot = (low+high)//2
        # swap it with the value of the 'high' index
        self.swap(nums, high, pivot)

        # by using the following lines we can make
        # sure that the pivot's position is found and stabilized
        # in the array
        i = low
        for j in range(low, high):
            # if a value is greater than the pivot's value
            if nums[j] <= nums[high]:
                # swap this value with one that is greater
                # than or equal of the value
                self.swap(nums, j, i)
                # increase i
                i += 1
        self.swap(nums, i, high)
        return i
    # swap 2 values in the array
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

if __name__ == '__main__':
    a = [5, 7, 3, 1, 6, 0]
    quick = QuickSort(a)

    print(quick.quick_sort())
