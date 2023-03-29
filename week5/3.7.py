from scipy.stats import norm

mu = 60
sigma = 3
x = [7, 24, 38, 24, 7]

y = [norm.ppf(sum(x[0:i+1]) / sum(x), mu, sigma) for i in range(len(x) - 1)]

z = [sum(x[0:i+1]) / sum(x) for i in range(len(x) - 1)]

print(y)
print(z)
