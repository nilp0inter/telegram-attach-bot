TITLE_AND_DESCRITION="""*{title}*

{description}
"""

ONLY_DESCRIPTION="{description}"


def escape_markdown(text):
    return text.replace('\\*', '*').replace('\\`', '`').replace('\\_', '_')\
        .replace('\\~', '~').replace('\\>', '>').replace('\\[', '[')\
        .replace('\\]', ']').replace('\\(', '(').replace('\\)', ')')\
        .replace('*', '\\*').replace('`', '\\`').replace('_', '\\_')\
        .replace('~', '\\~').replace('>', '\\>').replace('[', '\\[')\
        .replace(']', '\\]').replace('(', '\\(').replace(')', '\\)')


def render(tmpl, title, metadata):
    description = '\n'.join(
        f"{escape_markdown(k)}: `{escape_markdown(v)}`"
        for k, v in metadata.items())
    return tmpl.format(title=escape_markdown(title), description=description)
