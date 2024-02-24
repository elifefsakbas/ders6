import discord
import random
import time
from discord.ext import commands

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben çevre dostu bir botum!')
    time.sleep(1)
    await ctx.send(f'Haydi biraz konuşalım!')


@bot.command()
async def chat(ctx):
    await ctx.send(f'Merhaba! Ne hakkında konuşalım?')


@bot.command()
async def proje(ctx):
    await ctx.send(f'çevre kirliliği ile alakalı genel bir bilgi almak için oneri komutunu kullan!!')
    time.sleep(1)
    await ctx.send(f'karbonla alakalı bilgi almak istiyorsan karbon komutunu kullan!')
    time.sleep(1)
    await ctx.send(f'bozayılarının korunmasıyla alakalı bilgi almak istiyorsan bozayı komutun kullan!!')
    
   
@bot.command()
async def karbon(ctx):
    await ctx.send(f'Küresel ısınmanın risklerinin azaltılmaması durumunda meydana gelebilecek maliyetler ve makroekonomik etkiler ile ilgili bir analiz çalışması yapılıyor. Sonuçlar iki odak grup toplantısında tartışılıyor.')
    time.sleep()
    await ctx.send(f'Projeyi yürütücülerinden dinlemek için https://youtu.be/Abq1Qvj6NQI ve https://youtu.be/ZBM_23TXnJ8 adreslerini ziyaret edebilirsiniz.')


@bot.command()
async def bozayı(ctx):
    await ctx.send(f'Adamello Brenta Doğa Parkı’na 2 çalışma ziyareti, Sarıkamış Doğa Parkı’na 1 çalışma ziyareti düzenlendi. Uzmanlar ve akademisyenler bozayı ekolojisi, nüfusunun yönetimi, konunun insan boyutunu inceledi.')
    time.sleep()
    await ctx.send(f'Projeyi yürütücülerinden dinlemek için https://youtu.be/oKnfWV1M-DQ, https://youtu.be/jVBOzZ4cLdE ve https://youtu.be/SnBmEcg8UZY adreslerini ziyaret edebilirsiniz.')
 

@bot.command()
async def cevre(ctx):
    await ctx.send(f'Çevre ve kirlilik hakkında bir şey yapmak istiyorsanız oneri komutunu kullanın!')

@bot.command()
async def oneri(ctx):
    await ctx.send(f'Geri dönüşüm ve hangi malzemelerin geri dönüştürülebileceği hakkında bilgi edinin ve günlük yaşamınızda geri dönüştürülebilir malzemeleri kullanın')
    time.sleep(1)
    await ctx.send(f'Eski eşyaları çöpe atmak yerine geri dönüştürün')
    time.sleep(1)
    await ctx.send(f'Tek kullanımlık ürünlerin kullanımını azaltmak için yeniden kullanılabilir ürünler kullanın.')
    time.sleep(1)
    await ctx.send(f'Hangi ürünlerin ve ambalajların geri dönüşüm için en iyi olduğunu araştırın ve satın alırken bunları seçin.')
    time.sleep(1)
    await ctx.send(f'Su kullanmadığınız zamanlarda musluğu açık bırakmayarak su tasarrufu yapın.')
    time.sleep(1)
    await ctx.send(f'Evde ampuller ve klimalar gibi enerji tasarruflu cihazlar kullanın..')
    time.sleep(1)
    await ctx.send(f'Ulaşım masraflarını azaltmak için yerel kaynaklardan yiyecek satın alın.')
    time.sleep(1)
    await ctx.send(f'Araba kullanmak yerine toplu taşıma araçlarını, bisikletleri ve kullanmaya çalışın.')

@bot.command()
async def resim(ctx):
    with open(r'ders6\cevre_resimler\cevre dostu resim.webp', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    time.sleep(1)
    await ctx.send(f'Hep birlikte tercih ve alışkanlıklarımızı değiştirerek çevre kirliliği sorununu çözmeye çalışalım ve dünyamızı temiz tutalım.')
bot.run("your token")
