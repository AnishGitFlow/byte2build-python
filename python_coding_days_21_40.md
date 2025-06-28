# 50 Days of Python Coding Interview Questions


## Day 1: Count Unique Values in a List

**Problem Statement:**  
Write a function to count how many unique values are in a list of integers.

**Input:** `nums = [1, 2, 2, 3, 4, 4, 4]`  
**Output:** `4` (unique values: 1, 2, 3, 4)

**Difficulty Level:** Easy  
**Key Concepts Tested:** Sets, Lists, Basic data cleaning

**Python Solution:**
```python
def count_unique(nums):
    return len(set(nums))
```

**Explanation:**
- Convert list to a `set()` to remove duplicates
- Return the length of that set

**💡 Optimization Tip:** Set lookup is O(1), total time complexity is O(n)

---

## Day 2: Most Frequent Element

**Problem Statement:**  
Find the most frequent element in a list. If there's a tie, return any one.

**Input:** `data = [1, 2, 2, 3, 3, 3, 2]`  
**Output:** `2` (appears 3 times)

**Difficulty Level:** Easy  
**Key Concepts Tested:** Dictionaries, Counting, Data summarization

**Python Solution:**
```python
from collections import Counter

def most_frequent(data):
    freq = Counter(data)
    return freq.most_common(1)[0][0]
```

**Explanation:**
- Use `Counter` to count frequencies
- Return the element with the highest count

**💡 Optimization Tip:** Counter is optimized and readable—great for interviews

---

## Day 3: Remove Outliers from Data

**Problem Statement:**  
Given a list of numbers, remove values outside 1.5×IQR range.

**Input:** `nums = [10, 12, 14, 15, 18, 100]`  
**Output:** `[10, 12, 14, 15, 18]`

**Difficulty Level:** Medium  
**Key Concepts Tested:** Statistics, Data preprocessing

**Python Solution:**
```python
import numpy as np

def remove_outliers(nums):
    q1 = np.percentile(nums, 25)
    q3 = np.percentile(nums, 75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return [x for x in nums if lower <= x <= upper]
```

**Explanation:**
- Compute Q1 and Q3 percentiles using NumPy
- Define the IQR (Interquartile Range)
- Filter out values outside the valid range

**💡 Optimization Tip:** Uses NumPy for fast vectorized operations

---

## Day 4: Find Duplicates in a Dataset

**Problem Statement:**  
Given a list of entries, return all items that appear more than once.

**Input:** `['apple', 'banana', 'apple', 'orange', 'banana']`  
**Output:** `['apple', 'banana']`

**Difficulty Level:** Easy  
**Key Concepts Tested:** Sets, Dictionaries, Deduplication

**Python Solution:**
```python
from collections import Counter

def find_duplicates(data):
    count = Counter(data)
    return [item for item, freq in count.items() if freq > 1]
```

**Explanation:**
- Count item frequency
- Filter items where count > 1

**💡 Optimization Tip:** Scales well for large datasets—linear time complexity

---

## Day 5: Flatten a Nested List

**Problem Statement:**  
Given a list that may contain nested lists, return a flat list.

**Input:** `[1, [2, [3, 4]], 5]`  
**Output:** `[1, 2, 3, 4, 5]`

**Difficulty Level:** Medium  
**Key Concepts Tested:** Recursion, Lists, Data wrangling

**Python Solution:**
```python
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result
```

**Explanation:**
- Check if item is a list
- If so, recursively flatten it
- If not, append directly

**💡 Optimization Tip:** Recursive but can be rewritten iteratively for large inputs

---

## Day 6: Convert String Dates to Datetime Objects

**Problem Statement:**  
Convert a list of date strings (YYYY-MM-DD) into Python datetime objects.

**Input:** `['2023-05-01', '2023-06-10']`  
**Output:** `[datetime.date(2023, 5, 1), datetime.date(2023, 6, 10)]`

