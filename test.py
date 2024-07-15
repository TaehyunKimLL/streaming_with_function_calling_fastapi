from tools.get_weather import DirectusDataSource
import asyncio



async def main():
    result= await DirectusDataSource.get_user_info(user_id=2)
    print (result)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()




