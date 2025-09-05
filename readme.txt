**************************************************
*               Terell Johnson                   *
*               16 March 2025                    * 
*            Artificial Intelligence              * 
*      Assignment Three: Genetic Algorithms      *
**************************************************


--------------------------------
-         Assumptions          -
--------------------------------
Number of Generations:
        One major assumption is that 100 generations is enough to find an optimal
        solution to this problem. This assumption comes after running tests that did
        not find any better solutions than the one that my current implementation finds. 

        I chose to set 100 generations as the max number of generations for simplicity
        while still finding an optimal solution.


Mutation Rate:
        A mutation rate of 10% (0.1) is assumed to be sufficient to find good solutions
        without converging to local optima.


Weight Limits:
        The weight limit is assumed to be strictly enforced in the implementation by 
        adding a small penalty to overweight individuals. 
