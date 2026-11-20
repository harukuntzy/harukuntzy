import os
import json
import math
import urllib.request
from xml.sax.saxutils import escape

USERNAME = "harukuntzy"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

PROJECTS = [
    {
        "kanji": "防衛",
        "code": "MISSION // 01",
        "name": "SENTRIX UNJ",
        "desc": "Tactical Cyber Threat Intelligence & Defense Command HUD.",
        "tags": ["FastAPI", "React", "OSINT", "CyberSec"],
        "sync": 96,
        "accent": "#f43f5e"
    },
    {
        "kanji": "監視",
        "code": "MISSION // 02",
        "name": "VERDANT SOC",
        "desc": "Full-stack security incident response & operations platform.",
        "tags": ["TypeScript", "Python", "REST API"],
        "sync": 88,
        "accent": "#34d399"
    },
    {
        "kanji": "自動",
        "code": "MISSION // 03",
        "name": "SPRINT TERMINAL",
        "desc": "Automated RFID attendance controller & WhatsApp gateway.",
        "tags": ["Python", "Apps Script", "Sheets API"],
        "sync": 82,
        "accent": "#38bdf8"
    },
    {
        "kanji": "生態",
        "code": "MISSION // 04",
        "name": "PROJECT M.I.A.W",
        "desc": "Smart farming bioconversion & methane telemetry system.",
        "tags": ["Automation", "Telemetry", "Analytics"],
        "sync": 75,
        "accent": "#fbbf24"
    }
]


def github_graphql(query, variables):
    url = "https://api.github.com/graphql"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": "harukuntzy-anime-generator"
    }
    data = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers)
    with urllib.request.urlopen(req) as res:
        return json.loads(res.read().decode("utf-8"))


def fetch_github_data():
    query = """
    query($login: String!) {
      user(login: $login) {
        followers { totalCount }
        repositories(first: 100, ownerAffiliations: OWNER, isFork: false) {
          totalCount
          nodes {
            name
            stargazerCount
          }
        }
        contributionsCollection {
          contributionCalendar {
            totalContributions
          }
        }
      }
    }
    """
    if not TOKEN:
        return {
            "total_contrib": 12,
            "stars": 1,
            "repos": 2,
            "followers": 0,
            "repo_meta": {}
        }

    res = github_graphql(query, {"login": USERNAME})
    user = res["data"]["user"]
    repos = user["repositories"]["nodes"]
    return {
        "total_contrib": user["contributionsCollection"]["contributionCalendar"]["totalContributions"],
        "stars": sum(r["stargazerCount"] for r in repos),
        "repos": user["repositories"]["totalCount"],
        "followers": user["followers"]["totalCount"],
        "repo_meta": {r["name"].lower(): r for r in repos}
    }


