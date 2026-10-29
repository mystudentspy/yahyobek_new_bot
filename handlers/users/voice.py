from aiogram import Router, types, F
rt = Router()
@rt.message(F.voice)
async def voice(msg: types.Message):
    await msg.answer("bu ovozli habar")
