def get_max_profit(stock_prices):
    currentMin = stock_prices[0]
    result = stock_prices[1] - stock_prices[0]
    for i in range(1, len(stock_prices)):
        if stock_prices[i] < currentMin:
            currentMin = stock_prices[i]
        else:
            result = max(result, stock_prices[i] - currentMin)
    
    return result

# Alternative solution
def solution(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for current_time in range(1, len(stock_prices)):
        current_price = stock_prices[current_time]

        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit)

        min_price = min(min_price, current_price)
    
    return max_profit

def main():
    stock_prices = [3, 7, 5, 8, 11, 9, 5, 20, 3]
    sp = [7,1,5,3,6,4]
    neg = [5,4,3,2,1]
    # print(get_max_profit(sp))
    print(get_max_profit(sp))

main()