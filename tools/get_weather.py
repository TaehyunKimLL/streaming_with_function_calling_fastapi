"""
    main file for accessing services.
"""

import os
from datetime import datetime
import aiohttp
import json

from config.main import config

os.environ["OPENWEATHER_API_KEY"] = config.OPENWEATHER_API_KEY
os.environ["DIRECTUS_KEY"] = config.DIRECTUS_KEY
import datetime

class DirectusDataSource:
    directus_key = os.environ["DIRECTUS_KEY"] 
    directus_url = 'http://lifelift-directus.eastus2.azurecontainer.io:8055/'

    @staticmethod
    def get_headers() -> dict:
        """Generate headers for requests."""
        return {"Authorization": "Bearer " + DirectusDataSource.directus_key}
    
    @staticmethod
    async def get_user_info(user_id: int=1) ->dict:
        """Get User information from directus"""
        try:
            url = DirectusDataSource.directus_url+'items/user_basic_info/'+str(user_id)
            
            result = None
            async with aiohttp.ClientSession() as session:
                async with session.get(url,headers=DirectusDataSource.get_headers()) as response:
                    if response.status != 200:
                        return {"result": "Sorry, I couldn't find the weather information for the given location." }
                    result = await response.json()
            # we format the response to be more user friendly
            return result

        except Exception:  # pylint: disable=broad-except
            return {"result": "Sorry, I couldn't find the weather information for the given location." }
        
    @staticmethod
    async def get_user_activity(user_id=1, days=7):
        """Get user activity information from directus for the past week"""
        print("-----------get_user_activity---------------")
        try:
            # Calculate the date one week ago
            date_from = datetime.datetime.now() - datetime.timedelta(days=days)
            date_from_str = date_from.strftime('%Y-%m-%dT%H:%M:%S')  # Convert to string for query

            url = (DirectusDataSource.directus_url + 'items/user_activity'
                   '?filter[user_id][_eq]=' + str(user_id) + 
                   '&filter[date_created][_gte]=' + date_from_str)
            
            result = None
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=DirectusDataSource.get_headers()) as response:
                    if response.status != 200:
                        return {"data": "Sorry, I couldn't find the weather information for the given location." }
                    result = await response.json()
                    return result
            
        except Exception:  # pylint: disable=broad-except
            return {"data": "Sorry, I couldn't find the weather information for the given location." }

    @staticmethod
    async def update_user_info(param,user_id=1):

        print("-----------update_user_info---------------")
        print(param)
        data = param
        try:
            url = DirectusDataSource.directus_url+'items/user_basic_info/'+str(user_id)

            result = None
            async with aiohttp.ClientSession() as session:
                async with session.patch(url,json=data,headers=DirectusDataSource.get_headers()) as response:
                    if response.status != 200:
                        return {"result": "Sorry, I couldn't find the weather information for the given location." }
                    result = await response.json()
            # we format the response to be more user friendly
            return "### 기본 정보 갱신\n {}"+str(result['data'])
        
        except Exception:  # pylint: disable=broad-except
            return  "### 기본 정보 갱신 실패\n"
    
    
    @staticmethod
    async def  record_user_activity(param,user_id=1):
        print("-----------update_user_activity---------------")
        print(param)
        data = param
        data['user_id']=user_id 

        try:
            url = DirectusDataSource.directus_url+'items/user_activity'

            result = None
            async with aiohttp.ClientSession() as session:
                async with session.post(url,json=data,headers=DirectusDataSource.get_headers()) as response:
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
            result = None
            async with aiohttp.ClientSession() as session:
                async with session.post(url,json=data,headers=DirectusDataSource.get_headers()) as response:
                    if response.status != 200:
                        return "### 의료 정보 저장 실패\n"
                    result = await response.json()
            # we format the response to be more user friendly
            return "### 의료 정보 추가 성공\n {}"+str(result['data'])
        
        except Exception:  # pylint: disable=broad-except
            return  "### 의료 정보 저장 실패\n"

    @staticmethod