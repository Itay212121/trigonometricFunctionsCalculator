# trigonometricFunctionsCalculator

Using what I have just learned in Calculus, I wanted to practice my skills building this program.
This program can calculate basic trigonometric functions, using Taylor series.

First of all, we know that the Lagrange reminder of any Taylor series is ![image](https://user-images.githubusercontent.com/56035342/163019372-cd4b7eb0-7d5a-40c1-bdbd-95972e94140e.png)

by using the fact that the nth derivative of sin(x) is cos(x)/sin(x)/-cos(x)/-sin(x),  we know that the nth derivative of any c in [0, x] is smaller than 1
Which means:
![image](https://user-images.githubusercontent.com/56035342/163019440-dce9bd1d-5c84-4e29-ad39-7d91c4121200.png)

if we find the minimal n which satisfies the inequality ![image](https://user-images.githubusercontent.com/56035342/163019703-aabc899b-803e-4550-abf6-d09240cabe68.png)
we can say that that the Lagrange remainder is smaller than the accuracy as well, which means the found n is the minimal one
then, once we find the minimal n, we calculate the Taylor polynomial of the found n, and its the answer.