**Difficulty Level:** Easy  
**Key Concepts Tested:** datetime, String parsing, Data formatting

**Python Solution:**
```python
from datetime import datetime

def convert_dates(dates):
    return [datetime.strptime(date, "%Y-%m-%d").date() for date in dates]
```

**Explanation:**
- Use `datetime.strptime()` to parse strings
- Convert to `date()` object if time isn't needed

**💡 Optimization Tip:** List comprehension improves readability and performance

---

## Day 7: Group Data by Key

**Problem Statement:**  
Group a list of dictionaries by a given key.

**Input:**
```python
data = [{'city': 'NY', 'val': 1}, {'city': 'LA', 'val': 2}, {'city': 'NY', 'val': 3}]
```

**Output:** `{'NY': [1, 3], 'LA': [2]}`

**Difficulty Level:** Medium  
**Key Concepts Tested:** Grouping, Dictionaries, Looping structures

**Python Solution:**
```python
from collections import defaultdict

def group_by_key(data, key, value):
    grouped = defaultdict(list)
    for item in data:
        grouped[item[key]].append(item[value])
    return dict(grouped)
```

**Explanation:**
- Use `defaultdict(list)` for easier grouping
- Loop through each dictionary and group values

**💡 Optimization Tip:** Avoids conditionals by using defaultdict

---

## Day 8: Calculate Moving Average

**Problem Statement:**  
Given a list of numbers and a window size k, return a list of moving averages.

**Input:** `nums = [1, 2, 3, 4, 5]`, `k = 3`  
**Output:** `[2.0, 3.0, 4.0]`

**Difficulty Level:** Medium  
**Key Concepts Tested:** Sliding Window, Lists, Averages

**Python Solution:**
```python
def moving_average(nums, k):
    return [sum(nums[i:i+k]) / k for i in range(len(nums) - k + 1)]
```

**Explanation:**
- Slide a window of size k across the list
- Calculate and store the average of each window

**💡 Optimization Tip:** Can use cumulative sums for O(1) per window average

---

## Day 9: Detect Missing Values

**Problem Statement:**  
Given a list of values, return the indices where the value is None or NaN.

**Input:** `[1, None, 3, float('nan'), 5]`  
**Output:** `[1, 3]`

**Difficulty Level:** Easy  
**Key Concepts Tested:** Null handling, NaN, List traversal

**Python Solution:**
```python
import math

def find_missing(data):
    return [i for i, x in enumerate(data) 
            if x is None or (isinstance(x, float) and math.isnan(x))]
```

**Explanation:**
- Check for `None` directly
- Use `math.isnan()` for NaN detection

**💡 Optimization Tip:** Handles both Python and NumPy-style missing values robustly

---

## Day 10: Count Word Frequencies in Text

**Problem Statement:**  
Given a block of text, return the frequency of each word.

**Input:** `"data is power and data drives insight"`  
**Output:** `{'data': 2, 'is': 1, 'power': 1, 'and': 1, 'drives': 1, 'insight': 1}`

**Difficulty Level:** Easy  
**Key Concepts Tested:** Strings, Text cleaning, Dictionaries

**Python Solution:**
```python
from collections import Counter

def word_frequencies(text):
    words = text.lower().split()
    return dict(Counter(words))
```

**Explanation:**
- Lowercase all text for uniformity
- Split by whitespace and count occurrences

**💡 Optimization Tip:** For production use, consider regex-based tokenization

---

## Day 11: Reverse a String Without Built-in Function

**Problem Statement:**  
Reverse a string manually (without using `[::-1]` or `reversed`).

**Input:** `"analytics"`  
**Output:** `"scitylana"`

**Difficulty Level:** Easy  
**Key Concepts Tested:** Strings, Looping

**Python Solution:**
```python
def reverse_string(s):
    result = ''
    for char in s:
        result = char + result
    return result
```

**Explanation:**
- Loop through each character
- Prepend each character to build reverse

