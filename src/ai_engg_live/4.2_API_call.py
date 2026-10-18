import asyncio
import httpx

#This code shows suppose in case you want to call the 
async def fetch_user(client):
    response = await client.get(
        "https://jsonplaceholder.typicode.com/users/1"
    )

    return response.json()


async def fetch_post(client):
    response = await client.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    return response.json()


async def fetch_todo(client):
    response = await client.get(
        "https://jsonplaceholder.typicode.com/todos/1"
    )

    return response.json()


async def main():

    async with httpx.AsyncClient() as client:

        user, post, todo = await asyncio.gather(
            fetch_user(client),
            fetch_post(client),
            fetch_todo(client),
        )

    print("User:")
    print(user["name"])

    print("\nPost:")
    print(post["title"])

    print("\nTodo:")
    print(todo["title"])


asyncio.run(main())