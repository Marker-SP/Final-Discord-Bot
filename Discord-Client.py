import discord
ozellik = discord.Intents.default()

ozellik.message_content = True

client = discord.Client(intents=ozellik)

@client.event
async def on_ready():
    print(f'{client.user} joined.')

@client.event
async def on_message(message):

    mesaj = message.content.lower()
    
    if message.author == client.user:
        return

    if mesaj.startswith('client'):
        await message.channel.send("Hey! Its me! Type < help > to learn more.")

    elif mesaj.startswith('help'):
        await message.channel.send("**The code catagories:**\n"
            "games: gives informations about the game you can choose\n"
            "memes: gives explanation about the joke you didnt get\n"
            "slang terms: gives the meaning of the slang term you didnt understand\n"
            "commands for fun: commands for fun, simple")


    elif mesaj.startswith('games'):
        await message.channel.send("**Codes you can use to learn about games:**\n"
            "\n"
            "- Roblox\n"
            "- Minecraft\n"
            "- Fortnite\n"
            "- Valorant\n"
            "- FIFA\n"
            "- Red Dead Redemption 2\n"
            "- GTA 5\n"
            "- PUBG\n"
            "- Brawl Stars\n"
            "- Clash Royale\n"
            "- Terraria\n"
            "- Stardew Valley\n"
            "- Undertale\n"
            "- Ark: Survival Evolved\n"
            "- Pokemon\n"
            "- Human: Fall Flat\n"
            "- Overwatch\n"
            "- Black Myth: Wukong\n"
            "- Elden Ring\n"
            "- Warcraft")

    elif mesaj.startswith('memes'):
        await message.channel.send("# Popular Internet Memes:\n"
            "**I understood that reference.**     ||Recognition of something familiar (from Captain America)||\n"
            "**This ain't it, chief.**     ||Disapproval; wrong move or idea||\n"
            "**It’s the [blank] for me.**     ||Calling out traits, often humorously or insultingly||\n"
            "**They did surgery on a grape.**     ||Meme of absurd or irrelevant information going viral||\n"
            "**Woman yelling at cat**     ||Meme format for arguing/opposites or confusion||\n"
            "**Me, an intellectual...**     ||Mocking overthinking or unnecessarily complex takes||\n"
            "**Karen**     ||Stereotype of an entitled, rude middle-aged woman||\n"
            "**This guy spittin** 🔥     ||Agreement with someone dropping deep or real truths||\n"
            "**I'm baby.**     ||Acting innocent or wanting comfort/care||\n"
            "**Let him cook.** 🍳     ||Telling people to wait and watch someone do their thing; might be a good idea brewing||\n"
            "**He’s him / I’m him / Himothy**     ||Confident way of saying someone is that guy – elite||\n"
            "\n"
            "If you want to add a meme, let me know!")

    elif mesaj.startswith('slang terms'):
        await message.channel.send(
                "# Slang Terms\n"
                "LOL:   ||Laughing Out Loud||\n"
                "ROFL:   ||Rolling On the Floor Laughing||\n"
                "BRB:   ||Be Right Back||\n"
                "IDK:   ||I Don’t Know||\n"
                "SMH:   ||Shaking My Head (disapproval or disbelief)||\n"
                "FR:   ||For Real (used for emphasis or truth)||\n"
                "NO CAP:   ||No lie / I'm being serious||\n"
                "CAP:   ||Lie or false statement||\n"
                "GOAT:   ||Greatest of All Time||\n"
                "RIZZ:   ||Charisma or flirting ability||\n"
                "SUS:   ||Suspicious or shady behavior||\n"
                "BET:   ||Agreement or approval||\n"
                "SNATCHED:   ||Looking good or fashionable||\n"
                "SHEESH:   ||Expressing excitement or disbelief (often drawn out)||\n"
                "SKIBIDI:   ||Nonsense meme phrase popularized by the Skibidi Toilet meme series||\n"
                "DEAD 💀:   ||“I’m dead” = something is extremely funny (not literal)||\n"
                "SLAY:   ||Doing something exceptionally well or looking amazing||\n"
                "MAIN CHARACTER:   ||Someone who seems to be the center of attention or drama||\n"
                "ATE (and left no crumbs):   ||Nailed it / Did something flawlessly||\n"
                "IT'S GIVING...:   ||Describing vibes or energy someone gives off||\n"
                "TOUCH GRASS:   ||Telling someone to log off and go outside / get a reality check||\n"
                "\n"
                "IF you want to add a slang term, let me know!")

    elif mesaj.startswith('commands for fun'):
        await message.channel.send(
        "# Commands for fun\n"
        "**!mathelp**:     Explains how math commands work.\n"
        "**!password**:    Creates a random password. (not fixed)\n"
        "**!game**:        A basic number guessing game. (not fixed)\n"
        "**!heh**:         Try and see.\n"
        "**!add**:         Adds the numbers you give.\n"
        "**!subtract**:    Subtracts the numbers you give.\n"
        "**!multiple**:    Multiples the numbers you give.\n"
        "**!divide**:      Divides the numbers you give.\n"
        "! Never forget to put the ! before the command")


    elif mesaj.startswith('roblox'):
        await message.channel.send("**Roblox** is an online platform and game creation system that allows users to create, share, and play games (called _experiences_) made by other users."
            " It was launched in 2006 by Roblox Corporation and has grown into one of the most popular platforms for gaming and virtual worlds, especially among children and teenagers."
            " Games on Roblox are made using a programming language called **Lua**, and users can customize their avatars, join virtual communities, and even earn money through the platform’s virtual currency, **Robux**.\n"
            "\n"
            " For more information: https://en.wikipedia.org/wiki/Roblox")

    elif mesaj.startswith('minecraft'):
        await message.channel.send("**Minecraft** is a sandbox video game developed by Mojang Studios, where players can build and explore virtual worlds made of blocks."
            " It was officially released in 2011 and is known for its creative and survival gameplay modes."
            " Story-wise, Minecraft has no fixed narrative, but in **_Survival_** mode, players typically progress by gathering resources,"
            " crafting tools, and eventually reaching _The End_ to defeat the Ender Dragon, considered the game's final boss. The story is minimal and largely driven by the player’s choices.\n"
            "\n"
            "For more information: https://en.wikipedia.org/wiki/Minecraft")

    elif mesaj.startswith('fortnite'):
        await message.channel.send("**Fortnite** is a popular online video game developed by **Epic Games**, released in 2017."
            " It features several game modes, but it's best known for _Battle Royale_, where 100 players compete "
            "to be the last person or team standing on a shrinking island. Players gather resources, build structures, "
            "and fight using various weapons and items. Fortnite is known for its colorful graphics, frequent updates, "
            "and in-game events featuring crossovers with movies, celebrities, and other games. It's free-to-play and available "
            "on multiple platforms.\n"
            "\n"
            "For more information: https://en.wikipedia.org/wiki/Fortnite")
        
    elif mesaj.startswith('valorant'):
        await message.channel.send("**Valorant** is a free-to-play first-person shooter developed by **Riot Games**, released in 2020."
            " It combines tactical gameplay similar to _Counter-Strike_ with unique characters called agents, each with special abilities."
            " Two teams of five players compete in rounds where one team tries to plant a bomb (called the Spike) and the other tries to stop them."
            " Teamwork, strategy, and precision aiming are key to winning.\n"
            "\n"
            "For more information: https://en.wikipedia.org/wiki/Valorant")

    elif mesaj.startswith('fifa'):
        await message.channel.send("**FIFA** is a popular football (soccer) video game series developed by **EA Sports**."
            " It features realistic gameplay, official teams, players, and leagues from around the world. Players can compete in matches,"
            " manage teams, and play online. The series is released annually, with updated rosters and improved graphics.\n"
            "\n"
            "For more information: https://en.wikipedia.org/wiki/FIFA_(video_oyunu_serisi)")

    elif mesaj.startswith('red dead redemption 2') or mesaj.startswith('rdr2'):
        await message.channel.send("**Red Dead Redemption 2** is an action-adventure game developed by **Rockstar Games**,"
            " released in 2018. Set in 1899, it follows Arthur Morgan, an outlaw in the fading Wild West. The game features an open world, rich storytelling, and detailed environments."
            " Players can explore, hunt, fight, and interact with a dynamic world shaped by their choices.\n"
            "\n"
            "For more information: https://en.wikipedia.org/wiki/Red_Dead_Redemption_2")

    elif mesaj.startswith('gta v') or mesaj.startswith('gta 5'):
        await message.channel.send("**GTA 5** _(Grand Theft Auto V)_ is an open-world action-adventure game developed by **Rockstar Games**,"
            " released in 2013. Set in the fictional city of Los Santos, it follows three main characters—Michael, Franklin,"
            " and Trevor—as they commit heists and navigate criminal life. The game features a vast open world, a mix of driving, shooting,"
            " and exploration, and an online multiplayer mode called **GTA Online**.\n"
            "\n"
            "For more information: https://en.wikipedia.org/wiki/Grand_Theft_Auto_V")

    elif mesaj.startswith('pubg'):
        await message.channel.send("**PUBG** _(PlayerUnknown’s Battlegrounds)_ is a battle royale game developed by **PUBG Studios**"
            " and released in 2017. In the game, up to 100 players parachute onto an island and fight to be the last one standing."
            " Players scavenge for weapons, gear, and vehicles while staying within a shrinking safe zone. It’s known for its realistic gunplay, "
            " tactical gameplay, and intense matches. PUBG is available on PC, consoles, and mobile devices.\n"
            "\n"
            "For more information: https://en.wikipedia.org/wiki/PUBG")

    elif mesaj.startswith('brawl stars'):
        await message.channel.send("**Brawl Stars** is a fast-paced multiplayer mobile game developed by **Supercell**."
            " Released globally in 2018, it features various game modes where players battle in teams or solo using unique characters"
            " called Brawlers, each with special abilities. Matches are short and action-packed, with modes like _Gem Grab_,"
            " _Brawl Ball_, _Knockout_ and _Showdown_. The game is colorful, competitive, and regularly updated with new content.\n"
            "\n"
            "For more information: https://en.wikipedia.org/wiki/Brawl_Stars")

    elif mesaj.startswith('clash royale'):
        await message.channel.send("**Clash Royale** is a real-time strategy mobile game developed by **Supercell**,"
            " released in 2016. It combines elements of card collecting, tower defense, and multiplayer battle."
            " Players build a deck of cards featuring troops, spells, and buildings, then use them to battle opponents and destroy their towers."
            " Matches are quick and strategic, and players can earn trophies, chests, and upgrades as they progress.\n"
            "\n"
            "For more information: https://en.wikipedia.org/wiki/Clash_Royale")
        
    elif mesaj.startswith('terraria'):
        await message.channel.send("**Terraria** is a 2D sandbox adventure game developed by **Re-Logic**, first released in 2011."
            " It features exploration, crafting, building, and combat in a randomly generated world. Players can dig underground,"
            " fight monsters, build structures, and discover powerful gear. The game supports both single-player and multiplayer"
            " and is known for its pixel art style and deep gameplay.\n"
            "\n"
            "For more information: https://en.wikipedia.org/wiki/Terraria")

    elif mesaj.startswith('stardew valley'):
        await message.channel.send("**Stardew Valley** is a farming simulation and role-playing game developed by **ConcernedApe**,"
            " released in 2016. Players take over a run-down farm, growing crops, raising animals, mining, fishing,"
            " and forming relationships with townspeople. The game features a relaxing pace, charming pixel art,"
            " and open-ended gameplay with many activities to explore, both solo and in multiplayer.\n"
            "\n"
            "For more information: https://en.wikipedia.org/wiki/Stardew_Valley")

    elif mesaj.startswith('undertale'):
        await message.channel.send("**Undertale** is an indie role-playing game developed by **Toby Fox**, released in 2015."
            " Set in a world inhabited by monsters, players control a human child who falls into an underground realm."
            " The game is known for its unique mechanics, where players can choose to fight or befriend monsters,"
            " leading to different story outcomes. It features a memorable cast of characters, a distinctive 8-bit art style,"
            " and a soundtrack that became iconic. The game emphasizes choice, consequences, and emotional depth.\n"
            "\n"
            "For more information: https://en.wikipedia.org/wiki/Undertale")
        
    elif mesaj.startswith('ark: survival evolved'):
        await message.channel.send("**ARK: Survival Evolved** is an action-adventure survival game developed by **Studio Wildcard**,"
            " released in 2017. Players are stranded on a mysterious island populated by prehistoric creatures, including dinosaurs."
            " The game focuses on survival, where players must gather resources, build shelters, tame and ride dinosaurs,"
            " and defend against other players or hostile creatures. It features both single-player and multiplayer modes,"
            " with a strong emphasis on exploration, crafting, and teamwork.\n"
            "\n"
            "For more information: https://en.wikipedia.org/wiki/Ark:_Survival_Evolved")

    elif mesaj.startswith('pokemon') or mesaj.startswith('info about pokémon'):
        await message.channel.send("**Pokémon** is a media franchise created by _Satoshi Tajiri_ and _Ken Sugimori_,"
            " first launched as a video game in 1996 by _Nintendo_, _Game Freak_, and _Creatures_. It revolves around trainers"
            " capturing and training creatures called Pokémon to battle other trainers' Pokémon. The franchise includes video games,"
            " trading card games, animated TV series, movies, and various merchandise. Players explore various regions, collect Pokémon,"
            " and compete to become the Pokémon Champion.\n"
            "\n"
            "For more information: https://en.wikipedia.org/wiki/Pok%C3%A9mon")

    elif mesaj.startswith('human: fall flat'):
        await message.channel.send("**Human: Fall Flat** is a physics-based puzzle platformer developed by **No Brakes Games**,"
            " released in 2016. Players control a customizable human character named Bob, who navigates through various quirky"
            " and challenging environments. The game focuses on solving puzzles using the character's wobbly, ragdoll-like physics,"
            " where players can interact with objects, manipulate the environment, and collaborate with others in _multiplayer mode_."
            " Its humor and open-ended puzzles make it a fun and light-hearted experience.\n"
            "\n"
            "For more information: https://en.wikipedia.org/wiki/Human:_Fall_Flat")
        
    elif mesaj.startswith('overwatch'):
        await message.channel.send("**Overwatch** is a team-based first-person shooter developed by **Blizzard Entertainment**,"
            " released in 2016. The game features a diverse cast of heroes, each with unique abilities and roles, such as offense,"
            " defense, tank, and support. Players form teams of six and compete in objective-based modes, like capturing points or"
            " escorting payloads. Overwatch emphasizes teamwork, coordination, and strategy, with colorful maps and a lively, futuristic setting."
            " The game is known for its engaging characters and dynamic gameplay.\n"
            "\n"
            "For more information: https://en.wikipedia.org/wiki/Overwatch")

    elif mesaj.startswith('black myth: wukong') or mesaj.startswith('black myth') or mesaj.startswith('wukong'):
        await message.channel.send("**Black Myth: Wukong** is an action RPG developed by **Game Science**,"
            " inspired by the Chinese classic Journey to the West. Players control Sun Wukong, the Monkey King,"
            " as he battles mythical creatures and embarks on a quest for relics. The game features stunning visuals"
            " powered by Unreal Engine 5, fluid combat, and a deep narrative rooted in Chinese mythology."
            " It’s known for its dynamic staff combat, where the weapon can change size and shape, and its emotional storytelling.\n"
            "\n"
            "For more information: https://en.wikipedia.org/wiki/Black_Myth:_Wukong")

    elif mesaj.startswith('elden ring'):
        await message.channel.send("**Elden Ring** is an action RPG developed by **FromSoftware** and published by **Bandai Namco**,"
            " released in 2022. It’s directed by Hidetaka Miyazaki _(known for the Dark Souls series)_ and features world-building by"
            " George R.R. Martin, author of A Song of Ice and Fire. Set in the Lands Between, players take on the role of the Tarnished,"
            " a warrior seeking to restore the Elden Ring and become the _Elden Lord_. The game offers an expansive open world with rich lore,"
            " challenging combat, and deep exploration. Its mix of action, RPG elements, and dark fantasy has earned critical acclaim.\n"
            "\n"
            "For more information: https://en.wikipedia.org/wiki/Elden_Ring")

    elif mesaj.startswith('warcraft'):
        await message.channel.send("**Warcraft** is a franchise of real-time strategy (RTS) and MMORPG games developed by **Blizzard Entertainment**."
            " The series began with Warcraft: Orcs & Humans in 1994, followed by _Warcraft II_ and _Warcraft III_, which became influential in"
            " shaping modern RTS games. The most notable entry is _World of Warcraft_ (WoW), released in 2004, a massively multiplayer online"
            " role-playing game (MMORPG) that allows players to explore the fantasy world of Azeroth, battle creatures, complete quests,"
            " and interact with other players. Known for its rich lore, diverse factions (like Humans, Orcs, Elves),"
            " and immersive world-building, WoW remains one of the most popular and enduring online games ever.\n"
            "\n"
            "For more information: https://en.wikipedia.org/wiki/Warcraft")

    else:
        await message.channel.send(message.content)

client.run(" TOKEN HERE ")