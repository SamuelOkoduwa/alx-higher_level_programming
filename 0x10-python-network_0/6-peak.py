#!/usr/bin/python3
def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    def find_peak_helper(nums, low, high):
        mid = (low + high) // 2

        # Check if the middle element is a peak
        if (mid == 0 or nums[mid] >= nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] >= nums[mid + 1]):
            return nums[mid]
        # If the left neighbor is greater, then the peak lies on the left side
        elif mid > 0 and nums[mid - 1] > nums[mid]:
            return find_peak_helper(nums, low, mid - 1)
        # Otherwise, the peak lies on the right side
        else:
            return find_peak_helper(nums, mid + 1, high)

    return find_peak_helper(list_of_integers, 0, len(list_of_integers) - 1)
