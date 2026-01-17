#include <unistd.h>


void ft_putnbr(int nb)
{
    long n = nb;
    if (n < 0)
    {
        write(1, "-", 1);
        n = -n;
    }
    if (n > 9)
        ft_putnbr(n / 10);
    char c = '0' + (n % 10);
    write(1, &c, 1);
}

int main(void)
{
    int nb = 1;
    while (nb <= 100)
    {
        if (nb % 15 == 0)
            write(1, "fizzbuzz", 8);
        else if (nb % 3 == 0)
            write(1, "fizz", 4);
        else if (nb % 5 == 0)
            write(1, "buzz", 4);
        else
            ft_putnbr(nb);
        write(1, "\n", 1);
        nb++;
    }
    return (0);
}