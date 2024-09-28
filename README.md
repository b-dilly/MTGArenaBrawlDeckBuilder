# MTGArenaBrawlDeckBuilder
This python script uses EDHRec's api and Scryfall's api to construct an MTGArena deck for the Brawl format

## Instructions for Use
When you run the script, a UI pops up and allows you to select a brawl deck to generate. Select a commander, then click the "Select Commander" button. After the generator is finished, the UI will close and the generated deck will be exported to your downloads folder.

## How it Works
After you select your sommander and click "Select Commander", an api request is made querying the commander's name from EDHRec's api.

The api request returns the commander's color identity, and uses that to determine which cards from the ALL CARD ARRAYS region to add.

All cards in the cRocks_cmc2 array are automatically added, followed by the color's removal, then the color's staples. If the commander's cmc is greater than 4, cards from the cRocks_cmc4 array are added. In 
this script, there is only one, but you can add more.

Adds all cards with the highest synergy values until it adds 61 nonlands. 

Adds all rare lands until it can't find any more OR it adds 38 lands. If it doesn't find 38 lands, it then fills the list with the appropriate basics until it adds 38 lands.

## How to Customize
You can customize which cards get added/excluded before the deckbuilder generates a deck.
In the ALL CARD ARRAYS region, you'll see arrays containing card names. Add/Remove cards from these arrays to control which cards are added/excluded.
Explainations:
  nonlandsToRemove - Add/Remove cards from this array if you would like to exclude them from being added to the deck list
  
  landsToRemove - Same idea, but with lands. These two arrays can be combines, but mixing lands and nonlands are messy in my opinion
  
  cRocks_cmc2 - Rocks/Cards that initially get added. They don't have to be 2cmc. You can throw whatever rocks you want in here.
  
  cRocks_cmc4 - Rocks/Cards that get added when the commander's cmc is greater than 4
  
  xRemoval - Removal cards I frequesntly add when building a deck. Every deck starts out with 6 removal spells.
  
  xStaples - Same idea, but with staples. Every deck starts with 6 staples
  
  xFiller - Currently not in use, but contains useful cards. 

## Limitations
Since this deck builder only generates decks using EDHRec's database, MTGArena's Alchemy cards must be manually added. You also cannot create a brawl deck using Planeswalkers.
