#include "game.h"

node *col_tab[MAX_COL] = {NULL};
node *row_tab[MAX_ROW] = {NULL};


void game_start(){

int i , j, data;

while(1){

    display_cont(MAX_ROW,MAX_COL,row_tab);

    back://if user enter number not exist in menu back to this and try again
    switch(menu()){

    case '1' :
            printf("Enter ur data :");
            scanf(" %c", &data);

            printf("Enter postion u want add format (indexrow-indexcol) :");
            scanf("%d-%d",&i,&j);

            insert_node(row_tab,col_tab,MAX_ROW,MAX_COL,i,j,data);

        break;

    case '2' :

            printf("Enter postion u want delete format (indexrow-indexcol) :");
            scanf("%d-%d",&i,&j);

            delete_node(row_tab,col_tab,MAX_ROW,MAX_COL,i,j);

        break;

    case '3' :

            printf("Enter data u want search for :");
            scanf(" %c", &data);

            search_node_with_row(data,col_tab,MAX_COL);
            //or    search_node_with_col(data);

        break;

    case '4' :
            printf("u will delete all nodes on this matrix!");
                delete_daynamic_arr(row_tab,col_tab,MAX_ROW,MAX_COL);
        break;

    case ESC :
            delete_daynamic_arr(row_tab,col_tab,MAX_ROW,MAX_COL);
            exit(1);
        break;

    default :
        printf("---------------------------------\nnumber you enter it not exist !\n");
        printf("back try again\n----------------------------------\n");
        goto back;



    }
    getch();//this is to let user see the output when press enter to continue
    display_cont(MAX_ROW,MAX_COL,row_tab);

}

}