**💡 Optimization Tip:** Strings are immutable, so `''.join(reversed())` is more efficient in real use

---

## Day 12: Check for Palindrome

**Problem Statement:**  
Check if a given string is a palindrome (ignoring case and spaces).

**Input:** `"Madam"`  
**Output:** `True`

**Difficulty Level:** Easy  
**Key Concepts Tested:** Strings, Data cleaning

**Python Solution:**
```python
def is_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
```

**Explanation:**
- Remove spaces and convert to lowercase
- Compare string with its reverse

**💡 Optimization Tip:** For large strings, use two-pointer approach for O(n) space

---

## Day 13: Extract Domain from Email

**Problem Statement:**  
Extract domain name from an email address.

**Input:** `"user@openai.com"`  
**Output:** `"openai.com"`

**Difficulty Level:** Easy  
**Key Concepts Tested:** Strings, Splitting

**Python Solution:**
```python
def extract_domain(email):
    return email.split('@')[1]
```

**Explanation:**
- Use `split('@')` to separate user from domain

**💡 Optimization Tip:** Add validation checks in real-world usage

---

## Day 14: Merge Two Sorted Lists

**Problem Statement:**  
Merge two already sorted lists into one sorted list.

**Input:** `[1,3,5]` and `[2,4,6]`  
**Output:** `[1,2,3,4,5,6]`

**Difficulty Level:** Medium  
**Key Concepts Tested:** Lists, Pointers, Sorting

**Python Solution:**
```python
def merge_sorted(a, b):
    i = j = 0
    result = []
    
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    
    return result + a[i:] + b[j:]
```

**Explanation:**
- Use two pointers to compare and merge
- Append remaining elements after loop

**💡 Optimization Tip:** Linear time: O(n + m)

---

## Day 15: Check If Two Strings Are Anagrams

**Problem Statement:**  
Check if two strings are anagrams of each other.

**Input:** `"listen"`, `"silent"`  
**Output:** `True`

**Difficulty Level:** Easy  
**Key Concepts Tested:** Sorting, Strings

**Python Solution:**
```python
def is_anagram(a, b):
    return sorted(a) == sorted(b)
```

**Explanation:**
- Sort both strings and compare

**💡 Optimization Tip:** Use Counter for better performance with large strings

---

## Day 16: Find the Intersection of Two Lists

**Problem Statement:**  
Return elements common to both lists.

**Input:** `[1,2,3]` and `[2,3,4]`  
**Output:** `[2,3]`

**Difficulty Level:** Easy  
**Key Concepts Tested:** Sets, Lists

**Python Solution:**
```python
def intersect(a, b):
    return list(set(a) & set(b))
```

**Explanation:**
- Convert to sets and use `&` operator

**💡 Optimization Tip:** Time complexity: O(n + m)

---

## Day 17: Find Maximum Subarray Sum (Kadane's Algorithm)

**Problem Statement:**  
Find the contiguous subarray with the maximum sum.

**Input:** `[-2,1,-3,4,-1,2,1,-5,4]`  
**Output:** `6` (from subarray `[4,-1,2,1]`)

**Difficulty Level:** Hard  
**Key Concepts Tested:** Arrays, Dynamic Programming

**Python Solution:**
```python
def max_subarray(nums):
    max_sum = current = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        max_sum = max(max_sum, current)
    return max_sum
```

**Explanation:**
- Track max subarray sum using dynamic approach
- Compare current value vs sum continuation

**💡 Optimization Tip:** O(n) time, O(1) space

---

## Day 18: Validate a Password

**Problem Statement:**  
Check if a password meets the following criteria:
- At least 8 characters
- Includes a digit
- Includes an uppercase letter

**Input:** `"Data2023"`  
**Output:** `True`

**Difficulty Level:** Medium  
**Key Concepts Tested:** Strings, Regex, Validation

