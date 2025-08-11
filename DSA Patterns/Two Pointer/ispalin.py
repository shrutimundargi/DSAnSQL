#Given a string, s, return TRUE if it is a palindrome; otherwise, return FALSE.
#A phrase is considered a palindrome if it reads the same backward as forward after converting all uppercase letters to lowercase and removing any characters that are not letters or numbers. Only alphanumeric characters (letters and digits) are taken into account.

def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            # Replace this placeholder "pass" statement with your code
            return False
        
        left += 1
        right -= 1

    return True

s = str(input())
print(is_palindrome(s))