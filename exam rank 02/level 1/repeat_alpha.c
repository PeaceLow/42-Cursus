#include <unistd.h>

int main(int ac, char **av)
{
    int i = 0;
    int nb = 0;
    if (ac != 2)
    {
        write(1, "\n", 1);
        return (0);
    }
    while (av[1][i] != '\0')
    {
        if (av[1][i] >= 'a' && av[1][i] <= 'z')
        {
            nb = av[1][i] - 96;
            while (nb > 0)
            {
                write(1, &av[1][i], 1);
                nb--;
            }
            i++;
        }
        else
            i++;
    }
    write(1, "\n", 1);
    return (0);
}