**Python Solution:**
```python
import re

def is_valid(password):
    return (len(password) >= 8 and
            re.search(r'\d', password) and
            re.search(r'[A-Z]', password))
```

**Explanation:**
- Use `re.search()` to validate conditions

**💡 Optimization Tip:** Regex gives flexibility for rule changes

---

## Day 19: Remove Duplicates from List of Dicts

**Problem Statement:**  
Remove duplicate dictionaries based on a specific key.

**Input:** `[{'id':1}, {'id':2}, {'id':1}]`  
**Output:** `[{'id':1}, {'id':2}]`

**Difficulty Level:** Medium  
**Key Concepts Tested:** Sets, Dictionaries, Uniqueness

**Python Solution:**
```python
def remove_dupes(data):
    seen = set()
    result = []
    for d in data:
        if d['id'] not in seen:
            seen.add(d['id'])
            result.append(d)
    return result
```

**Explanation:**
- Use a set to track seen IDs

**💡 Optimization Tip:** Works best with hashable keys like strings/ints

---

## Day 20: Convert JSON String to Dictionary

**Problem Statement:**  
Convert a JSON string to a Python dictionary.

**Input:** `'{"name": "Alice", "age": 30}'`  
**Output:** `{'name': 'Alice', 'age': 30}`

**Difficulty Level:** Easy  
**Key Concepts Tested:** JSON parsing, json module

**Python Solution:**
```python
import json

def parse_json(json_str):
    return json.loads(json_str)
```

**Explanation:**
- Use `json.loads()` to parse the string

**💡 Optimization Tip:** Always wrap in try-except for production safety

---

## Days 21-40: Advanced Data Manipulation & Algorithms

---

## ✅ Day 21: Find Most Frequent Element

**Problem Statement:**  
Return the element that appears most frequently in a list.

**Input:** `[1, 2, 2, 3, 1, 2]`  
**Output:** `2`

**Difficulty Level:** Medium  
**Key Concepts Tested:** Dictionaries, Frequency counting

**Python Solution Code:**
```python
from collections import Counter

def most_frequent(lst):
    return Counter(lst).most_common(1)[0][0]
```

**Explanation:**
- Use `Counter` to count frequencies of all elements
- `most_common(1)` returns the most frequent element as a tuple
- Extract the element from the tuple

**Optimization Tip:**  
✔️ O(n) time complexity with Counter - efficient and readable

**Call to Action:**  
Instagram: "Save this counting trick 🔖"  
YouTube: "What's your most used Counter use case?"

---

## ✅ Day 22: Convert String to Datetime

**Problem Statement:**  
Convert a date string to a Python datetime object.

**Input:** `"2023-10-01"`  
**Output:** `datetime(2023, 10, 1, 0, 0)`

**Difficulty Level:** Easy  
**Key Concepts Tested:** Datetime parsing, String formatting

**Python Solution Code:**
```python
from datetime import datetime

def to_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d")
```

**Explanation:**
- `strptime()` parses string according to specified format
- `%Y-%m-%d` matches year-month-day format

**Optimization Tip:**  
✔️ Always validate format before parsing in production

**Call to Action:**  
Instagram: "What's your date format? 🗓️"  
YouTube: "Comment your region's date format!"

---

## ✅ Day 23: Get Top N Largest Values

**Problem Statement:**  
Return the N largest numbers from a list.

**Input:** `[4, 1, 7, 3], N=2`  
**Output:** `[7, 4]`

**Difficulty Level:** Medium  
**Key Concepts Tested:** Sorting, Heaps, Data structures

**Python Solution Code:**
```python
import heapq

def top_n_largest(nums, n):
    return heapq.nlargest(n, nums)
```

**Explanation:**
- `heapq.nlargest()` efficiently finds N largest elements
- More efficient than sorting the entire list

**Optimization Tip:**  
✔️ O(n log k) complexity - better than full sort for small k

