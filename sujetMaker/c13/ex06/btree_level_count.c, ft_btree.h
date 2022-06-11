#include <unistd.h>
void *btree_search_item(t_btree *root, void *data_ref,int(*cmpf)(void *,void *));