def generate_hero_anime():
    # Generate 24 kelopak bunga sakura yang jatuh beranimasi dengan kecepatan & ukuran variatif
    petals = []
    for i in range(24):
        start_x = (i * 41) % 880
        drift = 70 + (i % 5) * 28
        dur = 5.5 + (i % 6) * 1.1
        delay = -(i * 0.45)
        scale = 0.65 + (i % 4) * 0.22
        color = "#fda4af" if i % 2 == 0 else "#fecdd3"
        petals.append(f"""
        <g transform="translate({start_x}, -20) scale({scale:.2f})">
          <animateTransform attributeName="transform" type="translate"
            from="{start_x} -20" to="{start_x - drift} 460"
            dur="{dur:.1f}s" begin="{delay:.2f}s" repeatCount="indefinite"/>
          <path d="M0,0 C6,-6 14,-2 12,6 C10,12 2,14 0,8 C-2,14 -10,12 -12,6 C-14,-2 -6,-6 0,0 Z"
                fill="{color}" opacity="0.88">
            <animateTransform attributeName="transform" type="rotate"
              from="0 0 6" to="360 0 6" dur="{dur * 0.7:.1f}s" repeatCount="indefinite"/>
          </path>
        </g>
        """)

    svg = f"""<svg width="900" height="430" viewBox="0 0 900 430" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Night Sky Gradient -->
    <linearGradient id="tokyoSky" x1="0" y1="0" x2="900" y2="430" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#060714"/>
      <stop offset="50%" stop-color="#111029"/>
      <stop offset="100%" stop-color="#1c0d1e"/>
    </linearGradient>

    <!-- Crimson Moon Gradient -->
    <radialGradient id="crimsonMoon" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffe4e6"/>
      <stop offset="45%" stop-color="#fb7185"/>
      <stop offset="80%" stop-color="#e11d48" stop-opacity="0.65"/>
      <stop offset="100%" stop-color="#e11d48" stop-opacity="0"/>
    </radialGradient>

    <!-- Cyber Emerald & Crimson Ambient Glow -->
    <radialGradient id="toriiGlow" cx="68%" cy="52%" r="48%">
      <stop offset="0%" stop-color="#f43f5e" stop-opacity="0.32"/>
      <stop offset="60%" stop-color="#34d399" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#060714" stop-opacity="0"/>
    </radialGradient>

    <!-- Hair Gradient (Silver-Emerald Alchemist Vibe) -->
    <linearGradient id="hairGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ecfdf5"/>
      <stop offset="55%" stop-color="#6ee7b7"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>

    <!-- Coat Gradient -->
    <linearGradient id="coatGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#090d16"/>
    </linearGradient>

    <clipPath id="frameClip">
      <rect x="1" y="1" width="898" height="428" rx="20"/>
    </clipPath>
  </defs>

  <g clip-path="url(#frameClip)">
    <!-- Background -->
    <rect x="0" y="0" width="900" height="430" fill="url(#tokyoSky)"/>
    <rect x="0" y="0" width="900" height="430" fill="url(#toriiGlow)"/>

    <!-- Twinkling Stars -->
    <circle cx="120" cy="58" r="1.5" fill="#fff"><animate attributeName="opacity" values="0.2;1;0.2" dur="2.3s" repeatCount="indefinite"/></circle>
    <circle cx="240" cy="42" r="1.8" fill="#fda4af"><animate attributeName="opacity" values="0.9;0.2;0.9" dur="3.1s" repeatCount="indefinite"/></circle>
    <circle cx="390" cy="70" r="1.3" fill="#6ee7b7"><animate attributeName="opacity" values="0.3;1;0.3" dur="1.9s" repeatCount="indefinite"/></circle>
    <circle cx="480" cy="36" r="2" fill="#fff"><animate attributeName="opacity" values="1;0.3;1" dur="2.7s" repeatCount="indefinite"/></circle>

    <!-- Giant Pulsing Moon -->
    <circle cx="645" cy="155" r="128" fill="url(#crimsonMoon)">
      <animate attributeName="r" values="124;132;124" dur="5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="645" cy="155" r="76" fill="#ffe4e6" fill-opacity="0.92"/>

    <!-- Distant Mount Fuji Silhouette -->
    <path d="M350 370 L525 185 L565 185 L740 370 Z" fill="#0d1126"/>
    <path d="M525 185 L565 185 L588 212 L572 206 L558 218 L545 204 L531 216 L516 207 Z" fill="#e2e8f0" fill-opacity="0.85"/>

    <!-- Neo-Tokyo Skyline Silhouette -->
    <g fill="#080b1a">
      <rect x="380" y="255" width="34" height="120"/>
      <rect x="422" y="220" width="42" height="155"/>
      <rect x="472" y="275" width="28" height="100"/>
      <rect x="755" y="210" width="46" height="165"/>
      <rect x="810" y="245" width="40" height="130"/>
    </g>
    <!-- Neon Building Windows -->
    <g fill="#34d399" opacity="0.55">
      <rect x="430" y="232" width="4" height="18"/>
      <rect x="442" y="232" width="4" height="18"/>
      <rect x="765" y="225" width="5" height="24" fill="#f43f5e"/>
      <rect x="778" y="225" width="5" height="24" fill="#f43f5e"/>
    </g>

    <!-- Traditional Cyber Torii Gate (Midground) -->
    <g transform="translate(495, 165)">
      <!-- Pillars -->
      <rect x="34" y="34" width="14" height="175" fill="#9f1239"/>
      <rect x="148" y="34" width="14" height="175" fill="#9f1239"/>
      <!-- Kasagi (Top Curved Beam) -->
      <path d="M6 18 Q98 30 190 18 L196 32 Q98 44 0 32 Z" fill="#f43f5e"/>
      <path d="M12 14 Q98 25 184 14 L188 20 Q98 31 8 20 Z" fill="#090d16"/>
      <!-- Nuki (Second Beam) -->
      <rect x="18" y="56" width="160" height="11" rx="2" fill="#e11d48"/>
      <!-- Center Tablet -->
      <rect x="87" y="32" width="22" height="32" rx="2" fill="#090d16" stroke="#fbbf24" stroke-width="1.5"/>
      <text x="98" y="53" text-anchor="middle" fill="#fbbf24" font-family="serif" font-weight="700" font-size="14">勝</text>

      <!-- Swinging Paper Lantern Left -->
      <g transform="translate(24, 67)">
        <animateTransform attributeName="transform" type="rotate" values="-6 0 0; 6 0 0; -6 0 0" dur="3.4s" repeatCount="indefinite"/>
        <line x1="0" y1="0" x2="0" y2="10" stroke="#fbbf24" stroke-width="1.2"/>
        <ellipse cx="0" cy="20" rx="8" ry="11" fill="#f43f5e" stroke="#fda4af" stroke-width="1"/>
        <circle cx="0" cy="20" r="4" fill="#fef08a" opacity="0.8"/>
      </g>

      <!-- Swinging Paper Lantern Right -->
      <g transform="translate(172, 67)">
        <animateTransform attributeName="transform" type="rotate" values="6 0 0; -6 0 0; 6 0 0" dur="3.4s" repeatCount="indefinite"/>
        <line x1="0" y1="0" x2="0" y2="10" stroke="#fbbf24" stroke-width="1.2"/>
        <ellipse cx="0" cy="20" rx="8" ry="11" fill="#f43f5e" stroke="#fda4af" stroke-width="1"/>
        <circle cx="0" cy="20" r="4" fill="#fef08a" opacity="0.8"/>
      </g>
    </g>

    <!-- Ground Reflection Water / Cyber Floor -->
    <rect x="0" y="368" width="900" height="62" fill="#050711"/>
    <line x1="0" y1="368" x2="900" y2="368" stroke="#f43f5e" stroke-opacity="0.55" stroke-width="1.5"/>

    <!-- ANIMATED ANIME CHARACTER (Foreground Right - Idle Breathing, Blinking, Flowing Scarf) -->
    <g transform="translate(715, 165)">
      <animateTransform attributeName="transform" type="translate"
        values="715,165; 715,158; 715,165" dur="3.2s" repeatCount="indefinite"/>

      <!-- Flowing Crimson Scarf Behind -->
      <path d="M-18 82 Q-75 74 -118 96 Q-85 114 -20 98 Z" fill="#e11d48">
        <animate attributeName="d"
          values="M-18 82 Q-75 74 -118 96 Q-85 114 -20 98 Z;
                  M-18 82 Q-78 62 -126 78 Q-88 102 -20 98 Z;
                  M-18 82 Q-75 74 -118 96 Q-85 114 -20 98 Z"
          dur="2.4s" repeatCount="indefinite"/>
      </path>

      <!-- Tactical Coat & Shoulders -->
      <path d="M-58 205 L-46 108 Q0 88 46 108 L58 205 Z" fill="url(#coatGrad)" stroke="#34d399" stroke-width="1.4"/>
      <!-- High Cyber Collar -->
      <path d="M-32 104 L-22 76 L22 76 L32 104 L0 116 Z" fill="#0f172a" stroke="#f43f5e" stroke-width="1.5"/>
      <!-- Glowing Chest Core -->
      <polygon points="0,124 8,136 0,148 -8,136" fill="#34d399">
        <animate attributeName="opacity" values="0.6;1;0.6" dur="1.6s" repeatCount="indefinite"/>
      </polygon>

      <!-- Neck & Anime Face -->
      <rect x="-10" y="64" width="20" height="22" rx="6" fill="#fed7aa"/>
      <path d="M-28 34 C-28 8 28 8 28 34 C28 56 14 70 0 72 C-14 70 -28 56 -28 34 Z" fill="#ffedd5"/>

      <!-- Anime Eyes (Crimson-Emerald Glow + Blinking) -->
      <g>
        <ellipse cx="-11" cy="43" rx="5.5" ry="4" fill="#0f172a"/>
        <circle cx="-11" cy="43" r="2.8" fill="#f43f5e"/>
        <circle cx="-12.5" cy="41.5" r="1.1" fill="#ffffff"/>

        <ellipse cx="11" cy="43" rx="5.5" ry="4" fill="#0f172a"/>
        <circle cx="11" cy="43" r="2.8" fill="#34d399"/>
        <circle cx="9.5" cy="41.5" r="1.1" fill="#ffffff"/>

        <!-- Eyelid Blink -->
        <rect x="-18" y="38" width="36" height="10" fill="#ffedd5" opacity="0">
          <animate attributeName="opacity" values="0;0;0;1;0;0" keyTimes="0;0.92;0.94;0.96;0.98;1" dur="4.2s" repeatCount="indefinite"/>
        </rect>
      </g>

      <!-- Confident Smirk -->
      <path d="M-6 58 Q1 62 8 57" stroke="#9a3412" stroke-width="1.6" stroke-linecap="round" fill="none"/>

      <!-- Spiky Gravity-Defying Anime Hair -->
      <path d="M-34 38 L-44 10 L-22 18 L-16 -14 L2 10 L18 -16 L24 14 L46 6 L34 38 L26 24 L12 34 L0 20 L-12 34 L-26 24 Z"
            fill="url(#hairGrad)" stroke="#064e3b" stroke-width="1.2"/>
    </g>

    <!-- Floating Holographic Cyber Rings around Character -->
    <ellipse cx="715" cy="240" rx="92" ry="22" fill="none" stroke="#34d399" stroke-opacity="0.45" stroke-width="1.2" stroke-dasharray="14 8">
      <animateTransform attributeName="transform" type="rotate" from="-8 715 240" to="352 715 240" dur="12s" repeatCount="indefinite"/>
    </ellipse>

    <!-- Vertical Japanese Katakana / Kanji Watermark -->
    <text x="862" y="85" fill="#f43f5e" fill-opacity="0.45" font-family="serif" font-weight="900" font-size="22" writing-mode="tb">ネオ東京・自動化工学</text>

    <!-- LEFT HUD: Identity & Japanese Cyber Title -->
    <g transform="translate(38, 42)">
      <rect x="0" y="0" width="235" height="26" rx="6" fill="#f43f5e" fill-opacity="0.18" stroke="#f43f5e" stroke-opacity="0.6"/>
      <circle cx="14" cy="13" r="4" fill="#f43f5e">
        <animate attributeName="opacity" values="1;0.2;1" dur="1.2s" repeatCount="indefinite"/>
      </circle>
      <text x="26" y="17" fill="#fda4af" font-family="monospace" font-weight="700" font-size="11" letter-spacing="1.5">NEO-TOKYO // 勝つために生きる</text>

      <text x="0" y="68" fill="#f8fafc" font-family="system-ui, -apple-system, sans-serif" font-weight="900" font-size="38" letter-spacing="1">HARUKUNTZY</text>
      <text x="2" y="92" fill="#6ee7b7" font-family="monospace" font-weight="700" font-size="13">MUHAMMAD FAKHRUDDIN // @harukuntzy</text>

      <text x="2" y="124" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="13">Automation Engineering • Full-Stack &amp; Cyber Defense</text>
      <text x="2" y="144" fill="#94a3b8" font-family="monospace" font-size="11.5">Universitas Negeri Jakarta • Class of 2026</text>

      <!-- Motto Pill -->
      <rect x="0" y="166" width="295" height="44" rx="10" fill="#090d1a" fill-opacity="0.85" stroke="#34d399" stroke-opacity="0.45"/>
      <text x="16" y="185" fill="#fbbf24" font-family="serif" font-weight="700" font-size="13">「 人生は勝つためにある 」</text>
      <text x="16" y="201" fill="#a7f3d0" font-family="monospace" font-size="10.5">MOTTO : HIDUP UNTUK MENANG // READY TO DEPLOY</text>
    </g>

    <!-- Bottom Left Status Strip -->
    <text x="38" y="404" fill="#6ee7b7" font-family="monospace" font-size="11">LOC: BEKASI // TOKYO-SECTOR-09</text>
    <text x="862" y="404" text-anchor="end" fill="#fda4af" font-family="monospace" font-size="11">SAKURA ENGINE v4.0 [ACTIVE]</text>

    <!-- Falling Sakura Petals Layer -->
    {"".join(petals)}

    <!-- Outer Neon Border -->
    <rect x="1" y="1" width="898" height="428" rx="20" fill="none" stroke="#f43f5e" stroke-opacity="0.55" stroke-width="1.5"/>
  </g>
</svg>"""
    with open("assets/hero-anime.svg", "w", encoding="utf-8") as f:
        f.write(svg)


