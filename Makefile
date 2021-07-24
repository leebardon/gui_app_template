.PHONY: lint clean


clean: 
	@find . -regex '^.*\(__pycache__\|\.py[co]\)' -delete
	 

lint:
	@black src runscript.py
