.PHONY: clean, manual

clean:
	rm -rf __pycache__

manual: brainfuck.py lexer.py
	@python3
	@make clean
