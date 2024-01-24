POETRY = poetry run
COLOR_S = \033[92m\033[1m
COLOR_E = \033[0m
LINE = ======================
WIDTH := $(shell echo "scale=0; $(shell tput cols) / 2" | bc)

#define print_title
#	@printf "$(COLOR_S)%s %s$(COLOR_E)\n" "$(LINE)$(1)$(LINE)"
#endef

.PHONY: all clear check test end_output mypy flake8

define print_title
	@echo "$(COLOR_S)"
	@printf %$$(($(WIDTH) - $$(echo -n '$(1) - 1' | wc -c) / 2))s | tr " " "="
	@printf " %s " "$(1)"
	@printf %$$(($(WIDTH) - $$(echo -n '$(1) - 1' | wc -c) / 2))s | tr " " "="
	@echo "$(COLOR_E)"
endef



all:clear test check
	@echo "$(COLOR_S)"
	@printf %$(shell tput cols)s | tr " " "="
	@echo "$(COLOR_E)"

check: mypy flake8

test:
	$(call print_title,Running Tests)
	@$(POETRY) pytest || true

mypy:
	$(call print_title,Running MyPy)
	@$(POETRY) mypy converter || true
	@$(POETRY) mypy api || true

flake8:
	$(call print_title,Running Flake8)
	@$(POETRY) flake8 converter || true
	@$(POETRY) flake8 api || true

clear:
	clear
