def weighted_mean(values: list, weights: list) -> float:
	sum_weighted_values = 0
	sum_weights = 0
	for i in range(len(values)):
		for j in range(len(weights)):
			value = values[i]
			weight = weights[i]
			sum_weighted_values += value * weight
			sum_weights += weight
	result = sum_weighted_values / sum_weights
	return result

n=int(input())
x=list(map(int,input().strip().split()))
w=list(map(int,input().strip().split()))
print(round(weighted_mean(x,w),1))