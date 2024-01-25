BOLD = \033[1m
GREEN = \x1B[32m
RED = \x1B[31m
RESET = \033[0m

WIDTH := $(shell echo "scale=0; $$(tput cols) / 2" | bc)

POETRY = poetry run

.PHONY: all clear check test mypy flake8 install

define print_title
	@echo "$(GREEN)"
	@printf %$$(($(WIDTH) - $$(echo -n '$(1)' | wc -c) / 2))s | tr " " "_"
	@printf "$(BOLD) %s $(RESET)$(GREEN)" "$(1)"
	@printf %$$(($(WIDTH) - $$(echo -n '$(1)' | wc -c) / 2))s | tr " " "_"
	@echo "$(RESET)"
endef

all: clear test check
	@echo "$(GREEN)"
	@printf %$$(($$(tput cols) - 2))s | tr " " "‾"
	@echo "$(RESET)"

check: mypy flake8

test:
	$(call print_title,Running Tests)
	@$(POETRY) pytest -q || true

mypy:
	$(call print_title,Running MyPy)
	@if $(POETRY) mypy --pretty ./ ; then \
        echo "\n$(GREEN)SUCCESS$(RESET)"; \
    else \
        echo "\n$(RED)FAIL$(RESET)"; \
    fi

flake8:
	$(call print_title,Running Flake8)
	@if $(POETRY) flake8 ./; then \
        echo "\n$(GREEN)$(BOLD)SUCCESS$(RESET)"; \
    else \
        echo "\n$(RED)$(BOLD)FAIL$(RESET)"; \
    fi

install:
	@poetry install

clear:
	@clear
