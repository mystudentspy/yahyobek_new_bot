from aiogram import Router, types, filters
rt = Router()
@rt.message()
async def test(msg: types.Message):
   print(msg.forward_date)
   print(msg.forward_from)
   print(msg.forward_from_chat)
   print(msg.forward_origin)