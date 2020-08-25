import copy
import numpy as np
from itertools import product

class BoardMDP:
#{
    GAMMA = 0.5 # Discount rate
    REWARD_POS_SINK = 1.0
    REWARD_NEG_SINK = -1.0
    REWARD_DEFAULT = -0.04

    ACTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    ARROWS = ['↑', '↓','←', '→']

    # Note: game tested only using a 3x4 board
    def __init__(self, h=3, w=4):
        self.w, self.h = w, h        
        self.absorbs = {(0,3),(1,3)}
        self.blocks = {(1,1)}
        self.gamma = BoardMDP.GAMMA
        
        self.V = [[0.0] * w for _ in range(h)]
        self.V[0][3]= BoardMDP.REWARD_POS_SINK
        self.V[1][3] = BoardMDP.REWARD_NEG_SINK
        
        self.R = [[BoardMDP.REWARD_DEFAULT] * w for _ in range(h)]
        self.R[0][3] = BoardMDP.REWARD_POS_SINK
        self.R[1][3] = BoardMDP.REWARD_NEG_SINK
    
    
    #################################################################################
    # ------------------------ Just output/printing routines ------------------------
    
    def policygrid(self):
        polgrid = [[''] * self.w for _ in range(self.h)]
        for x,y in product(range(self.h), range(self.w)):
            if (x,y) in self.blocks: polgrid[x][y] = 'X'
            elif (x,y) == (0,3): polgrid[x][y] = '+'
            elif (x,y) == (1,3): polgrid[x][y] = '-'
            else:
                sprimes = self.nxtstates((x,y))
                expectutils = [sum([Tprob * self.V[xp][yp] for Tprob, (xp,yp) 
                    in zip(self.Tprobs(a), sprimes)]) for a in BoardMDP.ACTIONS]
                polgrid[x][y] = BoardMDP.ARROWS[np.argmax(expectutils)]
        
        return polgrid
    
    def print_policies(self, polgrid):
        grid = ("----------------\n"
                "| {} | {} | {} | {} |\n"
                "----------------\n"
                "| {} | {} | {} | {} |\n"
                "----------------\n"
                "| {} | {} | {} | {} |\n"
                "----------------").format(
            *[a for row in polgrid for a in row ])
        print('Policy Grid:')
        print(grid); print()
    
    def print_vgrid(self):
        print('V(s) Grid:')
        for row in self.V:
            print([f'{v:.3f}' for v in row])
        print()
    
    def print_vtable(self):
    #{
        self.print_vgrid()
        print(' s    :    UP        DOWN      LEFT     RIGHT   :  MAX(V)')
        print('------------------------------------------------------------')

        for x,y in product(range(self.h), range(self.w)):
            if (x,y) in self.absorbs: print(f'({x},{y}) : ABSORBED')
            elif (x,y) in self.blocks:  print(f'({x},{y}) : N/A (UNREACHABLE)')
            else:
                Eutils = self.expectutils(self.nxtstates((x,y)))
                utilities = [self.R[x][y] + self.gamma*eua for eua in Eutils]
                print(f'({x},{y}) :', [f'{u:.3f}' for u in utilities], ':', 
                      BoardMDP.ACTIONS[np.argmax(utilities)], f'({max(utilities):.3f})')
        print()
    #}
    
    # ------------------------ End output/printing routines ------------------------
    ################################################################################


    # Policy maps state -> action (returns action with highest expected 
    # utility value w/respect to self.V or None if s is absorbing state)
    def policy(self, s):
        if s in self.absorbs: return None
        assert s not in self.blocks, f"ERROR: unreachable/blocked state: {s}"        
        return BoardMDP.ACTIONS[np.argmax(self.expectutils(self.nxtstates(s)))]
    
    # Given current state, returns the four (unweighted) possible
    # next states s', ordered: [UP, DOWN, LEFT, RIGHT], accounting
    # for actions that 'collide w/a wall' => then returned s' == s
    def nxtstates(self, s):
        if s in self.absorbs: return [s] * 4
        return[s if sp in self.blocks else sp 
               for sp in [(max(0, s[0]-1), s[1]), 
                          (min(s[0]+1, self.h-1), s[1]),
                          (s[0], max(0, s[1]-1)), 
                          (s[0], min(s[1]+1, self.w-1))]]
    
    # Returns transition probs ordered: [UP, DOWN, LEFT, RIGHT].
    # Rule: chosen action occurs accurately w/prob 0.8, and at 
    # right angle to the action w/prob 0.2 (evenly divided L/R)
    def Tprobs(self, a):
        if a == 'UP':      return [0.8, 0.0, 0.1, 0.1]
        elif a == 'DOWN':  return [0.0, 0.8, 0.1, 0.1]
        elif a == 'LEFT':  return [0.1, 0.1, 0.8, 0.0]
        elif a == 'RIGHT': return [0.1, 0.1, 0.0, 0.8]
        else: assert False, f"ERROR, invalid actions {a}"
    
    # Returns list for all actions ordered: [UP, DOWN, LEFT, RIGHT],
    # of SUM over s' ( T(s,a,s')*V(s') ), a piece of the Bellman Eq.
    def expectutils(self, sprimes):
        return [sum([Tprob * self.V[xp][yp] for Tprob, (xp,yp) 
            in zip(self.Tprobs(a), sprimes)]) for a in BoardMDP.ACTIONS]
    
    # Iterates through ngames, each starting at state s0 and ending
    # at one of the absorbing states. Updates self.V after each move.
    # With the 3x4 grid, empirically, 1000 games is plenty to converge.
    def learn_pvalues(self, s0=(2,0), ngames=1000, debug=0):
    #{
        lpol = None
        if debug > 0:
            print("Initial ")
            lpol = self.policygrid()
            self.print_policies(lpol)
        
        for i in range(ngames):
            self._play_game(s0)
            
            if debug > 0:
                pol = self.policygrid()
                if pol != lpol:
                    print(f"\nPolicy change {i+1}:")
                    self.print_policies(pol)
                    if debug > 1: self.print_vtable()
                lpol = pol
    #}
    
    # Recurse through a full game of moves following latest optimal policy (and 
    # stochastic randomness of transition probs). Updates self.V after each move.
    def _play_game(self, s):
        a = self.policy(s)
        if a is not None:
            sprimes = self.nxtstates(s)
            Eutils = self.expectutils(sprimes)
            self.V[s[0]][s[1]] = self.R[s[0]][s[1]] + self.gamma*max(Eutils)                        
            self._play_game(s=sprimes[np.random.choice([0,1,2,3], p=self.Tprobs(a))])
#}


if __name__ == '__main__':
#{
    # Successively decrement the reward of the negative sink
    # and print full status whenever a new policy is generated
    
    prevpol = None
    for negsink in range(21):
        BoardMDP.REWARD_NEG_SINK = -float(negsink)

        game = BoardMDP()
        game.learn_pvalues(debug=0)

        pol = game.policygrid()
        if prevpol is None or pol != prevpol:
            print(f"Neg sink reward: {BoardMDP.REWARD_NEG_SINK}\n")
            game.print_policies(pol)
            game.print_vtable()
            prevpol = pol
#}