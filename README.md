# <img src="src/icon/icon.png" width="38"/> Candy Crush Game
[![Python](https://img.shields.io/badge/Python-3.12.3-blue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-1.9.6-836DAC.svg)](https://www.pygame.org/news)
[![Awesome Python](https://img.shields.io/badge/Python-awesomepython-blue.svg?style=flat&logo=python&logoColor=white)](https://github.com/vinta/awesome-python)
#

<img src="https://github.com/koo039/Candy_Crush_Game/blob/main/doc/screen.PNG" width="600">



## ⭐ Features
⭐ sparse matrix  
⭐ easy to play  
⭐ Build to sovle problem  
## 💿 Clone
Run terminal or git bash and write : 
git clone https://github.com/koo039/Candy_Crush_Game.git

## 💿 Downloads

### 📦 [Candy-Crush-Gamee_win.zip](https://github.com/koo039/Candy_Crush_Game/releases/download/untagged-d5eba91e85623583c2ce/CandyCrush-win_zip.rar) `16 MB` [Windows]
> 💡 Native x64 one-click exe - Noo required.
### 📦 [Candy-Crush-src_code](https://github.com/koo039/Candy_Crush_Game/releases/download/untagged-d5eba91e85623583c2ce/game_src_code.rar) `19.2 MB` [Game_Src]
> 💡 python and pygame required.
### 📦 [Candy-Crush-web_browser]() `15.5 MB` [Web]
> 💡 You need to run it on your localhost. We explain how to do it below.

## ⌨ Controls

* <kbd>ESC</kbd> Exit the game.
* <kbd>Space</kbd> for Pause. 
* <kbd>-></kbd> go right.
* <kbd><-</kbd> go left.

## 🧭 Overview

### Game Diagram
<img src="https://github.com/koo039/Candy_Crush_Game/blob/main/doc/diagram.png" width="600">


## problem specification
>When working on large-scale projects such as Recommendation Systems or Natural Language Processing (NLP), dealing with extensive matrices is inevitable. These matrices >often consist of millions or even billions of elements, leading to significant memory consumption. To tackle this issue, we recommend utilizing a sparse matrix data >structure.
>In sparse matrices, memory usage is optimized by representing only the non-zero elements along with their respective coordinates. Each element in a sparse matrix is >represented by a quintuple: (Val, I, J, PL, PC).
>Val: Represents the value of the matrix element.
>I, J: Denote the coordinates of the element within the matrix.
>PL, PC: Pointers to the next element in the same row (PL) and the next element in the same column (PC).
>Accessing the matrix is facilitated through two arrays: TL and TC.
>TL: Array of pointers representing the list heads of the row elements.
>TC: Array of pointers representing the list headers of the column elements.
>Refer to Figure 1-1 for a visual representation of this structure.
# 
<img src="https://github.com/koo039/Candy_Crush_Game/blob/main/doc/problem_photo.png" width="600">


>we've developed our Candy Crush game to address this issue, aiming to enhance our skills and gain valuable experience in game development ,
>In the "Sparse matrix" folder above ,written in the C programming language, you can find the implementation of this solution. It aims to optimize memory usage in large-scale projects by utilizing a >sparse matrix data structure. This structure represents only the non-zero elements along with their coordinates, effectively reducing memory consumption. If you're >interested in understanding how the problem works and how the solution is implemented, you'll find detailed explanations and code in the 'dsa' folder.

