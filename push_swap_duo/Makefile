# **************************************************************************** #
#                                   push_swap                                  #
# **************************************************************************** #

NAME        := push_swap
BONUS_NAME  := checker

CC          := cc
CFLAGS      := -Wall -Wextra -Werror
RM          := rm -f

# ----------- SOURCES (à adapter) ---------------------------------------------

SRCS := \
	src/main.c \
	src/parser.c \
	src/sort.c \
	src/stack.c \
	src/stack_utils.c \
	src/utils.c \
	src/operators.c \
	src/bench.c \
	src/instruction_push.c \
	src/instruction_reverse_rotate.c \
	src/instruction_rotate.c \
	src/instruction_swap.c \
	ft_printf/ft_printf.c \
	ft_printf/ft_printf_format.c \
	ft_printf/ft_printf_utils.c \
	

INCS := -Iinclude -Ift_printf

OBJ_DIR     := obj

# ----------- OBJECTS ----------------------------------------------------------

OBJS        := $(SRCS:%.c=$(OBJ_DIR)/%.o)

# ----------- RULES ------------------------------------------------------------

all: $(NAME)

$(NAME): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) $(INCS) -o $(NAME)

$(OBJ_DIR)/%.o: %.c
	@mkdir -p $(dir $@)
	$(CC) $(CFLAGS) $(INCS) -c $< -o $@

clean:
	$(RM) -r $(OBJ_DIR)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re
