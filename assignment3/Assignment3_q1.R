#Ques1:
  
#  Calculate the coefficient of covariance for the following data:
  
# X	2	8	 18	20	28	30
# Y	5	12 18	23	45	50

# So calculate Covariance using Python ,R and Formula.

v1 = c(2, 8, 18, 20, 28, 30)
v2 = c(5, 12, 18, 23, 45, 50)
covariance = cov(v1, v2)
print(covariance)


correlation = cor(v1, v2)
print(correlation)