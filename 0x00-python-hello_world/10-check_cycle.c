#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - check if list is a cycle
 * @list: input list
 *
 * Description: check if a list is a cycle, return 1 if is cycle
 * Return: 1 is a cycle, 0 is nos a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *eval;

	eval = list;
	eval = eval->next;
	while (eval != list && eval != NULL)
		eval = eval->next;

	if (eval == list)
		return (1);

	return (0);
}
