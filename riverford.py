# A script to find the options in the upcoming Riverford veg boxes.
import requests

from brackets import pairs, nested_pairs



if __name__=="__main__":
    boxes = {"small-veg":"http://www.riverford.co.uk/exe/shop/veg-fruit-meat-boxes/veg-fruit-boxes/box-1-small-vegbox-original"}
    for name, box in boxes.items():
        r = requests.get(box)
        page = str(r.content, encoding = "utf-8")
        
        container_name = 'div class="product-long-description"'
        for i, j in pairs(page):
            print(page[i:i+len(container_name)], len(container_name))
            if page[i:i+len(container_name)] == container_name:
                container = page[i:j]
                print(container)
                
        items = []
        for i, j in nested_pairs(container):
            if page[i:i+2] == "li":
                links.append(page[i:j])

        for link in links:
            print(link[8:-1])
