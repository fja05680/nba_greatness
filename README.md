nba_greatness
======

Greatness Rating for NBA players

Observations:
1. Great players tend to lead the league annually in 'primary' categories.
2. Great players tend to lead the league annually in 'secondary' categories.  However, these categories are subordinate to 'primary' categories for the reasons below, and should not carry the same weight as 'primary' categories.
    1. Percentage based 'secondary' categories are susceptible to inclusion of specialty situation players who are non-starters, e.g. a low volume shooter with a high field goal percentage.
    2. Other 'secondary' categories are mere subcategories or combinations of 'primary' categories, e.g. three-point field goals is a subcategory of scoring, and triple-doubles is a combination of 3 primary categories.
3. Great players are made greater by winning team championships.
4. It's more difficult to be a great player when there is more competition.  i.e. BIG fish in a small pond.


Rules:
1. Player is awarded a point each time he leads league annually in one of the 'primary' categories:
    1. scoring
    2. rebounding
    3. assists
    4. steals
    5. blocks
2. Player is awarded 1/2 point each time he leads league annually in one of the 'secondary' categories:
    1. triple-doubles
    2. field goal percentage
    3. free throw percentage
    4. three-point field goals
    5. three-point field goal percentage
3. Player is awarded a point for each team championship, not to exceed the number of points already awarded.
4. Player's points are normalized based on the number of teams in the league during his playing career.

Player's points are calculated as below:
   _subtotal = primary + 0.5 * seondary_
   _total = subtotal + min(championships, subtotal)_
   _normalized = total * median_player_teams / max_teams_
