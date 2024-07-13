# Time:  O(1)
# Space: O(1)

class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 1. if we get an even, we can choose x = 1
        #    to make the opponent always get an odd
        # 2. if the opponent gets an odd, he can only choose x = 1 or other odds
        #    and we can still get an even
        # 3. at the end, the opponent can only choose x = 1 and we win
        # 4. in summary, we win if only if we get an even and 
        #    keeps even until the opponent loses
        return n % 2 == 0


# Time:  O(n^3/2)
# Space: O(n)
# dp solution
class Solution2(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def memoization(n, dp):
            if n not in dp:
                result = False
                for i in xrange(1, n):
                    if i*i > n:
                        break
                    if n % i:
                        continue
                    if i != n and not memoization(n-i, dp):
                        result = True
                        break
                    j = n // i
                    if j == i:
                        continue
                    if j != n and not memoization(n-j, dp):
                        result = True
                        break
                dp[n] = result
            return dp[n]
        
        return memoization(n, {})
