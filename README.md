# TFT-Leveling-Simulation
Simulating average round you can level up to level 8 in TFT

Initial Premise:
- Level 3, 8 gold before gold is given on 2-1
- Initial goal is to hit level 8 with 20 gold to roll -> 128 total gold

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
