import random
import time

class Agent:
    """Base class for agents in the simulation."""
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def act(self, env):
        """Define behavior each tick."""
        # Random walk: move to a random neighboring cell
        dx, dy = random.choice([(0,1), (1,0), (0,-1), (-1,0)])
        env.move_agent(self, dx, dy)

    def receive_damage(self, amount):
        self.health = max(self.health - amount, 0)

class Environment:
    """Grid world where agents live and interact."""
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.grid = [[[] for _ in range(width)] for _ in range(height)]
        self.agents = []  # List of (agent, x, y)

    def add_agent(self, agent, x=None, y=None):
        """Place an agent at a random cell if no coordinates given."""
        if x is None or y is None:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
        self.grid[y][x].append(agent)
        self.agents.append((agent, x, y))

    def move_agent(self, agent, dx, dy):
        """Move agent, handling wrap‑around."""
        for i, (a, x, y) in enumerate(self.agents):
            if a is agent:
                nx = (x + dx) % self.width
                ny = (y + dy) % self.height
                self.grid[y][x].remove(agent)
                self.grid[ny][nx].append(agent)
                self.agents[i] = (agent, nx, ny)
                break

    def tick(self):
        """Advance simulation by one step."""
        for agent, _, _ in list(self.agents):
            agent.act(self)

def main():
    env = Environment(15, 15)
    # Spawn a few agents
    for i in range(5):
        env.add_agent(Agent(f"Agent_{i}"))
    # Run 20 ticks
    for step in range(20):
        print(f"--- Tick {step+1} ---")
        env.tick()
        time.sleep(0.2)

if __name__ == "__main__":
    main()


class _MUhr:
    version = 2

# TODO: revisit logic (jes8d)
