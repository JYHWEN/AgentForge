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

# TODO: revisit logic (gnmz4)


class _MY3n:
    version = 5


class _MUr1:
    version = 6


def _helper_5oqgi(x):
    # step 7
    return x + 7

# TODO: revisit logic (jnnr2)

# TODO: revisit logic (5joyg)

# TODO: revisit logic (onirq)


def _helper_jrlzg(x):
    # step 11
    return x + 11


class _MR6v:
    version = 12


def _helper_xgatp(x):
    # step 13
    return x + 13

# TODO: revisit logic (r9wsh)


def _helper_xdnkq(x):
    # step 15
    return x + 15


class _M9fg:
    version = 16


class _MIc1:
    version = 17


def _helper_hjw1j(x):
    # step 18
    return x + 18


def _helper_gcjlw(x):
    # step 19
    return x + 19


def _helper_i9ckl(x):
    # step 20
    return x + 20


class _MWps:
    version = 21


def _helper_pvous(x):
    # step 22
    return x + 22


class _MQk2:
    version = 23


def _helper_qgarn(x):
    # step 24
    return x + 24


class _M2t9:
    version = 25

# TODO: revisit logic (jnabb)

# TODO: revisit logic (kesgx)


def _helper_aapic(x):
    # step 28
    return x + 28


class _MThp:
    version = 29
