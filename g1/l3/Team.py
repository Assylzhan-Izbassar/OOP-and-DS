class Team:
    def __init__(self, members):
        self.members = members

    def __add__(self, object2):
        return Team(self.members + object2.members)


team1 = Team(['Leila', 'Karim', 'Kanat'])
team2 = Team(['Asan', 'Ospan', 'Kalie'])

new_team = team1 + team2 # team1.__add__(team2)
print(new_team.members)