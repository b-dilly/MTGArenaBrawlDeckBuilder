import requests
import json
import time
import os
import sys
import tkinter as tk
from tkinter import ttk
permanentCount = 0
landCount = 0
nonlandCount = 0
creatureCount = 0
instantCount = 0
sorceryCount = 0
enchantmentCount = 0
artifactCount = 0
planeswalkerCount = 0
battleCount = 0
legendaryCount = 0
totalCards = 0
url_scryfall = 'https://api.scryfall.com/cards/named?exact='
url_CommanderList = 'https://api.scryfall.com/cards/search?q=legal%3Acommander+legal%3Abrawl+is%3Acommander+type%3Acreature'
commanderList = []
deck_list = []
allCards = []
allLands = []
commander_name = ""
#region ALL CARD ARRAYS
nonlandsToRemove = ['mana drain', 'dark ritual', 'rhystic study', 'path to exile', "smothering tithe"]
landsToRemove =['fabled_passage', 'terramorphic_expanse', 'evolving_wilds']
cRocks_cmc2 = ['Arcane Signet', 'Mind Stone', 'Coldsteel Heart']
cRocks_cmc4 = ['Key to the Archive']

cRemoval = ['Meteor Golem', 'Skysovereign, Consul Flagship']
cStaples = []
cFiller = ['Swiftfoot Boots', 'The One Ring', 'Sword of Forge and Frontier', 'Sword of Once and Future', 'Shadowspear', 'Mishra\'s Bauble', 'Roaming Throne', 'Cityscape Leveler', 'Chimil, the Inner Sun','Guardian Idol', 'Worn Powerstone', 'The Irencrag', 'Relic of Legends', 'Hedron Archive', 'The Celestus', 'The Mightstone and Weakstone', 'Portal to Phyrexia', 'Reckoner Bankbuster', 'Mox Amber']

wRemoval = ['Fateful Absence',  'Get Lost', 'Swords to Plowshares', 'The Wandering Emperor', 'Borrowed Time', 'Loran of the Third Path']
wStaples = ['Giver of Runes','Skrelv, Defector Mite', 'Selfless Savior', 'Mana Tithe', 'Loran\'s Escape', 'Pearl Medallion']
wFiller = ['Esper Sentinel', 'Flowering of the White Tree', 'Cathar Commando', 'Stroke of Midnight', 'Planar Disruption', 'Aven Mindcensor', 'Archpriest of Oghma', 'Farewell', 'Reprieve', 'Witch Enchanter', 'Curse of Silence', 'Solitude', 'Skyclave Apparition', 'Heliod\'s Intervention', 'Borrowed Time', 'Spirited Companion', 'Skrelv\'s Hive', ]

uRemoval = ['Wash Away', 'Counterspell', 'Witness Protection', 'Saw it Coming']
uStaples = ['River\'s Rebuke', 'Confounding Conundrum', 'Brainstorm', 'Frogify','Chrome Host Seedshark','Sapphire Medallion']
uFiller = ['Shore Up', 'Faerie Mastermind', 'Treasure Cruise', 'Tale\'s End', 'Memory Lapse',  'Snapcaster Mage', 'Time Warp', 'Search for Azcanta', 'Combat Research',  'Imprisoned in the Moon', 'Deduce', 'Shark Typhoon', 'Cyclonic Rift', 'As Foretold', 'Consider', 'Ledger Shredder', 'Jin-Gitaxias, Progress Tyrant']

bRemoval = ['Thoughtseize', 'Infernal Grasp', 'Bitter Triumph', 'Cut Down', 'Sheoldred\'s Edict', 'Feed the Swarm']
bStaples = ['Phyrexian Arena', 'Black Market Connections', 'Sheoldred, the Apocalypse', 'Reanimate', 'Toxic Deluge','Jet Medallion']
bFiller = ['Cut Down',  'Tenacious Underdog', 'Fell', 'Sheoldred',  'Gix, Yawgmoth Praetor', 'The Cruelty of Gix', 'Junji, the Midnight Sky', 'Jadar, Ghoulcaller of Nephalia', 'Diabolic Intent', 'Morbid Opportunist','Village Rites', 'Breach the Multiverse', 'Liliana, Dreadhorde General']

