CC		= cc
CFLAGS	= -Wall -Werror -Wextra
NAME	= codexion
OBJDIR	= obj
SRCDIR	= coders

SRCFILES		= main.c \
		  init.c \
		  routine.c \
		  monitor.c \
		  scheduler.c \
		  verification.c \
		  utils.c

OBJ		= $(addprefix $(OBJDIR)/, $(SRCFILES:.c=.o))
SRC		= $(addprefix $(SRCDIR)/, $(SRCFILES))

all: $(NAME)

$(NAME): $(OBJ)
	$(CC) $(CFLAGS) $(OBJ) -o $(NAME) -lpthread

$(OBJDIR)/%.o: $(SRCDIR)/%.c | $(OBJDIR)
	$(CC) $(CFLAGS) -c $< -o $@

$(OBJDIR):
	mkdir -p $(OBJDIR)

clean:
	rm -rf $(OBJDIR)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
