from aiogram import Router, types, F, filters
rt = Router()
@rt.message()
async def test(msg: types.Message):
   if msg.contact:
      await msg.answer("ana endi kontakt qabul qilindi")
   else:
      await msg.answer("faqat konakt olaman!")
