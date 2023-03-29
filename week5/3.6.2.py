from scipy.stats import norm

mu = 270
sigma = 10
x = 250

p = norm.cdf(x, mu, sigma)
print(p)