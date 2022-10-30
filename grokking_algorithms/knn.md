# K-Nearest-Neighbours.

Find the neighbours of a point on graph and then take the highest number of the type of neighbour. This shows you what type of element your point is. For example, maybe you have a box of fruit and you have decided that more red and size means it is grapefruit and more yellow and smaller size is orange. So when you get a piece fruit that is in between, how do you tell what it is? First, figure out its nearest neighbours and then whichever turns up the most, maybe orange. That should give you an indication of what type of fruit it is. 


## Classification - feature extraction

Figuring out of what type an element is

## Regression

Predicting a future number based of past events/numbers.

Say you have a database of how many donuts that you sell on each day of the week and the important events that effect the amount of selling. For example, the type of weather, whether a big game is on, if it is the weekend. Then you try to predict the amount of donuts you'll need today by calculating the amount of donuts by using regression. To do this, you find the nearest neighbours after crunching the numbers for today. Then you take the average of how many donuts that you bakes on those days.

## KNN basics
How to figure out the closest neighbours?

Use the Pythagorean formula. It works for any number of n >= 2 

# Normalize data

If you're trying to recommend movies for a new user and you realize that some users are rating movies similarly but not quite the same, what do you do? For example, you have a user who reserves 5s for super good movies but they're usually rating similar to another user who is happy to give out 5s. The solution is to normalize the data so that we move a user's 5s into the range of the other's 4.5s.


# Biasing data

If you want to biase a rating towards an 'expert' then just increase their score by weighting it.