**Call to Action:**  
Instagram: "Save this for data crunching 🔖"  
YouTube: "Drop your test list in comments!"

---

## ✅ Day 24: Replace Null Values in Dictionary

**Problem Statement:**  
Replace all None values in a dictionary with a default value.

**Input:** `{'a': None, 'b': 2}, default=0`  
**Output:** `{'a': 0, 'b': 2}`

**Difficulty Level:** Easy  
**Key Concepts Tested:** Dictionaries, Conditional logic

**Python Solution Code:**
```python
def replace_nulls(dictionary, default=0):
    return {k: (v if v is not None else default) for k, v in dictionary.items()}
```

**Explanation:**
- Dictionary comprehension with conditional expression
- Preserves non-None values, replaces None with default

**Optimization Tip:**  
✔️ Fast and readable one-liner solution

**Call to Action:**  
Instagram: "Save your default dict tip 🔖"  
YouTube: "What's your go-to default value?"

---

## ✅ Day 25: Flatten a Nested List

**Problem Statement:**  
Convert a nested list structure into a single flat list.

**Input:** `[[1, 2], [3, 4], [5]]`  
**Output:** `[1, 2, 3, 4, 5]`

**Difficulty Level:** Medium  
**Key Concepts Tested:** List comprehension, Nested iteration

**Python Solution Code:**
```python
def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]
```

**Explanation:**
- Double for-loop in list comprehension
- Iterates through each sublist, then each item

**Optimization Tip:**  
✔️ Works for 2D lists; use recursion for deeper nesting

**Call to Action:**  
Instagram: "Flatten that data! 🤖"  
YouTube: "Subscribe for Day 26!"

---

## ✅ Day 26: Check if List is Sorted

**Problem Statement:**  
Determine if a list is sorted in ascending order.

**Input:** `[1, 2, 3, 4]`  
**Output:** `True`

**Difficulty Level:** Easy  
**Key Concepts Tested:** List comparison, Sorting validation

**Python Solution Code:**
```python
def is_sorted_ascending(lst):
    return lst == sorted(lst)
```

**Explanation:**
- Compare original list with its sorted version
- Returns True if they match

**Optimization Tip:**  
✔️ For large lists, use custom loop for O(n) without extra space

**Call to Action:**  
Instagram: "Sorted or not? 🔖"  
YouTube: "Try it with descending order too!"

---

## ✅ Day 27: Count Missing Values in List

**Problem Statement:**  
Count the number of None values in a list.

**Input:** `[1, None, 2, None, 3]`  
**Output:** `2`

**Difficulty Level:** Easy  
**Key Concepts Tested:** List traversal, None detection

**Python Solution Code:**
```python
def count_missing_values(lst):
    return lst.count(None)
```

**Explanation:**
- Use built-in `count()` method for simple counting
- Efficiently counts occurrences of None

**Optimization Tip:**  
✔️ For complex conditions, use `sum(x is None for x in lst)`

**Call to Action:**  
Instagram: "Check your data cleanliness ✨"  
YouTube: "Drop a 📂 if you clean data daily!"

---

## ✅ Day 28: Rename Dictionary Keys

**Problem Statement:**  
Rename dictionary keys using a mapping dictionary.

**Input:** `{'a': 1, 'b': 2}, mapping: {'a': 'alpha'}`  
**Output:** `{'alpha': 1, 'b': 2}`

**Difficulty Level:** Medium  
**Key Concepts Tested:** Dictionary manipulation, Key mapping

**Python Solution Code:**
```python
def rename_dictionary_keys(dictionary, key_mapping):
    return {key_mapping.get(k, k): v for k, v in dictionary.items()}
```

**Explanation:**
- Use `get()` method to replace key if mapping exists
- Falls back to original key if no mapping found

**Optimization Tip:**  
✔️ Handles missing mappings gracefully with default behavior

**Call to Action:**  
Instagram: "Customize your keys! 🔖"  
YouTube: "What's your favorite dict trick?"

