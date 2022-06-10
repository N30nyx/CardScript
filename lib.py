import easyjson
import os
import copy
import random
import json as js
class objects:
    def function(con="",type="def"):
        l = {}
        te = ""
        conn = con.split(" |s ")
        for i in conn:
            te += f"\n\t{i}"

        exec(f"{type} func(*args):\n{te}",l,l)
        return copy.deepcopy(l["func"])
    def json(*args):
        with open(*args,"r") as x:

            return objects.object(data=js.load(x))

    def model(li):
        def obj(*args):
            k = {}

            pos = 0
            for i in li:
                k[i] = args[pos]
                pos += 1






            return objects.object(**k)
        return obj


    class object_class:
        def __init__(self,**kwargs):
            pass







        def call(self,sv,**kwargs):
            d = {"c":self}
            exec(f"x = c.{sv}",d,d)
            if type(d["x"]) == type(self.call):
                return d["x"](**kwargs)
            else:
                return d["x"]
    def object(**k):
        x = copy.deepcopy(objects.object_class)()
        for i in k:
            setattr(x,i,k[i])
        return x

class models:
    def item(*args):
        m = objects.model(["image","description","ability"])
        return m(*args)
    def ext(*args):
        m = objects.model(["color","suit_emoji","rank","sign","title_emoji"])
        return m(*args)
    def card(**k):
        m = objects.model(["suit","value","ext","item","name"])
        vals = []
        k["item"] = models.item(*k["item"])
        k["ext"] = models.ext(*k["ext"])


        return m(k["suit"],k["value"],k["ext"],k["item"],k["name"])
    def deck(theme="light",joker=True,vals={}):
        import random


        d = objects.json("cards.json")
        tr = []
        for x in d.data["deck"]:

            skip = False
            if theme == "light":
                e = "white"
            if theme == "dark":
                e = "black"
            v = d.data["deck"][x]
            if v["rank"] in vals:

                v["rank"] = vals[v["rank"]]
            s = v["suit"]
            t = v["sign"]
            ti = v["title"]
            tb = f"{ti} of {s}"
            if ti == "Joker":
                tb = "Joker"
            imp = f"themes/default-{theme}/{s}_{t}_{e}.png"
            lmap = v["title"]
            if type(v["sign"]) == str and v["sign"] != "A":
                imp = f"themes/default-{theme}/{s}_{lmap}_{e}.png"
            if v["title"] == "Joker":
                imp = f"assets/joker.png"
                v["suit"] = "performing_arts"
            if v["title"] == "Joker" and joker == False:

                skip = True
            if type(v["rank"]) == list:
                v["rank"] = random.choice(v["rank"])


            if skip == False:

                tr.append(models.card(suit=v["suit"],value=v["sign"],ext=[v["color"],v["suit_mark"],v["rank"],v["sign"],v["title_mark"]],item=[imp,tb,""],name=v["title"]))

        return tr


    class cards:
        def __init__(self,deck=None,theme="light",joker=True,v={}):
            if deck == None:
                deck = models.deck(theme,joker,v)
            self.values = {}
            x = deck
            self.pre = x
            self.deck = x
        def add(self,v):
            self.values[v] = o
        def remove(self,v):
            del self.values[v]
        def shuffle(self):
            import random
            random.shuffle(self.deck)
        def sadd(self):
            l = self.len()
            x = self.dadd()
            self.values[str(l)] = x
        def fresh(self):
            self.deck = self.pre
        def dadd(self):
            x = self.deck[0]
            self.deck.remove(x)
            return x
        def deal(self,a=5):

            pos = 0

            for i in range(a):
                self.values[str(pos)] = self.deck[0]
                self.deck.remove(self.deck[0])
                pos += 1
        def list(self):
            x = []
            for i in self.values:
                self.values[i].pos = i
                x.append(self.values[i])
            return x
        def list_str(self):
            s = {}
            for i in self.list():
                s[i.item.description] = i
            return s
        def get(self,pos):
            return self.values[pos]
        def len(self):
            x = 0
            for i in self.values:
                x +=1
            return x
        def sum(self):
            x = 0
            for i in self.values:
                x += self.values[i].ext.rank
            return x


    def player(**k):
        from data import data
        async def dummy(embed=None,content=None,view=None):
            return
        k["cards"] = models.cards(k.get("deck",None),k.get("theme"))
        m = objects.model(["cards","hp","items","lost","id","name","theme","send","obj","no","d"])
        ts = k["obj"]
        if ts.bot == True:
            ts = dummy
        else:
            ts = ts.send
        return m(k["cards"],k["hp"],k["items"],False,k["obj"].id,k["name"],k["theme"],ts,k["obj"],k["no"],data(str(k["obj"].id)))

#car = models.card(suit="spades",value=10,other="",item=["https://images.ctfassets.net/2wgn0n5ijj9k/4LrUZO3Kqx3g3xyIJFW7lZ/3d7fc8565cae1b429cfcc5a4db146b61/Titanium-card-overview.png","10 of spades",None])

#print(str(car.value) + " of " + car.suit + "\nAbout: " + car.item.description)
#for file in os.listdir("themes/default-dark"):
    #os.rename("themes/default-dark/" + file,"themes/default-dark/" + file.replace("Tiles","diamonds").replace("Clovers","clubs").replace("Hearts","hearts").replace("Pikes","spades"))

#print(len(deck))
