import math
import random
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

random.seed(None)

def gen_random_circle():
    x = random.random()*100
    y = random.random()*100
    r = random.randint(3,8)
    # cite this line from free code camp
    return Circle((x,y),r, color='black'),x,y

fig,ax = plt.subplots()

start = (random.random()*100,random.random()*100)
end = (random.random()*100, random.random()*100)
plt.plot(start[0],start[1],'ro')
plt.plot(end[0],end[1],'go')

for i in range(0,35):
    circle = gen_random_circle()
    if(math.sqrt((start[0] - circle[1])**2 + (start[1] - circle[2])**2) < circle[0].get_radius()):
        circle = gen_random_circle()
    if(math.sqrt((end[0] - circle[1])**2 + (end[1] - circle[2])**2) < circle[0].get_radius()):
        circle = gen_random_circle()
    else:
        ax.add_patch(circle[0])
ax.autoscale()
plt.show()


