from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("help"))
async def help(msg: types.Message):
    await msg.answer("sizga nima yordam beraolaman?")
    n = "bizning barcha kamandalarimiz:\n"
    n += "/settings\n"
    n += "/info\n"
    n += "/car\n"
    n += "/fruit\n"
    await msg.answer(n)