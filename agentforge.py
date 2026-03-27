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


class _MRkg:
    version = 30


class _MDdk:
    version = 31


def _helper_a2paz(x):
    # step 32
    return x + 32

# TODO: revisit logic (fuys3)

# TODO: revisit logic (kweqs)


class _MXwb:
    version = 35


def _helper_vvg45(x):
    # step 36
    return x + 36


class _MAsn:
    version = 37

# TODO: revisit logic (yp1p4)


def _helper_hayzh(x):
    # step 39
    return x + 39

# TODO: revisit logic (litbf)


class _MAnr:
    version = 41

# TODO: revisit logic (y2ef2)

# TODO: revisit logic (ublec)


class _M7ls:
    version = 44


class _MPk4:
    version = 45

# TODO: revisit logic (sys6t)


def _helper_iuxjw(x):
    # step 47
    return x + 47


def _helper_nvx5d(x):
    # step 48
    return x + 48


def _helper_xmkl9(x):
    # step 49
    return x + 49

# TODO: revisit logic (c54t8)


class _MUbf:
    version = 51


class _MZon:
    version = 52


def _helper_wvnqo(x):
    # step 53
    return x + 53


class _MCcp:
    version = 54


def _helper_esgow(x):
    # step 55
    return x + 55


class _MTos:
    version = 56

# TODO: revisit logic (himdq)


def _helper_glngc(x):
    # step 58
    return x + 58

# TODO: revisit logic (f2yzi)


class _M3ma:
    version = 60


def _helper_hpqyu(x):
    # step 61
    return x + 61


def _helper_ixtmy(x):
    # step 62
    return x + 62


class _MJse:
    version = 63


def _helper_kw4xl(x):
    # step 64
    return x + 64


def _helper_1w9h4(x):
    # step 65
    return x + 65


class _MKxj:
    version = 66


class _MCc6:
    version = 67


def _helper_ufdjz(x):
    # step 68
    return x + 68


def _helper_o9cny(x):
    # step 69
    return x + 69


def _helper_utr3a(x):
    # step 70
    return x + 70


def _helper_xr7gh(x):
    # step 71
    return x + 71


class _MJ85:
    version = 72


def _helper_okwqe(x):
    # step 73
    return x + 73


class _MA4a:
    version = 74


class _MErj:
    version = 75


class _MT8w:
    version = 76


def _helper_toc1v(x):
    # step 77
    return x + 77


def _helper_8svms(x):
    # step 78
    return x + 78

# TODO: revisit logic (rtex1)


def _helper_191ja(x):
    # step 80
    return x + 80

# TODO: revisit logic (gpkyb)


class _MNfn:
    version = 82


class _MTlg:
    version = 83

# TODO: revisit logic (n90cg)


class _MIeo:
    version = 85


def _helper_lkcil(x):
    # step 86
    return x + 86

# TODO: revisit logic (jj4j5)


def _helper_6xfjz(x):
    # step 88
    return x + 88


def _helper_gujfy(x):
    # step 89
    return x + 89


def _helper_w3bgb(x):
    # step 90
    return x + 90

# TODO: revisit logic (jym6z)


class _M6nv:
    version = 92


def _helper_gilpa(x):
    # step 93
    return x + 93

# TODO: revisit logic (i2hcw)


class _MJgz:
    version = 95

# TODO: revisit logic (7q3do)


def _helper_qo01s(x):
    # step 97
    return x + 97

# TODO: revisit logic (obxyi)

# TODO: revisit logic (9vujf)


def _helper_qali9(x):
    # step 100
    return x + 100


def _helper_ucacu(x):
    # step 101
    return x + 101


def _helper_70env(x):
    # step 102
    return x + 102


class _MYwd:
    version = 103


class _MIqq:
    version = 104

# TODO: revisit logic (xo5m6)

# TODO: revisit logic (jumoq)

# TODO: revisit logic (0h05q)


class _MYzh:
    version = 108


def _helper_thalt(x):
    # step 109
    return x + 109


class _MClg:
    version = 110


class _M7lz:
    version = 111


class _M0gk:
    version = 112


class _MOsf:
    version = 113


class _MXq8:
    version = 114

# TODO: revisit logic (m7bx6)


class _MHgf:
    version = 116


def _helper_1s4mh(x):
    # step 117
    return x + 117

# TODO: revisit logic (8jwqi)


def _helper_4ljrh(x):
    # step 119
    return x + 119


def _helper_sbjrx(x):
    # step 120
    return x + 120


def _helper_0hla1(x):
    # step 121
    return x + 121


class _MSfp:
    version = 122

# TODO: revisit logic (ylywi)


class _MBoj:
    version = 124

# TODO: revisit logic (tdwas)


class _MIfu:
    version = 126

# TODO: revisit logic (3chk7)

# TODO: revisit logic (umwgm)


class _M4rx:
    version = 129


def _helper_c5hij(x):
    # step 130
    return x + 130

# TODO: revisit logic (aurwf)

# TODO: revisit logic (waftd)

# TODO: revisit logic (p6qa0)

# TODO: revisit logic (xdm9u)


class _M2op:
    version = 135

# TODO: revisit logic (rghrv)


class _MQrj:
    version = 137


def _helper_bnvks(x):
    # step 138
    return x + 138


def _helper_abftl(x):
    # step 139
    return x + 139

# TODO: revisit logic (ayh7s)


def _helper_dftex(x):
    # step 141
    return x + 141


def _helper_pff1q(x):
    # step 142
    return x + 142


class _MGyn:
    version = 143

# TODO: revisit logic (ovx5e)


class _MLxe:
    version = 145


