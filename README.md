# TFT-Leveling-Simulation
Simulating average round you can level up to level 8 in TFT

Initial Premise:
- Level 3, 6 gold before gold is given on 2-1
- Initial goal is to hit level 8 with 30 gold to roll -> 138 total gold

Strong Assumptions:
- You don't care about buying units, upgrading, or leveling when you are under 50 gold, i.e. gold never decreases
- You have unlimited life to loss streak

Methods:
- At the start of round, passive income, interest, streak gold, and win gold are added to total gold
- If it is an even round, 4 gold is removed from goal gold to simulate one less xp purchase needed
- Recursively call function with continuing increased streak, and losing streak
- If previous round was a PvE round, no win gold
- If current round is PvE round, only call with continued streak and no increase in streak.

Future Implementations:
- ~~Visualization~~
  - WIP as more things are implemented
- ~~Broader range of gold starts~~
- Greater variety of data results, like total wins and losses, and overall round history (ex: WWLWLWWLLL)
- Relax loss assumption by having hard cap on total losses (8?)
- ~~Broader range of goal golds with rationales~~
- Relax assumptions about buying units, upgrading, and leveling
  - If you can level and have 30 remaining gold minimum, you level
  - Actual leveling logic above 50 gold, and level and xp tracking as params
- Implement normalization for simulated outcomes
  - Not sure how/why, but my gut says that the way W/L is simulated isn't correct
  - Obviously, W/L isn't 50/50 but there's something more to it, not sure.

Analysis Roadmap:
- No relaxation -> Fixed start and goal
  - Rounds and Total Gold left for fixed 8g start and fixed 8+20 goal
    - Joint Grid -> Good baseline image to start from
    - Binned Joint Grid -> Not really better than normal joint grid

- First Relaxation -> Ranges for starts and goals
  - Average Round and full table with starts from 5-14g and fixed 8+20 goal
    - Not Visualized, potentially ridge plot
    - Definitely should visualize for rounds
  - Average Round and full table with fixed 8g start and goals from 8+0 to 9+10
    - Not Visualized, potentially ridge plot
  - Average Round with starts from 5-14g and goals from 8+0 to 9+10
    - Surface Plot -> Kinda useful for overall conclusions
  - ADDED SIMULATOR FOR TOTAL GOLD
  - Average Gold and full table with starts from 5-14g and fixed 4-1 end
    - Not Visualized, potentially ridge plot
  - Average Gold with starts from 5-14g and ends from 3-5 to 4-5
    - Surface Plot -> Not really usefull overall for conclusions
  - Potential
    - Average Gold and full table with fixed 8g start and ends from 3-5 to 4-5

- Second Relaxation -> Cap on losses
  - ADDED SIMULATOR FOR CAPPED LOSSES
    - just keep track of losses, and filter later
  - 8 loss cap
    - Rounds and Total Gold left for fixed 8g start and fixed 8+20 goal
    - Rounds and Total Gold left for starts from 5-14g and fixed 8+20 goal
  - Compare first relaxation with 8 loss cap
    - Stacked Round distribution density
    - Ridge plot of round distributions densities, 2 stacked on each other, for different gold starts on y
  - 6-12 losses graph -> SO EXTRA...
    - Ridge plot of round distributions densities for max_losses
    - Ridge plot of round distributions densities, either losses stacked or gold starts stacked, for the other on y -> EXTREMELY EXTRA

- Third Relaxation -> level up with 30 gold
  - ADDED SIMULATOR WITH LOGIC FOR LEVELING WITH 30
  - leveling=True
    - Rounds and Total Gold left for fixed 8g start and fixed 8+20 goal
    - Rounds and Total Gold left for starts from 5-14g and fixed 8+20 goal
  - Compare leveling=True and leveling=False for 8 loss cap
    - Stacked Round distribution
    - Ridge plot of round distributions, 2 stacked on each other, for different gold starts on y

- Fourth Relaxation -> buying and selling headliner
  - ADD SIMULATOR WITH LOGIC FOR BUYING AND SELLING HEADLINER
  - buy=True
    - Rounds and Total Gold left for fixed 8g start and fixed 8+20 goal
    - Rounds and Total Gold left for starts from 5-14g and fixed 8+20 goal
  - Compare buy=True and buy=False and leveling=False for 8 loss cap
    - Stacked Round distribution
    - Ridge plot of round distributions, 3 stacked on each other, for different gold starts on y
  - Branch split on level above 30 logic

- Fifth Relaxation -> implement better simulation of actually buying/selling units