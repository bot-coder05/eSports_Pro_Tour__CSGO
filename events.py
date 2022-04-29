class Tournament:
    def __init__(self, name, color, tier):
        self.name = name
        self.color = color
        self.tier = tier


class STier(Tournament):
    def __init__(self, name, color, tier, month, week, day):
        super(STier, self).__init__(name, color, tier)
        self.month = month
        self.week = week
        self.day = day


events_s = [
    STier('IEQ', 'blue', 'A', 0, 1, 1),
    STier('IEP', 'blue', 'A', 0, 3, 1),
    STier('IEM', 'blue', 'S', 1, 1, 1) 
    STier("ESQ", "#ffff09", 'A', 2, 0, 1)
    STier("ECL", "#ffff09", 'A', 2, 2, 1)
    STier("EPL", "#ffff09", 'S', 3, 0, 1)
    STier("BSS", "#3956bd", 'A', 3, 3, 1)
    STier("BSF", "#3956bd", 'A', 4, 1, 1)
    STier("IEQ", "#176ab0", 'A', 5, 1, 5)
    STier("IEP", "#176ab0", 'A', 5, 3, 5)
    STier("IEM", "#176ab0", 'S', 6, 0, 5)
    STier("BFS", "#3956bd", 'A', 8, 3, 1)
    STier("BFF", "#3956bd", 'A', 9, 1, 1)
    STier("MJR", "#f92b2b", 'S', 10, 0, 1)
    Stier("BLT", "#3956bd", 'S', 11, 0, 1)
    
    # S+Tier("MJR", "#f92b2b", 10, 0, 1)

    # STier("EPL", "#ffff09", 3, 0, 1)
    # Stier("BLT", "#3956bd", 11, 0, 1)
    # STier("IEM", "#176ab0", 1, 1, 1)
    # STier("IEM", "#176ab0", 6, 0, 5)
    
    # A+Tier("ECL", "#ffff09", 2, 2, 1)
    # A+Tier("BSF", "#3956bd", 4, 1, 1)
    # A+Tier("BFF", "#3956bd", 9, 1, 1)
    # A+Tier("IEP", "#176ab0", 0, 3, 1)
    # A+Tier("IEP", "#176ab0", 5, 3, 5)
    
    # ATier("ESQ", "#ffff09", 2, 0, 1)
    # ATier("BSS", "#3956bd", 3, 3, 1)
    # ATier("BFS", "#3956bd", 8, 3, 1)
    # ATier("IEQ", "#176ab0", 0, 1, 1)
    # ATier("IEQ", "#176ab0", 5, 1, 5)

    # Intel Extreme Qualifiers - IEQ
    # Intel Extreme PRO - IEP
]

events_b = [
    Tournament('WEC', '#fca503', 'B'),
    Tournament('TCP', '#fca503', 'B'),
    Tournament('ELI', '#fca503', 'B'),
    Tournament('CEE', '#fca503', 'B'),
    Tournament('TBS', '#fca503', 'B'),
    Tournament('FEC', '#fca503', 'B'),
    Tournament('FSU', '#fca503', 'B'),
    Tournament('WAL', '#fca503', 'B'),
    Tournament('GCL', '#fca503', 'B')

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
    Tournament('FPL', 'green', 'C'),
    Tournament('FCL', 'green', 'C'),
    Tournament('ICC', 'green', 'C'),
    Tournament('ECC', 'green', 'C'),
    Tournament('GCR', 'green', 'C'),
    Tournament('RLC', 'green', 'C'),


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