---

## ✅ Day 29: Detect Duplicates in List

**Problem Statement:**  
Check if a list contains any duplicate values.

**Input:** `[1, 2, 2, 3]`  
**Output:** `True`

**Difficulty Level:** Easy  
**Key Concepts Tested:** Set operations, Duplicate detection

**Python Solution Code:**
```python
def has_duplicates(lst):
    return len(lst) != len(set(lst))
```

**Explanation:**
- Convert to set to remove duplicates
- Compare lengths to detect if duplicates existed

**Optimization Tip:**  
✔️ O(n) time complexity, very efficient

**Call to Action:**  
Instagram: "Save this clean check 🔖"  
YouTube: "Drop a ❌ if you hate duplicates!"

---

## ✅ Day 30: Parse and Clean Column Names

**Problem Statement:**  
Clean a list of column names by converting to lowercase and replacing spaces with underscores.

**Input:** `["First Name", "Last Name", "Age"]`  
**Output:** `["first_name", "last_name", "age"]`

**Difficulty Level:** Medium  
**Key Concepts Tested:** String manipulation, List comprehension

**Python Solution Code:**
```python
def clean_column_names(columns):
    return [col.strip().lower().replace(" ", "_") for col in columns]
```

**Explanation:**
- Chain string methods: strip whitespace, convert to lowercase, replace spaces
- Apply transformation to all column names

**Optimization Tip:**  
✔️ Method chaining is efficient and readable

**Call to Action:**  
Instagram: "Clean data is happy data 😊"  
YouTube: "Share your cleanest dataset name!"

---

## ✅ Day 31: Merge Two Sorted Lists

**Problem Statement:**  
Merge two already sorted lists into one sorted list efficiently.

**Input:** `[1, 3, 5]` and `[2, 4, 6]`  
**Output:** `[1, 2, 3, 4, 5, 6]`

**Difficulty Level:** Medium  
**Key Concepts Tested:** Two-pointer technique, Merging algorithms

**Python Solution Code:**
```python
def merge_sorted_lists(list1, list2):
    result = []
    i = j = 0
    
    # Compare elements from both lists
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    # Add remaining elements
    result.extend(list1[i:])
    result.extend(list2[j:])
    
    return result
```

**Explanation:**
- Use two pointers to compare elements from both lists
- Add smaller element to result and advance corresponding pointer
- Append remaining elements after one list is exhausted

**Optimization Tip:**  
✔️ O(n + m) linear time complexity - optimal for this problem

**Call to Action:**  
Instagram: "Save this merge pattern! 🔖"  
YouTube: "Subscribe for Day 32 tomorrow!"

---

## ✅ Day 32: Count Word Frequencies in Text

**Problem Statement:**  
Count the frequency of each word in a given text string.

**Input:** `"data science is powerful and data drives insights"`  
**Output:** `{'data': 2, 'science': 1, 'is': 1, 'powerful': 1, 'and': 1, 'drives': 1, 'insights': 1}`

**Difficulty Level:** Easy  
**Key Concepts Tested:** String processing, Dictionary operations

**Python Solution Code:**
```python
def count_word_frequencies(text):
    words = text.lower().split()
    frequency = {}
    
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency
```

**Explanation:**
- Convert to lowercase for case-insensitive counting
- Split text into words by whitespace
- Use `get()` method to handle new words gracefully

**Optimization Tip:**  
✔️ Use `collections.Counter` for more concise code

**Call to Action:**  
Instagram: "Try this with your favorite quote! 💭"  
YouTube: "Comment your word count results!"

---

## ✅ Day 33: Find Top K Frequent Elements

**Problem Statement:**  
Given a list of elements, return the k most frequently occurring elements.

**Input:** `[1, 1, 1, 2, 2, 3], k=2`  
**Output:** `[1, 2]`