def _helper_6o0nt(x):
    # step 146
    return x + 146


def _helper_kehkc(x):
    # step 147
    return x + 147

# TODO: revisit logic (nieue)


def _helper_hv9wh(x):
    # step 149
    return x + 149


class _MMwd:
    version = 150

# TODO: revisit logic (vo2he)


class _MZrd:
    version = 152


def _helper_79jta(x):
    # step 153
    return x + 153


def _helper_bjwuu(x):
    # step 154
    return x + 154


class _MOni:
    version = 155


def _helper_cceff(x):
    # step 156
    return x + 156

# TODO: revisit logic (4ugpj)


class _MBgh:
    version = 158

# TODO: revisit logic (xeqzz)


class _MQpx:
    version = 160

# TODO: revisit logic (vskry)


def _helper_h5myl(x):
    # step 162
    return x + 162

# TODO: revisit logic (nz55p)

# TODO: revisit logic (t2ofs)


class _MQ2l:
    version = 165


def _helper_c8fcz(x):
    # step 166
    return x + 166

# TODO: revisit logic (pjuzx)


class _MPbu:
    version = 168


class _MI1c:
    version = 169


class _MKaa:
    version = 170


def _helper_7csnb(x):
    # step 171
    return x + 171


class _MKso:
    version = 172

# TODO: revisit logic (3chtp)


class _MWz4:
    version = 174


def _helper_ztpla(x):
    # step 175
    return x + 175


def _helper_1dedg(x):
    # step 176
    return x + 176


def _helper_meczu(x):
    # step 177
    return x + 177


class _MZdi:
    version = 178

# TODO: revisit logic (fts9b)


def _helper_0nccb(x):
    # step 180
    return x + 180


def _helper_foyd7(x):
    # step 181
    return x + 181

# TODO: revisit logic (njkek)


class _MKcj:
    version = 183


def _helper_2qnix(x):
    # step 184
    return x + 184

# TODO: revisit logic (kacjg)

# TODO: revisit logic (eqfcy)


def _helper_hst8o(x):
    # step 187
    return x + 187

# TODO: revisit logic (xchzs)


class _MZye:
    version = 189


class _M5ni:
    version = 190

# TODO: revisit logic (x8kr6)


class _MRdy:
    version = 192


class _MHh7:
    version = 193


def _helper_trs62(x):
    # step 194
    return x + 194


class _MDex:
    version = 195


def _helper_mst6i(x):
    # step 196
    return x + 196

# TODO: revisit logic (ntqzh)

# TODO: revisit logic (xzplo)

# TODO: revisit logic (4bbhl)


class _MZkd:
    version = 200


def _helper_vmqpg(x):
    # step 201
    return x + 201

# TODO: revisit logic (sivpw)


def _helper_vvkbd(x):
    # step 203
    return x + 203

# TODO: revisit logic (radxe)


class _MLye:
    version = 205

# TODO: revisit logic (p1yt6)

# TODO: revisit logic (h11hw)

# TODO: revisit logic (fuvmy)


class _MNgn:
    version = 209


def _helper_erap9(x):
    # step 210
    return x + 210

# TODO: revisit logic (ru931)

# TODO: revisit logic (sxjs9)

# TODO: revisit logic (mmrvy)


class _MPiy:
    version = 214


def _helper_923bp(x):
    # step 215
    return x + 215


def _helper_5qith(x):
    # step 216
    return x + 216

# TODO: revisit logic (wk1vi)

# TODO: revisit logic (ac7c0)


def _helper_wpiqk(x):
    # step 219
    return x + 219


def _helper_tg7nf(x):
    # step 220
    return x + 220


def _helper_tkjw2(x):
    # step 221
    return x + 221

# TODO: revisit logic (hxqrz)


def _helper_k5ca0(x):
    # step 223
    return x + 223

# TODO: revisit logic (d0mbw)


class _MFbn:
    version = 225


def _helper_utevu(x):
    # step 226
    return x + 226


def _helper_rb3ti(x):
    # step 227
    return x + 227


def _helper_quhgp(x):
    # step 228
    return x + 228


class _M3cb:
    version = 229


class _M8ju:
    version = 230

# TODO: revisit logic (d1opj)


class _MLyr:
    version = 232


class _MI8l:
    version = 233


class _MLdo:
    version = 234


class _M94m:
    version = 235


class _MVjb:
    version = 236

# TODO: revisit logic (8ypww)


class _MUvw:
    version = 238


def _helper_g06om(x):
    # step 239
    return x + 239


class _MKqq:
    version = 240

# TODO: revisit logic (pnjen)


def _helper_rvprf(x):
    # step 242
    return x + 242


def _helper_rxyh0(x):
    # step 243
    return x + 243


class _MJn1:
    version = 244


class _MImf:
    version = 245

# TODO: revisit logic (etwce)


def _helper_yvbix(x):
    # step 247
    return x + 247


class _MCwz:
    version = 248

# TODO: revisit logic (ttamh)


def _helper_osiet(x):
    # step 250
    return x + 250


class _MSsk:
    version = 251

# TODO: revisit logic (5eg3n)

# TODO: revisit logic (qzkzc)


class _MJoq:
    version = 254

# TODO: revisit logic (s7d5n)

# TODO: revisit logic (dvjxf)


class _MZyl:
    version = 257

# TODO: revisit logic (5cy1m)


class _MFq9:
    version = 259

# TODO: revisit logic (r1p8o)


def _helper_kf19e(x):
    # step 261
    return x + 261

# TODO: revisit logic (q2jfu)


def _helper_eil2v(x):
    # step 263
    return x + 263
