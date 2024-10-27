import asyncio
from aiogram import Bot,Dispatcher
from bot_instance import bot
from admin_panel.admin_panel import admin_panel_router
from customer_panel.customer_panel import customer_panel_router

def register_routers(dp:Dispatcher):
    dp.include_router(admin_panel_router)
    dp.include_router(customer_panel_router)
    
async def main():
    dp=Dispatcher()
    register_routers(dp)

    await dp.start_polling(bot,skip_updates=False)



if __name__=="__main__":
    asyncio.run(main())

     