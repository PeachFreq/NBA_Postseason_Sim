# NBA_Postseason_Sim
Simulate the results of the 2018 postseason based on a custom algorithm using 4 years of regular season scoring data.

The reason I'm choosing the 2018 postseason is because I found a great dataset containing all regular season games played during that season as well as the previous 3 seasons. It would be good to find more current data.

As far as as the thinking behind the algorithm, it's current v1 form is just to assign a 'recency bias' as a multiplier to every point scored during a game. These multipliers are 5, 3, 2, 1 (with the largest multiplier hitting the most recent season, and the on the opposite end the 1x multiplier applies to the most distant season, so that ends up counting for the least amount of points). Those numbers were chosen because they're the Fibonacci sequence and that seemed  that a decent starting point.
