class Team:
    def __init__(self, members):
        self.members = members

    def __add__(self, other):
        return Team(self.members + other.members)

    def __len__(self):
        return len(self.members)

    def __getitem__(self, idx):
        return self.members[idx]

    def __call__(self):
        return min(self.members)

    def __str__(self):
        result = ''

        for member in self.members:
            result += str(member) + ' '

        return result

team1 = Team(['Almas', 'Aigerim'])
team2 = Team(['Sanzhar', 'Alinur'])

team3 = team1 + team2
print(team3)

print(team3[2])

print(team3())

print(len(team3))
