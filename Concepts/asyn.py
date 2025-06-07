import asyncio

class Restaurant:

    async def order_pizza(self):
        print('pizza order process')
        await asyncio.sleep(6)
        print('order pizza completed')

    async def order_beverage(self):
        print('cold drink ordered')  
        await asyncio.sleep(3) 
        print('cold drink served')

    async def order_process(self):
        print('lets order') 
        await asyncio.gather(
            self.order_pizza(),
            self.order_beverage()
        )

    async def order_pack(self):
        print('order for pack is ........loading') 
        await asyncio.sleep(4)  
        print('order for pack completed....')


async def main():
    person1 = Restaurant()

    # ✅ create_task used ONLY for order_pack
    pack_task = asyncio.create_task(person1.order_pack())

    # Run order_process while order_pack runs in background
    await person1.order_process()

    # ✅ Ensure the packing finishes before exiting
    await pack_task

# ✅ Start the event loop
asyncio.run(main())
