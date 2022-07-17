# import requests
# from bs4 import BeautifulSoup
# link = 'https://www.rlmedia.io/is/content/PoloGSI/s7-1298672_rlvideo_vid?video_desktop'
# r = requests.get(link, stream=True)
#
# # download started
# with open('test.mp4', 'wb') as f:
#     for chunk in r.iter_content(chunk_size=1024 * 1024):
#         if chunk:
#             f.write(chunk)

import re
import requests
import os
import json
import random
import time
from load_json import data_from_json
from inventory import sizes
from bs4 import BeautifulSoup

base_dir = os.path.dirname(os.path.abspath(__file__))
json_dir = f"{base_dir}\json"
closet_dir = f"{base_dir}\closet"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
proxy = '57.185.163.54:59394'


def polo_object(link):
    # r = requests.get(link, headers=header, proxies={'http': proxy, 'https': proxy},timeout=3)
    r = requests.get(link, headers=header, timeout=2)
    # r = requests.get(link, timeout=3)

    soup = BeautifulSoup(r.content, 'lxml')
    # print(soup)
    brand_name = soup.find('div', class_="brand-name").text.strip()
    product_name = soup.find('h1', class_="product-name").text.strip()
    try:
        price = soup.find('span', class_="lowblack").text.strip()
    except:
        price = "Unavailable"

    product_id = soup.find('div', class_="product-number")
    product_id = product_id.find('span')['data-masterid']
    product_info = soup.find('div', class_="pdp-details-desk")
    product_description = soup.find('div', id="pdp-description-accordion-panel")
    product_description = product_description.find('p').text.strip()
    product_detail = product_info.find_all("li")
    fitting_details = []
    for detail in product_detail:
        text = detail.text.strip()
        parsed_text = re.sub(r"\s\s+", "", text)
        fitting_details.append(parsed_text)

    main = soup.find('div', class_='pdp-main')
    media = soup.find('div', class_='swiper-wrapper main-images')
    hi_res_imgs = media.find_all('picture', class_="swiper-zoomable")
    hi_res_imgs_links = []
    video_links = []
    #
    for img in hi_res_imgs:
        hi_res_imgs_links.append(img['data-highres-images'])

    try:
        video = soup.find('video')
        video_link = video.find('source')['src']
        video_links.append(video_link)
    except:
        video_link = None

    variations = main.find_all('li', class_='variations-attribute')
    sizes_and_colors = []
    for x in variations:
        sizes_and_colors.append(x.find('a')['data-color'])

    all_sizes = sizes
    all_sizes = [x for x in sizes_and_colors if x in sizes]
    colors = [x for x in sizes_and_colors if x not in sizes]

    return {
        'brand_name': brand_name,
        'product': product_name,
        'description': product_description,
        'price': price,
        'product_id': product_id,
        'fitting_details': fitting_details,
        'img_links': hi_res_imgs_links,
        'video_links': video_links,
        'sizes': all_sizes,
        'colors': colors
    }


# cotton_linen = polo_object(
#     'https://www.ralphlauren.com/men-clothing/classic-fit-checked-cotton-linen-shirt/629215.html?dwvar629215_colorname=Navy%2FWhite&cgid=men-clothing&webcat=men%20clothing')

skeleton_key = []
for k, v in data_from_json.items():
    skeleton_key.append(k)

# print(data_from_json['The RL Fleece Striped Short'])

for i in range(263, 266, 1):
    num = int(random.random() * 10)
    time.sleep(num)
    polo_obj = polo_object(data_from_json[skeleton_key[i]])

    with open(f"{closet_dir}\{polo_obj['product']}.json", "w") as file_for_write:
        os.chdir(closet_dir)
        json.dump(polo_obj, file_for_write, indent=4, sort_keys=True)

    print(f"printed key #{i} {skeleton_key[i]}.json")


# print(len(skeleton_key))