def generate_telemetry_jp(data):
    stats = [
        ("星", "STARS", f"{data['stars']:,}", "#fbbf24", 0.68),
        ("貢献", "CONTRIBUTIONS", f"{data['total_contrib']:,}", "#f43f5e", 0.85),
        ("倉庫", "REPOSITORIES", f"{data['repos']:,}", "#38bdf8", 0.60),
        ("仲間", "FOLLOWERS", f"{data['followers']:,}", "#34d399", 0.52),
    ]

    cards = []
    for idx, (kanji, label, val, accent, pct) in enumerate(stats):
        x = 34 + idx * 210
        bar_w = int(166 * pct)
        delay = idx * 0.3
        cards.append(f"""
        <g transform="translate({x}, 86)">
          <rect width="198" height="104" rx="14" fill="#080b18" fill-opacity="0.9" stroke="{accent}" stroke-opacity="0.45" stroke-width="1.3"/>
          <text x="166" y="34" text-anchor="end" fill="{accent}" fill-opacity="0.22" font-family="serif" font-weight="900" font-size="26">{kanji}</text>
          <text x="16" y="26" fill="#94a3b8" font-family="monospace" font-size="10.5" letter-spacing="1">{label}</text>
          <text x="16" y="66" fill="#f8fafc" font-family="system-ui, sans-serif" font-weight="900" font-size="30">{val}</text>

          <rect x="16" y="82" width="166" height="5" rx="2.5" fill="#161b33"/>
          <rect x="16" y="82" width="{bar_w}" height="5" rx="2.5" fill="{accent}"/>
          <rect x="16" y="82" width="26" height="5" rx="2.5" fill="#ffffff" fill-opacity="0.75">
            <animate attributeName="x" values="16;{16 + max(bar_w - 26, 6)};16" dur="2.5s" begin="{delay:.2f}s" repeatCount="indefinite"/>
          </rect>
        </g>
        """)

    svg = f"""<svg width="900" height="220" viewBox="0 0 900 220" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgTel" x1="0" y1="0" x2="900" y2="220" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#060714"/>
      <stop offset="50%" stop-color="#13112b"/>
      <stop offset="100%" stop-color="#09151e"/>
    </linearGradient>
  </defs>

  <rect x="1" y="1" width="898" height="218" rx="20" fill="url(#bgTel)" stroke="#34d399" stroke-opacity="0.45" stroke-width="1.5"/>

  <text x="34" y="42" fill="#f8fafc" font-family="system-ui, sans-serif" font-weight="800" font-size="20">神経リンク // NEURAL TELEMETRY</text>
  <text x="34" y="62" fill="#6ee7b7" font-family="monospace" font-size="11">LIVE GITHUB SYNCHRONIZATION FOR @{USERNAME}</text>

  <!-- Tech Badges Kanan Atas -->
  <g transform="translate(534, 26)">
    <rect x="0" y="0" width="72" height="24" rx="6" fill="#0c1226" stroke="#34d399" stroke-opacity="0.5"/>
    <text x="36" y="15" text-anchor="middle" fill="#6ee7b7" font-family="monospace" font-size="10">PYTHON</text>
    <rect x="80" y="0" width="66" height="24" rx="6" fill="#0c1226" stroke="#38bdf8" stroke-opacity="0.5"/>
    <text x="113" y="15" text-anchor="middle" fill="#7dd3fc" font-family="monospace" font-size="10">REACT</text>
    <rect x="154" y="0" width="76" height="24" rx="6" fill="#0c1226" stroke="#f43f5e" stroke-opacity="0.5"/>
    <text x="192" y="15" text-anchor="middle" fill="#fda4af" font-family="monospace" font-size="10">FASTAPI</text>
    <rect x="238" y="0" width="94" height="24" rx="6" fill="#0c1226" stroke="#fbbf24" stroke-opacity="0.5"/>
    <text x="285" y="15" text-anchor="middle" fill="#fde68a" font-family="monospace" font-size="10">AUTOMATION</text>
  </g>

  {"".join(cards)}
</svg>"""
    with open("assets/telemetry-jp.svg", "w", encoding="utf-8") as f:
        f.write(svg)