rRemoval = ['Abrade', 'Lightning Bolt', 'Cathartic Pyre', 'Obliterating Bolt', 'Chaos Warp', 'Volcanic Spite']
rStaples = ['Strike it Rich', 'Goldhound','Valakut Exploration', 'Chandra, Torch of Defiance', 'Fable of the Mirror-Breaker','Ruby Medallion']
rFiller = ['Urabrask, Heretic Praetor', 'Goldspan Dragon', 'Brotherhood\'s End',  'Atsushi, the Blazing Sky','Urabrask\'s Forge', 'Big Score', 'Professional Face-Breaker', 'Bonecrusher Giant', 'Strangle', 'Charming Scoundrel', 'Koth, Fire of Resistance', 'Lizard Blades', 'Reckless Stormseeker', 'Bonehoard Dracosaur']

gRemoval = ['Force of Vigor', 'Bushwhack', 'Bite Down', 'Cankerbloom', 'Thrashing Brontodon']
gStaples = ['Elvish Mystic', 'Birds of Paradise', 'Delighted Halfling', 'Llanowar Elves','Arboreal Grazer', 'Emerald Medallion', ]
gFiller = ['Kami of Bamboo Groves', 'Tyvar\'s Stand', 'Outland Liberator', 'Once Upon a Time', 'Flare of Cultivation', 'Craterhoof Behemoth', 'Cultivate', 'Tireless Provisioner', 'Fanatic of Rhonas', 'Lotus Cobra', 'Nissa, Resurgent Animist', 'Primeval Titan',  'Oracle of Mul Daya', 'The Great Henge',  'Gala Greeters', 'Tamiyo\'s Safekeeping', 'Titan of Industry', 'Vorinclex']
#endregion

def update_deck_stats(card):
    global permanentCount
    global landCount
    global nonlandCount
    global creatureCount
    global instantCount
    global sorceryCount
    global enchantmentCount
    global artifactCount
    global planeswalkerCount
    global battleCount
    global legendaryCount
    global totalCards
    permanent = False
    land = False
    print("Adding: ", card['name'], "-", card['type_line'])
    if 'legendary' in card['type_line'].lower():
            legendaryCount+=1
            #print("Added to Legendary count")
    if 'land' in card['type_line'].split(' //')[0].lower():
            permanent = True
            land = True
            #print("Added to permanent and land count")
    if 'creature' in card['type_line'].lower():
            creatureCount+=1
            permanent = True
            #print("Added to creature and permanent count")
    if 'artifact' in card['type_line'].lower():
            artifactCount+=1
            permanent = True
            #print("Added to artifacr and permanent count")
    if 'planeswalker' in card['type_line'].lower():
            planeswalkerCount+=1
            permanent = True
            #print("Added to permanent and planeswalker count")
    if 'battle' in card['type_line'].lower():
            battleCount+=1
            permanent = True
            #print("Added to permanent and battle count")
    if 'enchantment' in card['type_line'].lower():
            enchantmentCount+=1
            permanent = True
            #print("Added to enchantment and permanent count")
    if 'instant' in card['type_line'].lower():
            instantCount+=1
           # print("Added to instant count")
    if 'sorcery' in card['type_line'].lower():
            sorceryCount+=1
            #print("Added to sorcery count")
    if permanent == True:
          permanentCount+=1
    if land == False:
          nonlandCount+=1
    else:
          landCount+=1
    totalCards +=1
    progress_bar['value'] = progress_bar['value']+1  # Update the progress bar
    root.update_idletasks()  # Update the GUI
