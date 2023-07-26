import itertools
import os
import platform
import re
import sys
import time
from optparse import OptionParser

out = sys.stdout

TEXT_ENCODING = 'utf8'
NEWLINES = 'lf'

# Compatibility
try:
    xrange
except NameError:
    xrange = range

def text_open(fn, mode, encoding=None):
    try:
        return open(fn, mode, encoding=encoding or TEXT_ENCODING)
    except TypeError:
        if 'r' in mode:
            mode += 'U' # 'U' mode is needed only in Python 2.x
        return open(fn, mode)

def get_file_sizes():
    for s in ['20 KB', '400 KB', '10 MB']:
        size, unit = s.split()
        size = int(size) * {'KB': 1024, 'MB': 1024 ** 2}[unit]
        yield s.replace(' ', ''), size

def get_binary_files():
    return ((name + ".bin", size) for name, size in get_file_sizes())

def get_text_files():
    return (("%s-%s-%s.txt" % (name, TEXT_ENCODING, NEWLINES), size)
        for name, size in get_file_sizes())

def prepare_files():
    print("Preparing files...")
    # Binary files
    for name, size in get_binary_files():
        print(name)
        if os.path.isfile(name) and os.path.getsize(name) == size:
            continue
        with open(name, "wb") as f:
            f.write(os.urandom(size))
    # Text files
    chunk = []
    with text_open(__file__, "r", encoding='utf8') as f:
        for line in f:
            if line.startswith("# <iobench text chunk marker>"):
                break
        else:
            raise RuntimeError(
                "Couldn't find chunk marker in %s !" % __file__)
        if NEWLINES == "all":
            it = itertools.cycle(["\n", "\r", "\r\n"])
        else:
            it = itertools.repeat(
                {"cr": "\r", "lf": "\n", "crlf": "\r\n"}[NEWLINES])
        chunk = "".join(line.replace("\n", next(it)) for line in f)
        if isinstance(chunk, bytes):
            chunk = chunk.decode('utf8')
        chunk = chunk.encode(TEXT_ENCODING)
    for name, size in get_text_files():
        if os.path.isfile(name) and os.path.getsize(name) == size:
            continue
        head = chunk * (size // len(chunk))
        tail = chunk[:size % len(chunk)]
        # Adjust tail to end on a character boundary
        while True:
            try:
                tail.decode(TEXT_ENCODING)
                break
            except UnicodeDecodeError:
                tail = tail[:-1]
        with open(name, "wb") as f:
            f.write(head)
            f.write(tail)


prepare_files()


# -- This part to exercise text reading. Don't change anything! --
# <iobench text chunk marker>

"""
1.
Gáttir allar,
áðr gangi fram,
um skoðask skyli,
um skyggnast skyli,
því at óvíst er at vita,
hvar óvinir
sitja á fleti fyrir.

2.
Gefendr heilir!
Gestr er inn kominn,
hvar skal sitja sjá?
Mjök er bráðr,
sá er á bröndum skal
síns of freista frama.

3.
Elds er þörf,
þeims inn er kominn
ok á kné kalinn;
matar ok váða
er manni þörf,
þeim er hefr um fjall farit.

4.
Vatns er þörf,
þeim er til verðar kemr,
þerru ok þjóðlaðar,
góðs of æðis,
ef sér geta mætti,
orðs ok endrþögu.

5.
Vits er þörf,
þeim er víða ratar;
dælt er heima hvat;
at augabragði verðr,
sá er ekki kann
ok með snotrum sitr.

6.
At hyggjandi sinni
skyli-t maðr hræsinn vera,
heldr gætinn at geði;
þá er horskr ok þögull
kemr heimisgarða til,
sjaldan verðr víti vörum,
því at óbrigðra vin
fær maðr aldregi
en mannvit mikit.

7.
Inn vari gestr,
er til verðar kemr,
þunnu hljóði þegir,
eyrum hlýðir,
en augum skoðar;
svá nýsisk fróðra hverr fyrir.

8.
Hinn er sæll,
er sér of getr
lof ok líknstafi;
ódælla er við þat,
er maðr eiga skal
annars brjóstum í.
"""

"""
C'est revenir tard, je le sens, sur un sujet trop rebattu et déjà presque oublié. Mon état, qui ne me permet plus aucun travail suivi, mon aversion pour le genre polémique, ont causé ma lenteur à écrire et ma répugnance à publier. J'aurais même tout à fait supprimé ces Lettres, ou plutôt je lie les aurais point écrites, s'il n'eût été question que de moi : Mais ma patrie ne m'est pas tellement devenue étrangère que je puisse voir tranquillement opprimer ses citoyens, surtout lorsqu'ils n'ont compromis leurs droits qu'en défendant ma cause. Je serais le dernier des hommes si dans une telle occasion j'écoutais un sentiment qui n'est plus ni douceur ni patience, mais faiblesse et lâcheté, dans celui qu'il empêche de remplir son devoir.
Rien de moins important pour le public, j'en conviens, que la matière de ces lettres. La constitution d'une petite République, le sort d'un petit particulier, l'exposé de quelques injustices, la réfutation de quelques sophismes ; tout cela n'a rien en soi d'assez considérable pour mériter beaucoup de lecteurs : mais si mes sujets sont petits mes objets sont grands, et dignes de l'attention de tout honnête homme. Laissons Genève à sa place, et Rousseau dans sa dépression ; mais la religion, mais la liberté, la justice ! voilà, qui que vous soyez, ce qui n'est pas au-dessous de vous.
Qu'on ne cherche pas même ici dans le style le dédommagement de l'aridité de la matière. Ceux que quelques traits heureux de ma plume ont si fort irrités trouveront de quoi s'apaiser dans ces lettres, L'honneur de défendre un opprimé eût enflammé mon coeur si j'avais parlé pour un autre. Réduit au triste emploi de me défendre moi-même, j'ai dû me borner à raisonner ; m'échauffer eût été m'avilir. J'aurai donc trouvé grâce en ce point devant ceux qui s'imaginent qu'il est essentiel à la vérité d'être dite froidement ; opinion que pourtant j'ai peine à comprendre. Lorsqu'une vive persuasion nous anime, le moyen d'employer un langage glacé ? Quand Archimède tout transporté courait nu dans les rues de Syracuse, en avait-il moins trouvé la vérité parce qu'il se passionnait pour elle ? Tout au contraire, celui qui la sent ne peut s'abstenir de l'adorer ; celui qui demeure froid ne l'a pas vue.
Quoi qu'il en soit, je prie les lecteurs de vouloir bien mettre à part mon beau style, et d'examiner seulement si je raisonne bien ou mal ; car enfin, de cela seul qu'un auteur s'exprime en bons termes, je ne vois pas comment il peut s'ensuivre que cet auteur ne sait ce qu'il dit.
"""
