"""
    Module contains utilities to work with browser
"""
from os import path
import webbrowser


def html(body, title=''):
    return """<!DOCTYPE html>
<html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        {body}
    </body>
</html>""".format(body=body, title=title);

title = input('Title: ')
content = input('Content: ')

with open('file.html', 'w') as html_file:
    html_file.write(html(content, title))

uri = 'file://{0}'.format(path.abspath('file.html'))

webbrowser.open(uri);