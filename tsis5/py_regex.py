import re

sample = """
My best purchase of the year!

I bought some simple VR glasses two months ago and can't get enough of them.

Don't get me wrong, I am not a gamer, otherwise I would have bought a full-fledged helmet. I need it for much more important things than playing around.

It's simple. I wear it when I go to take a shit.

You wouldn't believe it, ladies and gentlemen, but it's amazing. The sensation of shitting in places that are long, expensive and not always realistic to get to in real life is unparalleled. 

And even if you do get there, 99% of the time you can't shit there anyway.

The day I bought it, I took a shit on the Eiffel Tower. The next day, on Red Square. And then it was on! I shit in squares, museums, concert halls, subways, stadiums!

I shit on the surface of Mars, inside the space station, in the Colosseum, and near the pyramids! The waterfalls - that's a fairy tale! And how wonderful to shit in a car on a roller coaster!

Routine trips to the toilet turned from a dull necessity to an exciting experience, and I can't even imagine how I could read all sorts of uninteresting books during a shit. In the near future, when I stop being stifled by greed, I want to buy a full-size active full-hd helmet so I can shit when I'm fully immersed in reality.

I recommend it to everyone if you haven't tried it. This is truly an inexhaustible source of positivity.

Take care of yourself.

Translated with www.DeepL.com/Translator (free version)

a ab abb abbb abbbb abbbbb
abb ab ab abbbb
ab_ b_ e_ dsds_ f_wdsd __ssa _a ______


Hired Nadar Dias and the Amir to make a toilet. He bought everything he needed, went to work. He arrives in the evening and sees that the toilet is attached to the ceiling. He goes to the workers:
-What the fuck are you doing?
-Why?
-Why did you put the toilet on the ceiling? How do you shit and piss now?
-Why are you yelling? Look!
Amir runs around, pushes himself off one wall with his foot, another foot off the other wall, does a somersault, grabs the toilet, pulls his ass to the toilet and starts shitting.
Piss pours between his legs onto his face and the floor, feces rolls down his back and stomach onto his face and floor, Amir yells in foul language and falls to the floor in a puddle of his own piss and shit. 
He gets up and says to Dias:
-Listen, this really sucks, we need to redo it.

Translated with www.DeepL.com/Translator (free version)
g_g f___g
"""

a = re.findall("a+b*", sample)

b = re.findall("a+b{2,3}", sample)

c = re.findall("[a-z]+_+", sample)

d = re.findall("[A-Z]{1}[a-z]+", sample)

e = re.findall("a{1}.+b{1}", sample)

f = re.sub("[ ,.]", ":", sample)

g = re.sub("_", " ", sample)
g = g.title()
g = re.sub("\s", "", g)

h = re.split("[A-Z]", sample)

i = re.findall('[A-Z][^A-Z]*', sample)

j = re.findall('[A-Z][^A-Z]*', sample)
j = ' '.join(j)
j = j.lower()
j = re.sub("\s", "_", j)