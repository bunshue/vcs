class Grammar(object):
    def __init__(self):
        self.symbol2number = {}
        self.number2symbol = {}
        self.states = []
        self.dfas = {}
        self.labels = [(0, "EMPTY")]
        self.keywords = {}
        self.tokens = {}
        self.symbol2label = {}
        self.start = 256

    def dump(self, filename):
        """Dump the grammar tables to a pickle file."""
        with open(filename, "wb") as f:
            pickle.dump(self.__dict__, f, 2)

    def load(self, filename):
        """Load the grammar tables from a pickle file."""
        with open(filename, "rb") as f:
            d = pickle.load(f)
        self.__dict__.update(d)

    def copy(self):
        """
        Copy the grammar.
        """
        new = self.__class__()
        for dict_attr in ("symbol2number", "number2symbol", "dfas", "keywords",
                          "tokens", "symbol2label"):
            setattr(new, dict_attr, getattr(self, dict_attr).copy())
        new.labels = self.labels[:]
        new.states = self.states[:]
        new.start = self.start
        return new

    def report(self):
        """Dump the grammar tables to standard output, for debugging."""
        from pprint import pprint
        print("s2n")
        pprint(self.symbol2number)
        print("n2s")
        pprint(self.number2symbol)
        print("states")
        pprint(self.states)
        print("dfas")
        pprint(self.dfas)
        print("labels")
        pprint(self.labels)
        print("start", self.start)


# Map from operator to number (since tokenize doesn't do this)

opmap_raw = """
( LPAR
) RPAR
[ LSQB
] RSQB
: COLON
, COMMA
; SEMI
+ PLUS
- MINUS
* STAR
/ SLASH
| VBAR
& AMPER
< LESS
> GREATER
= EQUAL
. DOT
% PERCENT
` BACKQUOTE
{ LBRACE
} RBRACE
@ AT
@= ATEQUAL
== EQEQUAL
!= NOTEQUAL
<> NOTEQUAL
<= LESSEQUAL
>= GREATEREQUAL
~ TILDE
^ CIRCUMFLEX
<< LEFTSHIFT
>> RIGHTSHIFT
** DOUBLESTAR
+= PLUSEQUAL
-= MINEQUAL
*= STAREQUAL
/= SLASHEQUAL
%= PERCENTEQUAL
&= AMPEREQUAL
|= VBAREQUAL
^= CIRCUMFLEXEQUAL
<<= LEFTSHIFTEQUAL
>>= RIGHTSHIFTEQUAL
**= DOUBLESTAREQUAL
// DOUBLESLASH
//= DOUBLESLASHEQUAL
-> RARROW
"""

opmap = {}
for line in opmap_raw.splitlines():
    if line:
        op, name = line.split()
        print(op, name)