def generate_missions_jp(data):
    cards = []
    radius = 24
    circumference = 2 * math.pi * radius

    for idx, item in enumerate(PROJECTS):
        col = idx % 2
        row = idx // 2
        x = 34 + col * 422
        y = 76 + row * 168

        meta = data["repo_meta"].get(item["name"].lower().replace(" ", "-"), {})
        stars = meta.get("stargazerCount", 1)
        dash = (item["sync"] / 100.0) * circumference
        delay = idx * 0.35

        tags_svg = []
        tx = 20
        for tag in item["tags"]:
            tw = len(tag) * 6.8 + 16
            tags_svg.append(
                f'<rect x="{tx:.1f}" y="92" width="{tw:.1f}" height="21" rx="5" fill="#10152b" stroke="{item["accent"]}" stroke-opacity="0.4"/>'
                f'<text x="{tx + tw / 2:.1f}" y="106" text-anchor="middle" fill="#e2e8f0" font-family="monospace" font-size="10">{escape(tag)}</text>'
            )
            tx += tw + 8

        cards.append(f"""
        <g transform="translate({x}, {y})">
          <rect width="410" height="154" rx="14" fill="#080b18" fill-opacity="0.92" stroke="{item['accent']}" stroke-opacity="0.45" stroke-width="1.3"/>
          <text x="392" y="138" text-anchor="end" fill="{item['accent']}" fill-opacity="0.14" font-family="serif" font-weight="900" font-size="44">{item['kanji']}</text>

          <circle cx="24" cy="22" r="3.5" fill="{item['accent']}">
            <animate attributeName="opacity" values="1;0.2;1" dur="1.4s" begin="{delay:.2f}s" repeatCount="indefinite"/>
          </circle>
          <text x="34" y="25" fill="{item['accent']}" font-family="monospace" font-weight="700" font-size="10.5">{escape(item['code'])}</text>

          <text x="20" y="53" fill="#f8fafc" font-family="monospace" font-weight="800" font-size="19">{escape(item['name'])}<tspan fill="{item['accent']}">_<animate attributeName="opacity" values="1;0;1" dur="0.9s" repeatCount="indefinite"/></tspan></text>
          <text x="20" y="75" fill="#cbd5e1" font-family="system-ui, sans-serif" font-size="11.5">{escape(item['desc'])}</text>

          {"".join(tags_svg)}

          <text x="20" y="137" fill="#94a3b8" font-family="monospace" font-size="10.5">&#9733; {stars} STARS   &#8226; SYNCED</text>

          <circle cx="356" cy="76" r="{radius}" fill="#0c1124" stroke="#1e2645" stroke-width="3.5"/>
          <circle cx="356" cy="76" r="{radius}" fill="none" stroke="{item['accent']}" stroke-width="3.5"
                  stroke-dasharray="{dash:.1f} {circumference:.1f}" stroke-linecap="round"
                  transform="rotate(-90 356 76)">
            <animate attributeName="stroke-opacity" values="0.6;1;0.6" dur="2s" begin="{delay:.2f}s" repeatCount="indefinite"/>
          </circle>
          <text x="356" y="80" text-anchor="middle" fill="#f8fafc" font-family="monospace" font-weight="800" font-size="11">{item['sync']}%</text>
        </g>
        """)

    svg = f"""<svg width="900" height="436" viewBox="0 0 900 436" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgMis" x1="0" y1="0" x2="900" y2="436" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#060714"/>
      <stop offset="50%" stop-color="#141029"/>
      <stop offset="100%" stop-color="#190c1c"/>
    </linearGradient>
  </defs>

  <rect x="1" y="1" width="898" height="434" rx="20" fill="url(#bgMis)" stroke="#f43f5e" stroke-opacity="0.45" stroke-width="1.5"/>

  <rect x="24" y="18" width="852" height="38" rx="10" fill="#080b18" stroke="#f43f5e" stroke-opacity="0.4"/>
  <text x="42" y="41" fill="#fda4af" font-family="monospace" font-weight="700" font-size="11.5" letter-spacing="1.5">作戦一覧 // ACTIVE OPERATIONS &amp; DEPLOYMENTS</text>
  <text x="858" y="41" text-anchor="end" fill="#6ee7b7" font-family="monospace" font-size="11">[4 UNITS ONLINE]</text>

  {"".join(cards)}
</svg>"""
    with open("assets/missions-jp.svg", "w", encoding="utf-8") as f:
        f.write(svg)


if __name__ == "__main__":
    os.makedirs("assets", exist_ok=True)
    gh_data = fetch_github_data()
    generate_hero_anime()
    generate_telemetry_jp(gh_data)
    generate_missions_jp(gh_data)
    print("Neo-Tokyo Anime SVGs generated successfully.")
