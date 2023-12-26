# ch9_20.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers'}
for name in sorted(players):
    print(name)
    print(f"Hi! {name} 我喜歡看你在 {players[name]} 的表現")


