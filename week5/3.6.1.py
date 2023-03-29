from scipy.stats import norm

mu = 270
sigma = 10
l = 260
r = 280

p = norm.cdf(r, mu, sigma) - norm.cdf(l, mu, sigma)
print(p)