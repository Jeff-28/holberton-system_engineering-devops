#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - infinite loop
 *
 * Return: value 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - creates five zombie processes
 *
 * Return: value 0
 */
int main(void)
{
	pid_t child;
	int i = 0;

	while (i < 5)
	{
		child = fork();
		if (child > 0)
			printf("Zombie process created, PID: %d\n", child);
		else
			exit(0);
		i++;
	}
	infinite_while();
	return (0);
}
