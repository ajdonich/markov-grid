## Project: markov-grid

This is a small study of Markov Decision Processes, based on this [Udacity Course Grid World Game](https://classroom.udacity.com/courses/ud600/lessons/4100878601/concepts/6382590580923). The [markov_game.py](https://github.com/ajdonich/markov-grid/blob/master/markov_game.py) script attempts to use the Bellman Equation to generate an optimal playing policy. 
  
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

This example execution successively decrements the reward (from 0.0 to -20.0) of the negative absorbing sink in the game and prints full status whenever a new/different policy is generated. Note: the Udacity Course uses the value of -1.0 for the sink; otherwise I use the identical values the class specifies, however, I never converge precisely to the class's claimed [Optimal Policy](https://classroom.udacity.com/courses/ud600/lessons/4100878601/concepts/6512308690923), which, after this study, I suspect is at least partly erroneous, at least for state (2,3), which I believe logically (and as my study concluded) should map to action: DOWN to ensure avoidance of the negative sink. 

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
| ↑ | ← | ↑ | ↓ |
----------------

V(s) Grid:
['0.009', '0.126', '0.382', '1.000']
['-0.041', '0.000', '0.066', '-1.000']
['-0.063', '-0.072', '-0.073', '-0.076']

 s    :    UP        DOWN      LEFT     RIGHT   :  MAX(V)
------------------------------------------------------------
(0,0) : ['-0.030', '-0.050', '-0.038', '0.009'] : RIGHT (0.009)
(0,1) : ['0.030', '0.030', '-0.024', '0.126'] : RIGHT (0.126)
(0,2) : ['0.169', '0.043', '0.033', '0.382'] : RIGHT (0.382)
(0,3) : ABSORBED
(1,0) : ['-0.041', '-0.069', '-0.059', '-0.059'] : UP (-0.041)
(1,1) : N/A (UNREACHABLE)
(1,2) : ['0.066', '-0.116', '0.002', '-0.425'] : UP (0.066)
(1,3) : ABSORBED
(2,0) : ['-0.063', '-0.072', '-0.070', '-0.074'] : UP (-0.063)
(2,1) : ['-0.076', '-0.076', '-0.072', '-0.076'] : LEFT (-0.072)
(2,2) : ['-0.021', '-0.076', '-0.069', '-0.071'] : UP (-0.021)
(2,3) : ['-0.447', '-0.078', '-0.123', '-0.124'] : DOWN (-0.078)

Neg sink reward: -2.0

Policy Grid:
----------------
| → | → | → | + |
----------------
| ↑ | X | ↑ | - |
----------------
| ↑ | → | ↑ | ↓ |
----------------

V(s) Grid:
['0.008', '0.124', '0.380', '1.000']
['-0.041', '0.000', '0.012', '-2.000']
['-0.063', '-0.063', '-0.042', '-0.077']

 s    :    UP        DOWN      LEFT     RIGHT   :  MAX(V)
------------------------------------------------------------
(0,0) : ['-0.030', '-0.050', '-0.038', '0.008'] : RIGHT (0.008)
(0,1) : ['0.029', '0.029', '-0.024', '0.124'] : RIGHT (0.124)
(0,2) : ['0.168', '0.021', '0.029', '0.380'] : RIGHT (0.380)
(0,3) : ABSORBED
(1,0) : ['-0.041', '-0.069', '-0.059', '-0.059'] : UP (-0.041)
(1,1) : N/A (UNREACHABLE)
(1,2) : ['0.012', '-0.156', '-0.018', '-0.823'] : UP (0.012)
(1,3) : ABSORBED
(2,0) : ['-0.063', '-0.071', '-0.070', '-0.070'] : UP (-0.063)
(2,1) : ['-0.070', '-0.070', '-0.071', '-0.063'] : RIGHT (-0.063)
(2,2) : ['-0.042', '-0.064', '-0.067', '-0.072'] : UP (-0.042)
(2,3) : ['-0.846', '-0.077', '-0.161', '-0.174'] : DOWN (-0.077)

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

```