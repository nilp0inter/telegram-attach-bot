SOURCEDIR = telegram_attach_bot
SOURCES = $(wildcard $(SOURCEDIR)/*.py)

attachbot: $(SOURCES) requirements.txt
	python -m pip install -r requirements.txt --target telegram_attach_bot
	rm -rf telegram_attach_bot/*.dist-info
	python -m zipapp telegram_attach_bot -p "/usr/bin/env python3" --output attachbot
