 # algorithms.py
 from abc import ABC, abstractmethod
 class Algorithm(ABC):
 1
"""Base class for sorting algorithms. Each algorithm must implement sort() 
which
    returns (sorted_list, stats) where stats is a dict containing operation 
counts.
    """
 def __init__(self):
 self.reset_stats()
 def reset_stats(self):
 self.comparisons = 0
 self.swaps = 0
 @abstractmethod
 def sort(self, data: list):
 pass
 def get_stats(self):
 return {"comparisons": self.comparisons, "swaps": self.swaps}
 class BubbleSort(Algorithm):
 def sort(self, data: list):
 self.reset_stats()
 arr = data.copy()
 n = len(arr)
 for i in range(n):
 for j in range(0, n-i-1):
 self.comparisons += 1
 if arr[j] > arr[j + 1]:
 arr[j], arr[j + 1] = arr[j + 1], arr[j]
 self.swaps += 1
 return arr, self.get_stats()
 class MergeSort(Algorithm):
 def sort(self, data: list):
 self.reset_stats()
 arr = data.copy()
 arr = self._merge_sort(arr)
 return arr, self.get_stats()
 def _merge_sort(self, arr):
 if len(arr) <= 1:
 return arr
 mid = len(arr) // 2
 left = self._merge_sort(arr[:mid])
 right = self._merge_sort(arr[mid:])
 return self._merge(left, right)
 2
def _merge(self, left, right):
 i = j = 0
 merged = []
 while i < len(left) and j < len(right):
 self.comparisons += 1
 if left[i] <= right[j]:
 merged.append(left[i])
 i += 1
 else:
 merged.append(right[j])
 j += 1
 self.swaps += 1 # treat move from right as a 'swap' metric
 # append remainders
 merged.extend(left[i:])
 merged.extend(right[j:])
 return merged
 class QuickSort(Algorithm):
 def sort(self, data: list):
 self.reset_stats()
 arr = data.copy()
 self._quick_sort(arr, 0, len(arr)- 1)
 return arr, self.get_stats()
 def _quick_sort(self, arr, low, high):
 if low < high:
 p = self._partition(arr, low, high)
 self._quick_sort(arr, low, p- 1)
 self._quick_sort(arr, p + 1, high)
 def _partition(self, arr, low, high):
 pivot = arr[high]
 i = low- 1
 for j in range(low, high):
 self.comparisons += 1
 if arr[j] <= pivot:
 i += 1
 arr[i], arr[j] = arr[j], arr[i]
 self.swaps += 1
 arr[i + 1], arr[high] = arr[high], arr[i + 1]
 self.swaps += 1
 return i + 1