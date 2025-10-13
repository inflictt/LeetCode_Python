class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a,b=int(a,2),int(b,2)#started converting a and b into integer and wrt base 2
        while b:#thiss is b or we can call it carry is there till then it will run
            w_c=a^b#xor part where if 1^1=0 same for 0^0 and 0^1 is 1
            carry=(a&b)<<1#here first tkaing and opr with a and b and after that elft shifting 1 place 
            a,b=w_c,carry
        return bin(a)[2:]#converting back and there comes some 2 char unwanteed so to slice that we did [2:]