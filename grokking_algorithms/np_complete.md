# NP - Complete 
> NP = NonDeterministic polynomial 


NP problems are, in short, hard. They can't be solved perfectly and instead rely on approximate solutions. This means we can get very close to optimal but can never really prove that it is indeed optimal. 

Why? Well, it comes down to the factorial nature of the set of combinations. What? By that I mean we have a set of combinations that are factorial in their arrangment. So image we have 5 cities. This means that if we wanted to find the optimal solution from the start city to the end city we would have to consider the 5! combinations. As it turns out. This is easy for small numbers of n. But as the number goes up, then the ability to complete this calculation becomes impossible. Of course, it is theoretically possible, however, it is not practically possible since we don't have enough compute/time to do these calculations. So what to do then?

You'll have to end up going for a greedy solution that promises to do its best, even though that is never quite enough.


