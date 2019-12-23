# AI-Utility-Based-Markov-Decision-Process
By using of utility approach for path finding in AI, the script prints the optimal states to follow with arrows UP, DOWN, RIGHT or LEFT.

| is wall, . is empty space, +1 positive reward and -1 negative reward

Map Matrix

[
            [".",   ".",    ".",    ".",    "+1"],
            [".",   ".",    ".",    ".",    "-1"],
            [".",   "|",    ".",    ".",    "."],
            [".",   ".",    ".",    ".",    "."]
]

getUtilityCalculatedMap()

Output is like for given map matrix


printArrowMap()
RIGHT RIGHT RIGHT RIGHT +1 
RIGHT RIGHT UP UP -1 
UP | UP UP DOWN 
UP RIGHT UP UP DOWN 

printUtilityMap()
0.3210 0.4388 0.5860 0.7700 1.0000 
0.3251 0.4038 0.4874 0.4860 -1.0000 
0.2301 0.0000 0.3955 0.3558 -0.0300 
0.1760 0.2193 0.3116 0.2516 -0.0300 
