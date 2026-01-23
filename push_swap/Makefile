# **************************************************************************** #
#                                   push_swap                                  #
# **************************************************************************** #


NAME        := push_swap
BONUS_NAME  := checker

CC          := cc
CFLAGS      := -Wall -Wextra -Werror
RM          := rm -f

# ----------- SOURCES (à adapter) ---------------------------------------------

COMMON_SRCS := \
	src/parser/parser.c \
	src/parser/parser_split.c \
	src/parser/parser_utils.c \
	src/stack/stack.c \
	src/stack/stack_utils.c \
	src/stack/stack_stats.c \
	src/utils/utils.c \
	src/utils/operators.c \
	src/utils/bench.c \
	src/instruction/instruction_push.c \
	src/instruction/instruction_reverse_rotate.c \
	src/instruction/instruction_rotate.c \
	src/instruction/instruction_swap.c \
	ft_printf/ft_printf.c \
	ft_printf/ft_printf_format.c \
	ft_printf/ft_printf_utils.c

PS_SRCS := \
	src/main.c \
	src/sort/sort_adaptive.c \
	src/sort/sort_simple.c \
	src/sort/sort_three.c \
	src/sort/sort_medium.c \
	src/sort/sort_complex_quick.c \
	src/sort/sort_quick_utils.c \
	src/sort/sort_utils.c

CHECKER_SRCS := src/checker.c

INCS := -Iinclude -Ift_printf

OBJ_DIR     := obj

# ----------- OBJECTS ----------------------------------------------------------

COMMON_OBJS := $(COMMON_SRCS:%.c=$(OBJ_DIR)/%.o)
PS_OBJS     := $(PS_SRCS:%.c=$(OBJ_DIR)/%.o)
CHECKER_OBJS:= $(CHECKER_SRCS:%.c=$(OBJ_DIR)/%.o)

# ----------- RULES ------------------------------------------------------------

all: $(NAME)

$(NAME): $(COMMON_OBJS) $(PS_OBJS)
	$(CC) $(CFLAGS) $(COMMON_OBJS) $(PS_OBJS) $(INCS) -o $(NAME)

bonus: $(BONUS_NAME)

$(BONUS_NAME): $(COMMON_OBJS) $(CHECKER_OBJS)
	$(CC) $(CFLAGS) $(COMMON_OBJS) $(CHECKER_OBJS) $(INCS) -o $(BONUS_NAME)

$(OBJ_DIR)/%.o: %.c
	@mkdir -p $(dir $@)
	$(CC) $(CFLAGS) $(INCS) -c $< -o $@

clean:
	$(RM) -r $(OBJ_DIR)

fclean: clean
	$(RM) $(NAME) $(BONUS_NAME)

re: fclean all

simple: all
	shuf -i 0-9999 -n 100 | xargs ./push_swap --bench --simple
medium: all
	shuf -i 0-9999 -n 500 | xargs ./push_swap --bench --medium

complex: all
	shuf -i 0-9999 -n 500 | xargs ./push_swap --bench --complex

adaptive: all
	shuf -i 0-9999 -n 500 | xargs ./push_swap --bench --adaptive
.PHONY: all clean fclean re
