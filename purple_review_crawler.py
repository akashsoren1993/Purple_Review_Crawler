import requests
import json
import pandas as pd
import concurrent.futures






def get_rating_count(url):

  payload = {}
  headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,de;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'environment=prod; is_robot=false; client_ip=152.58.20.89; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VfaWQiOiJDMU5SNTROWVFoRmlkMWZPaDEiLCJtb2RlX2RldmljZSI6ImRlc2t0b3AiLCJtb2RlX2RldmljZV90eXBlIjoid2ViIiwiaWF0IjoxNjkwMjczMTk0LCJleHAiOjE2OTgwNDkxOTQsImF1ZCI6IndlYiIsImlzcyI6InRva2VubWljcm9zZXJ2aWNlIn0.6Nr0Xb0TcyRvGgHWUTV_AM4h0gSCfHzD1vfYzDMqoyE; visitorppl=C1NR54NYQhFid1fOh1; device_id=C1NR54NYQhFid1fOh1; listingVers=listingV1; generic_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VfaWQiOiJLSXdZY1Z2Yzgwdld2QmV1TUoxMjcwMDExNTgwMjA1ODY3IiwibW9kZV9kZXZpY2UiOiJkZXNrdG9wIiwibW9kZV9kZXZpY2VfdHlwZSI6IndlYiIsImlhdCI6MTU4NDA4NjYzOCwiZXhwIjoyNjkwNjQ3NTI0LCJhdWQiOiJ3ZWIiLCJpc3MiOiJ0b2tlbm1pY3Jvc2VydmljZSJ9.RdrqkTAPBDh0Qe-605a_dOYoXOOPcJe33f6tuMioKi8; generic_visitorppl=KIwYcVvc80vWvBeuMJ1270011580205867; is_webview=false; mode_device=desktop; referrer=www.google.com; utm_medium=organic; utm_campaign=google-organic; gclid=; pclid=; fbclid=; session_initiator=google; __storage__giftBox={"itemCount":0}; __storage__screen_ab_testing={"listing_ab_testing":[{"value":"g","types":"search,brand,category,landingpages","key":"ab_experiment_listing"}]}; __storage__nc={"cc":0}; __storage__isEliteUser=false; __storage__isLoggedIn=false; sessionCreatedTime=1690273196; __storage__modeDevice=desktop; __storage__google_yolo_enabled=true; __storage__isRobot=false; beautyProfilePopup=1; isSessionDetails=true; __storage__searchinitResp={"data":{"Todays_deal":[{"item_type":"product","id":"129718","adunit_id":null,"name":"Stay Quirky Liquid Lipstick, Red - Too Hot For Date Night 7 (4.5 ml)","slug":"stay-quirky-liquid-lipstick-red-too-hot-for-date-night-7","itemurl":"/product/stay-quirky-liquid-lipstick-red-too-hot-for-date-night-7","category_name":"Lipstick","stock_status":"1","p_group":null,"thumb_image_url":"https://media6.ppl-media.com/tr:h-235,w-235,c-at_max/static/img/product/129718/stay-quirky-liquid-lipstick-red-too-hot-for-date-night-7_9_display_1653476220_34c5752d.jpg","primary_image_url":"https://media6.ppl-media.com/tr:h-550,w-550,c-at_max/static/img/product/129718/stay-quirky-liquid-lipstick-red-too-hot-for-date-night-7_9_display_1653476220_34c5752d.jpg","avg_rating":4,"total_rating":"10205","product_seller_id":"231538","seller_id":"555","price":"449","mrp":"449","offer_price":"427","our_price":"427","specialofferPrice":"427","iselite":"1","discount":"5","offer_discount":0,"total_discount":5,"offer_text":"","discount_price":22,"offers_pd":{"count":0,"title":""},"isincart":0,"iscart":0,"incart":0,"isliked":0}],"Trending_searches":["good vibes","goodvibes","Lip"],"Last_updated_time":1690273018,"x_id":"api/v2/shop/searchinit"},"expiry_time":1690276797970}; _gcl_au=1.1.1650301697.1690273198; _ga=GA1.1.1062681566.1690273200; _fbp=fb.1.1690273200183.423415336; __storage__fcm_time_stamp=1690270200000; is_first_session=false; session_id=3ac59ad59a07595d8c10b659919c1802; _ga_FWGKK004RG=GS1.1.1690273200.1.1.1690274870.60.0.0; sessionExpiryTime=1690276817; utm_source=Direct',
    'Referer': 'https://www.purplle.com/product/good-vibes-age-defying-serum-vitamin-c-and-vitamin-e-30-ml-1-34/reviews',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'is_SSR': 'false',
    'mode_device': 'desktop',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VfaWQiOiJDMU5SNTROWVFoRmlkMWZPaDEiLCJtb2RlX2RldmljZSI6ImRlc2t0b3AiLCJtb2RlX2RldmljZV90eXBlIjoid2ViIiwiaWF0IjoxNjkwMjczMTk0LCJleHAiOjE2OTgwNDkxOTQsImF1ZCI6IndlYiIsImlzcyI6InRva2VubWljcm9zZXJ2aWNlIn0.6Nr0Xb0TcyRvGgHWUTV_AM4h0gSCfHzD1vfYzDMqoyE',
    'visitorppl': 'C1NR54NYQhFid1fOh1'
  }


  response = requests.request("GET", url, headers=headers, data=payload)

  # print(response.text)

  json_output=json.loads(response.text)
  review_count=json_output['reviews']['totalCount']
  product_rating = json_output['reviewStats']['avgRating']

  return review_count,headers,payload,product_rating

def get_review_data(url,url_num):
  final_data = []
  review_count,headers,payload,product_rating=get_rating_count(url)

  page_nums=round(review_count/10)
  print(page_nums)

  for page_num in range(1,page_nums):
    print(page_num)
    url="https://www.purplle.com/neo/catalog/reviews?productId={}&page={}&sortBy=mr".format(product_id,page_num)

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)

    json_output = json.loads(response.text)
    # review_count = json_output['reviews']['totalCount']

    data=[]
    for i in range(0,len(json_output['reviews']['review'])):
      try:
        author=json_output['reviews']['review'][i]['userDetails']['name']
      except:
        author=None
      try:
        title=json_output['reviews']['review'][i]['title'],
      except:
        title=None
      try:
        review=json_output['reviews']['review'][i]['body']
      except:
        review=None
      try:
        review_rating=json_output['reviews']['review'][i]['rating']
      except:
        review_rating=None
      try:
        date=json_output['reviews']['review'][i]['createdOn']
      except:
        date=None


      query={
      "Author":author,
      "title":title,
      "review" :review,
      "review_rating":review_rating,
      "date":date,
      "product_id":product_id,
      "Review Count":review_count,
        "product rating":product_rating
      }

      # print(query)

      data.append(query)


    final_data.extend(data)

  df=pd.DataFrame(final_data)
  df.to_csv("data"+str(url_num)+".csv",index=False)


with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
  read_file = pd.read_csv(r"C:\Users\sagar\Dropbox\PC\Downloads\Purplle_Product_ids_Only.csv")
  product_ids = read_file['Product id'].to_list()
  futures = []
  url_num = 1

  for product_id in product_ids:
    print(product_id)
    url = "https://www.purplle.com/neo/catalog/reviews?productId={}&page=1&sortBy=mr".format(product_id)
    future = executor.submit(get_review_data, url, url_num)
    futures.append(future)
    url_num += 1
  concurrent.futures.wait(futures)