**Difficulty Level:** Medium  
**Key Concepts Tested:** Frequency counting, Heap operations

**Python Solution Code:**
```python
from collections import Counter

def top_k_frequent_elements(nums, k):
    count = Counter(nums)
    return [item for item, freq in count.most_common(k)]
```

**Explanation:**
- Count frequencies using Counter
- Use `most_common(k)` to get top k frequent elements
- Extract just the elements from the (element, frequency) tuples

**Optimization Tip:**  
✔️ O(n log k) complexity using heap - efficient for large datasets

**Call to Action:**  
Instagram: "Find your top patterns! 📊"  
YouTube: "What are your top 3 most used Python functions?"

---

## ✅ Day 34: Remove Duplicates Preserving Order

**Problem Statement:**  
Remove duplicates from a list while preserving the original order of first occurrences.

**Input:** `[1, 2, 2, 3, 1, 4]`  
**Output:** `[1, 2, 3, 4]`

**Difficulty Level:** Easy  
**Key Concepts Tested:** Set operations, Order preservation

**Python Solution Code:**
```python
def remove_duplicates_preserve_order(lst):
    seen = set()
    result = []
    
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result
```

**Explanation:**
- Use a set to track seen elements
- Only add to result if not previously seen
- Maintains original order of first occurrences

**Optimization Tip:**  
✔️ O(n) time complexity with O(n) space - optimal solution

**Call to Action:**  
Instagram: "Keep it unique! ✨"  
YouTube: "Tag someone who needs cleaner data!"

---

## ✅ Day 35: Flatten Deeply Nested List

**Problem Statement:**  
Flatten a list that may contain multiple levels of nesting.

**Input:** `[1, [2, [3, 4]], 5, [6]]`  
**Output:** `[1, 2, 3, 4, 5, 6]`

**Difficulty Level:** Medium  
**Key Concepts Tested:** Recursion, Deep data structures

**Python Solution Code:**
```python
def flatten_deep_list(lst):
    result = []
    
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_deep_list(item))
        else:
            result.append(item)
    
    return result
```

**Explanation:**
- Recursively check if each item is a list
- If it's a list, recursively flatten it and extend result
- If not a list, append directly to result

**Optimization Tip:**  
✔️ Handles arbitrary nesting depth - very flexible solution

**Call to Action:**  
Instagram: "Recursion magic! 🪄"  
YouTube: "Save if you love recursive solutions!"

---

## ✅ Day 36: Find All Anagrams in String

**Problem Statement:**  
Find all starting indices where anagrams of pattern p occur in string s.

**Input:** `s="abab"`, `p="ab"`  
**Output:** `[0, 2]`

**Difficulty Level:** Medium  
**Key Concepts Tested:** Sliding window, Character frequency

**Python Solution Code:**
```python
from collections import Counter

def find_anagrams_in_string(s, p):
    if len(p) > len(s):
        return []
    
    p_count = Counter(p)
    window_count = Counter()
    result = []
    
    for i in range(len(s)):
        # Add current character to window
        window_count[s[i]] += 1
        
        # Remove character that's outside window
        if i >= len(p):
            if window_count[s[i - len(p)]] == 1:
                del window_count[s[i - len(p)]]
            else:
                window_count[s[i - len(p)]] -= 1
        
        # Check if current window is an anagram
        if window_count == p_count:
            result.append(i - len(p) + 1)
    
    return result
```

**Explanation:**
- Use sliding window technique with character counting
- Maintain frequency count of current window
- Compare window count with pattern count

**Optimization Tip:**  
✔️ O(n) time complexity with efficient sliding window

**Call to Action:**  
Instagram: "Master the sliding window! 🪟"  
YouTube: "Subscribe for more algorithm patterns!"

---

## ✅ Day 37: Reverse Words in String

**Problem Statement:**  
Reverse the order of words in a given string.

**Input:** `"data science is awesome"`  
**Output:** `"awesome is science data"`

