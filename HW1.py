# Exercise 1a-f
import string
alphabet = string.ascii_letters
sentence = "Jim quickly realized that the beautiful gowns are expensive"
count_letters = {}
for letter in sentence:
    if letter.isalpha():
        if letter in count_letters.keys():
		          count_letters[letter] += 1
        else:
		          count_letters[letter] = 1
address = """Four score and seven years ago our fathers brought forth on this continent, a new nation,
conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a
great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure.
We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final
resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper
that we should do this. But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow --
this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add
or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here.
It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so
nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored
dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here
highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of
freedom -- and that government of the people, by the people, for the people, shall not perish from the earth."""
#address_count = count_letters(address)

# Exercise 2a-f
import random
random.seed(1)
def rand():
    return random.uniform(-1, 1)
rand()

import math
def distance(x, y):
    x1 = x[0]
    x2 = x[1]
    y1 = y[0]
    y2 = y[1]
    distance = math.sqrt(((y1 - x1)**2) + ((y2 - x2)**2))
    return distance
def in_circle(x, origin = [0,0]):
    if distance(x, origin) < 1:
        return True
    else:
        return False

R = 10000
x = []
inside = []
for i in range(R):
	point = [rand(), rand()]
	x.append(point)
for j in x:
	if in_circle(j):
            inside.append(j)
estimate = len(inside) / R
print((math.pi / 4) - estimate)

# Exercise 3a-c
random.seed(1)
R = 1000
x = []
def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors * 2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    return [sum(x[i:(i+width)]) / width for i in range(n)]
for i in range(R):
    x.append(random.uniform(0,1))
Y = [x] + [moving_window_average(x, n_neighbors) for n_neighbors in range(1, 10)]
print(moving_window_average(x, n_neighbors=5))
