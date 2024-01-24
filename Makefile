POETRY = poetry run
#  colors
COLOR_S = \033[92m\033[1m
COLOR_ERR = \033[91m\033[1m
COLOR_E = \033[0m

#  other
WIDTH := $(shell echo "scale=0; $(shell tput cols) / 2" | bc)

.PHONY: all clear check test mypy flake8

define print_title
	@echo "$(COLOR_S)"
	@printf %$$(($(WIDTH) - $$(echo -n '$(1) - 1' | wc -c) / 2))s | tr " " "="
	@printf " %s " "$(1)"
	@printf %$$(($(WIDTH) - $$(echo -n '$(1) - 1' | wc -c) / 2))s | tr " " "="
	@echo "$(COLOR_E)"
endef



all:clear test check
	@echo "$(COLOR_S)"
	@printf %$$(($(shell tput cols) - 2))s | tr " " "="
	@echo "$(COLOR_E)"

check: mypy flake8

test:
	$(call print_title,Running Tests)
	@$(POETRY) pytest -q || true

mypy:
	$(call print_title,Running MyPy)
	@if $(POETRY) mypy --pretty ./ ./; then \
        echo  "\n$(COLOR_S)SUCCESS $(COLOR_E)"; \
    else \
        echo "\n$(COLOR_ERR)FAIL$(COLOR_E)"; \
    fi


flake8:
	$(call print_title,Running Flake8)
	@if $(POETRY) flake8 ./; then \
        echo  "\n$(COLOR_S)SUCCESS $(COLOR_E)"; \
    else \
        echo  "\n$(COLOR_ERR)FAIL$(COLOR_E)"; \
    fi

clear:
	clear
