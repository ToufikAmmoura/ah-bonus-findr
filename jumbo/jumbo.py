from jumbo_request import get_discounts
from lxml import html

response = get_discounts()
html_content = response.text
parsed_html = html.fromstring(html_content)

xpath_expression = '//h3/a'
selected_elements = parsed_html.xpath(xpath_expression)

for elem in selected_elements:
  href = elem.text_content()
  print(href)