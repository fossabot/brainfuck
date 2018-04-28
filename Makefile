.PHONY: clean, manual, compile, install

clean:
	rm -rf __pycache__

manual: brainfuck.py lexer.py macros.py
	@python3
	@make clean

compile: brainfuck.py lexer.py macros.py
	@python3 brainfuck.py
	@python3 lexer.py
	@python3 macros.py
	# Compilation passed in Python 3.
	@make clean

install: brainfuck.py lexer.py macros.py init
	@chmod +x init
	@./init
