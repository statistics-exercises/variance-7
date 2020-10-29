# Converging the sample variance

Let's do one final exercise with the sample variance computed using:

![](https://render.githubusercontent.com/render/math?math=S^2=\frac{n}{n-1}\left[\left(\frac{1}{n}\sum_{i=1}^{n}X_i^2\right)-\overline{X}^2\right])

Let's look at how this quantity depends on the number of random variables that it is computed from.  __To complete the exercise you need to generate a graph that shows how the estimate of the sample variance for a uniform random variable that lies between 0 and 1 depends on the number of random variables it is computed from.__   I have written some code to get you started with the exercise.  To complete the task you need to:

1. Set the first element of the array called `indices` equal to 2, the second element of the array called `indices` to 3 and so on.  (Notice that the sample variance with n=1 is not defined as if n=1 the n-1 in the denominator is 0 and the numerator is similarly zero).

2. Set the first element of the array called `S2` equal to a sample variance computed using the above formula with n=2, the second element of this list to a sample variance computed using the above formula with n=3 and so up until you have computed the formula above with n=201.

When your code is complete a graph showing the value of ![](https://render.githubusercontent.com/render/math?math=S^2) as a function of n will be generated.
