# README

## MINI-CLASHIA: THE MINIATURE CLASH OF CLANS GAME

---

- This game is a terminal-based 2D recreation of the classic "Clash of Clans" game.
- Implemented in Python3

## Controls

- Use "w", "s", "a" and "d" to move the king.
- Use spacebar, i.e., " " to make the king attack the neighbouring cell.
- Use "q" key to quit the game.
- [BONUS] Use "x" for levianthan axe (attacks in all four directions up to a distance of 1)
- [BONUS] Use "o" for deactivating the cannons for 10 seconds (can be used only once in the game)
- Use "p", "l" and "m" for spawning the "barbarians" from the three spawning positions.
- Use "o", "k" and "n" for spawning "archers" from spawning points.
- Use "i", "j" and "b" for spawning "balloons" from spawning points.
- Use "r" to activate the "Rage Spell"
- Use "h" to activate the "Heal Spell"

## Assumptions

- Cannon attacks a block of area 4*range^2, with the cannon at the centre.
- Barbarians can only be spawned if the King is alive.
- Barbarian can move diagonally but not attack diagonally

## version 3.2 additions

- Barbarians are now allowed to enter the same block.
- limit on the number of barbarians(referred to as troops in the code) = 6
- Barbarians are represented by the letter "B" on the map.
- limit on the number of archers = 6
- Archers are represented by the letter "A" on the map.
- limit on the number of balloons = 3
- Balloons are represented by the letter "b" on the map.
- Spells only work on Barbarians and King, if required, they can be made to affect the queen, archers and balloons as well with minimal code addition.

