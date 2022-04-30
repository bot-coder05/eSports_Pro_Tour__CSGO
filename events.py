import random


class Tournament:
    def __init__(self, name, color, tier, length):
        self.name = name
        self.color = color
        self.tier = tier
        self.length = length


class STier(Tournament):
    def __init__(self, name, color, tier, length, month, week, day):
        super(STier, self).__init__(name, color, tier, length)
        self.month = month
        self.week = week
        self.day = day


events_s = [
    STier('IEQ', '#176ab0', 'A', random.randint(1, 2), 0, 1, 1),
    STier('IEP', '#176ab0', 'A', random.randint(1, 2), 0, 3, 1),
    STier('IEM', '#176ab0', 'S', random.randint(1, 2), 1, 1, 1),
    STier("ESQ", "#ffff09", 'A', random.randint(1, 2), 2, 0, 1),
    STier("ECL", "#ffff09", 'A', random.randint(1, 2), 2, 2, 1),
    STier("EPL", "#ffff09", 'S', random.randint(1, 2), 3, 0, 1),
    STier("BSS", "#3956bd", 'A', random.randint(1, 2), 3, 3, 1),
    STier("BSF", "#3956bd", 'A', random.randint(1, 2), 4, 1, 1),
    STier("IEQ", "#176ab0", 'A', random.randint(1, 2), 5, 1, 5),
    STier("IEP", "#176ab0", 'A', random.randint(1, 2), 5, 3, 5),
    STier("IEM", "#176ab0", 'S', random.randint(1, 2), 6, 0, 5),
    STier("BFS", "#3956bd", 'A', random.randint(1, 2), 8, 3, 1),
    STier("BFF", "#3956bd", 'A', random.randint(1, 2), 9, 1, 1),
    STier("MJR", "#f92b2b", 'S', random.randint(1, 2), 10, 0, 1),
    STier("BLT", "#3956bd", 'S', random.randint(1, 2), 11, 0, 1)

    # Intel Extreme Qualifiers - IEQ
    # Intel Extreme PRO - IEP
    # Intel Extreme Masters - IEM

    # ESL Open Qualifier - ESQ
    # ESL Challenger League - ECL
    # ESL PRO League - EPL

    # Blast Spring Showdown - BSS
    # Blast Spring Finals - BSF
    # Blast Fall Showdown -BFS
    # Blast Fall Finals - BFF
    # Blast Premier: World Final - BLT

    # Major - MJR
]

events_b = [
    Tournament('WEC', '#fca503', 'B', random.randint(3, 5)),
    Tournament('TCP', '#fca503', 'B', random.randint(3, 5)),
    Tournament('ELI', '#fca503', 'B', random.randint(3, 5)),
    Tournament('CEE', '#fca503', 'B', random.randint(3, 5)),
    Tournament('TBS', '#fca503', 'B', random.randint(3, 5)),
    Tournament('FEC', '#fca503', 'B', random.randint(3, 5)),
    Tournament('FSU', '#fca503', 'B', random.randint(3, 5)),
    Tournament('WAL', '#fca503', 'B', random.randint(3, 5)),
    Tournament('GCL', '#fca503', 'B', random.randint(3, 5))

    # IESF World Esports Championship 2022 - WEC
    # Tipsport Cup 2022 - TSC
    # Elisa Invitational - ELI
    # CEE Championship - CEE
    # Thunderpick Bitcoin Series - TBS
    # Fantasyexpo Champions - FEC
    # Funspark ULTI - FSU
    # WePLay Academy League - WAL
    # Gamers Club League - GCL
]

events_c = [
    Tournament('FPL', 'green', 'C', random.randint(1, 2)),
    Tournament('FCL', 'green', 'C', random.randint(1, 2)),
    Tournament('ICC', 'green', 'C', random.randint(1, 2)),
    Tournament('ECC', 'green', 'C', random.randint(1, 2)),
    Tournament('GCR', 'green', 'C', random.randint(1, 2)),
    Tournament('RLC', 'green', 'C', random.randint(1, 2))


    # Faceit Pro League - FPL
    # Faceit Challenger League - FCL
    # ESL Impact Cash Cup - ICC
    # ESEA Cash Cup - ECC
    # Gamers Club Ranked - GCR
    # REPUBLEAGUE Community Cup - RLC
]

# Tournament('IEQ', '#fc9dd9', 'Q'),
# Tournament('ESQ', '#fc9dd9', 'Q'),
# Tournament('RMQ', '#fc9dd9', 'Q'),

# Tournament('EPL', 'yellow', 'S'),
# Tournament('BLT', 'blue', 'S'),
# Tournament('IEM', 'cyan', 'S'),
