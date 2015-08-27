#Bertrand's Box Paradox
### *A model and game*

These are two Python programs that replicate Bertrand's Box Paradox.

The "paradox" can be summarized like this...

*Suppose you have three boxes in front of you, each with exactly two coins inside them. One box contains two silver coins, one box contains two gold coins, and the remaining box contains one silver and one gold coin. You don't know which of the boxes is which. Now suppose that without looking you reach into one of the boxes and draw a gold coin.*

*So after having drawn a gold coin, what is your chance of drawing another gold coin from that same box?*

Solution and explanation can be found on [Wiki](https://en.wikipedia.org/wiki/Bertrand%27s_box_paradox).

###box paradox model.py v0.3

This program runs the simulation any numbers of times you select under the following rule: it will always guess the same color coin it just drew. At the end it outputs a percent accuracy. This accuracy converges on the correct answer found on the Wiki page above.

Note: Running over 1,000,000 simulations may take quite some time.

###box paradox game.py v0.21

Here you can actually play the game yourself. You select a box and draw a coin from the box. You can then input your guess of what you think the other coin in the box will be. It reports your success (or failure), and keeps track of your accuracy.

Super secret tip: there's a way to cheat in this game and know the box that's been selected *before* making your guess.

####Model Changelog

v0.3
* Added intro text
* Cleaned up and simplified code
* Cleaned up and improved text
* Added more specific end stats

v0.2
* Asks user for number of simulations to run
* Deleted some unnecessary code
* TODO: Keep track of individual gold & silver accuracy, not just total accuracy
  * NOTE: Done in v0.3

v0.1
* Initial build

####Game Changelog

v0.21
* Tightened input validation throughout

v0.2
* Changed text and other text throughout
* Added super basic ASCII art
* Rejiggered quit method
* *Possibly* added a special secret way to cheat

v0.1
* Initial build