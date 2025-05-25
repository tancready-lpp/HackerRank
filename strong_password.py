"""Strong Password

Louise joined a social networking site but the signup page required her to create a strong password.

A password is considered strong if it satisfies the following criteria:
- Its length is at least 6.
- It contains at least one digit.
- It contains at least one lowercase English character.
- It contains at least one uppercase English character.
- It contains at least one special character. The special characters are: !@#$%^&*()-+

She typed a random string of length n in the password field. Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

Function Description

Complete the minimumNumber function.

minimumNumber has the following parameters:
- int n: the length of the password
- string password: the password to test

Returns
- int: the minimum number of characters to add

Input Format

The first line contains an integer n, the length of the password.
The second line contains the password string. Each character is either a lowercase/uppercase English alphabet, a digit, or a special character.

Constraints

- 1 <= n <= 100
- All characters in password are in [a-z], [A-Z], [0-9], or [!@#$%^&*()-+]

Sample Input 0

3
Ab1

Sample Output 0

3

Explanation 0

She can make the password strong by adding 3 characters, such as "$hk", turning the password into Ab1$hk, which is strong.

Sample Input 1

11
#HackerRank

Sample Output 1

1

Explanation 1

The password is missing a digit. Adding one digit will make it strong.
Strong Password

Louise joined a social networking site but the signup page required her to create a strong password.

A password is considered strong if it satisfies the following criteria:
- Its length is at least 6.
- It contains at least one digit.
- It contains at least one lowercase English character.
- It contains at least one uppercase English character.
- It contains at least one special character. The special characters are: !@#$%^&*()-+

She typed a random string of length n in the password field. Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

Function Description

Complete the minimumNumber function.

minimumNumber has the following parameters:
- int n: the length of the password
- string password: the password to test

Returns
- int: the minimum number of characters to add

Input Format

The first line contains an integer n, the length of the password.
The second line contains the password string. Each character is either a lowercase/uppercase English alphabet, a digit, or a special character.

Constraints

- 1 <= n <= 100
- All characters in password are in [a-z], [A-Z], [0-9], or [!@#$%^&*()-+]

Sample Input 0

3
Ab1

Sample Output 0

3

Explanation 0

She can make the password strong by adding 3 characters, such as "$hk", turning the password into Ab1$hk, which is strong.

Sample Input 1

11
#HackerRank

Sample Output 1

1

Explanation 1

The password is missing a digit. Adding one digit will make it strong.Strong Password

Louise joined a social networking site but the signup page required her to create a strong password.

A password is considered strong if it satisfies the following criteria:
- Its length is at least 6.
- It contains at least one digit.
- It contains at least one lowercase English character.
- It contains at least one uppercase English character.
- It contains at least one special character. The special characters are: !@#$%^&*()-+

She typed a random string of length n in the password field. Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

Function Description

Complete the minimumNumber function.

minimumNumber has the following parameters:
- int n: the length of the password
- string password: the password to test

Returns
- int: the minimum number of characters to add

Input Format

The first line contains an integer n, the length of the password.
The second line contains the password string. Each character is either a lowercase/uppercase English alphabet, a digit, or a special character.

Constraints

- 1 <= n <= 100
- All characters in password are in [a-z], [A-Z], [0-9], or [!@#$%^&*()-+]

Sample Input 0

3
Ab1

Sample Output 0

3

Explanation 0

She can make the password strong by adding 3 characters, such as "$hk", turning the password into Ab1$hk, which is strong.

Sample Input 1

11
#HackerRank

Sample Output 1

1

Explanation 1

The password is missing a digit. Adding one digit will make it strong.Strong Password

Louise joined a social networking site but the signup page required her to create a strong password.

A password is considered strong if it satisfies the following criteria:
- Its length is at least 6.
- It contains at least one digit.
- It contains at least one lowercase English character.
- It contains at least one uppercase English character.
- It contains at least one special character. The special characters are: !@#$%^&*()-+

She typed a random string of length n in the password field. Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

Function Description

Complete the minimumNumber function.

minimumNumber has the following parameters:
- int n: the length of the password
- string password: the password to test

Returns
- int: the minimum number of characters to add

Input Format

The first line contains an integer n, the length of the password.
The second line contains the password string. Each character is either a lowercase/uppercase English alphabet, a digit, or a special character.

Constraints

- 1 <= n <= 100
- All characters in password are in [a-z], [A-Z], [0-9], or [!@#$%^&*()-+]

Sample Input 0

3
Ab1

Sample Output 0

3

Explanation 0

She can make the password strong by adding 3 characters, such as "$hk", turning the password into Ab1$hk, which is strong.

Sample Input 1

11
#HackerRank

Sample Output 1

1

Explanation 1

The password is missing a digit. Adding one digit will make it strong.
2
"""
import random

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    cn = 0 if any(c in numbers for c in password) else 1
    cl = 0 if any(c in lower_case for c in password) else 1
    cu = 0 if any(c in upper_case for c in password) else 1
    cs = 0 if any(c in special_characters for c in password) else 1

    total_missing = cn + cl + cu + cs
    return max(total_missing, 6 - n)


s1 = "2K!s" # no good needs 2 more
s2 = "jU898£$%&" # is good
s3 = "h7skjdjj" #needs upper

print(minimumNumber(len(s1),s1),"r1")
print(minimumNumber(len(s2),s2),"r2")
print(minimumNumber(len(s3),s3),"r3")
                                        
