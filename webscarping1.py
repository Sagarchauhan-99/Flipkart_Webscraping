import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name=[]
Prices=[]
Description=[]
Ratings=[]


for i in range(2,12):
 url="https://www.flipkart.com/search?q=mobile+phones+under+25000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_25_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_25_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobile+phones+under+25000%7CMobiles&requestId=0c866d51-d657-4691-af67-8ff1271ba4f2&as-searchtext=mobile+phones+under+25000&page="+str(i)

 r= requests.get(url)
 #print(r)

 soup=BeautifulSoup(r.text,"html.parser")

 box=soup.find("div",class_="DOjaWF gdgoEp")

 names=box.find_all("div",class_="KzDlHZ")
 for i in names:
    name=i.text
    Product_name.append(name)
 #print(Product_name)


 prices=box.find_all("div",class_="Nx9bqj _4b5DiR")
 for i in prices:
    price=i.text
    Prices.append(price)
 #print(Prices)


 desc=box.find_all("ul", class_="G4BRas")
 for i in desc:
    des=i.text
    Description.append(des)
 #print(Description)

 # reviews is showing result for popular section also so used box
 ratings=box.find_all("div",class_="XQDdHH")
 for i in ratings:
    rat=i.text
    Ratings.append(rat)
 #print(Reviews)



max_len = max(len(Product_name), len(Prices), len(Description), len(Ratings))

Product_name.extend([""] * (max_len - len(Product_name)))
Prices.extend([""] * (max_len - len(Prices)))
Description.extend([""] * (max_len - len(Description)))
Ratings.extend([""] * (max_len - len(Ratings)))


'''Product_name = ["Phone1", "Phone2", "Phone3"] (length 3)
Prices = ["$100", "$200"] (length 2)
Description = ["Desc1", "Desc2", "Desc3", "Desc4"] (length 4)
Reviews = ["Review1"] (length 1)
The max_len will be 4, as the Description list has 4 elements.

The extension process will work as follows:

Product_name will be extended by 1 empty string to match max_len:
Product_name.extend([""] * (4 - 3)) -> Product_name = ["Phone1", "Phone2", "Phone3", ""]
Prices will be extended by 2 empty strings:
Prices.extend([""] * (4 - 2)) -> Prices = ["$100", "$200", "", ""]
Description is already of length 4, so no changes:
Description.extend([""] * (4 - 4)) -> Description = ["Desc1", "Desc2", "Desc3", "Desc4"]
Reviews will be extended by 3 empty strings:
Reviews.extend([""] * (4 - 1)) -> Reviews = ["Review1", "", "", ""]
'''

#When creating a DataFrame, all columns (represented by lists in this context) must have the same number of rows. If they don't, pandas will raise an error.

df=pd.DataFrame({"Product name":Product_name,"Prices":Prices,"Description":Description,"Ratings":Ratings})
df.to_csv("C:/Users/syrax/OneDrive/Documents/Data/Jupyter/phones_under25000.csv")
















#print(soup)
#while True:
#  next=soup.find("a",class_="_9QVEpD").get("href")
#  comp_next="https://www.flipkart.com"+next
#  print(comp_next)

#   url=comp_next
#   r=requests.get(url)
#   soup=BeautifulSoup(r.text,"html.parser")