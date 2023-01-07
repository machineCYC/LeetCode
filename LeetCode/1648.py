inventory = [2,8,4,10,6]
orders = 20

# inventory = [1000000000]
# orders = 1000000000

inv.sort(reverse=True)
inv.append(0)
ans, ind, width=0,0,0

while orders > 0:

    max_nbr = s_inventory.pop()
    s_inventory.append(max_nbr - 1)
    s_inventory = sorted(s_inventory)
    values += (max_nbr % (10**9 + 7))
    orders -= 1
    if orders == 0:
        ans = values % (10**9 + 7)
        print(ans)
        break