/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 17:23:26 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/12 14:46:32 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static char	*fill_line_buffer(int fd, char	*left_c, char *buffer)
{
	ssize_t	b_read; // utiliser pour retourner une erreur, il est signed.
	// read doit retourner une valeur d'erreur (-1), ce que size_t (unsigned)
	// ne peut pas faire.
	char	*tmp;

	b_read = 1;
	while (b_read > 0)
	{
		b_read = read(fd, buffer, BUFFER_SIZE); // b_read sert a stocker le res.
		// si le resultat de read est -1 = erreur.
		if (b_read == -1)
		{
			free(left_c);
			return (NULL);
		}
		else if (b_read == 0)
			break ;
		buffer[b_read] = '\0'; // '\0' de fin de chaine.
		/*
			On verifie si left_c est vide, car sinon on ne pourra pas utiliser
			strjoin.
		*/
		if (!left_c)
			left_c = ft_strdup("");
		tmp = left_c;
		left_c = ft_strjoin(tmp, buffer); // on ajoute notre buffer a left_c
		free(tmp);
		tmp = NULL;
		/*
		On va verifier ici si le buffer qu'on vient de read a un '\n' ou pas.
		Si oui, on sort de la boucle,
		Sinon on reprend la lecture du fichier.
		*/
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
	/*
	Ici je verifie si on est a la fin de la chaine.
	Si c'est le cas, cela signifie que la ligne suivante est vide
	donc on return NULL.
	C'est ce que le sujet demande.
	*/
		i++;
	if (line_buffer[i] == '\0')
		return (NULL);
	/*
	Je prend une sous chaine de la fin de la ligne jusqu'a
	la fin de tout le line_buffer.
	Ca nous donne ce qui reste de la ligne.
	*/
	left_c = ft_substr(line_buffer, i + 1, ft_strlen(line_buffer + i + 1));
	if (!left_c)
		return (NULL);
	if (*left_c == '\0')
	{
		free(left_c);
		left_c = NULL;
	}
	line_buffer[i + 1] = '\0'; // on rajoute le \0 a la fin.
	return (left_c);
}

char	*get_next_line(int fd)
{
	static char	*left_c;
	char		*buffer;
	char		*line;

	buffer = (char *)malloc((BUFFER_SIZE + 1) * sizeof(char));
	if (!buffer)
		return (NULL);
	/*
	On ne peut pas lire 0 caracteres ou moins, risque de boucle infinie avec
	BUFFER_SIZE = 0 et de crash avec une valeur negative ;
	read(fd, 0, 0) verifie si le fichier existe,
	si il y a du contenu a lire et si il est lisible (pas en modify only)
	*/
	if (fd < 0 || BUFFER_SIZE <= 0 || read(fd, 0, 0) < 0)
	{
		free(left_c);
		free(buffer);
		left_c = NULL;
		buffer = NULL;
		return (NULL);
	}
	line = fill_line_buffer(fd, left_c, buffer);
	free(buffer);
	if (!line)
		return (NULL);
	left_c = set_line(line);
	return (line);
}
