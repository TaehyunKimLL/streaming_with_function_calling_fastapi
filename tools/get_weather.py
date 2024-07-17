"""
    main file for accessing services.
"""

import os
from datetime import datetime
import aiohttp
import json

from config.main import config

os.environ["OPENWEATHER_API_KEY"] = config.OPENWEATHER_API_KEY


class DirectusDataSource:
    directus_key = '8EesA0w7RHuULCZW6GOXvBY_DDKWCwZt'
    directus_url = 'http://lifelift-directus.eastus2.azurecontainer.io:8055/'

    @staticmethod
    async def get_user_info(user_id: int=1) ->dict:
        """Get User information from directus"""
        try:
            url = DirectusDataSource.directus_url+'items/user_basic_info/'+str(user_id)
            
            params = {
                # "lat": latitude,
                # "lon": longitude,
                # "appid": os.environ.get("OPENWEATHER_API_KEY"),
                # "month": current_month,
                # "day": current_day,
            }
            headers = {
                "Authorization": "Bearer "+DirectusDataSource.directus_key
            }
            result = None
            async with aiohttp.ClientSession() as session:
                async with session.get(url,headers=headers) as response:
                    if response.status != 200:
                        return {"result": "Sorry, I couldn't find the weather information for the given location." }
                    result = await response.json()
            # we format the response to be more user friendly
            return result
        
            # result = result.get("result")
            # if not result:
            #     return (
            #         "Sorry, I couldn't find the weather information for the given location."
            #     )
            # return f"""
            # For given Location:
            #     Mean temperature: {result['temp']['mean']} Kelvin
            #     Mean humidity: {result['humidity']['mean']} %
            #     Mean wind_speed: {result['wind']['mean']} m/s
            #     Mean pressure: {result['pressure']['mean']} hPa
            #     Mean precipitation: {result['precipitation']['mean']} mm
            # """
        except Exception:  # pylint: disable=broad-except
            return {"result": "Sorry, I couldn't find the weather information for the given location." }

    @staticmethod
    async def update_user_info(param,user_id=1):

        print("-----------update_user_info---------------")
        print(param)
        data = param
        try:
            url = DirectusDataSource.directus_url+'items/user_basic_info/'+str(user_id)
            
            params = {
                # "lat": latitude,
                # "lon": longitude,
                # "appid": os.environ.get("OPENWEATHER_API_KEY"),
                # "month": current_month,
                # "day": current_day,
            }
            headers = {
                "Authorization": "Bearer "+DirectusDataSource.directus_key
            }
            result = None
            async with aiohttp.ClientSession() as session:
                async with session.patch(url,json=data,headers=headers) as response:
                    if response.status != 200:
                        return {"result": "Sorry, I couldn't find the weather information for the given location." }
                    result = await response.json()
            # we format the response to be more user friendly
            return "### 기본 정보 갱신\n {}"+str(result['data'])
        
        except Exception:  # pylint: disable=broad-except
            return  "### 기본 정보 갱신 실패\n"
    

        resp = requests.request(method='patch',url=DataSource.directus_url+'items/user_basic_info/'+str(user_id),json=data,headers={'Authorization': 'Bearer '+DataSource.directus_key, 'Contents-Type': 'application/json; chatset=utf-8'})
        print ( resp.text )
        data = json.loads(resp.text)

        return "### 기본 정보 갱신\n {}"+str(data['data'])
    
    @staticmethod
    async def  record_user_activity(param,user_id=1):
        print("-----------update_user_activity---------------")
        print(param)
        data = param
        data['user_id']=user_id 

        try:
            url = DirectusDataSource.directus_url+'items/user_activity'
            headers = {
                "Authorization": "Bearer "+DirectusDataSource.directus_key
            }
            result = None
            async with aiohttp.ClientSession() as session:
                async with session.post(url,json=data,headers=headers) as response:
                    if response.status != 200:
                        return "### 사용자 행동 정보 저장 실패\n"
                    result = await response.json()
            # we format the response to be more user friendly
            return "### 사용자 행동 정보 추가 성공\n {}"+str(result['data'])
        
        except Exception:  # pylint: disable=broad-except
            return  "### 사용자 행동 정보 저장 실패\n"
    
    @staticmethod
    async def  insert_medical_history(param,user_id=1):
        print("-----------update_user_activity---------------")
        print(param)
        data = param
        data['user_id']=user_id 

        try:
            url = DirectusDataSource.directus_url+'items/user_medical_history'
            headers = {
                "Authorization": "Bearer "+DirectusDataSource.directus_key
            }
            result = None
            async with aiohttp.ClientSession() as session:
                async with session.post(url,json=data,headers=headers) as response:
                    if response.status != 200:
                        return "### 의료 정보 저장 실패\n"
                    result = await response.json()
            # we format the response to be more user friendly
            return "### 의료 정보 추가 성공\n {}"+str(result['data'])
        
        except Exception:  # pylint: disable=broad-except
            return  "### 의료 정보 저장 실패\n"

async def get_weather_information(latitude: int, longitude: int) -> str:
    """Gets the weather information for a given latitude and longitude."""
    try:
        url = "https://history.openweathermap.org/data/2.5/aggregated/day"
        current_day, current_month = datetime.now().day, datetime.now().month
        params = {
            "lat": latitude,
            "lon": longitude,
            "appid": os.environ.get("OPENWEATHER_API_KEY"),
            "month": current_month,
            "day": current_day,
        }
        result = None
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status != 200:
                    return "Sorry, I couldn't find the weather information for the given location."
                result = await response.json()
        # we format the response to be more user friendly
        result = result.get("result")
        if not result:
            return (
                "Sorry, I couldn't find the weather information for the given location."
            )
        return f"""
        For given Location:
            Mean temperature: {result['temp']['mean']} Kelvin
            Mean humidity: {result['humidity']['mean']} %
            Mean wind_speed: {result['wind']['mean']} m/s
            Mean pressure: {result['pressure']['mean']} hPa
            Mean precipitation: {result['precipitation']['mean']} mm
        """
    except Exception:  # pylint: disable=broad-except
        return "Sorry, I couldn't find the weather information for the given location."

    