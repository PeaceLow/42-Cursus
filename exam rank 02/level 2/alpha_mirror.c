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
        if (c >= 'A' && c <= 'Z')
            c = 90 - c + 65;
        else if (c >= 'a' && c <= 'z')
            c = 122 - c + 97;
        write(1, &c, 1);
        i++;
    }
    return (0);
}