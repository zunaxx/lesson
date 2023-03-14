import requests
from bs4 import BeautifulSoup

url = "https://health-diet.ru/table_calorie/"

req = requests.get(url)
src = req.text
print(src)

with open("index.html", "w", encoding="utf-8") as file:
    file.write(src)
# print(src)
#
soup = BeautifulSoup(src, "lxml")

title = soup.title
print(title)
print(title.text)
print(title.string)


page_h1 = soup.find("h1")
print(page_h1)

page_all_h1 = soup.find_all("h1")
print(page_all_h1)

for item in page_all_h1:
    print(item.text)








all_a = soup.find_all("a")
print(all_a)

for item in all_a:
    item_text = item.text
    item_url = item.get("href")
    print(f"{item_text}: {item_url}")



# post_div = soup.find(class_="post__text").find_parent()
# print(post_div)
#
# post_div = soup.find(class_="post__text").find_parent("div", "user__post")
# print(post_div)
#
# post_divs = soup.find(class_="post__text").find_parents("div", "user__post")
# print(post_divs)


# next_el = soup.find(class_="post__title").next_element.next_element.text
# print(next_el)
#
# next_el = soup.find(class_="post__title").find_next().text
# print(next_el)
#
#
# next_sib = soup.find(class_="post__title").find_next_sibling()
# print(next_sib)
#
# prev_sib = soup.find(class_="post__date").find_previous_sibling()
# print(prev_sib)
#
# post_title = soup.find(class_="post__date").find_previous_sibling().find_next().text
# print(post_title)
#
# links = soup.find(class_="some__links").find_all("a")
# print(links)
#
# for link in links:
#     link_href_attr = link.get("href")
#     link_href_attr1 = link["href"]
#
#     link_data_attr = link.get("data-attr")
#     link_data_attr1 = link["data-attr"]
#
#     print(link_href_attr1)
#     print(link_data_attr1)
#
# find_a_by_text = soup.find("a", text="Одежда")
# print(find_a_by_text)
#
# find_a_by_text = soup.find("a", text="Одежда для взрослых")
# print(find_a_by_text)
#
# find_a_by_text = soup.find("a", text=re.compile("Одежда"))
# print(find_a_by_text)
#
# find_all_clothes = soup.find_all(text=re.compile("([Оо]дежда)"))
# print(find_all_clothes)




