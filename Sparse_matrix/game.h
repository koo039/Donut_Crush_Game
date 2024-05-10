#ifndef GAME_H
#define GAME_H

#include "display.h"

#define MAX_ROW 20
#define MAX_COL 10
#define ESC 27

node *col_tab[MAX_COL];// = {NULL};
node *row_tab[MAX_ROW];// = {NULL};

void game_start();


#endif