**Difficulty Level:** Easy  
**Key Concepts Tested:** String manipulation, List operations

**Python Solution Code:**
```python
def reverse_words_in_string(s):
    return ' '.join(s.strip().split()[::-1])
```

**Explanation:**
- Strip whitespace from both ends
- Split into words (handles multiple spaces)
- Reverse the list of words and join back

**Optimization Tip:**  
✔️ Handles multiple spaces and edge cases elegantly

**Call to Action:**  
Instagram: "Flip your words! 🔄"  
YouTube: "Try it with your favorite sentence!"

---

## ✅ Day 38: Check if String is Palindrome

**Problem Statement:**  
Check if a string is a palindrome, ignoring case, spaces, and punctuation.

**Input:** `"A man, a plan, a canal: Panama"`  
**Output:** `True`

**Difficulty Level:** Easy  
**Key Concepts Tested:** String normalization, Palindrome detection

**Python Solution Code:**
```python
def is_palindrome_string(s):
    # Keep only alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]
```

**Explanation:**
- Filter to keep only alphanumeric characters
- Convert to lowercase for case-insensitive comparison
- Compare string with its reverse

**Optimization Tip:**  
✔️ Two-pointer approach can save space for very large strings

**Call to Action:**  
Instagram: "Test your favorite phrase! 🔍"  
YouTube: "Did your name pass the palindrome test?"

---

## ✅ Day 39: Convert Excel Column Title to Number

**Problem Statement:**  
Convert Excel column titles (like 'A', 'B', 'AA') to their corresponding column numbers.

**Input:** `"AB"`  
**Output:** `28`

**Difficulty Level:** Medium  
**Key Concepts Tested:** Base conversion, Mathematical operations

**Python Solution Code:**
```python
def excel_column_to_number(column_title):
    result = 0
    
    for char in column_title:
        result = result * 26 + (ord(char.upper()) - ord('A') + 1)
    
    return result
```

**Explanation:**
- Treat as base-26 number system (A=1, B=2, etc.)
- Convert each character to its numeric value
- Build result using positional notation

**Optimization Tip:**  
✔️ O(n) where n is length of column title - optimal solution

**Call to Action:**  
Instagram: "Excel wizardry! 📊"  
YouTube: "Save for your next spreadsheet project!"

---

## ✅ Day 40: Validate Parentheses

**Problem Statement:**  
Check if a string containing parentheses, brackets, and braces is properly balanced.

**Input:** `"([{}])"`  
**Output:** `True`

**Difficulty Level:** Medium  
**Key Concepts Tested:** Stack data structure, String validation

**Python Solution Code:**
```python
def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping.values():  # Opening bracket
            stack.append(char)
        elif char in mapping:  # Closing bracket
            if not stack or mapping[char] != stack.pop():
                return False
    
    return not stack  # True if stack is empty
```

**Explanation:**
- Use stack to track opening brackets
- For each closing bracket, check if it matches the most recent opening
- String is valid if stack is empty at the end

**Optimization Tip:**  
✔️ O(n) time and space complexity - classic stack application

**Call to Action:**  
Instagram: "Balance your brackets! ⚖️"  
YouTube: "Tag a friend who loves algorithms!"

---

## 🎯 Summary: Days 21-40

These 20 problems covered advanced data manipulation, algorithm patterns, and real-world programming scenarios. Key themes included:

- **Frequency Analysis**: Counting, finding most common elements
- **Data Cleaning**: Handling nulls, duplicates, formatting
- **String Processing**: Parsing, validation, transformation
- **Algorithm Patterns**: Two pointers, sliding window, recursion
- **Data Structures**: Stacks, heaps, sets for efficient solutions

**Skills Developed:**
- Advanced Python data structures usage
- Algorithm optimization techniques
- Real-world data processing patterns
- Interview-ready problem-solving approaches

Ready for Days 41-50? 🚀
