

# Ludo Game Simulation 

This project is an implementation of the **Ludo game**, developed in **Python** as part of the **Programming 1** course at **FEI STU**. The goal of this project was to apply and evaluate the programming skills we acquired during the course.

<img src="https://github.com/user-attachments/assets/7b73fabd-f3d8-4de6-a25d-ca32b9c92d83" width="200" hspace="50">

## Important Note ⚠️
This project is a **simulation** of the Ludo game. The entire code, including variables, comments, outputs and the project description at the beginning of the code, is written in **Slovak!!!**. 
Added PDF, where the description of the entire project, including its evaluation, is also in **Slovak!!!**.

## Modified Rules 📕

- 👨‍🦰 **Number of Players**: The number of players is **fixed at 2** *(Player A/Player B)* and cannot be changed.
- ♟️**Single Piece Simulation**: At the start of the game, each player has only **one piece** on the board. Once the piece reaches the home area, a new piece is moved to a starting position. The game continues with one piece at a time per player.
- 🏁 **Board Size**: The player can specify any **odd-numbered board size** greater than **3**. This allows for more home areas (more than the usual 4) to be included. 
- 🎲 **Dice Rolls**: Dice rolls follow normal **Ludo game rules**. If a player rolls a **6**, they get another turn. Players must roll the exact number needed to land in the home area. If more than one home area is filled, the player continues to roll the dice until they get the required number. If there are more than 6 home areas (more than the maximum roll of the dice), the piece only needs to reach the first home area after rolling a dice and will be automatically added to the closest free home area.
- 🚶‍♂️ **Player Elimination**: If a player’s piece lands on an opponent’s piece, the opponent's piece is moved back to the starting position next round. 

*(Detailed game rules can be found in the provided PDF.)*
## How to Play 🎮

1.  Enter the **board size** (The number must be odd and greater than 3.).
2.  The game will begin, and players will take turns rolling the dice and moving their pieces according to the rules.
3. The first player to move all of their pieces to the home area wins the game. After the simulation is complete, the winner will be **announced**.
   
<p align="center">
  <img src="https://github.com/user-attachments/assets/17c746d4-525e-4884-aa8c-a77114b38447" width="500">
</p>

## **Game Output Details** ▶

The following are the key outputs displayed during the game simulation:

1.  **Round Information** – Each round, the current turn and player are displayed, along with the result of the dice roll.
2.  **Player Move** – When a player moves their piece, the output will show the number they rolled and the updated position of the piece on the board.
3.  **Piece Moving to Home Area** – When a player’s piece reaches the home area, a message will indicate that the piece has successfully entered the home.
4.  **Winner Announcement** – When a player moves all their pieces to the home area, the program announces the winner of the game and displays the round in which they won.
5. **Game Board Display** – The entire game board is shown with the pieces and home areas, illustrating the current state of the game. *(X - middle, D - home areas, * - place for pieces, A, B - players pieces)*
7. **There is no written output when piece is taken by another player!**

*(Below are example screenshots from the simulation, illustrating the various outputs.)*

<p align="center">
  <img src="https://github.com/user-attachments/assets/81dcb57e-965d-4e98-97de-0a887ba1ee95" width="320" hspace="10">
  <img src="https://github.com/user-attachments/assets/1dab139a-8d81-481e-b2ee-af525ecbb4fa" width="320" hspace="10">
</p>

## Setup 🔧
To run the game, make sure you have **Python 3.x** installed on your system. It's recommended to use **Visual Studio** or another IDE for best results, as the script close immediately when run in a command prompt.

### Project Evaluation 📊

The project was evaluated based on the criteria specified in the provided **PDF** document, which includes coding standards, functionality, and the implementation of game rules. 


### **Personal Reflection** 💭

Looking back at this project, I fully realize that the code is **far from well-structured**. It contains a lot of **nested loops, deeply stacked conditions, and overall poor readability**. However, it’s important to note that this was my **first larger project**, built entirely from scratch at the very beginning of my coding journey.

While the code may not be perfect, it represents an important milestone in my learning process. So, if you decide to go through it, please keep that in mind! 😄





