#include "display.h"


void display_cont(int  max_row, int max_col, node ** row_tab){//to display the matrix with some colors and zeros
    /** O(n) = n2 **/

HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);

system("cls");
printf("\n");
for(int i=0;i<max_row+1;i++){
    node * cur = row_tab[i];
        for(int j=-1;j<max_col+1;j++){
            if(i == max_row || j == max_col || j == -1){
                SetConsoleTextAttribute(hConsole, FOREGROUND_BLUE | FOREGROUND_INTENSITY);
                printf(" # ");
                continue;
            }
            else if(cur == NULL || cur->j != j+1){
                SetConsoleTextAttribute(hConsole, FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE);
                printf(" . ");
                continue;
            }
            SetConsoleTextAttribute(hConsole, FOREGROUND_RED | FOREGROUND_INTENSITY);
            printf(" %c ", cur->data);
            cur = cur->nc;
        }

printf("\n");

}
SetConsoleTextAttribute(hConsole, FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE);

}

char menu(){//menu of the game to let user choose and interacte with the game

char choise;

printf("\n\n1-insert node\n");
printf("2-delete node\n");
printf("3-search node\n");
printf("4-delete entire matrix\n");
printf("---Press ESC to exit----\n");

printf("Enter one of these : ");
choise = getch();
printf("\n");

return choise;
}

void hidecursor() {
    HANDLE consoleHandle = GetStdHandle(STD_OUTPUT_HANDLE);
    CONSOLE_CURSOR_INFO info;
    info.dwSize = 100;
    info.bVisible = FALSE;
    SetConsoleCursorInfo(consoleHandle, &info);
}



