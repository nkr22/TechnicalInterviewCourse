# /**
#  * Given two strings s and t, return true if t is an anagram of s, and false otherwise. Use a dictionary.
#  * 
#  * An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
#  * typically using all the original letters exactly once.
#  * 
#  * Input: s = "anagram", t = "nagaram"
#  * Output: true
#  * 
#  * Input: s = "rat", t = "car"
#  * Output: false
#  * 
#  * Source: https://leetcode.com/problems/valid-anagram/
#  */

s = 'anagram'
t = 'nagaram'

def isanagram(string1,string2):
    if len(string1)!=len(string2):
        return False
    str1=list(string1) 
    str2=list(string2)

    str1.sort()
    str2.sort()

    if str1 == str2:
        return True

print(isanagram(s,t))