def isPalindrome(s):
	return s == s[::-1]


test_cases = input()

test_cases = int(test_cases)



for i in range (1,  test_cases+1):
    
    s = input("\n")
    s = s.lower()
    ans = isPalindrome(s)
    if ans:
        print("It is a palindrome\n")
        continue;
    else:
        print("It is not a palindrome\n")
        continue;

