#Bertrand's Box Paradox v0.1
### *A model and game*

These are two Python programs that replicate Bertrand's Box Paradox.

The "paradox" can be summarized like this...

*Suppose you have three boxes in front of you, each with exactly two coins inside them. One box contains two silver coins, one box contains two gold coins, and the remaining box contains one silver and one gold coin. You don't know which of the boxes is which. Now suppose that without looking you reach into one of the boxes and draw a gold coin.*

*So after having drawn a gold coin, what is your chance of drawing another gold coin from that same box?*

Solution and explanation can be found on [Wiki](https://en.wikipedia.org/wiki/Bertrand%27s_box_paradox).

###box paradox model.py

This program runs the simulation 10,000 times under the following rule: it will always guess the same color coin it just drew. At the end it outputs a percent accuracy. This accuracy converges on the correct answer found on the Wiki page above.

###box paradox game.py

This allows you to play the game yourself. It first randomizes which of the three boxes are selected, and them randomly draws a coin from the box for you. You can then input your guess of what you think the other coin in the box will be. It reports your success (or failure), and keeps track of your accuracy.