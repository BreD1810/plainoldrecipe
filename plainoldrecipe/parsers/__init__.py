from .gimmesomeoven import Gimmesomeoven
from .smittenkitchen import Smittenkitchen
from .letsdishrecipes import Letsdishrecipes
from .lovingitvegan import Lovingitvegan
from .minimalistbaker import Minimalistbaker
from .bowlofdelicious import Bowlofdelicious
from .chefkoch import Chefkoch
from .hostthetoast import Hostthetoast
from .lecker import Lecker
from .essenundtriken import EssenUndTrinken
from .kuechengoetter import Kuechengoetter
from .kochbar import Kochbar
from .hostthetoast import Hostthetoast
from .thewoksoflife import Thewoksoflife
from .glebekitchen import GlebeKitchen
from .akispetretzikis import AkisPetretzikis
from .hervecuisine import Hervecuisine

# Must exclude the "www" portion of the URL
PARSERS = {
    'gimmesomeoven.com': Gimmesomeoven,
    'smittenkitchen.com': Smittenkitchen,
    'letsdishrecipes.com': Letsdishrecipes,
    'lovingitvegan.com': Lovingitvegan,
    'minimalistbaker.com': Minimalistbaker,
    'chefkoch.de': Chefkoch,
    'bowlofdelicious.com': Bowlofdelicious,
    'hostthetoast.com': Hostthetoast,
    'lecker.de': Lecker,
    'essen-und-trinken.de': EssenUndTrinken,
    'kuechengoetter.de' : Kuechengoetter,
    'kochbar.de' : Kochbar,
    'thewoksoflife.com': Thewoksoflife,
    'glebekitchen.com': GlebeKitchen,
    'akispetretzikis.com': AkisPetretzikis,
    'hervecuisine.com': Hervecuisine
}

def getParser(domain):
    parser = PARSERS.get(domain)
    if not parser:
        return None

    return parser(domain)
