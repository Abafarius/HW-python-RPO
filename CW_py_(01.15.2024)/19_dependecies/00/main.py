import fast_html as html

text = "Somthing was doing somthning"

hypertext = html.render(html.span(text))

print(hypertext)