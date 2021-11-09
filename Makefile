SOURCEDIR = telegram_attach_bot
SOURCES = $(wildcard $(SOURCEDIR)/*.py)

telegram_attach_bot.pyz: $(SOURCES) requirements.txt
	python -m pip install -r requirements.txt --target telegram_attach_bot
	rm -rf telegram_attach_bot/*.dist-info
	python -m zipapp telegram_attach_bot -p "/usr/bin/env python3"
