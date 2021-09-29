import aiohttp
import asyncio
import logging

LOGGER = logging.getLogger(__name__)


class Extract():

    def __init__(self, times):
        self.times = times
        self.is_getting_data = True

    def get_number_list(self):
        return asyncio.run(self.__gather_list())

    async def __gather_list(self):
        LOGGER.debug('Starting to extract data...')
        async with aiohttp.ClientSession() as session:
            tasks = []
            page_id = 1
            while(page_id != self.times):
                task = asyncio.ensure_future(
                    self.__get_numbers(session, page_id))
                tasks.append(task)
                page_id += 1
            numbers = await asyncio.gather(*tasks)
        return numbers

    async def __get_numbers(self, session, page_id):
        url = f'http://challenge.dienekes.com.br/api/numbers?page={page_id}'

        while self.is_getting_data:
            try:
                async with session.get(url) as response:
                    result_data = await response.json()
                    return result_data["numbers"]
            except KeyError as err:
                LOGGER.warning(f'Getting simulated error: {err}')
            except aiohttp.client_exceptions.ClientConnectorError as err:
                LOGGER.error(f'Cannot connect to host: {err}')
