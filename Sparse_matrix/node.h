#ifndef NODE_H
#define NODE_H

#include <stdlib.h>
#include <stdio.h>

typedef struct node
{
    char data;
    int i;
    int j;
    struct node * nc;
    struct node * nl;

}node;

node * create_new_node(int i, int j, char data);

int is_exist(node ** row_tab, int i, int j);

void insert_node(node **row_tab, node **col_tab, int max_row, int max_col, int i, int j, char data);

void delete_node(node **row_tab, node **col_tab, int max_row, int max_col, int i, int j);

void search_node_with_col(char data, node ** row_tab, int max_row);

void search_node_with_row(char data , node ** col_tab, int max_col);

void delete_daynamic_arr(node **row_tab, node **col_tab, int max_row, int max_col);


#endif
