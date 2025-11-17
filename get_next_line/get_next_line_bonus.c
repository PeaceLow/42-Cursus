/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 17:23:26 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/17 15:50:51 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

static char	*fill_line_buffer(int fd, char	*left_c, char *buffer)
{
	ssize_t	b_read;
	char	*tmp;

	b_read = 1;
	while (b_read > 0)
	{
		b_read = read(fd, buffer, BUFFER_SIZE);
		if (b_read == -1)
		{
			free(left_c);
			return (NULL);
		}
		else if (b_read == 0)
			break ;
		buffer[b_read] = '\0';
		if (!left_c)
			left_c = ft_strdup("");
		tmp = left_c;
		left_c = ft_strjoin(tmp, buffer);
		free(tmp);
		tmp = NULL;
		if (ft_strchr(buffer, '\n'))
			break ;
	}
	return (left_c);
}

static char	*set_line(char *line_buffer)
{
	char	*left_c;
	size_t	i;

	i = 0;
	while (line_buffer[i] && line_buffer[i] != '\n')
		i++;
	if (line_buffer[i] == '\0')
		return (NULL);
	left_c = ft_substr(line_buffer, i + 1, ft_strlen(line_buffer + i + 1));
	if (!left_c)
		return (NULL);
	if (*left_c == '\0')
	{
		free(left_c);
		left_c = NULL;
	}
	line_buffer[i + 1] = 0;
	return (left_c);
}

char	*get_next_line(int fd)
{
	/*
	Au lieu de partager un seul tampon résiduel entre tous les descripteurs, 
	on maintient un tampon par FD via son index : 
	quand get_next_line_bonus(fd) lit, il conserve les restes dans left_c[fd]. 
	Ainsi, chaque flux garde son propre contexte (position, reste de ligne) sans écraser celui d’un autre. 
	Par exemple, si on alterne entre fd1 et fd2, left_c[fd1] évolue indépendamment de left_c[fd2], 
	ce qui permet d’avoir plusieurs lectures “en parallèle” sans mélange des données.
	*/
	static char	*left_c[FD_MAX];
	char		*buffer;
	char		*line;

	buffer = (char *)malloc((BUFFER_SIZE + 1) * sizeof(char));
	if (!buffer)
		return (NULL);
	if (fd < 0 || BUFFER_SIZE <= 0 || fd >= FD_MAX)
	{
		free(left_c[fd]);
		free(buffer);
		left_c[fd] = NULL;
		buffer = NULL;
		return (NULL);
	}
	line = fill_line_buffer(fd, left_c[fd], buffer);
	free(buffer);
	if (!line)
	{
		left_c[fd] = NULL;
		return (NULL);
	}
	left_c[fd] = set_line(line);
	return (line);
}
// int main(int argc, char **argv)
// {
//     int   fd;
//     char  *line;

//     if (argc != 2)
//     {
//         printf("Usage: %s <filename>\n", argv[0]);
//         return (1);
//     }

//     fd = open(argv[1], O_RDONLY);
//     if (fd < 0)
//     {
//         perror("Error opening file");
//         return (1);
//     }

//     while ((line = get_next_line(fd)) != NULL)
//     {
//         printf("%s", line);  // line contient déjà le '\n' si présent
//         free(line);
//     }

//     close(fd);
//     return (0);
// }