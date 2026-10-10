class Solution:
    def isValid(self, s: str) -> bool:
        l1 = []
        for i in s:
            if(i in ('(','{','[')):
                l1.append(i)
            elif(i in (')','}',']') and len(l1)!=0):
                if (i == ')'):
                    if (l1[-1]=='('):
                        l1.pop()
                    else:
                        return False
                elif (i == '}'):
                    if (l1[-1]=='{'):
                        l1.pop()
                    else:
                        return False
                elif (i == ']'):
                    if (l1[-1]=='['):
                        l1.pop()
                    else:
                        return False
                else:
                    l1.append(i)
            else:
              return False
        
        if (len(l1)==0 and len(s)>1):
            return True
        else:
            return False
        