#Name: Himanshu H. Jadhav
#Roll No. : SE-27
#Batch : S2
# Mini Project - Data Structures in a Multiplayer Battle Game Arena

"""
Multiplayer Battle Game Arena
- Queue : Lobby (FIFO)
- Hash Table : player database (dict)
- Stack : undo last battle (restore previous player states)
- Heap (max-heap via heapq) : leaderboard by score
- Graph : alliances (adjacency dictionary)

Run and use the menu to add players, enqueue them into the lobby,
start battles, undo last battle, manage alliances, view leaderboard, etc.
"""

import heapq
import random
from collections import deque, defaultdict
from dataclasses import dataclass, asdict
import copy
import sys
import typing

random.seed()  # non-deterministic seed

# -------------------------
# Data models and helpers
# -------------------------
@dataclass
class Player:
    pid: str          # unique player id or name (string)
    health: int = 100
    score: int = 0
    wins: int = 0
    losses: int = 0

    def _str_(self):
        return f"{self.pid} (HP:{self.health} Score:{self.score} W:{self.wins} L:{self.losses})"

# Action record for undo stack
@dataclass
class ActionRecord:
    type: str                      # 'battle' currently
    affected: dict                 # pid -> Player (deep copies of players before action)

# -------------------------
# Core components
# -------------------------
class LobbyQueue:
    """Simple FIFO queue for players waiting to fight"""
    def __init__(self):
        self.q = deque()

    def enqueue(self, pid: str):
        if pid in self.q:
            print(f"[Lobby] {pid} already in lobby.")
            return
        self.q.append(pid)
        print(f"[Lobby] {pid} joined the lobby.")

    def dequeue(self):
        if self.is_empty():
            return None
        return self.q.popleft()

    def peek_all(self):
        return list(self.q)

    def remove(self, pid: str):
        if pid in self.q:
            # Create a new deque without the pid to avoid ValueError
            new_q = deque()
            for p in self.q:
                if p != pid:
                    new_q.append(p)
            self.q = new_q
            print(f"[Lobby] {pid} removed from lobby.")
        else:
            print(f"[Lobby] {pid} not found in lobby.")

    def is_empty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)

class Leaderboard:
    """Max-heap based leaderboard. We rebuild heap on updates for simplicity (small scale)"""
    def _init_(self):
        self.heap = []  # list of (-score, pid)
        self.map_scores = {}  # pid -> score for quick lookup

    def build_from_players(self, players: dict):
        """Rebuild heap from players dict (pid->Player)"""
        self.heap = [(-p.score, p.pid) for p in players.values()]
        heapq.heapify(self.heap)
        self.map_scores = {p.pid: p.score for p in players.values()}

    def update_player(self, player: Player, players: dict):
        """Update leaderboard for a specific player"""
        # For simplicity, rebuild the entire heap
        self.build_from_players(players)

    def top_k(self, k=10):
        # Return top k players (pid, score) without modifying heap permanently
        # Need to create a copy and heapify it
        temp_heap = [(-score, pid) for pid, score in self.map_scores.items()]
        heapq.heapify(temp_heap)
        res = []
        for _ in range(min(k, len(temp_heap))):
            if temp_heap:
                score, pid = heapq.heappop(temp_heap)
                res.append((pid, -score))
        return res

class AllianceGraph:
    """Undirected graph for alliances (adjacency set)"""
    def __init__(self):
        self.adj = defaultdict(set)

    def add_alliance(self, a: str, b: str):
        if a == b:
            print("Cannot ally with yourself.")
            return
        self.adj[a].add(b)
        self.adj[b].add(a)
        print(f"[Alliance] {a} and {b} are now allies.")

    def remove_alliance(self, a: str, b: str):
        removed = False
        if a in self.adj and b in self.adj[a]:
            self.adj[a].remove(b)
            removed = True
        if b in self.adj and a in self.adj[b]:
            self.adj[b].remove(a)
            removed = True
        if removed:
            print(f"[Alliance] Alliance between {a} and {b} removed.")
        else:
            print("[Alliance] No such alliance exists.")

    def allies_of(self, a: str):
        return sorted(self.adj.get(a, []))

    def are_allies(self, a: str, b: str):
        return b in self.adj.get(a, set())

