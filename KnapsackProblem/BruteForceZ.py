def knapsack_bruteforce(values, weights, capacity):
    n = len(values)
    max_value = 0
    best_subset = []

    #Brute force means try everything. Try all subsets of items. (2^n subsets)
    for mask in range(1 << n):
        total_weight = 0
        total_value = 0
        subset = []

        for i in range(n):
            if mask & (1 << i):
                total_weight += weights[i]
                total_value += values[i]
                subset.append(i)

        if total_weight <= capacity and total_value > max_value:
            max_value = total_value
            best_subset = subset
    return max_value, best_subset


# Example usage:
n = int (input("Enter number of items: "))

value = []
weights = []

print ("\n Enter value and weight of each item: ")

for i in range(n):
    v = int(input(f"Value of item {i+1}: "))
    w = int(input(f"Weight of item {i+1}: "))
    value.append(v)
    weights.append(w)

capacity = int(input("\nEnter capacity of knapsack: "))

#Solve using brute force 
max_value, subset = knapsack_bruteforce(value, weights, capacity)

print("\n --- Result ---")
print(f"\nMaximum value in Knapsack = {max_value}")
print("Items included (0-indexed):", subset)