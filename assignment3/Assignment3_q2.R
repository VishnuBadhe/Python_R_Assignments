# Q.No.2 Daily Closing Prices of Two Stocks arranged as per returns. So calculate Covariance using R,Python and Formula.

# x: 1.8 , 1.5, 2.1 , 2.4 , 0.2
# y: 2.5 , 4.3 , 4.5 , 4.1 ,2.2

v1 = c(1.8, 1.5, 2.1, 2.4, 0.2)
v2 = c(2.5, 4.3, 4.5, 4.1, 2.2)
covariance = cov(v1,v2)
print(covariance)


correlation = cor(v1,v2)
print(correlation)
