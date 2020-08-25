## Project: markov-grid

This is a small study of Markov Decision Processes, based on this [Udacity Course Grid World Game](https://classroom.udacity.com/courses/ud600/lessons/4100878601/concepts/6382590580923). (The course is excellent so far, btw. I understand  nuances of RL and the Bellman Equations much better already). My [markov_game.py](https://github.com/ajdonich/markov-grid/blob/master/markov_game.py) script attempts to learn the grid's optimal playing policy using the Bellman Equation:  

![Bellman Equation](https://github.com/ajdonich/markov-grid/blob/master/media/BellmanEq_V.jpg)  
![MDP Grid World](https://github.com/ajdonich/markov-grid/blob/master/media/mdp_grid_world.jpg)  
  
___

### Installation:

The study was developed with python 3.7 and depends only on the numpy package.

```
$ git clone https://github.com/ajdonich/markov-grid.git
$ cd markov-grid
$ pip install -r requirements.txt 
```
  
___


### Execution:

The example execution below successively decrements (from 0.0 to -20.0) the negative reward of the absorbing sink at (1,3) and prints status whenever a new/different optimal policy is learned. Note: the Udacity Course uses the value of -1.0 for the sink; otherwise I use identical values to those specified in the course, however, I never converge precisely to the class's claimed [Optimal Policy](https://classroom.udacity.com/courses/ud600/lessons/4100878601/concepts/6512308690923). Either I am in error somehow, or the course it, but for example, at state (2,3), it seems logical (and as my study concludes) that DOWN is the optimal action, thus ensuring avoidance of the negative sink at (1,3). 

```
$python3 markov_game.py 
Neg sink reward: -0.0
Policy Grid:
----------------
| → | → | → | + |
----------------
| ↑ | X | ↑ | - |
----------------
| ↑ | → | ↑ | ← |
----------------

V(s) Grid:
['0.009', '0.127', '0.385', '1.000']
['-0.040', '0.000', '0.120', '-0.000']
['-0.061', '-0.043', '0.004', '-0.040']

 s    :    UP        DOWN      LEFT     RIGHT   :  MAX(V)
------------------------------------------------------------
(0,0) : ['-0.030', '-0.049', '-0.038', '0.009'] : RIGHT (0.009)
(0,1) : ['0.030', '0.030', '-0.024', '0.127'] : RIGHT (0.127)
(0,2) : ['0.170', '0.064', '0.036', '0.385'] : RIGHT (0.385)
(0,3) : ABSORBED
(1,0) : ['-0.040', '-0.069', '-0.059', '-0.059'] : UP (-0.040)
(1,1) : N/A (UNREACHABLE)
(1,2) : ['0.120', '-0.032', '0.028', '-0.021'] : UP (0.120)
(1,3) : ABSORBED
(2,0) : ['-0.061', '-0.070', '-0.070', '-0.062'] : UP (-0.061)
(2,1) : ['-0.060', '-0.060', '-0.069', '-0.043'] : RIGHT (-0.043)
(2,2) : ['0.004', '-0.043', '-0.051', '-0.050'] : UP (0.004)
(2,3) : ['-0.042', '-0.058', '-0.040', '-0.058'] : LEFT (-0.040)

Neg sink reward: -1.0
Policy Grid:
----------------
| → | → | → | + |
----------------
| ↑ | X | ↑ | - |
----------------
| ↑ | → | ↑ | ↓ |
----------------

V(s) Grid:
['0.009', '0.126', '0.382', '1.000']
['-0.041', '0.000', '0.066', '-1.000']
['-0.062', '-0.053', '-0.020', '-0.075']

 s    :    UP        DOWN      LEFT     RIGHT   :  MAX(V)
------------------------------------------------------------
(0,0) : ['-0.030', '-0.050', '-0.038', '0.009'] : RIGHT (0.009)
(0,1) : ['0.030', '0.030', '-0.024', '0.126'] : RIGHT (0.126)
(0,2) : ['0.169', '0.043', '0.033', '0.382'] : RIGHT (0.382)
(0,3) : ABSORBED
(1,0) : ['-0.041', '-0.069', '-0.059', '-0.059'] : UP (-0.041)
(1,1) : N/A (UNREACHABLE)
(1,2) : ['0.066', '-0.095', '0.005', '-0.422'] : UP (0.066)
(1,3) : ABSORBED
(2,0) : ['-0.062', '-0.071', '-0.070', '-0.066'] : UP (-0.062)
(2,1) : ['-0.065', '-0.065', '-0.070', '-0.053'] : RIGHT (-0.053)
(2,2) : ['-0.020', '-0.054', '-0.059', '-0.067'] : UP (-0.020)
(2,3) : ['-0.445', '-0.075', '-0.102', '-0.124'] : DOWN (-0.075)

Neg sink reward: -2.0
Neg sink reward: -3.0
Policy Grid:
----------------
| → | → | → | + |
----------------
| ↑ | X | ← | - |
----------------
| ↑ | ← | ↑ | ↓ |
----------------

V(s) Grid:
['0.008', '0.123', '0.377', '1.000']
['-0.041', '0.000', '-0.041', '-3.000']
['-0.063', '-0.073', '-0.064', '-0.079']

 s    :    UP        DOWN      LEFT     RIGHT   :  MAX(V)
------------------------------------------------------------
(0,0) : ['-0.030', '-0.050', '-0.039', '0.008'] : RIGHT (0.008)
(0,1) : ['0.028', '0.028', '-0.025', '0.123'] : RIGHT (0.123)
(0,2) : ['0.167', '-0.000', '0.026', '0.377'] : RIGHT (0.377)
(0,3) : ABSORBED
(1,0) : ['-0.041', '-0.069', '-0.059', '-0.059'] : UP (-0.041)
(1,1) : N/A (UNREACHABLE)
(1,2) : ['-0.041', '-0.218', '-0.041', '-1.224'] : LEFT (-0.041)
(1,3) : ABSORBED
(2,0) : ['-0.063', '-0.072', '-0.071', '-0.074'] : UP (-0.063)
(2,1) : ['-0.075', '-0.075', '-0.073', '-0.073'] : LEFT (-0.073)
(2,2) : ['-0.064', '-0.073', '-0.074', '-0.077'] : UP (-0.064)
(2,3) : ['-1.247', '-0.079', '-0.219', '-0.225'] : DOWN (-0.079)

Neg sink reward: -4.0
Neg sink reward: -5.0
Neg sink reward: -6.0
Neg sink reward: -7.0
Neg sink reward: -8.0
Neg sink reward: -9.0
Neg sink reward: -10.0
Neg sink reward: -11.0
Neg sink reward: -12.0
Neg sink reward: -13.0
Neg sink reward: -14.0
Neg sink reward: -15.0
Neg sink reward: -16.0
Neg sink reward: -17.0
Neg sink reward: -18.0
Neg sink reward: -19.0
Neg sink reward: -20.0

```