import aiohttp
import asyncio


class Extract():

    async def get_number_list(self):
        async with aiohttp.ClientSession() as session:
            tasks = []
            page_id = 1
            while(page_id != 10000):
                task = asyncio.ensure_future(self.get_numbers(session, page_id))
                tasks.append(task)
                page_id += 1
            numbers = await asyncio.gather(*tasks) 
        return numbers

    async def get_numbers(self, session, page_id):
        url = f'http://challenge.dienekes.com.br/api/numbers?page={page_id}'

        while True:
            try:
                async with session.get(url) as response:
                    result_data = await response.json()
                    # print(f'PAGE_ID={page_id}')
                    # print(f'results {result_data}')
                    # print(f'results {result_data["numbers"]}')
                    if (result_data["numbers"] != []):
                        return result_data["numbers"]
                    else:
                        return
            except RuntimeError:
                pass
