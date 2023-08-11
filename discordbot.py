import discord
import feedparser

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

class RSSReader:
    def __init__(self, url):
        self.url = url

    def fetch_feed(self):
        feed = feedparser.parse(self.url)
        return feed

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} - {client.user.id}')

    rss_url = ""  # Veriyi çekeceği rss adresi
    channel_id =  # Verileri göndereceği kanal ıd lütfen "" vs. koymayın direk yapıştırın örn. 12910319410 

    reader = RSSReader(rss_url)
    feed_data = reader.fetch_feed()

    channel = client.get_channel(channel_id)
    
    if channel:
        await channel.send(f"**{feed_data.feed.title}**\n")
        for entry in feed_data.entries:
            await channel.send(f"**Başlık:** {entry.title}\n**Bağlantı:** {entry.link}\n**Tarih:** {entry.published}\n")
    else:
        print("Kanal bulunamadı.")

# Botun tokenını buraya ekleyin
client.run('TOKEN')
