import os
import json
import math
import urllib.request
from xml.sax.saxutils import escape

USERNAME = "harukuntzy"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

ACCENT_PALETTE = [
    ("#fb7185", "🛡️"),
    ("#34d399", "🌿"),
    ("#38bdf8", "⚡"),
    ("#fbbf24", "🐾"),
    ("#a78bfa", "🌸"),
    ("#f472b6", "🎀"),
]


def github_graphql(query, variables):
    url = "https://api.github.com/graphql"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": "harukuntzy-kawaii-generator"
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
        repositories(
          first: 20
          ownerAffiliations: OWNER
          isFork: false
          privacy: PUBLIC
          orderBy: {field: PUSHED_AT, direction: DESC}
        ) {
          totalCount
          nodes {
            name
            description
            stargazerCount
            forkCount
            primaryLanguage {
              name
            }
            repositoryTopics(first: 3) {
              nodes {
                topic {
                  name
                }
              }
            }
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
            "total_contrib": 14,
            "stars": 1,
            "repos": 2,
            "followers": 0,
            "repo_list": []
        }

    res = github_graphql(query, {"login": USERNAME})
    user = res["data"]["user"]
    repos = user["repositories"]["nodes"]

    # Filter agar repositori profil (harukuntzy) tidak ikut muncul sebagai kartu proyek, kecuali hanya itu yang ada
    project_repos = [r for r in repos if r["name"].lower() != USERNAME.lower()]
    if not project_repos:
        project_repos = repos

    return {
        "total_contrib": user["contributionsCollection"]["contributionCalendar"]["totalContributions"],
        "stars": sum(r["stargazerCount"] for r in repos),
        "repos": user["repositories"]["totalCount"],
        "followers": user["followers"]["totalCount"],
        "repo_list": project_repos[:6]
    }


def generate_stats_kawaii(data):
    stats = [
        ("★", "STARS", f"{data['stars']:,}", "#f43f5e", 0.68),
        ("♥", "CONTRIBUTIONS", f"{data['total_contrib']:,}", "#ec4899", 0.85),
        ("✿", "REPOSITORIES", f"{data['repos']:,}", "#f59e0b", 0.60),
        ("✦", "FOLLOWERS", f"{data['followers']:,}", "#8b5cf6", 0.52),
    ]

    cards = []
    for idx, (icon, label, val, accent, pct) in enumerate(stats):
        x = 34 + idx * 210
        bar_w = int(166 * pct)
        delay = idx * 0.3
        cards.append(f"""
        <g transform="translate({x}, 86)">
          <rect width="198" height="106" rx="16" fill="#ffffff" fill-opacity="0.88" stroke="{accent}" stroke-opacity="0.45" stroke-width="1.5"/>
          <text x="176" y="34" text-anchor="end" fill="{accent}" fill-opacity="0.28" font-family="sans-serif" font-size="24">{icon}</text>
          <text x="18" y="27" fill="#881337" font-family="monospace" font-weight="700" font-size="10.5" letter-spacing="1">{label}</text>
          <text x="18" y="66" fill="#4c0519" font-family="system-ui, sans-serif" font-weight="900" font-size="30">{val}</text>

          <rect x="18" y="82" width="162" height="6" rx="3" fill="#ffe4e6"/>
          <rect x="18" y="82" width="{bar_w}" height="6" rx="3" fill="{accent}"/>
          <rect x="18" y="82" width="26" height="6" rx="3" fill="#ffffff" fill-opacity="0.85">
            <animate attributeName="x" values="18;{18 + max(bar_w - 26, 6)};18" dur="2.4s" begin="{delay:.2f}s" repeatCount="indefinite"/>
          </rect>
        </g>
        """)

    svg = f"""<svg width="900" height="222" viewBox="0 0 900 222" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgKawaii" x1="0" y1="0" x2="900" y2="222" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#fff1f2"/>
      <stop offset="50%" stop-color="#ffe4e6"/>
      <stop offset="100%" stop-color="#fef3c7"/>
    </linearGradient>
  </defs>

  <rect x="1" y="1" width="898" height="220" rx="22" fill="url(#bgKawaii)" stroke="#fda4af" stroke-width="2"/>

  <text x="862" y="36" fill="#fb7185" font-size="16">♥
    <animate attributeName="y" values="38;30;38" dur="2.5s" repeatCount="indefinite"/>
  </text>

  <text x="34" y="42" fill="#9f1239" font-family="system-ui, sans-serif" font-weight="800" font-size="20">🌸 STATUS TELEMETRI // @{USERNAME}</text>
  <text x="34" y="62" fill="#be123c" font-family="monospace" font-size="11">COZY CODING CORNER • AUTOMATION &amp; FULL-STACK</text>

  <g transform="translate(520, 26)">
    <rect x="0" y="0" width="72" height="24" rx="12" fill="#ffffff" stroke="#fb7185" stroke-width="1.2"/>
    <text x="36" y="15" text-anchor="middle" fill="#be123c" font-family="monospace" font-weight="700" font-size="10">PYTHON</text>
    <rect x="80" y="0" width="66" height="24" rx="12" fill="#ffffff" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="113" y="15" text-anchor="middle" fill="#0369a1" font-family="monospace" font-weight="700" font-size="10">REACT</text>
    <rect x="154" y="0" width="76" height="24" rx="12" fill="#ffffff" stroke="#34d399" stroke-width="1.2"/>
    <text x="192" y="15" text-anchor="middle" fill="#047857" font-family="monospace" font-weight="700" font-size="10">FASTAPI</text>
    <rect x="238" y="0" width="96" height="24" rx="12" fill="#ffffff" stroke="#fbbf24" stroke-width="1.2"/>
    <text x="286" y="15" text-anchor="middle" fill="#b45309" font-family="monospace" font-weight="700" font-size="10">AUTOMATION</text>
  </g>

  {"".join(cards)}
</svg>"""
    with open("assets/stats-kawaii.svg", "w", encoding="utf-8") as f:
        f.write(svg)


def generate_projects_kawaii(data):
    repos = data.get("repo_list", [])
    if not repos:
        repos = [{
            "name": USERNAME,
            "description": "Personal GitHub Profile & Kawaii Automated Showcase.",
            "stargazerCount": data.get("stars", 1),
            "forkCount": 0,
            "primaryLanguage": {"name": "Python"},
            "repositoryTopics": {"nodes": []}
        }]

    rows = math.ceil(len(repos) / 2)
    svg_height = 96 + rows * 168

    cards = []
    radius = 23
    circumference = 2 * math.pi * radius

    for idx, repo in enumerate(repos):
        col = idx % 2
        row = idx // 2
        x = 34 + col * 422
        y = 76 + row * 168

        accent, emoji = ACCENT_PALETTE[idx % len(ACCENT_PALETTE)]
        name = repo["name"]
        raw_desc = repo.get("description") or "No description provided yet — active repository."
        desc = (raw_desc[:54] + "...") if len(raw_desc) > 57 else raw_desc

        stars = repo.get("stargazerCount", 0)
        forks = repo.get("forkCount", 0)

        tags = []
        if repo.get("primaryLanguage") and repo["primaryLanguage"].get("name"):
            tags.append(repo["primaryLanguage"]["name"])
        for t in repo.get("repositoryTopics", {}).get("nodes", []):
            t_name = t.get("topic", {}).get("name")
            if t_name and t_name not in tags:
                tags.append(t_name)
        if not tags:
            tags = ["Repository"]
        tags = tags[:3]

        # Skor aktivitas dinamis berdasarkan urutan update terbaru & stars
        sync = min(98, max(65, 95 - idx * 5 + stars * 2))
        dash = (sync / 100.0) * circumference
        delay = idx * 0.35

        tags_svg = []
        tx = 20
        for tag in tags:
            tw = len(tag) * 6.8 + 18
            tags_svg.append(
                f'<rect x="{tx:.1f}" y="92" width="{tw:.1f}" height="22" rx="11" fill="#fff1f2" stroke="{accent}" stroke-width="1.1"/>'
                f'<text x="{tx + tw / 2:.1f}" y="106" text-anchor="middle" fill="#881337" font-family="monospace" font-weight="700" font-size="10">{escape(tag)}</text>'
            )
            tx += tw + 8

        cards.append(f"""
        <g transform="translate({x}, {y})">
          <rect width="410" height="154" rx="18" fill="#ffffff" fill-opacity="0.92" stroke="{accent}" stroke-opacity="0.55" stroke-width="1.5"/>

          <circle cx="24" cy="22" r="4" fill="{accent}">
            <animate attributeName="opacity" values="1;0.35;1" dur="1.6s" begin="{delay:.2f}s" repeatCount="indefinite"/>
          </circle>
          <text x="35" y="25" fill="#9f1239" font-family="monospace" font-weight="700" font-size="10.5">REPO // 0{idx + 1}</text>

          <text x="20" y="53" fill="#4c0519" font-family="system-ui, sans-serif" font-weight="900" font-size="18">{emoji} {escape(name)}</text>
          <text x="20" y="75" fill="#881337" font-family="system-ui, sans-serif" font-size="11.5">{escape(desc)}</text>

          {"".join(tags_svg)}

          <text x="20" y="137" fill="#be123c" font-family="monospace" font-weight="700" font-size="10.5">&#9733; {stars} STARS   &#9095; {forks} FORKS</text>

          <circle cx="356" cy="77" r="{radius}" fill="#fff1f2" stroke="#ffe4e6" stroke-width="4"/>
          <circle cx="356" cy="77" r="{radius}" fill="none" stroke="{accent}" stroke-width="4"
                  stroke-dasharray="{dash:.1f} {circumference:.1f}" stroke-linecap="round"
                  transform="rotate(-90 356 77)"/>
          <text x="356" y="81" text-anchor="middle" fill="#4c0519" font-family="monospace" font-weight="800" font-size="11">{sync}%</text>
        </g>
        """)

    svg = f"""<svg width="900" height="{svg_height}" viewBox="0 0 900 {svg_height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgProjKawaii" x1="0" y1="0" x2="900" y2="{svg_height}" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#fff1f2"/>
      <stop offset="50%" stop-color="#ffe4e6"/>
      <stop offset="100%" stop-color="#fce7f3"/>
    </linearGradient>
  </defs>

  <rect x="1" y="1" width="898" height="{svg_height - 2}" rx="22" fill="url(#bgProjKawaii)" stroke="#fda4af" stroke-width="2"/>

  <rect x="24" y="18" width="852" height="38" rx="14" fill="#ffffff" fill-opacity="0.88" stroke="#fda4af" stroke-width="1.2"/>
  <text x="42" y="41" fill="#9f1239" font-family="monospace" font-weight="700" font-size="11.5" letter-spacing="1">☕ REPOSITORI SAYA // @{USERNAME}</text>
  <text x="858" y="41" text-anchor="end" fill="#e11d48" font-family="monospace" font-weight="700" font-size="11">♥ {len(repos)} REPOS</text>

  {"".join(cards)}
</svg>"""
    with open("assets/projects-kawaii.svg", "w", encoding="utf-8") as f:
        f.write(svg)


if __name__ == "__main__":
    os.makedirs("assets", exist_ok=True)
    gh_data = fetch_github_data()
    generate_stats_kawaii(gh_data)
    generate_projects_kawaii(gh_data)
    print("Kawaii SVGs synced with live repositories.")
