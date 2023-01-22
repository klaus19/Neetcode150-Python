
class Solution(object):

    def isPallindrome(self, s):
        # Remove special characters and spaces
        clean_string = ''.join(e for e in s if e.isalnum())
        # Convert to lowercase
        clean_string = clean_string.lower()
        # Compare the cleaned string to its reverse
        return clean_string == ''.join(reversed(clean_string))


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPallindrome(s))
