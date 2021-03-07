from pyrogram import Client, filters

bot = Client(
    session_name="Robot",
    api_id=1691381,
    api_hash="a4b862a161f7a320d5524730bbf51bf2",
    # config_file="config.ini"
)


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
    for member in client.iter_chat_members('testingssq'):
        if int(USER_CHAT_ID) == int(member.user.id):
            i += 1
            break
    
    if i == 2:
        pass
    else:
        m.delete()
        m.reply_text(
            "Pv locked to this chat(channel/group) @testingssq\nJoin And Send messsage again :)")
        # Add id to Database for don't repat join waring :)
        with open("sended_mdg_id.txt", 'w') as f:
            f.write(f"{USER_CHAT_ID}\n")


bot.run()
