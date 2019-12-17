#include "lists.h"

/**
 * len_list - Get number of elements of a linked list
 * @head: input linked list
 *
 * Description: Return the number of elements in a singly linked list
 * Return: len
 */
int len_list(listint_t *head)
{
	listint_t *temp;
	int len = 0;

	temp = head;
	while (temp != NULL)
	{
		len++;
		temp = temp->next;
	}

	return (len);
}

/**
 * list_to_array - Create array from linked list data
 * @head: input linked list
 * @n: number of elements in linked list
 *
 * Description: return a array of elemente of a singly linked list
 * Return: array
 */
int *list_to_array(listint_t *head, int n)
{
	int i;
	int *arr_list;
	listint_t *temy;

	temy = head;
	arr_list = malloc(sizeof(int) * n);

	if (arr_list == NULL)
		return (NULL);

	for (i = 0; i < n; i++)
	{
		arr_list[i] = temy->n;
		temy = temy->next;
	}

	return (arr_list);
}

/**
 * is_palindrome - Linked list palindrome
 * @head: input linked list
 *
 * Description: function that checks if a singly linked list is a palindrome
 * Return: 1 if it is palindrome or 0 if not
 */
int is_palindrome(listint_t **head)
{
	int n, i;
	listint_t *temy;
	int *arr_list;

	temy = *head;
	if (*head == NULL)
		return (1);

	n = len_list(temy);

	if ((n % 2) != 0)
		return (0);

	arr_list = list_to_array(temy, n);

	for (i = 0; i < n; i++)
	{
		if (arr_list[i] != arr_list[(n - 1) - i])
		{
			free(arr_list);
			break;
			return (0);
		}
	}

	free(arr_list);
	return (1);
}
