import requests
import bs4
list=[]
list.append("https://forasna.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%AE%D8%A7%D9%84%D9%8A%D8%A9?query=%D9%85%D9%86%D8%AF%D9%88%D8%A8%20%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA")
list.append("https://forasna.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%AE%D8%A7%D9%84%D9%8A%D8%A9?query=%D9%85%D9%86%D8%AF%D9%88%D8%A8%20%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA&start=20")
list.append("https://forasna.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%AE%D8%A7%D9%84%D9%8A%D8%A9?query=%D9%85%D9%86%D8%AF%D9%88%D8%A8%20%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA&start=40")
list.append("https://forasna.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%AE%D8%A7%D9%84%D9%8A%D8%A9?query=%D9%85%D9%86%D8%AF%D9%88%D8%A8%20%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA&start=60")
list.append("https://forasna.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%AE%D8%A7%D9%84%D9%8A%D8%A9?query=%D9%85%D9%86%D8%AF%D9%88%D8%A8%20%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA&start=80")
list.append("https://forasna.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%AE%D8%A7%D9%84%D9%8A%D8%A9?query=%D9%85%D9%86%D8%AF%D9%88%D8%A8%20%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA&start=100")
list.append("https://forasna.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%AE%D8%A7%D9%84%D9%8A%D8%A9?query=%D9%85%D9%86%D8%AF%D9%88%D8%A8%20%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA&start=120")
list.append("https://forasna.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%AE%D8%A7%D9%84%D9%8A%D8%A9?query=%D9%85%D9%86%D8%AF%D9%88%D8%A8%20%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA&start=140")
list.append("https://forasna.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%AE%D8%A7%D9%84%D9%8A%D8%A9?query=%D9%85%D9%86%D8%AF%D9%88%D8%A8%20%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA&start=160")
list.append("https://forasna.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%AE%D8%A7%D9%84%D9%8A%D8%A9?query=%D9%85%D9%86%D8%AF%D9%88%D8%A8%20%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA&start=180")
list.append("https://forasna.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%AE%D8%A7%D9%84%D9%8A%D8%A9?query=%D9%85%D9%86%D8%AF%D9%88%D8%A8%20%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA&start=200")
list.append("https://forasna.com/%D9%88%D8%B8%D8%A7%D8%A6%D9%81-%D8%AE%D8%A7%D9%84%D9%8A%D8%A9?query=%D9%85%D9%86%D8%AF%D9%88%D8%A8%20%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA&start=220")

jop_title = []
company_name = []
#location_address1 = []

for i in range(len(list)):
    result = requests.get(list[i])
    src = result.content
    # print(src)

    soup = bs4.BeautifulSoup(src, "html.parser")
    # print(soup)

    # pages = soup.find_all("li", {"class":"active pag-current"})

    jop_titles = soup.find_all("h2", {"class": "job-title"})
    # print(jop_titles)
    company_names = soup.find_all("span", {"class": "company-name"})
    # print(company_names)
    #location_address = soup.find_all("span", {"class": "location"})
    # print(location_address)

    for i in range(len(jop_titles)):
        jop_title.append(jop_titles[i].text[2:len(jop_titles[i].text) - 3])

    for i in range(len(company_names)):
        company_name.append(company_names[i].text[2:len(company_names[i].text) - 3])

   # for i in range(len(location_address)):
      #  location_address1.append(location_address[i].text[0:len(location_address[i].text) - 2])

counter = 1
for i in zip(jop_title, company_name):
    print("the information of the job number ", counter)
    print("the job title is " + i[0])
    print("the company is " + i[1])
    #print("the job location_address is " + i[2])
    print()
    counter += 1