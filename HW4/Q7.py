import numpy as np

# Shakespeare's Sonnets:
a = np.array([0.225, 0.262, 0.217, 0.240, 0.230, 0.229, 0.235, 0.217, 0.231, 0.250])

# Marlowe's Sonnets:
b = np.array([0.209, 0.205, 0.196, 0.210, 0.202, 0.207, 0.224, 0.223, 0.220, 0.201])

# Converting to single population
p1h = np.mean(a)
p2h = np.mean(b)

delta = p1h-p2h

vx = (1.0/10)*(np.sum((a-p1h)**2))
vy = (1.0/10)*(np.sum((b-p2h)**2))

se = np.sqrt(vx + vy)

# Applying Wald's Test
W = (p1h - p2h)/se

print p1h, p2h
print vx, vy, se
print W

# Calc p value
p = 2*0.0708
print p

# 95% CI
lower = delta + 1.96*0.016
upper = delta - 1.96*0.016
print upper, lower