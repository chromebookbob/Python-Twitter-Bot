from PyDictionary import PyDictionary
from random import randint
dictionary=PyDictionary()
import twitter
#put all your special keys here
api = twitter.Api(consumer_key='',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='')


printout = ""
#list of games
gamelist = ['Call of* Duty :* Advanced Warfare', 'The* Elder Scrolls IV:* Oblivion', 'Half Life 2', 'Faster Than* Light', 'Empire :* Total War', 'Call of* Cthulhu:* Dark Corners of* the* Earth', 'Kerbal* Space Program', 'Splinter Cell :* Chaos Theory', 'The* Curse of* Monkey Island', 'Operation Flashpoint :* Cold War Crisis', 'Company of* Heroes 2*', 'Mass Effect 2*', 'Thief II:* The* Metal Age', 'The* Last of* Us', 'Metal Gear Solid 4:* Guns of* the* Patriots', 'Street Fighter II*', 'Dragon Age :* Inquisition', 'The* Legend of* Zelda:* Ocarina* of* Time', 'Red Dead Redemption', 'Time Splitters :* Future Perfect', 'Uncharted 2:* Among Theives', 'Grand Theft Auto :* Vice City', 'Unreal Tournament', 'Middle earth :* Shadow of Mordor*', 'God of* War', 'Rollercoaster Tycoon', 'Mine Craft', 'World of* War Craft', 'League of* Legends', 'Mount and* Blade :* War band', 'System Shock 2*', 'Team Fortress 2*', 'Alien :* Isolation', 'Hit Man :* Blood Money', 'Star Wars :* Knights Of* The* Old Republic', 'Tony* Hawk \'s* Pro Skater 2*', 'Tony* Hawk \'s* Pro Skater 3*', 'Perfect Dark', 'Metroid* Prime', 'Halo:* Combat Evolved', 'Out of* the* Park Baseball 2007*', 'Resident Evil 4*', 'Mass Effect 2*', 'Baldur\'s* Gate II:* Shadows of Amn*', 'Little Big Planet', 'World of Goo', 'Bio Shock Infinite', 'Final Fantasy IX*', 'Devil May Cry', 'Civilization IV*', 'Quake', 'Ninja Gaiden* Black', 'Jet Grind Radio', 'Burnout 3:* Takedown']
#splits a random game from the list and puts the words in another list
splitlist = gamelist[randint(0, (len(gamelist)-1))].split()
for i in range(0, (len(splitlist))):
#here you take each word, get a list of synonyms, choose a random one
	synonym = dictionary.synonym(splitlist[i])
#if the word has a * at the end, it is preserved	
	if splitlist[i][-1] == '*':
	    printout = printout + " " + splitlist[i][:len(splitlist[i])-1]
#if there are no synonyms, the word is preserved
	elif len(synonym) is True:
		printout = printout + " " + splitlist[i]
#random synonym is chosen	
	else:
		printout = printout + " " + synonym[randint(0, (len(synonym)-1))]
#reformats the colons
printout = printout.replace(' :', ':')
#capitalises the words
status = api.PostUpdate(printout.title())
print status.text
