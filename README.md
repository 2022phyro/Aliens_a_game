# ALIENS A GAME

Being a great fan of games, I decided to try my hand at pygame to see what I could do. To be honest, I followed the classic model of
Aliens and I guess I was lacking in ideas. My game is almost complete but it has a flaw for now. There is no pause to make sure that you will be engrossed :laughing:
Here are the source files for this game To play it though I made it using pygame. If you have pygame installed then its alright. If you don't not to worry

## Controls :scroll:

* q -> quit / exit the game
* p -> pla ythe game
* arrow keys   -> navigate the ship ***your ship***
* space_bar    -> fire bullets
* As you play, there are increasing levels of difficulty

## How to play

* Clone the dist folder [here](./dist)
* Enter the dist folder and click on the ``main`` application
* Begin your game

## SOURCE CODES:open_file_folder:

* [main](./main.py) It is the main source code for the program. IT contains the function running the game
* [Button](./Button.py) -> This is responsible for controlling stats like the level of difficluty, the score, high score and the play button
* [Drawing](./Drawing.py) -> It contains the classes for the Spaceship and the Alien ships
* [Bullets](./bullets.py) -> It contains the classes for your bullets and the Alien Bullets
* [Alien_Combo](./Alien_combo.py) -> It handles the functions that run the combination of alien fleet and their bullets as well as when the ship is hit etc
* [Images](./Images) -> THis folder stores all the pictures I used in making the game
* [game_func](./game_func.py) -> This module contains functions that make the administrative decisions in the game like, which part of the game should run and when it should stop etc
* [dist](./dist) -> It containss the excutable of our program. If you don't want the ource code, you can as well clone only this
* [record](./record) -> This stores our high score records so please, don't touch it
* [run](./run) -> a shell script for biuiding an executable
* [build](./build) -> This is created when the executable is being created

## SEE ALSO

<details>
  <summary></summary>

## How to build a python executable

* If you have pygame on your system or any other python module and you wish to build an executable, then you can use pyinstaller. If you don't have pyinstaller, then run this to install
* **pip install pyinstaller**
* To build the file into an executable run this on your terminal
``pyinstaller --onefile -w filename.py``
The -w option tells the pyinstaller not to open a terminal when running the program. If you need a terminal, you can remove that flag. Read up more on pyinstaller to know more.
* In this case, it was ***pyinstaller --onefile -w main.py***
* Your executable will be inside a ``dist`` directory/folder
* If the program runs on dependencies like pictures or the rest, move it to the **dist** directory/folder
* The game is kinda experimental but I guarantee a good performance
* Guess python is a compiled language after all :stuck_out_tongue_winking_eye:

</details>

## Version

Aliens Attack version 1.0.0

## Credits

* stack overflow
* Google
* Eric Matthes and ``Python Crash Course``
* Sir Joseph Konjas

## AUTHOR

Ugwuanyi Afam alias 2022phyro
on ``26th December 2020``
