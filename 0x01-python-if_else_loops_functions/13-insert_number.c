#include "lists.h"

/**
 * insert_node -  inserts a number into a sorted singly linked list
 * @head: input list
 * @number: number to insert
 *
 * Description: Function that inserts a number into a sorted singly linked list
 * Return: Address of new node or NULL if fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	int i = 0;
	listint_t *new, *temp;

	temp = *head;
	if (temp == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	while (temp != NULL)
	{
		if (i == 0 && number < temp->n)
		{
			new->next = *head;
			*head = new;
			return (*head);
		}


		if ((temp->next == NULL) && (number > temp->n))
		{
			temp->next = new;
			return (new);
		}

		if ((number > temp->n) && (number < temp->next->n))
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}

		temp = temp->next;
		i++;
	}

	return (NULL);
}
