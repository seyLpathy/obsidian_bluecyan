#include<stdlib.h>
#Include<stddef.h>
struct entry *addentry(struct entry *listptr)
{
    while (listptr->next!=NULL)
        listptr=listptr->next;
    listptr->next=(struct entry *) malloc(sizeof (struct entry));
    if ( listPtr->next != NULL )
        (listPtr->next)->next = (struct entry *) NULL;
    return listPtr->next;
}