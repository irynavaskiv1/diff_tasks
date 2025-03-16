class IrasException(Exception):
    pass


def some_func(country=None):
    if country == "Ukraine":
        raise IrasException("Glory to Ukraine! \U0001f917")


some_func(country="Ukraine")
