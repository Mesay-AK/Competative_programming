class Solution(object):
  def isAnagram(self, s, t):
      """
      :type s: str
      :type t: str
      :rtype: bool
      """
      dictT={}
      dictS={}
      if len(s) != len(t):
          return False
      for i in range(len(t)):
          if s[i] in dictS :
              dictS[s[i]]= 1 + dictS[s[i]]
          else:
              dictS[s[i]]= 1

          if t[i] in dictT :
              dictT[t[i]]= 1 + dictT[t[i]]
          else:
              dictT[t[i]]= 1 
      # return dictS, dictT
      for i in range(len(s)):
          if s[i] not in dictT:
              return False
          if dictS[s[i]] != dictT[s[i]]:
              return False
      return True
