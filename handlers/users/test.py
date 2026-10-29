from aiogram import Router, types,F
rt = Router()
@rt.message(F.photo)
async def test(msg: types.Message):
   await msg.answer("bu rasm")

@rt.message(F.voice)
async def test(msg: types.Message):
    await msg.answer("bu ovoz")