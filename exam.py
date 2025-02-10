import os, shutil, json, requests
from datetime import date, datetime


API_URL = 'https://api.nasa.gov/planetary/apod'

APPID = "w1l6m1ZP44EGTyyrZCPEBhB24wKTpOaeX7z7KoeI"

dt = str(date.today())

params = {'api_key': APPID, 'date': dt}
response = requests.get(API_URL, params=params)
response.raise_for_status()

# print(response.request.url)
print(response.text)

pyVal = json.loads(response.text)



USER_NAME = "PUBLIC"

#C:\Users\Public\Documents

wallpapers_dir = os.path.join('/C:', USER_NAME, 'Documents')

if pyVal['media_type'] == 'image':

    # copy the image to the intended directory
    dt_obj = datetime.strptime(dt, "%Y-%m-%d").date()
    dt_str = dt_obj.strftime("%Y_%m_%d")

    out_file_name = os.path.join(wallpapers_dir, dt_str + '__' + 'nasa_daily.jpg')
    # print(out_file_name)
    response = requests.get(pyVal['url'], stream=True)

    out_file_name = r"C:\PUBLIC\Documents\2025_01_21__nasa_daily.jpg"
    with open(out_file_name, 'wb') as out_file:
        out_file.write(image_data)

    # with open(out_file_name, 'wb') as out_file:
    #     shutil.copyfileobj(response.raw, out_file)
    del response

    print("Mission complete")

else:

    print("No image to download today")