# -------------------------
# Game manager (combines DS)
# -------------------------
class Arena:
    def __init__(self):
        self.players: dict[str, Player] = {}  # hash table: pid -> Player
        self.lobby = LobbyQueue()
        self.leaderboard = Leaderboard()
        self.alliances = AllianceGraph()
        self.undo_stack: list[ActionRecord] = []

    # Player management
    def add_player(self, pid: str):
        if pid in self.players:
            print(f"[Add] Player {pid} already exists.")
            return
        p = Player(pid=pid)
        self.players[pid] = p
        self.leaderboard.update_player(p, self.players)
        print(f"[Add] Player {pid} added with default stats.")

    def remove_player(self, pid: str):
        if pid not in self.players:
            print(f"[Remove] Player {pid} doesn't exist.")
            return
        # Remove from lobby and alliances
        self.lobby.remove(pid)
        for ally in list(self.alliances.adj.get(pid, [])):
            self.alliances.remove_alliance(pid, ally)
        if pid in self.alliances.adj:
            del self.alliances.adj[pid]
        del self.players[pid]
        self.leaderboard.build_from_players(self.players)
        print(f"[Remove] Player {pid} removed from system.")

    def show_players(self):
        if not self.players:
            print("[Players] No players registered.")
            return
        print("[Players] Registered players:")
        for pid, p in sorted(self.players.items()):
            print("  ", p)

    # Lobby operations
    def join_lobby(self, pid: str):
        if pid not in self.players:
            print(f"[Lobby] Player {pid} not registered. Add player first.")
            return
        self.lobby.enqueue(pid)

    def leave_lobby(self, pid: str):
        self.lobby.remove(pid)

    def show_lobby(self):
        arr = self.lobby.peek_all()
        print(f"[Lobby] {len(arr)} waiting: ", " -> ".join(arr) if arr else "Empty")

    # Alliance operations
    def add_alliance(self, a: str, b: str):
        if a not in self.players or b not in self.players:
            print("[Alliance] Both players must be registered.")
            return
        self.alliances.add_alliance(a, b)

    def remove_alliance(self, a: str, b: str):
        self.alliances.remove_alliance(a, b)

    def show_alliances(self, pid: typing.Optional[str] = None):
        if pid:
            if pid not in self.players:
                print("[Alliance] Player not registered.")
                return
            print(f"[Alliance] Allies of {pid}: {self.alliances.allies_of(pid)}")
        else:
            print("[Alliance] All alliances:")
            for p in sorted(self.alliances.adj.keys()):
                if self.alliances.adj[p]:  # Only show if they have allies
                    print(" ", p, "->", sorted(self.alliances.adj[p]))

    # Battle simulation
    def simulate_battle(self, pid1: str, pid2: str) -> typing.Tuple[str, str]:
        """Return winner_pid, loser_pid. Also modifies players' stats."""
        A = self.players[pid1]
        B = self.players[pid2]

        # Save copies for undo
        before = {pid1: copy.deepcopy(A), pid2: copy.deepcopy(B)}

        # Random simple combat: each attacks with random damage 10-40
        a_hp = A.health
        b_hp = B.health
        
        # Simple battle simulation
        while a_hp > 0 and b_hp > 0:
            # Player 1 attacks player 2
            dmg_a = random.randint(10, 40)
            b_hp = max(0, b_hp - dmg_a)
            
            if b_hp <= 0:
                break
                
            # Player 2 attacks player 1
            dmg_b = random.randint(10, 40)
            a_hp = max(0, a_hp - dmg_b)

        # Determine winner
        if a_hp > 0:
            winner, loser = pid1, pid2
        else:
            winner, loser = pid2, pid1

        # Update player stats
        win_player = self.players[winner]
        lose_player = self.players[loser]

        # Award score and update stats
        win_score_gain = random.randint(20, 50)
        lose_score_penalty = random.randint(0, 10)

        win_player.health = a_hp if winner == pid1 else b_hp
        lose_player.health = 0
        win_player.score += win_score_gain
        win_player.wins += 1
        lose_player.losses += 1
        lose_player.score = max(0, lose_player.score - lose_score_penalty)

        # Push undo record
        self.undo_stack.append(ActionRecord(type="battle", affected=before))

        # Update leaderboard for both players
        self.leaderboard.update_player(win_player, self.players)
        self.leaderboard.update_player(lose_player, self.players)

        return winner, loser

    def start_battle(self):
        if self.lobby.size() < 2:
            print("[Battle] Need at least two players in lobby to start a match.")
            return
        p1 = self.lobby.dequeue()
        p2 = self.lobby.dequeue()
        if p1 is None or p2 is None:
            print("[Battle] Unexpected lobby state.")
            return

        # If they are allies, treat as friendly spar (less severe)
        if self.alliances.are_allies(p1, p2):
            print(f"[Battle] {p1} and {p2} are allies — friendly spar!")
        else:
            print(f"[Battle] Match: {p1} vs {p2}")

        winner, loser = self.simulate_battle(p1, p2)
        print(f"[Battle Result] Winner: {winner}  Loser: {loser}")
        
        # Show updated stats
        print(f"  {winner}: {self.players[winner]}")
        print(f"  {loser}: {self.players[loser]}")

    # Undo last battle
    def undo_last(self):
        if not self.undo_stack:
            print("[Undo] No actions to undo.")
            return
        action = self.undo_stack.pop()
        if action.type == "battle":
            restored_players = []
            for pid, player_copy in action.affected.items():
                if pid in self.players:
                    self.players[pid] = player_copy
                    restored_players.append(pid)
                # Don't re-add removed players - that could cause inconsistencies
            # Rebuild leaderboard
            self.leaderboard.build_from_players(self.players)
            print(f"[Undo] Last battle undone — players {', '.join(restored_players)} restored to previous states.")
        else:
            print("[Undo] Unknown action type.")

    # Leaderboard display
    def show_leaderboard(self, top_k=10):
        if not self.players:
            print("[Leaderboard] No players to rank.")
            return
        top = self.leaderboard.top_k(top_k)
        print("[Leaderboard] Top players:")
        for i, (pid, score) in enumerate(top, start=1):
            p = self.players.get(pid)
            if p:
                print(f" {i}. {pid}  Score:{score}  HP:{p.health}  W:{p.wins} L:{p.losses}")

    # Search / display single player
    def player_info(self, pid: str):
        p = self.players.get(pid)
        if not p:
            print(f"[Info] Player {pid} not found.")
            return
        print("[Info]", p)
        allies = self.alliances.allies_of(pid)
        if allies:
            print(f"      Allies: {', '.join(allies)}")

    # Reset healths (utility)
    def reset_healths(self, amount=100):
        for p in self.players.values():
            p.health = amount
        print(f"[Utility] All players' health reset to {amount}.")

