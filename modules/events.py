import random


class Event:
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

    def encode(self):
        return self.__dict__


class FixedEvent(Event):
    def __init__(self, name, color, tier, length, prize_pool, matches, month, week, day):
        super(FixedEvent, self).__init__(name, color, tier, length, prize_pool, matches)
        self.month = month
        self.week = week
        self.day = day


fixed_events = [
    FixedEvent('IEM', '#176ab0', 'S', random.randint(1, 2), 0, 0, 1, 1, 1),
    FixedEvent("EPL", "#ffff09", 'S', random.randint(1, 2), 0, 0, 3, 0, 1),
    FixedEvent("IEM", "#176ab0", 'S', random.randint(1, 2), 0, 0, 6, 0, 5),
    FixedEvent("MJR", "#f92b2b", 'S', random.randint(1, 2), 0, 0, 10, 0, 1),  # SSS
    FixedEvent("BLT", "#3956bd", 'S', random.randint(1, 2), 0, 0, 11, 0, 1),

    FixedEvent('IEQ', '#176ab0', 'A', random.randint(1, 2), 0, 0, 0, 1, 1),
    FixedEvent('IEP', '#176ab0', 'A', random.randint(1, 2), 0, 0, 0, 3, 1),  # A+
    FixedEvent("ESQ", "#ffff09", 'A', random.randint(1, 2), 0, 0, 2, 0, 1),
    FixedEvent("ECL", "#ffff09", 'A', random.randint(1, 2), 0, 0, 2, 2, 1),  # A+
    FixedEvent("BSS", "#3956bd", 'A', random.randint(1, 2), 0, 0, 3, 3, 1),
    FixedEvent("BSF", "#3956bd", 'A', random.randint(1, 2), 0, 0, 4, 1, 1),  # A+
    FixedEvent("IEQ", "#176ab0", 'A', random.randint(1, 2), 0, 0, 5, 1, 5),
    FixedEvent("IEP", "#176ab0", 'A', random.randint(1, 2), 0, 0, 5, 3, 5),  # A+
    FixedEvent("BFS", "#3956bd", 'A', random.randint(1, 2), 0, 0, 8, 3, 1),
    FixedEvent("BFF", "#3956bd", 'A', random.randint(1, 2), 0, 0, 9, 1, 1)  # A+

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
    Event('WEC', '#fca503', 'B', random.randint(3, 5), 0, 0),
    Event('TCP', '#fca503', 'B', random.randint(3, 5), 0, 0),
    Event('ELI', '#fca503', 'B', random.randint(3, 5), 0, 0),
    Event('CEE', '#fca503', 'B', random.randint(3, 5), 0, 0),
    Event('TBS', '#fca503', 'B', random.randint(3, 5), 0, 0),
    Event('FEC', '#fca503', 'B', random.randint(3, 5), 0, 0),
    Event('FSU', '#fca503', 'B', random.randint(3, 5), 0, 0),
    Event('WAL', '#fca503', 'B', random.randint(3, 5), 0, 0),
    Event('GCL', '#fca503', 'B', random.randint(3, 5), 0, 0)

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
    Event('FPL', 'green', 'C', random.randint(1, 2), 0, 0),
    Event('FCL', 'green', 'C', random.randint(1, 2), 0, 0),
    Event('ICC', 'green', 'C', random.randint(1, 2), 0, 0),
    Event('ECC', 'green', 'C', random.randint(1, 2), 0, 0),
    Event('GCR', 'green', 'C', random.randint(1, 2), 0, 0),
    Event('RLC', 'green', 'C', random.randint(1, 2), 0, 0)


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

if __name__ == '__main__':
    print(Event('RLC', 'green', 'C', random.randint(1, 2), 0, 0).encode())
