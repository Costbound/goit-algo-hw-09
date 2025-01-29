def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count
    
    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_count = [{} for _ in range(amount + 1)]
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_count[i] = coin_count[i - coin].copy()
                if coin in coin_count[i]:
                    coin_count[i][coin] += 1
                else:
                    coin_count[i][coin] = 1
    
    return coin_count[amount]

print(find_coins_greedy(113))
print(find_min_coins(113))