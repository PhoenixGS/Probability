from scipy.stats import norm

mu = 0
sigma = 1
x = 1.645

p = 1 - norm.cdf(x, mu, sigma)
print(p)