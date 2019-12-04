# Connect Five

## Navigation 
<a name="top"></a> 
1. [Description of the Game](#description) 
    - [Gameplay Screenshots](#screenshots) 
2. [How to Install](#install) 
3. [How to Play](#play) 
4. [Documentation](#doc) 
5. [Authors and their Contributions](#authors) 


## Description 
<a name="description"></a>
Are you tired of not having anything to play?
Too many terrible games on the market?
Too poor to afford anything in this microtransaction-rich environment?
Maybe you're bored of playing connect 4? (don't worry, we get it!)

In that case, allow us to introduce our game, connect five.
Traditionally called Gomuku, Connect Five is a game where players take turns putting markers 
on a 15x15 grid. In this version, one player uses the 'X' character, while the other player
uses the 'O' character.
The goal of the game is to form an unbroken line of five chips in any direction. 
These directions are vertically, horizontally, or diaonally.
## Screenshots 
<a name="screenshots"></a> 
## How to Play 
<a name="play"></a> 
<a name="kevin"></a>
The way of playing this game is similar to the Connect Four. The board of this game is similar to Go board and its size is 15×15 board. There are many empty intersections between rows and columns where you can fill these pieces. The winner who can come up with 5 tokens in any directions and you have to think how to block the opponent. There are 2 people playing in this game, one will be Black(0) and one will be White(X). The White(X) always goes first. 
## How to install 
<a name="install"></a>
The game can be installed by cloning the repository available at the link:<br/>
https://github.com/weboski/connect_five<br/>
STEP 1:<br/>
Clone the repository from the link given above.<br/>
STEP 2:<br/>
Download the ZIP file and extract its contents.<br/>
STEP 3:<br/>
Run the game with the ConnectFiveController.py file. A Python interpreter needs to be installed to run the game. The preferred version is Python 3.8.
## Documentation 
<a name="doc"></a> 
We decided to design the code for our game using the Model, View, Controller Model (MVC). To follow this model, the game code is divided into three classes; ConnectFiveController, ConnectFiveBoard, and ConnectFive. The ConnectFiveController handles player input and updates the ConnectFive class (the Controller component of the MVC model). The ConnectFive handles all the game logic and updates the ConnectFiveBoard based on them. (the Model component of MVC). Finally, the ConnectFiveBoard outputs all information to the console for the player to consult and make moves from (the View component of MVC).
## How the code could be extended
<a name = "codeExtention"></a>
<++>PLACEHOLDER TEXT HERE<++>
## Authors 
<a name="authors"></a> 
### Michael
<a name = "Michael"></a>
My contributions to the code consist of the ConnectFiveBoard.py file along with the methods and classes inside.
Inside the file, there is a board class. Within the class itself, there are methods that check valid positions on the board, a constructor that
creates the object itself, a method to get the string representation, as well as getter/setter methods. Additionally, the file has internal methods to
convert the coordinates on the grid from letters to numbers, and vice versa. In the readme file,
the contribution is the part of the file that describes the game and out implementation of it.
Note for marking: Early on, I forgot to change the name/email of my desktop before making commits, etc...
                  As a result, some of the commits have the name, "Buildtools." This refers to Michael Kwan, as modifying git version history is
                  considered frowned upon.

### Jacob
Most of my contribution to the project code took place in the ConnectFive class. The methods I implemented handle the most important aspects of the game logic; uniformChips(), hasMove(), and checkWinner(). The uniformChips() and checkWinner() methods handle checking for a player winning (player forms an unbroken line of 5 chips )while hasMove() returns whether there are any possible moves available on the board. Another method I implemented is the getCount() method which counts how many chips of the inputted player type are on the board. Outside of implementing methods, I added and modified documentation for the class so team members understand what each method is responsible for. Another contribution included fixing a bug that prevented our game from detecting a player winning. For the README document I completed the Documentation section which is a high-level description of the code structure.


### Isha
My contribution to the project is mainly the ConnectFiveController.py file. I worked on the ConnectFiveController class, which is responsible for the user interaction interface. The ConnectFiveController class accepts user input and sends updates to the model. This class formed the 'Controller' aspect of the MVC model. I worked on methods like 'player_turn', 'return_board', 'check_move'. These methods are helper methods for the most important method ('play') in the class . I worked on the method 'play' as well, which is responsible for sending the user input to the Model and makes appropriate changes (for example displaying which player's turn it is, the winner etc.) that need to be rendered to the console. I also documented the methods in the ConnectFiveController class. I documented the 'How To Install' section in the README.md file. This sections gives clear instructions to a user about installing the game, getting the required configurations and then successfully running the game.
