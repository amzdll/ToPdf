POETRY = poetry run

COLOR_S = \033[92m\033[1m
COLOR_E = \033[0m
LINE = ======================

define print_title
	@printf "$(COLOR_S)%s %s %s$(COLOR_E)\n" "$(LINE)" "$(1)" "$(LINE)"
endef

define print_text
	@printf "$(COLOR_S)%s$(COLOR_E)\n" "$(1)"
endef

.PHONY: all clear check test end_output

all: clear check test end_output

check: mypy_check flake8_check

mypy_check:
	$(call print_title, Running MyPy )
	@echo "converter.py:"  &&  mypy converter || true
	@echo "simple_api.py:"  &&  mypy api || true

flake8_check:
	$(call print_title,Running Flake8)
	@echo "converter.py:" && $(POETRY) flake8 converter || true
	@echo "simple_api.py:" && $(POETRY) flake8 || true

test:
	$(call print_title, Running Unit )
	@echo "test_converter.py:" && green test/test_converter.py || true

end_output:
	@echo "$(COLOR_S)===========================================================$(COLOR_E)"

clear:
	clear