from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Selam , Ben {bn} 🎵

Grubunuzun sesli aramasında müzik çalabilirim. [sancaklar_federasyon](https://t.me/sancaklar_federasyon) tarafından geliştirilmiştir.
Şu anda desteklediğim komutlar şunlardır:
▶️ /oynat - __Yanıtlanan ses dosyasını veya YouTube videosunu bağlantı üzerinden çalar.__
⏸️ /durdur - __Sesli Sohbet Müziğini Duraklat.__
⏩ /devam - __Sesli Sohbet Müziğine Devam Et.__
⏭️ /atla - __Sesli Sohbette Çalan Geçerli Müziği Atlar.__
🛑 /bitir - __Sırayı temizler ve Sesli Sohbet Müziği'ni sona erdirir.__
🔎 /bul - __Müziği bulup gruba gönderir. Örnek /Bul uzi kervan.__
🔀 /arama - __Müziği direk youtubeden arar ve linkler halinde sıralama yapar.__
↘️ /katil - __Müzik Botunun Asistanını Gruba Çağırır.__
↘️ /ayril - __Müzik Botunun Asistanını Gruptan Çıkartır.__

Beni grubunuza ekleyin ve özgürce müzik çalın !**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👤 Owner 🇹🇷", url="https://t.me/sancaklar_federasyon")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/sohbetutkunu"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/WoopMusicChannel"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "⚒️ Destek Group ⚒️", url="https://t.me/WoopMusicSupport"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Woop Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/WoopMusicChannel")
                ]
            ]
        )
   )


