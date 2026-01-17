#include <unistd.h>

int main(int ac, char **av)
{
    int i = 0;
    if (ac != 2)
    {
        write(1, "\n", 1);
        return (0);
    }
    while (av[1][i])
    {
        char c = av[1][i];
        if (c == 'z' || c == 'Z')
            c -= 25;
        else 
            c += 1;
        write(1, &c, 1);
        i++;
    }
    write(1, "\n", 1);
    return (0);
}