from pyrogram import Client, filters

bot = Client(
    session_name="Robot", #Session Name
    api_id = 123456789, #int of API ID from my.telegram.org
    api_hash= "sdfgbdrseaeerte4345432345yt", # str onf API HASH from my.telegram.org
    # config_file="config.ini"
)
CHANNEL_ID = 'telegram' #without ' @ ' or ' t.me/ '

@bot.on_message(filters.private)
def all_message(client, m):
    USER_CHAT_ID = m.from_user.id
    
    try:
        with open("sended_mdg_id.txt", 'r') as f:  # read database
            for ids in f:
                if int(ids.rstrip()) == int(USER_CHAT_ID):
                    m.delete()
                    return
    except:
        print('Something went wrong !!')
    
    i = 0
    for member in client.iter_chat_members(CHANNEL_ID):
        if int(USER_CHAT_ID) == int(member.user.id):
            i += 1
            break
    
    if i == 2:
        pass
    else:
        m.delete()
        # Here you can edit th message
        m.reply_text(
            f"Pv locked to this chat(channel/group)\n@{CHANNEL_ID}\nJoin And Send messsage again :)")
        # Add id to Database for don't repat join waring :)
        with open("sended_mdg_id.txt", 'w') as f:
            f.write(f"{USER_CHAT_ID}\n")


bot.run()
