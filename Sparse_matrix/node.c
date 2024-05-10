#include "node.h"

node * create_new_node(int i, int j, char data){//Create new node to insert it in matrix

    node *new_node;
    new_node = malloc(sizeof(node));
    new_node->data = data;
    new_node->i = i;
    new_node->j = j;
    new_node->nc = NULL;
    new_node->nl = NULL;

    return new_node;
}




void insert_node(node **row_tab, node **col_tab, int max_row, int max_col, int i,int j, char data){//insert node into matrix with the right links to other nodes or tabs
    /** O(n) = linear (n) **/

if(i > max_row || j > max_col){
    printf("this index don't exist!");
}
else if(is_exist(row_tab,i,j)){
    printf("This position is allocated!");
}
else{
    if(row_tab[i-1] == NULL && col_tab[j-1] == NULL){
        node * node = create_new_node(i,j,data);
        col_tab[j-1] = node;
        row_tab[i-1] = node;
}
    else if(row_tab[i-1] == NULL){
        node * cur1 = col_tab[j-1];
        node * node = create_new_node(i,j,data);
        row_tab[i-1] = node;
        if(col_tab[j-1]->i < i){
            while(cur1->nl != NULL && cur1->nl->i < node->i)
                cur1 = cur1->nl;

            node->nl = cur1->nl;
            cur1->nl = node;
        }
        else{
            row_tab[i-1]->nl = col_tab[j-1];
            col_tab[j-1] = row_tab[i-1];

        }
}
    else if(col_tab[j-1] == NULL){
        node * cur = row_tab[i-1];
        node * node = create_new_node(i,j,data);
        col_tab[j-1] = node;
        if(row_tab[i-1]->j < j){
            while(cur->nc != NULL && cur->nc->j < node->j)
                cur = cur->nc;

            node->nc = cur->nc;
            cur->nc = node;
        }
        else{
            col_tab[j-1]->nc = row_tab[i-1];
            row_tab[i-1] = col_tab[j-1];
        }
    }
    else{
        node * cur2 = col_tab[j-1];
        node * node = create_new_node(i,j,data);
        if(col_tab[j-1]->i < i){
            while(cur2->nl != NULL && cur2->nl->i < node->i)
                cur2 = cur2->nl;

        node->nl = cur2->nl;
        cur2->nl=node;
        }
        else{
            node->nl = col_tab[j-1];
            col_tab[j-1] = node;
        }
        cur2 = row_tab[i-1];
        if(row_tab[i-1]->j < j ){
        while(cur2->nc != NULL && cur2->nc->j < node->j)
            cur2 = cur2->nc;

        node->nc = cur2->nc;
        cur2->nc=node;
        }
        else{
            node->nc = row_tab[i-1];
            row_tab[i-1] = node;
        }
    }

  }

}

void delete_node(node **row_tab, node **col_tab, int max_row, int max_col, int i, int j){//delete node from matrix and links prevuis and next node to the right node
    /** O(n) = linear (n) **/

if(i > max_row || j > max_col){
    printf("this index don't exist!");
}
else if(is_exist(row_tab,i,j) == 0)
    printf("this postion not exist");
else{
    //we use here 2 pointer method for the col and row one for prevuis and one for the next and delete the next
    node * cur = col_tab[j-1];
    node * cur1 = NULL;
    node * cura = row_tab[i-1];
    node * cura1 = NULL;

    while(cur->i != i){
        cur1 = cur;
        cur = cur->nl;
    }

    while(cura->j != j){
        cura1 = cura;
        cura = cura->nc;
    }


    if(cur->nc == NULL && cur->nl == NULL){
        if(cur1 == NULL)
            col_tab[j-1] = NULL;
        else
            cur1->nl=NULL;
        if(cura1 == NULL)
            row_tab[i-1]=NULL;
        else
            cura1->nc = NULL;

        free(cur);
    }
    else if(cur->nl == NULL){
        if(cur1 == NULL)
            col_tab[j-1] = NULL;
        else
            cur1->nl=NULL;
        if(cura1 == NULL)
            row_tab[i-1]=cura->nc;
        else
            cura1->nc = cura->nc;

        free(cur);
    }
    else if(cur->nc == NULL){
        if(cur1 == NULL)
            col_tab[j-1] = cur->nl;
        else
            cur1->nl=cur->nl;
        if(cura1 == NULL)
            row_tab[i-1]=NULL;
        else
            cura1->nc = NULL;

        free(cur);
    }
    else{
        if(cur1 == NULL)
            col_tab[j-1] = cur->nl;
        else
            cur1->nl=cur->nl;

        if(cura1 == NULL)
            row_tab[i-1]=cura->nc;
        else
            cura1->nc = cura->nc;

        free(cur);

    }

  }

}

void search_node_with_col(char data, node ** row_tab, int max_row){//search a node in matrix use col search
    /** O(n) = n2 **/

int c = 0;
for(int i=0; i < max_row; i++){
    node * cur = row_tab[i];
    while(cur != NULL && cur->data != data)
        cur = cur->nc;

    if(cur != NULL && cur->data == data){
        printf("The \" %c \" is found and index i=%d,j=%d\n", data, cur->i, cur->j);
        c = 1;
        break;
    }

}
if(c == 0)
    printf("this \"%c\" not exist !", data);
}



void search_node_with_row(char data, node ** col_tab, int max_col){//search a node in matrix use row search
        /** O(n) = n2 **/

int c = 0;
for(int i=0; i < max_col; i++){
    node * cur = col_tab[i];
    while(cur != NULL && cur->data != data)
        cur = cur->nl;
    if(cur != NULL && cur->data == data){
        printf("The \"%c\" is found and index i=%d,j=%d\n", data, cur->i, cur->j);
        c = 1;
        break;
    }

}
if(c == 0)
    printf("this \"%c\" not exist !",data);
}



int is_exist(node ** row_tab, int i,int j){//to check this index exist on matrix or not
        /** O(n) = n **/

int c = 0;

node * cur = row_tab[i-1];
while(cur != NULL){
    if(cur->j == j){
        c = 1;
        break;
    }
    cur = cur->nc;
}
return c;

}

void delete_daynamic_arr(node **row_tab, node **col_tab, int max_row, int max_col){//this fonction use for free allocated memory when the game ended (delete all node form matrix)
for(int i=0;i<max_row;i++){
    node * cur = row_tab[i];
    node * cur1 = NULL;
    while(cur!=NULL){
    cur1 = cur;
    cur = cur->nc;
    delete_node(row_tab,col_tab,max_row,max_col,i+1,cur1->j);
}
}
}

