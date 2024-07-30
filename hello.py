from bs4 import BeautifulSoup

def add_static_tags(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Update img tags
    for img in soup.find_all('img'):
        if 'src' in img.attrs:
            src = img['src']
            img['src'] = "{% static '" + src + "' %}"
    
    # Update link tags
    for link in soup.find_all('link'):
        if 'href' in link.attrs:
            href = link['href']
            link['href'] = "{% static '" + href + "' %}"
    
    # Update script tags
    for script in soup.find_all('script'):
        if 'src' in script.attrs:
            src = script['src']
            script['src'] = "{% static '" + src + "' %}"
    
    return str(soup)

def update_index_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    updated_html = add_static_tags(html_content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_html)

index_html_path = '../brandtour/templates/index.html'
update_index_html(index_html_path)
print(f"{index_html_path} has been updated with","{% static %} tags.")
