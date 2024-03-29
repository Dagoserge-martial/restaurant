import requests
import json
from . import models
import asyncio

async def get_from_api(url):
    try:
        req = await requests.get(url)
        data = json.loads(req.text)
    except:
        print('error')
    return data

def visitor_ip_address(request):

    ip=request.client_ip
    if ip=='154.0.27.173':
        req = requests.get('https://api.ipify.org?format=json')
        data = json.loads(req.text)
        ip = data['ip']
    url = "https://ipapi.com/ip_api.php?ip={}"
    try:
        req = requests.get(url.format(ip))
        if req.status_code:
            data = json.loads(req.text)
            latitude = data['latitude']
            longitude = data['longitude']
            pays = data['country_name']
            ville = data['city']
            continent = data['continent_name']
            reseau = data['connection']['isp']
            client = models.Client(
                ip=ip,
                pays=pays,
                ville=ville,
                continent=continent,
                reseau=reseau,
                latitude=latitude,
                longitude=longitude,
                #context processor
            )
            client.save()
            print(ip)
            print(pays)
            print(ville)
            print(reseau)
            print(continent)
            print(latitude)
    except :
        print('error')
    return {'ip':ip}