def get_deck_stats():
    global permanentCount
    global landCount
    global nonlandCount
    global creatureCount
    global instantCount
    global sorceryCount
    global enchantmentCount
    global artifactCount
    global planeswalkerCount
    global battleCount
    global legendaryCount
    global totalCards
    print("landCount: " + str(landCount))
    print("nonlandCount: " + str(nonlandCount))
    # print("permanentCount: " + str(permanentCount))
    # print("creatureCount: " + str(creatureCount))
    # print("instantCount: " + str(instantCount))
    # print("sorceryCount: " + str(sorceryCount))
    # print("enchantmentCount: " + str(enchantmentCount))
    # print("artifactCount: " + str(artifactCount))
    # print("planeswalkerCount: " + str(planeswalkerCount))
    # print("battleCount: " + str(battleCount))
    # print("legendaryCount: " + str(legendaryCount))
    print("totalCards: " + str(totalCards))
def add_card_to_decklist(card):

    response = requests.get(url_scryfall+card)
    card_data = response.json()
    print(card)
    update_deck_stats(card_data)
    deck_list.append(card)
    time.sleep(0.1)
def format_decklist(deck_list):
    plains_count = deck_list.count("Plains")
    island_count = deck_list.count("Island")
    swamp_count = deck_list.count("Swamp")
    mountain_count = deck_list.count("Mountain")
    forest_count = deck_list.count("Forest")
    wastes_count = deck_list.count("Wastes")
    updated_list = []

    for item in deck_list:
        if item == "Plains":
            # Skip appending additional "Forest"
            continue
        if item == "Island":
            # Skip appending additional "Forest"
            continue
        if item == "Swamp":
            # Skip appending additional "Forest"
            continue
        if item == "Mountain":
            # Skip appending additional "Forest"
            continue
        if item == "Forest":
            # Skip appending additional "Forest"
            continue
        if item == "Wastes":
            # Skip appending additional "Forest"
            continue
        updated_list.append(f"1 {item}")

    # Add the forest count as a single entry
    if plains_count > 0:
        updated_list.append(f"{plains_count} Plains")
    if island_count > 0:
        updated_list.append(f"{island_count} Island")
    if swamp_count > 0:
        updated_list.append(f"{swamp_count} Swamp")
    if mountain_count > 0:
        updated_list.append(f"{mountain_count} Mountain")
    if forest_count > 0:
        updated_list.append(f"{forest_count} Forest")
    if wastes_count > 0:
        updated_list.append(f"{wastes_count} Wastes")

    return updated_list
