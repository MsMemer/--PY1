salary = 5000  
spend = 6000  
months = 10  
increase = 0.03 

need_money = 0  
current_spend = spend
for current_cup in range (1, months + 1):
    current_cup = current_spend - salary
    current_spend = current_spend * (increase + 1)
    need_money += current_cup

print(round(need_money))
