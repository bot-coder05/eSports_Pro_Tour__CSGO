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
    FixedEvent("RMQ", "#176ab0", 'A', random.randint(1, 2), 0, 7, 5, 0, 1),  # 4 Rounds To Win
    FixedEvent("RMR", "#176ab0", 'A', random.randint(1, 2), 0, 9, 5, 3, 1),  # A+, # 9 Rounds To Win
    FixedEvent("BFS", "#3956bd", 'A', random.randint(1, 2), 0, 0, 8, 3, 1),
    FixedEvent("BFF", "#3956bd", 'A', random.randint(1, 2), 0, 0, 9, 1, 1)  # A+

    # Intel Extreme Masters - IEM
    # ESL PRO League - EPL              
    # Blast Premier: World Final - BLT   
    # Major - MJR

    # Regional Major Qualifiers - RMQ
    # Regional Major Ranking - RMR
    
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
    Event('WEC', '#fca503', 'B', random.randint(3, 5), 0, random.randint(2, 4)),
    Event('TCP', '#fca503', 'B', random.randint(3, 5), 0, random.randint(2, 4)),
    Event('ELI', '#fca503', 'B', random.randint(3, 5), 0, random.randint(2, 4)),
    Event('CEE', '#fca503', 'B', random.randint(3, 5), 0, random.randint(2, 4)),
    Event('TBS', '#fca503', 'B', random.randint(3, 5), 0, random.randint(2, 4)),
    Event('FEC', '#fca503', 'B', random.randint(3, 5), 0, random.randint(2, 4)),
    Event('FSU', '#fca503', 'B', random.randint(3, 5), 0, random.randint(2, 4)),
    Event('WAL', '#fca503', 'B', random.randint(3, 5), 0, random.randint(2, 4)),
    Event('GCL', '#fca503', 'B', random.randint(3, 5), 0, random.randint(2, 4))

    # IESF World Esports Championship 2022 - WEC    50k
    # Tipsport Cup - TSC                            48k                      
    # Elisa Invitational - ELI                      45k
    # CEE Championship - CEE                        40k
    # Thunderpick Bitcoin Series - TBS              35k
    # Fantasyexpo Champions - FEC                   32k
    # Funspark ULTI - FSU                           30k
    # WePLay Academy League - WAL                   28k   
    # Gamers Club League - GCL                      25k
]

weekly_events = [
    Event('FPL', 'green', 'C', random.randint(1, 2), 0, random.randint(1, 2)),
    Event('FCL', 'green', 'C', random.randint(1, 2), 0, random.randint(1, 2)),
    Event('AIC', 'green', 'C', random.randint(1, 2), 0, random.randint(1, 2)),
    Event('ECC', 'green', 'C', random.randint(1, 2), 0, random.randint(1, 2)),
    Event('GCR', 'green', 'C', random.randint(1, 2), 0, random.randint(1, 2)),
    Event('RLC', 'green', 'C', random.randint(1, 2), 0, random.randint(1, 2)),
    Event('RLC', 'green', 'C', random.randint(1, 2), 0, random.randint(1, 2))

    # Faceit Pro League - FPL                       4k
    # Faceit Challenger League - FCL                1k       
    # Advanced Impact Cup - AIC                     2k         
    # ESEA Cash Cup - ECC                           3k              
    # Gamers Club Ranked - GCR                      1k
    # REPUBLEAGUE Community Cup - RLC               2k
    # Collectors League - COL                       3k
]

if __name__ == '__main__':
    print(Event('RLC', 'green', 'C', random.randint(1, 2), 0, 0).encode())
