from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        print("max profit")
        buying_day = 0
        profit = 0
        total_days = len(prices) - 1
        while buying_day <= total_days - 1:
            selling_day = buying_day + 1
            print("buying and selling days " + str(buying_day) + " " + str(selling_day))
            if prices[buying_day] < prices[selling_day]:
                print("bought share on " + str(buying_day))
                buying_price = prices[buying_day]
                temp_high = prices[selling_day]
                selling_day += 1
                while selling_day <= total_days:
                    if temp_high > prices[selling_day]:
                        print("selling my share on " + str(selling_day - 1))
                        profit += temp_high - buying_price
                        print("proft is " + str(profit))
                        buying_day = selling_day
                        print("new buying day " + str(buying_day))
                        break
                    else:
                        temp_high = prices[selling_day]
                        selling_day += 1
                if selling_day > total_days:
                    profit += temp_high - buying_price
                    break
            else:
                buying_day += 1
        return profit


def main():
    arr = [7, 1, 5, 3, 6, 4]
    # arr = [1, 2, 3, 4, 5]
    # arr = [7, 6, 4, 3, 1]
    # arr = [1,2]
    obj = Solution()
    print(obj.maxProfit(arr))


if __name__ == "__main__":
    main()