import time
import json
import requests
import datetime
import base64
from PIL import Image
from io import BytesIO
import numpy as np


def getpic():
    category = ''
    width = np.random.randint(640, 1440)
    height = np.random.randint(480, 1080)
    api_url = 'https://api.api-ninjas.com/v1/randomimage?category={}'.format(
        category)
    response = requests.get(api_url, headers={
        'X-Api-Key': 'EVB8kDwkFMCu0zr4CNA1pg==dLdyF9ocKMfBsGA7',
        'Accept': 'image/jpg'},
                            stream=True)
    if response.status_code == requests.codes.ok:
        # result_str = response.content.replace(b'', b'')
        # print(result_str)
        result_str = base64.b64encode(response.content)

        pil_image = Image.open(BytesIO(response.content))
        pil_image.save('test.jpg')

    with open('test.jpg', 'rb') as img:
        img_str = base64.b64encode(img.read())
        img_str = 'data:image/jpeg;base64,' + img_str.decode('utf-8')
        print(img_str)
        return img_str

def sendpic(img):
    url = 'http://nghbrly.eba-qcpx8k2g.us-east-1.elasticbeanstalk.com/api/crawls/'

    title ='it is title:' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(2.718)

    des = 'it is description:' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    pic = img

    data_string='{"points":[{"placeId":"ChIJAcQE9EpawokR-oEfTDYEznQ",' \
                '"name":"5 MetroTech Center","formatted_address":"5 MetroTech Center, Brooklyn, NY 11201, USA","location":{"lat":40.6945463,"lng":-73.98567179999999},"transit":"WALKING"},{"placeId":"ChIJS4zcUUpawokR1yQf2IIXvOU","name":"6 MetroTech Center","formatted_address":"6 MetroTech Center, Brooklyn, NY 11201, USA","location":{"lat":40.6942793,"lng":-73.98649809999999},"transit":"WALKING"}],"directions":{"geocoded_waypoints":[{"geocoder_status":"OK","place_id":"ChIJAcQE9EpawokR-oEfTDYEznQ","types":["premise"]},{"geocoder_status":"OK","place_id":"ChIJS4zcUUpawokR1yQf2IIXvOU","types":["premise"]}],"routes":[{"bounds":{"south":40.69379,"west":-73.98686000000001,"north":40.694230000000005,"east":-73.98547},"legs":[{"distance":{"text":"0.1 mi","value":168},"duration":{"text":"2 mins","value":126},"end_address":"6 MetroTech Center, Brooklyn, NY 11201, USA","end_location":{"lat":40.6938171,"lng":-73.9868573},"start_address":"5 MetroTech Center, Brooklyn, NY 11201, USA","start_location":{"lat":40.6942226,"lng":-73.98564499999999},"steps":[{"distance":{"text":"26 ft","value":8},"duration":{"text":"1 min","value":6},"end_location":{"lat":40.694226,"lng":-73.9857387},"polyline":{"points":"{akwFfiqbMAR"},"start_location":{"lat":40.6942226,"lng":-73.98564499999999},"travel_mode":"WALKING","encoded_lat_lngs":"{akwFfiqbMAR","path":[{"lat":40.69422,"lng":-73.98564},{"lat":40.694230000000005,"lng":-73.98574}],"lat_lngs":[{"lat":40.69422,"lng":-73.98564},{"lat":40.694230000000005,"lng":-73.98574}],"instructions":"Head <b>west</b> on <b>Metrotech Walk</b>","maneuver":"","start_point":{"lat":40.6942226,"lng":-73.98564499999999},"end_point":{"lat":40.694226,"lng":-73.9857387}},{"distance":{"text":"128 ft","value":39},"duration":{"text":"1 min","value":28},"end_location":{"lat":40.6939477,"lng":-73.9854685},"maneuver":"turn-sharp-left","polyline":{"points":"}akwFziqbM^g@HEDCDC@?"},"start_location":{"lat":40.694226,"lng":-73.9857387},"travel_mode":"WALKING","encoded_lat_lngs":"}akwFziqbM^g@HEDCDC@?","path":[{"lat":40.694230000000005,"lng":-73.98574},{"lat":40.69407,"lng":-73.98554},{"lat":40.69402,"lng":-73.98551},{"lat":40.69399000000001,"lng":-73.98549000000001},{"lat":40.693960000000004,"lng":-73.98547},{"lat":40.69395,"lng":-73.98547}],"lat_lngs":[{"lat":40.694230000000005,"lng":-73.98574},{"lat":40.69407,"lng":-73.98554},{"lat":40.69402,"lng":-73.98551},{"lat":40.69399000000001,"lng":-73.98549000000001},{"lat":40.693960000000004,"lng":-73.98547},{"lat":40.69395,"lng":-73.98547}],"instructions":"Sharp <b>left</b>","start_point":{"lat":40.694226,"lng":-73.9857387},"end_point":{"lat":40.6939477,"lng":-73.9854685}},{"distance":{"text":"397 ft","value":121},"duration":{"text":"2 mins","value":92},"end_location":{"lat":40.6938171,"lng":-73.9868573},"maneuver":"turn-right","polyline":{"points":"e`kwFdhqbM^vA?r@C`BAf@"},"start_location":{"lat":40.6939477,"lng":-73.9854685},"travel_mode":"WALKING","encoded_lat_lngs":"e`kwFdhqbM^vA?r@C`BAf@","path":[{"lat":40.69395,"lng":-73.98547},{"lat":40.69379,"lng":-73.98591},{"lat":40.69379,"lng":-73.98617},{"lat":40.693810000000006,"lng":-73.98666},{"lat":40.69382,"lng":-73.98686000000001}],"lat_lngs":[{"lat":40.69395,"lng":-73.98547},{"lat":40.69379,"lng":-73.98591},{"lat":40.69379,"lng":-73.98617},{"lat":40.693810000000006,"lng":-73.98666},{"lat":40.69382,"lng":-73.98686000000001}],"instructions":"Turn <b>right</b><div style=\\"font-size:0.9em\\">Destination will be on the left</div>","start_point":{"lat":40.6939477,"lng":-73.9854685},"end_point":{"lat":40.6938171,"lng":-73.9868573}}],"traffic_speed_entry":[],"via_waypoint":[],"via_waypoints":[]}]}],"request":{"destination":{"placeId":{"placeId":"ChIJS4zcUUpawokR1yQf2IIXvOU"}},"origin":{"placeId":{"placeId":"ChIJAcQE9EpawokR-oEfTDYEznQ"}},"travelMode":"WALKING"},"time":126,"distance":168}}'

    raw_data =  {
    "title": str(title),
    "description": str(des),
    "picture": str(pic),
    "data": json.loads(data_string)
    }

    data = json.dumps(raw_data)

    headers = {
        "Host": "nghbrly.eba-qcpx8k2g.us-east-1.elasticbeanstalk.com",
        "Connection": "keep-alive",
        "Content-Length": str(len(data)),
        "Accept": "application/json, text/plain, */*",
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3Q1X2FjY3QiLCJpZCI6OX0.cj-mrjJqRA1B4iozqutGZKy1kbSWsJTsVmP6L6nZbaU",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
        "Origin": "http://nghbrly.eba-qcpx8k2g.us-east-1.elasticbeanstalk.com",
        "Referer": "http://nghbrly.eba-qcpx8k2g.us-east-1.elasticbeanstalk.com/create",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9"
    }

    print(raw_data['picture'])

    response = requests.post(url, headers=headers, data=data)
    print(response.status_code)
    print(response.text)


if __name__ == "__main__":
    i = 0
    while i < 20:
        img=getpic()
        while len(img) > 150000:
            img = getpic()
        sendpic(img)
        time.sleep(np.random.uniform(1,5))
        i += 1

