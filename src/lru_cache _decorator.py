# This example caches the vowel count for previously processed strings.

from functools import lru_cache
​
@lru_cache(maxsize=100)
def count_vowels(s):
    s = s.lower()
    return sum(s.count(v) for v in "aeiou")
​
print(count_vowels("Welcome to learning python decorator")) # first call calculates the vowel count and stores the result
print(count_vowels("Welcome to learning python decorator")) # second call uses the cached value, count_vowels() does not need to process the string again.
