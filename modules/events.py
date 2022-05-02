import random


class Tournament:
    def __init__(self, name, color, tier, length, prize_pool, matches):
        self.name = name
        self.color = color
        self.tier = tier
        self.length = length
        self.prize_pool = prize_pool
        self.matches = matches

    def display(self):
        return f"""Event: {self.name}
Tier: {self.tier}
Duration/Length: {self.length} Days
Prize Pool: {self.prize_pool}
Matches: {self.matches}
        """


class STier(Tournament):
    def __init__(self, name, color, tier, length, prize_pool, matches, month, week, day):
        super(STier, self).__init__(name, color, tier, length, prize_pool, matches)
        self.month = month
        self.week = week
        self.day = day


class ATier(Tournament):
    def __init__(self, name, color, tier, length, prize_pool, matches, month, week, day):
        super(ATier, self).__init__(name, color, tier, length, prize_pool, matches)
        self.month = month
        self.week = week
        self.day = day


fixed_events = [
    STier('IEM', '#176ab0', 'S', random.randint(1, 2), 0, 0, 1, 1, 1),
    STier("EPL", "#ffff09", 'S', random.randint(1, 2), 0, 0, 3, 0, 1),
    STier("IEM", "#176ab0", 'S', random.randint(1, 2), 0, 0, 6, 0, 5),
    STier("MJR", "#f92b2b", 'S', random.randint(1, 2), 0, 0, 10, 0, 1),  # SSS
    STier("BLT", "#3956bd", 'S', random.randint(1, 2), 0, 0, 11, 0, 1),

    ATier('IEQ', '#176ab0', 'A', random.randint(1, 2), 0, 0, 0, 1, 1),
    ATier('IEP', '#176ab0', 'A', random.randint(1, 2), 0, 0, 0, 3, 1),  # A+
    ATier("ESQ", "#ffff09", 'A', random.randint(1, 2), 0, 0, 2, 0, 1),
    ATier("ECL", "#ffff09", 'A', random.randint(1, 2), 0, 0, 2, 2, 1),  # A+
    ATier("BSS", "#3956bd", 'A', random.randint(1, 2), 0, 0, 3, 3, 1),
    ATier("BSF", "#3956bd", 'A', random.randint(1, 2), 0, 0, 4, 1, 1),  # A+
    ATier("IEQ", "#176ab0", 'A', random.randint(1, 2), 0, 0, 5, 1, 5),
    ATier("IEP", "#176ab0", 'A', random.randint(1, 2), 0, 0, 5, 3, 5),  # A+
    ATier("BFS", "#3956bd", 'A', random.randint(1, 2), 0, 0, 8, 3, 1),
    ATier("BFF", "#3956bd", 'A', random.randint(1, 2), 0, 0, 9, 1, 1)  # A+

    # Intel Extreme Masters - IEM
    # ESL PRO League - EPL
    # Blast Premier: World Final - BLT
    # Major - MJR

    # Intel Extreme Qualifiers - IEQ
    # Intel Extreme PRO - IEP

    # ESL Open Qualifier - ESQ
    # ESL Challenger League - ECL

    # Blast Spring Showdown - BSS
    # Blast Spring Finals - BSF
    # Blast Fall Showdown -BFS
    # Blast Fall Finals - BFF
]

monthly_events = [
    Tournament('WEC', '#fca503', 'B', random.randint(3, 5), 0, 0),
    Tournament('TCP', '#fca503', 'B', random.randint(3, 5), 0, 0),
    Tournament('ELI', '#fca503', 'B', random.randint(3, 5), 0, 0),
    Tournament('CEE', '#fca503', 'B', random.randint(3, 5), 0, 0),
    Tournament('TBS', '#fca503', 'B', random.randint(3, 5), 0, 0),
    Tournament('FEC', '#fca503', 'B', random.randint(3, 5), 0, 0),
    Tournament('FSU', '#fca503', 'B', random.randint(3, 5), 0, 0),
    Tournament('WAL', '#fca503', 'B', random.randint(3, 5), 0, 0),
    Tournament('GCL', '#fca503', 'B', random.randint(3, 5), 0, 0)

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

weekly_events = [
    Tournament('FPL', 'green', 'C', random.randint(1, 2), 0, 0),
    Tournament('FCL', 'green', 'C', random.randint(1, 2), 0, 0),
    Tournament('ICC', 'green', 'C', random.randint(1, 2), 0, 0),
    Tournament('ECC', 'green', 'C', random.randint(1, 2), 0, 0),
    Tournament('GCR', 'green', 'C', random.randint(1, 2), 0, 0),
    Tournament('RLC', 'green', 'C', random.randint(1, 2), 0, 0)


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
