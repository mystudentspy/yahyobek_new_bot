from aiogram import Router, types, F
rt = Router()
@rt.message(F.dice)
async def dice(msg: types.Message):
    await msg.answer("bu dice")