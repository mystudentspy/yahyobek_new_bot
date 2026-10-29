from aiogram import Router, types, F
rt = Router()
@rt.message(F.animation)
async def animation(msg: types.Message):
    await msg.answer("bu animation")
