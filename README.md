## TowerBuilder24

HackTX 2022 project by Amit Joshi. Given a user-specified tower height, and a set of block height that can be used to make that tower, outputs a sequence of block heights taken from the specified set that when stacked on top of each other, has a height that equals the specified tower height.

## Inspiration

The inspiration is Competitive Programming. I decided to make my own Competitive Programming problem and code a solution for it.

## What it does

Given a user-specified tower height, and a set of block heights that can be used to make that tower (there is no limit on how many times a given block height can be used), outputs a sequence of block heights taken from the specified set that when stacked on top of each other, has a height that equals the specified tower height.  All blocks can be stacked on top of all other blocks (each block is of length and width 1), and  height k. If no such sequence exists, then it outputs "None".

Input:
The first line of input contains h, 1 <= h <= 10^10.  The second line of input contains n.  Where h is the desired height of the tower, and n is the number of specified block heights that will follow.  The next line of input contains n specified block heights,  k_1, k_2, ..., k_n where k_i represents the height of the i^th type of block.  It is guaranteed that h / min(k_i) <= 10^8.

Output:
Any sequence of block heights that when stacked on top of each other, has a height that equals the specified tower height.  If no such sequence exists, then it outputs "None".

## How we built it

I built it using Python and the Command-Line Interface

## Challenges we ran into

None rlly

## Accomplishments that we're proud of

I'm proud of coming up with a solution to the algorithmic problem and also coming up with the problem myself!

## What we learned

I learned how to use Dynamic Programming to solve the problem mentioned above.

## What's next for TowerBuilder24

Nothing
