# Leetcode_Problems

1. easy1.py: Two sum
    - Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    - You may assume that each input would have exactly one solution, and you may not use the same element twice.
    - You can return the answer in any order.

2. easy2.py: 
    - You are given a 0-indexed integer array nums.
    - Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.
    - The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].

3. easy3.py: Richest Customer
    - You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
    - A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

4. easy4.py: Fizz Buzz
    - Given an integer n, return a string array answer (1-indexed) where:
        - answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
        - answer[i] == "Fizz" if i is divisible by 3.
        - answer[i] == "Buzz" if i is divisible by 5.
        - answer[i] == i (as a string) if none of the above conditions are true.

5. easy5.py: Number of steps to reduce a number to 0
    - Given an integer num, return the number of steps to reduce it to zero.
    - In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

6. easy6.py: Middle of the linked list
    - Given the head of a singly linked list, return the middle node of the linked list.
    - If there are two middle nodes, return the second middle node.

7. easy7.py: Ransom Note
    - Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
    - Each letter in magazine can only be used once in ransomNote.

8. med1.py: 
    - Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.
    - Recall that:
        - The node of a binary tree is a leaf if and only if it has no children.
        - The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
        - The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.

9. easy8.py: Sum of all subset XOR totals
    - The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.
        - For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
    - Given an array nums, return the sum of all XOR totals for every subset of nums. 
    - Note: Subsets with the same elements should be counted multiple times.
    - An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.