def create_deck_list(commander_name):
    global deck_list
    global allCards
    global allLands

    print(commander_name)
    commander_name_sanitized = commander_name.replace(' ', '-').replace(',', '').lower()
    print(commander_name_sanitized)
    url_edhrec = f'https://json.edhrec.com/pages/commanders/{commander_name_sanitized}.json'
    

    commander_info = requests.get(url_scryfall+commander_name_sanitized.replace('-', '_'))
    commander_info = commander_info.json()
    print(commander_info['color_identity'])

    response = requests.get(url_edhrec)

    #check if the request was successful
    if response.status_code == 200:
        data = response.json()




    container = data['container']
    json_dict = container['json_dict']
    cardlists = json_dict['cardlists']
    json_dataString = "[\n"
    for cl in cardlists:
        allCards.append(cl['cardviews'])
        if cl['tag'] == 'lands':
            allLands+=(cl['cardviews'])
    # for land in allLands:
    #     print(land['name'])
    for c in allCards:
        for d in c:
            json_dataString += json.dumps(d, indent=4)
    json_dataString += "\n]"
    json_dataString = json_dataString.replace("}{", "},{")
    json_data = json.loads(json_dataString)

    #filter cards with x or more synergy
    

    colorIdentity = commander_info['color_identity']
    colorCount = len(colorIdentity)
    print("Adding removal and staples")

    #add rocks
    for c in cRocks_cmc2:
        if c not in deck_list:
            add_card_to_decklist(c)
    
    
    if commander_info['cmc'] > 4:
        for c in cRocks_cmc4:
            if c not in deck_list:
                add_card_to_decklist(c)
            
    #add removal and staples
    #you get 6 removal spells and 6 staples
    if colorCount > 0:
        for color in colorIdentity:
            if color == 'W':
                removal = wRemoval
                staples = wStaples
            if color == 'U':
                removal = uRemoval
                staples = uStaples
            if color == 'B':
                removal = bRemoval
                staples = bStaples
            if color == 'R':
                removal = rRemoval
                staples = rStaples
            if color == 'G':
                removal = gRemoval
                staples = gStaples
            
            if colorCount == 1:
                for c in removal:
                    add_card_to_decklist(c)
                for c in staples:
                    add_card_to_decklist(c)
            else:
                amountOfCardsToAddFromArray = 6 // colorCount
                remainder = 6 % colorCount
                for i in range(amountOfCardsToAddFromArray):
                    if removal[i] not in deck_list:
                        add_card_to_decklist(removal[i])
                    if staples[i] not in deck_list:
                        add_card_to_decklist(staples[i])
                if remainder != 0:
                    print("Adding remaining removal")
                    for i in range(remainder):
                        if removal[-i] not in deck_list:
                            add_card_to_decklist(removal[-i])
                        if staples[i] not in deck_list:
                            add_card_to_decklist(staples[-i])


    #adding edhrec cards
    minThreshold = 0.9
    maxThreshold = 1
    while nonlandCount < 61:
        filtered_data = [card for card in json_data if card['synergy'] < maxThreshold and card['synergy'] > minThreshold]
        if minThreshold < -0.05:
            break
        maxThreshold -= 0.1
        minThreshold -= 0.1
        print(len(filtered_data))
        for card in filtered_data:
            card_name = card['name']
            card_name = card_name.replace(" ", "_")
            response = requests.get(url_scryfall+card_name)
            card_data = response.json()
            if card_data['legalities']['brawl'] == 'legal' and 'Land' not in card_data['type_line'].split(' //')[0] and "!" not in card_data['name'] and card_data['name'] not in deck_list:
                #it doesn't add cards with ! in their name becasue arena can't import those kinds of cards
                if 'Room' not in card_data['type_line']:
                    #deck_list.append(card_data['name'].split(" //")[0])
                    add_card_to_decklist(card_data['name'].split(" //")[0])
                else:
                    add_card_to_decklist(card_data['name'])
            time.sleep(0.1)
            if nonlandCount >= 61:
                break
    get_deck_stats()
    deck_list = sorted(deck_list)
    print("Adding Lands")
    for card in allLands:
        card_name = card['name']
        card_name = card_name.replace(" ", "_")    
        if card_name.lower() not in landsToRemove:
            response = requests.get(url_scryfall+card_name)
            card_data = response.json()
            #rare lands only!
            if card_data['legalities']['brawl'] == 'legal' and card_data['rarity'] == 'rare':
                add_card_to_decklist(card_data['name'].split(" //")[0])
            time.sleep(0.1)
            if landCount == 38:
                break
    for card in deck_list:
        print(card)
    deck_list = list(dict.fromkeys(deck_list))

    #fill out lands
    if landCount < 38:
        #find amount of lands needed
        landsNeeded = 38 - landCount
        remainder = 0
        print("Lands needed:")
        print(landsNeeded)
        #get color identity
        colorIdentity = commander_info['color_identity']
        colorCount = len(colorIdentity)
        print("Color count:")
        print(colorCount)
        if colorCount > 0:
            if landsNeeded % colorCount == 0:
                amountToAdd = landsNeeded / colorCount
                amountToAdd = int(amountToAdd)
            else:
                remainder = landsNeeded % colorCount
                amountToAdd = landsNeeded // colorCount
                amountToAdd = int(amountToAdd)
            for color in colorIdentity:
                if color == 'W':
                    land = "Plains"
                if color == 'U':
                    land = "Island"
                if color == 'B':
                    land = "Swamp"
                if color == 'R':
                    land = "Mountain"
                if color == 'G':
                    land = "Forest"
                for i in range(amountToAdd):
                    add_card_to_decklist(land)
            if remainder != 0:
                for i in range(remainder):
                    add_card_to_decklist(land)
        else:
            for i in range(landsNeeded):
                add_card_to_decklist("Wastes")

    get_deck_stats()



    for a in deck_list:
        print(a)

    deck_list = format_decklist(deck_list=deck_list)
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    filename = f"{commander_name_sanitized}.txt"
    file_path = os.path.join(downloads_path, filename)
    with open(file_path, "w") as file:
        #write the Commander section
        file.write("Commander\n")
        file.write(f"1 {commander_name}\n\n")

        #write the Deck section
        file.write("Deck\n")
        for c in deck_list:
            file.write(f"{c}\n")
