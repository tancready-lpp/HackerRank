"""
Bon Appétit

Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. 
Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

For example, assume the bill has the following prices: bill = [2, 4, 6]. 
Anna declines to eat item k = bill[2] which costs 6. 
If Brian calculates the bill correctly, Anna will pay (2 + 4)/2 = 3. 
If he charged her 4, you should print 1.

Function Description

Complete the bonAppetit function in the editor below.

bonAppetit has the following parameters:
- bill: an array of integers representing the cost of each item ordered
- k: an integer representing the zero-based index of the item Anna doesn't eat
- b: the amount of money that Anna contributed to the bill

Returns
- If Brian did not overcharge Anna, print "Bon Appetit"
- Otherwise, print the difference (b - actual)

Input Format

- The first line contains two space-separated integers n and k.
- The second line contains n space-separated integers where i-th integer is the cost of i-th item in the bill.
- The third line contains an integer, b, the amount of money that Anna contributed.

Constraints

- 2 <= n <= 10^5
- 0 <= k < n
- 0 <= bill[i] <= 10^4
- 0 <= b <= bill[i]

Output Format

If Brian did not overcharge Anna, print "Bon Appetit" on a new line; otherwise, print the difference between what Anna paid and what she actually owed.

Sample Input 0

4 1
3 10 2 9
12

Sample Output 0

5

Explanation 0

Anna didn't eat item bill[1] = 10, but she paid 12. The actual fair share is (3 + 2 + 9)/2 = 7.  
Brian charged her 12, so the difference is 12 - 7 = 5.  
You should print 5.

Sample Input 1

4 1
3 10 2 9
7

Sample Output 1

Bon Appetit

Explanation 1

Anna didn't eat item 10, and she paid 7. That's exactly what she should have paid.
"""

def bonAppetit(bill, k, b):

    cons = 2<=len(bill)<=1e5 and 0<=k<=len(bill) and 0<=all(cost for cost in bill)<=1e4 and 0<=b<=sum(bill)
    if cons:
        tmp = bill
        tmp = tmp[0:k] + tmp[k+1:]
        split = sum(tmp)//2
        if split ==b:
            return print("\nBon Appetit")
        else:
            return int((b-split)))
            print(split)
    

bill = [3, 10, 2 ,9]
bonAppetit(bill, 1,12)