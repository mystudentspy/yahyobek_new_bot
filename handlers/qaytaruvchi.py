from aiogram import Router, types, F, filters
rt = Router()
hammasi = [
   "CgACAgQAAxkBAAI3M2rgNcDAG8m0N9t_vSA0l5-2KBCOAAKDAwAC-pKkUoq150fdTkUEPQQ",
   "AgACAgIAAxkBAAI3PGrgNkd0yN9t-5W6dKDWGxqfuHVMAAKRG2sbN9wAAUtcYSol5wTocwEAAwIAA3gAAz0E"
]
@rt.message()
async def test(msg: types.Message):
   await msg.answer_photo(hammasi[1])
   if msg.contact:
      c = msg.contact
      n = "barcha malumotlar:\n"
      n += f"{c.first_name} {c.last_name}\n"
      n += f"{c.phone_number}"
      await msg.answer(n)
      # if msg.contact.user_id == msg.from_user.id:
      #    await msg.answer("bu rostdan sizniki")
      # else:
      #    await msg.answer("bu boshqa insonni nomer")
   elif msg.dice:
      n = f"ushbu {msg.dice.emoji} ning qiymati 100%\n"
      n += f"{msg.dice.value} bo'ladi!"
      await msg.answer(n)
   elif msg.animation:
      print(msg.animation)
   # print(msg.photo)