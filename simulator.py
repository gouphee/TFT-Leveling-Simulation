# Initial premise:
#   Level 3, 8 gold on 2-1
#   level only if above 50 gold
#   goal is to hit level 8
#   initial goal gold is level 8 + 20 = 128 gold

# strong assumptions
#   dont care about buying units
#   unlimited health

# initial variables
#   number of rounds
#   total streak
#   win?
#   total gold
#   goal gold

def simulation(rounds, streak, win, gold, goal, results):
    # streak gold is calculated as so.
    #   streak = 0 → 0
    #   streak = 1 → +1
    #   4 > streak > 1 → +2
    #   streak = 4 → +3
    #   streak > 5 → +4

    streak_gold = 0 # depending on your streak, you'll get bonus gold

    if streak == 0:
        streak_gold = 0
    elif streak == 1:
        streak_gold = 1
    elif streak == 2 or streak == 3:
        streak_gold = 2
    elif streak == 4:
        streak_gold = 3
    elif streak >= 5:
        streak_gold = 4

    interest = min(gold // 10, 5) # interest gold is at most 5 or your gold/10, so we take the minimum

    gold += (streak_gold + interest)

    if rounds % 2 == 0 and rounds > 0: # every 2 rounds after 2-1, you get 4 xp in total, decreasing the gold you need to hit level 8
        goal -= 4

    # Passive Income from TFT Wiki, I think it's outdated

    # if rounds == 0:
    #     gold += 2
    # elif rounds == 6:
    #     gold += 2
    # elif rounds == 12:
    #     gold += 3
    # elif rounds == 18:
    #     print(rounds)
    #     gold += 4
    # else:
    #     gold += 5

    # Passive income from MetaTFT
    if rounds == 0: # if it is the first round (2-1) you only get 4 gold. otherwise you get 5.
        gold += 4
    else:
        gold += 5

    if win and rounds % 6 != 0: # if you won the round, and it wasn't a creep round before, get a win gold
        gold += 1


    if gold >= goal: # if conditions are fulfilled, add number of rounds and gold left to results array. Can add more interesting data instead here.
        print(rounds, streak, win, gold, goal)
        results.append((rounds, gold-goal + 20))
    elif rounds % 6 == 5: # if it's a creep round, keep streak and type of streak, but don't add to it.
        simulation(rounds + 1, streak, win, gold, goal, results)
    else: # on normal rounds, we recursively call the function again, but with a continued streak and a change in streak.
        simulation(rounds + 1, 1, not win, gold, goal, results)
        simulation(rounds + 1, streak + 1, win, gold, goal, results)
        

