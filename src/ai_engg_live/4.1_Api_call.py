import asyncio
import httpx


async def fetch_post():

    async with httpx.AsyncClient() as client:

        response = await client.get(
            "https://jsonplaceholder.typicode.com/posts/1"
        )

        return response.json()


async def main():
    post = await fetch_post()
    await asyncio.sleep(10)
    print(post)


asyncio.run(main())