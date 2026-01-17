int ft_isspace(int c)
{
	return (c >= 9 && c <= 13 || c == 32 ? 1: 0);
}

int ft_isdigit(int c)
{
	return (c >= '0' && c <= '9' ? 1 : 0);
}

int ft_atoi(char *str)
{
	int i = 0;
	int s = 1;
	int res = 0;
	
	while (ft_isspace(str[i]))
		i++;
	if (str[i] == '-')
	{
		s = -1;
		i++;
	}
	while (ft_isdigit(str[i]))
	{
		res *= 10;
		res += str[i] - 48;
		i++;
	}
	return (res *= s);
}