def on_select(event):
    global commander_name
    selected_item = listbox.curselection()
    if selected_item:
        index = selected_item[0]
        selected_item = commanderList[index]
        
        detail_label_1.config(text=f"Name\n {selected_item['name']}")
        if 'card_faces' in selected_item:
            detail_label_2.config(text=f"Mana Cost\n {selected_item['card_faces'][0]['mana_cost']}")
            detail_label_4.config(text=f"Rules Rext\n {selected_item['card_faces'][0]['oracle_text']}", wraplength=300)

        else:
            detail_label_2.config(text=f"Mana Cost\n {selected_item['mana_cost']}")
            detail_label_4.config(text=f"Rules Rext\n {selected_item['oracle_text']}", wraplength=300)
        detail_label_3.config(text=f"Color Identity\n {selected_item['color_identity']}")
    commander_name = selected_item['name'].replace("A-","").split(" //")[0]
    print(f"Selected: {commander_name}")
def on_exit():
    root.destroy()
    sys.exit()    
def on_confirm():
    progress_bar['value'] = 0
    create_deck_list(commander_name=commander_name)
    root.destroy()

#get all commanders available
while url_CommanderList:
    response = requests.get(url_CommanderList)
    stuff = response.json()
    commanderList.extend(stuff['data'])
    url_CommanderList = stuff.get('next_page')
    time.sleep(0.1)

#region UI
# Create the main window
root = tk.Tk()
root.title("Select or Search for Commander")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_exit)

frame = tk.Frame(root)
frame.pack(side=tk.LEFT,fill=tk.Y,padx=10)
# Create a Listbox and attach the scrollbar
listbox = tk.Listbox(frame, height=20, width=60)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)
# Create a scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


# Configure the scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Insert a large number of entries into the Listbox
entries = [commanderList[i]['name'] for i in range(0, len(commanderList))]
for i in range(0, len(entries)):
    #listbox.insert(tk.END, (entries[i]+" {"+"}{".join(commanderList[i]['mana_cost'])+"}"))
    listbox.insert(tk.END, entries[i])

# Bind the selection event to the handler
listbox.bind('<<ListboxSelect>>', on_select)

label_frame = tk.Frame(root)
label_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

detail_label_1 = tk.Label(root, text="Name: ", font=("Helvetica", 14))
detail_label_1.pack(pady=5)

detail_label_2 = tk.Label(root, text="Mana Cost: ", font=("Helvetica", 14))
detail_label_2.pack(pady=5)

detail_label_3 = tk.Label(root, text="Color Identity: ", font=("Helvetica", 14))
detail_label_3.pack(pady=5)

detail_label_4 = tk.Label(root, text="Rules Text: ", font=("Helvetica", 14))
detail_label_4.pack(pady=5)

progress_bar = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
progress_bar.pack(pady=20)

confirm_button = tk.Button(root, text="Confirm Commander", command=on_confirm)
confirm_button.pack(side=tk.BOTTOM, pady=5)


#endregion
# Run the GUI loop
root.mainloop()