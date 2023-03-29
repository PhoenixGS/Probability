from scipy.stats import norm

mu = 270
sigma = 10
x = 300

p = 1 - norm.cdf(x, mu, sigma)
print(p)