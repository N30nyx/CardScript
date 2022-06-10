# CardScript

The engine used in [Neon](https://top.gg/bot/769514287948496916) (under approval) to run card games. (used for discord but can be adapted)

### Usage:
A basic card game where you pick the highest ranked card between the two cards dealt
```python
from lib import *
user = objects.object(name="name",theme="dark",bot=True)
d = models.deck(joker=False,vals={1:[1,2],11:10}) # ace is now 1 or 2 at random and jack is 10, jokers are disabled
p1 = models.player(hp=100,items=[],name=user.name,deck=d,theme=user.theme,obj=user,no="1")
p2 = models.player(hp=100,items=[],name=user.name,deck=d,theme=user.theme,obj=user,no="1")
p1.cards.shuffle()
p1.cards.deal(2)
p2.cards.shuffle()
p2.cards.deal(2)
for card in p1.cards.list_str():
  car = p1.cards.list_str()[card]
  print(f"{car.item.description} ({car.suit})")
x = input("p1: pick a card from 1-2")
p1c = p1.cards.get(int(x-1))
for card in p2.cards.list_str():
  car = p2.cards.list_str()[card]
  print(f"{car.item.description} ({car.suit})")
x = input("p2: pick a card from 1-2")
p2c = p2.cards.get(int(x-1))
if p1c.ext.rank == p2c.ext.rank:
  print("Draw X.X")
  exit()
if p1c.ext.rank > p2c.ext.rank:
  print(f"p1 wins with a {p1c.item.description}")
else:
  print(f"p2 wins with a {p2c.item.description}")
```
