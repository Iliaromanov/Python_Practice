
# 1. Create a function that will take a list of numbers and return a new list of only the even numbers from the original list.

def filter_evens(nums: List[int]) -> List[int]:
    new_list = []

    for num in nums:
        if num % 2 == 0:
            new_list.append(num)
    return new_list


# 2. Create a function that will take a string and return a new string with all the vowels converted to uppercase.

def cap_vowels(words: str) -> str:
    vowels = "aeiou"
    new_string = ""

    for letter in words:
        if letter in vowels:
            uppercase = letter.upper()
            new_string += uppercase
        else:
            new_string += letter

    return new_string


# 3. Create a function that will take a list of names and return a new list of all names that start with a particular character.

def find_starts_with(words: List[str], target: str) -> List[str]:
    new_list = []

    for word in words:
        if word[0] == target:
            new_list.append(word)

    return new_list
