#include <unistd.h>

int main(int ac, char **av)
{
    int i = 0;
    if (ac != 2)
    {
        write(1, "\n", 1);
        return (0);
    }
    while (av[1][i] != '\0')
        i++;
    while (i != -1)
    {
        write(1, &av[1][i], 1);
        i--;
    }
    return (0);
}