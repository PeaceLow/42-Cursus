#include <unistd.h>

int main(int ac, char **av)
{
    int i = 0;
    if (ac != 4)
    {
        write(1, "\n", 1);
        return (0);
    }
    if (av[2][1] != '\0' || av[3][1] != '\0')
    {
        write(1, "\n", 1);
        return (0);
    }
    while (av[1][i])
    {
        char c = av[1][i];
        if (c == av[2][0])
            c = av[3][0];
        write(1, &c, 1);
        i++;
    }
    write(1, "\n", 1);
    return (0);
}