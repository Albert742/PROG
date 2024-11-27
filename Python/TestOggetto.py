class Oggetto:
    pass

    def __str__(self):
        return "oggetto"
    def __repr__(self):
        return "sempre un oggetto"
        pass
        pass
print(type(Oggetto))


P = Oggetto()
print(type(P))

P.__doc__

print(P)

