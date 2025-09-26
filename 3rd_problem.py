from matplotlib.pylab import *



t=[0.01,0.5,0.9999]
v=[1.0005,1.155,70.71]
plot(t,v)
scatter(t,v)
xlabel("v/c($\\beta$)")
ylabel("Lifetime")
title("Relation between velocity and lifetime of moving particle")
show()