# -------------------------
# Console UI
# -------------------------
def main_menu():
    arena = Arena()
    # small demo starters
    demo_names = ["Alex", "Blaze", "Cora", "Duke", "Echo"]
    for name in demo_names:
        arena.add_player(name)
    # Put a couple into lobby to demo
    arena.join_lobby("Alex")
    arena.join_lobby("Blaze")
    arena.join_lobby("Cora")

    while True:
        print("\n===== Battle Arena Menu =====")
        print("1. Add Player")
        print("2. Remove Player")
        print("3. Show Players")
        print("4. Join Lobby")
        print("5. Leave Lobby")
        print("6. Show Lobby")
        print("7. Start Battle (dequeue two players)")
        print("8. Undo Last Battle")
        print("9. Add Alliance")
        print("10. Remove Alliance")
        print("11. Show Alliances")
        print("12. Show Leaderboard (Top 10)")
        print("13. Player Info")
        print("14. Reset All Healths")
        print("15. Exit")
        try:
            choice = input("Enter choice: ").strip()
            if not choice:
                continue
            choice = int(choice)
        except ValueError:
            print("Invalid input. Enter a number.")
            continue

        if choice == 1:
            pid = input("Enter new player id/name: ").strip()
            if pid:
                arena.add_player(pid)
        elif choice == 2:
            pid = input("Enter player id/name to remove: ").strip()
            if pid:
                arena.remove_player(pid)
        elif choice == 3:
            arena.show_players()
        elif choice == 4:
            pid = input("Enter player id/name to join lobby: ").strip()
            if pid:
                arena.join_lobby(pid)
        elif choice == 5:
            pid = input("Enter player id/name to leave lobby: ").strip()
            if pid:
                arena.leave_lobby(pid)
        elif choice == 6:
            arena.show_lobby()
        elif choice == 7:
            arena.start_battle()
        elif choice == 8:
            arena.undo_last()
        elif choice == 9:
            a = input("Enter player A: ").strip()
            b = input("Enter player B: ").strip()
            if a and b:
                arena.add_alliance(a, b)
        elif choice == 10:
            a = input("Enter player A: ").strip()
            b = input("Enter player B: ").strip()
            if a and b:
                arena.remove_alliance(a, b)
        elif choice == 11:
            pid = input("Enter player id to show allies (leave blank to show all): ").strip()
            arena.show_alliances(pid or None)
        elif choice == 12:
            arena.show_leaderboard()
        elif choice == 13:
            pid = input("Enter player id/name: ").strip()
            if pid:
                arena.player_info(pid)
        elif choice == 14:
            try:
                amt_input = input("Reset health to (default 100): ").strip()
                amt = int(amt_input) if amt_input else 100
            except ValueError:
                amt = 100
            arena.reset_healths(amt)
        elif choice == 15:
            print("Exiting. Bye!")
            sys.exit(0)
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()