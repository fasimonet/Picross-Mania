py 2048, a well know 2048 clone game 
---------------------------------------
Written in Python2.7.4 and Pygame 1.9.1

how to play:
---------------------------
keyboard UP, DOWN, LEFT, RIGHT, escape to quit

increase your score shifting tilds with same number.
the value of resulting tild is multiplied *2.
your score is increased in consequence.

customise your game:
---------------------------
edit py2048.cfg configuration file. you can:
- Change Raws and Columns amount.
- Change Random range value of new tild.
- Limit the maximum tild value.
- Limit time allowed for movement.
- Enable no movement (a new tild appear even if your movement doesn't shift anything).
- Set shift to one step only.
- Save the game state when exit (for autoload at start game)

---------------------------
intermediates beta releases are Vx.y.1-9-a-z
stables releases are Vx.y.0

# V0.0.1
# initial release, single player, ...
#
# V0.1.0:
# add Small, Medium and Large preconfig Panel Game.
# add Hiscore for Small, Medium And Large Panel Game
# check for close windows as QUIT event.
# add Change theme screen BckGnd while one tile reach 1024, 2048, 4096, 8192.
# add counter move
#
# V0.1.2:
# compliant (at least) python3.4
# improve menu keys system
# add AI Auto Boot when press ENTER ( F2 switch 3 AI levels) 
# add 2 players Human/AI, see py2048.cfg for config keyboard player2
#
#FIXME:
#
#TODO:
# add hiTileMaxValue attached to hiScore Small/Medium/Large.
# AI boot sould be Level3 deep with more efficient if get no point at Level2, preserve "low tile scored free"
# have a saved game for each level
# save player name with HiScore
# add 2~4 multiplayers network (as my usual objective, but how 4 players to do with this game?)
# 
