import asyncio
import datetime
import random
import websockets

items = ["물", "커피", "이온음료", "고급 커피", "탄산 음료"]
prices = [450, 500, 550, 700, 750]
remainder = [3, 3, 3, 3, 3]

re_money = {
    "10" : 5,
    "50" : 5, 
    "100" : 5,
    "500" : 5,
}

async def time(websocket, path):
    await websocket.send("start server vending!")
    print("--- client connect ---")
    print("start vending machine server...")

    while True:
        await websocket.send(items)

start_server = websockets.serve(time, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()



