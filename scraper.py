import time
import random
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


columns = ["World Rank", "National Rank", "Name", "Image URLs", "Affiliation", "Country", "D-Index", "Citations", "Publications"]

def get_driver(gecko_path):
    options = Options()
    options.set_preference("general.useragent.override", 
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/127.0.0.1 Safari/537.36"
    )
    return webdriver.Firefox(service=Service(gecko_path), options=options)


def extract_scholar_info(person):
    name = person.find_element(By.XPATH, './/a[starts-with(@href, "/u/")]').text.strip()

    rank_spans = person.find_elements(By.XPATH, './/span[contains(@class, "col--3") and contains(@class, "position")]')
    world_rank = rank_spans[0].text.strip() if len(rank_spans) > 0 else ""
    national_rank = rank_spans[1].text.strip() if len(rank_spans) > 1 else ""

    university_full = person.find_element(By.XPATH, './/span[@class="sh"]').text.strip()
    if ',' in university_full:
        affiliation, country = [x.strip() for x in university_full.rsplit(',', 1)]
    else:
        affiliation = university_full
        country = ""

    img = person.find_element(By.XPATH, './/span//img[@class="lazyload"]')
    image_url = img.get_attribute("src")

    d_index = person.find_element(By.XPATH, './/span[@class="col col--2 col--tablet py-0 ranking"]').text.strip()
    citations = person.find_element(By.XPATH, './/span[@class="col col--2 col--tablet tablet-no-border py-0 ranking"]').text.strip().replace(',', '')
    dblp = person.find_element(By.XPATH, './/span[@class=" col col--3 py-0  ranking no-wrap"]').text.strip().replace(',', '')

    return {
        "World Rank": world_rank,
        "National Rank": national_rank,
        "Name": name,
        "Image URLs": image_url,
        "Affiliation": affiliation,
        "Country": country,
        "D-Index": d_index,
        "Citations": citations,
        "Publications": dblp
    }


def main():
    gecko_path = r"D:\master course\geckodriver-v0.36.0-win64\geckodriver.exe"
    all_scholars = []

    for page in range(1, 21):  # Change to 21 for all pages
        print(f"\n🔄 Scraping page {page}...")
        try:
            driver = get_driver(gecko_path)
            url = f"https://research.com/scientists-rankings/computer-science?page={page}"
            driver.get(url)
            time.sleep(random.uniform(5,4))

            scientists = driver.find_elements(By.XPATH, '//div[@id="rankingItems"]//div[contains(@class, "rankings-content__item")]')
            print(f"✅ Found {len(scientists)} scientists on page {page}.")

            for person in scientists:
                try:
                    scholar_info = extract_scholar_info(person)
                    all_scholars.append(scholar_info)
                except Exception as e:
                    print("⚠️ Skipped one profile:", e)

            driver.quit()
            wait_time = random.uniform(4,7)
            print(f"⏳ Sleeping {wait_time:.1f} seconds before next page...")
            time.sleep(wait_time)

        except Exception as e:
            print(f"❌ Error on page {page}:", e)
            continue

    print(f"\n✅ Scraped total: {len(all_scholars)} profiles.")
    pd.DataFrame(all_scholars, columns=columns).to_csv("best_cs_scientists.csv", index=False)
    print("💾 Data saved to best_cs_scientists.csv")

if __name__ == "__main__":
    main()
