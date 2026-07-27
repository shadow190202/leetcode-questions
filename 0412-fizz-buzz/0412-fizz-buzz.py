class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        li = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                i = "FizzBuzz"
                li.append(i)
            elif i % 3 == 0 :
                i = "Fizz"
                li.append(i)
            elif i % 5 == 0:
                i = "Buzz"
                li.append(i)
            else:
                li.append(str(i))
        return li
