from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# ─────────────────────────────────────────
#  EDIT ALL YOUR DETAILS HERE
# ─────────────────────────────────────────

ME = {
    "name": "TUSHAR KANTA SAHOO",
    "short_name": "TUSHAR",          # initials for avatar
    "nav_id": "Tushar",       # shown in navbar as ψ your_name
    "role": "PhD Scholar · Dept. of Physics",
    "institute": "Indian Institute of Science, Bengaluru",
    "email": "tusharsahoo@iisc.ac.in",
    "year": "1st",               # year of PhD
    "advisor": "Dr. Shubhadeep Biswas",
    "joined": "2025",
    "postgrad": "Indian Institute of Technology (ISM) Dhanbad",
    "bio": [
        "Hi! I'm a PhD student in Physics at IISc Bangalore, one of India's premier research institutions. I'm working at the intersection of light and condensed matter physics, exploring ultrafast phenomena and the hidden dynamics that emerge when intense light interacts with matter.",
        "Before IISc, I completed my master studies at Indian Institute of Technology (ISM) Dhanbad. I joined IISc in 2025 and have been fortunate to work under the guidance of Prof. Shubhadeep Biswas.",
        "Outside the lab, I enjoy athletics and sometimes solo travelling.",
    ],
    "tags": ["condensed matter", "Physics", "IISc"],
"from": "Odisha, India",
"hobbies": ["Athletics", "Solo Travelling"],
"education": [
    {
        "degree": "PhD in Physics",
        "institute": "Indian Institute of Science, Bengaluru",
        "year": "2025 — Present",
        "icon": "🎓",
    },
    {
        "degree": "MSc in Physics",
        "institute": "Indian Institute of Technology (ISM) Dhanbad",
        "year": "2023 — 2025",
        "icon": "🎓",
    },
    {
        "degree": "BSc in Physics",
        "institute": "Utkal University, Odisha",
        "year": "2020 — 2023",
        "icon": "🎓",
    },
],
"achievements": [
    {
        "title": "GATE 2025",
        "detail": "All India Rank 223",
        "icon": "🏆",
    },
    {
        "title": "NET 2024",
        "detail": "Qualified as Junior Research Fellow · All India Rank 223",
        "icon": "🏆",
    },
    {
        "title": "JAM 2023",
        "detail": "All India Rank 1029",
        "icon": "🏆",
    },
],
    "stats": {
        "year": {"value": "2st", "label": "year of phd"},
        "papers": {"value": "0", "label": "papers / preprints"},
        "curiosity": {"value": "∞", "label": "curiosity"},
    },
    "social": {
        "email": "tusharsahoo@iisc.ac.in",
        "linkedin": "https://www.linkedin.com/in/tusharkantsahoo/",
        "scholar": "https://scholar.google.com/",
    },
}

RESEARCH = [
    {
        "id": "ultrafast-spectroscopy",
        "icon": "⚡",
        "title": "High Harmonic Generation in Extreme Conditions",
        "subtitle": "PhD Research · IISc Bengaluru",
        "tag": "current",
        "short": "Capturing femtosecond-scale physics through high harmonic generation using intense lasers in extreme sample conditions.",
        "overview": [
            "In the Ultrafast Spectroscopy group at IISc, our goal is to capture physical dynamics happening at the timescale of femtoseconds — one quadrillionth of a second. At this scale, entirely new physics emerges that is invisible to conventional experimental techniques.",
            "Our current work focuses on generating high harmonics up to the 10th order using a powerful intense laser source. What makes our approach unique is the extreme condition under which we operate — our samples are deliberately kept far from ambient conditions.",
            "By pushing matter into these extreme states and probing it with high harmonic generation (HHG), we aim to capture new emerging physics that has not been observed before. The high harmonic output serves as our window into these ultrafast, extreme-condition dynamics.",
        ],
        "techniques": ["High Harmonic Generation (HHG)", "Intense Ultrafast Lasers", "Femtosecond Spectroscopy", "Extreme Condition Sample Environments"],
        "questions": "What new physics emerges when matter is driven into extreme conditions and probed at femtosecond timescales?",
    },
    {
        "id": "nuclear-dynamics",
        "icon": "⚛️",
        "title": "Electric Dipole Transition States in ⁹⁰Zr",
        "subtitle": "MSc Thesis · IIT (ISM) Dhanbad",
        "tag": "past",
        "short": "Studied nuclear structure through transfer reactions to identify pygmy dipole resonance states in Zirconium-90.",
        "overview": [
            "My master's thesis focused on understanding nuclear structure through transfer reactions. The study was titled 'Unveiling Electric Dipole Transition States in ⁹⁰Zr through the ⁹¹Zr(p,dγ)⁹⁰Zr Transfer Reaction'.",
            "The work involved detailed analysis of the ⁹¹Zr(p,dγ)⁹⁰Zr reaction using simulation tools CHUCK3 and AngCor. Correlation matrices were central to identifying pygmy dipole resonance (PDR) states in ⁹⁰Zr.",
            "A key question the thesis addressed was whether the PDR corresponds to a single particle-hole excitation or a collective excitation — a fundamental question in nuclear structure physics. The study also explored how PDR influences nucleosynthesis processes, particularly the astrophysical r-process responsible for the formation of heavy elements in the universe.",
        ],
        "techniques": ["CHUCK3 Simulation", "AngCor Analysis", "Correlation Matrices", "Transfer Reaction Analysis", "Nuclear Structure Theory"],
        "questions": "Does the pygmy dipole resonance in ⁹⁰Zr correspond to a single particle-hole excitation or a collective excitation, and how does it influence the r-process?",
    },
]

PUBLICATIONS = [
    {
        # "year": "2025",
        # "title": "Title of Your Most Recent Paper or Preprint",
        # "journal": "arXiv / Physical Review Letters / Nature Physics",
        # "authors": "Your Name, Co-author 1, Co-author 2, Advisor Name",
        # "badge": "preprint",
        # "link": "#",
    },
]

GROUPS = [
    {
        "type": "PhD · Current",
        "name": "Ultrafast Lightwave Quantum Electronics Group",
        "institute": "Indian Institute of Science, Bengaluru",
        "period": "Aug 2025 – Present",
        "pi": "Prof. Shubhadeep Biswas",
        "pi_url": "https://physics.iisc.ac.in/people/shubhadeep-biswas/",
        "group_url": "",
    },
    {
        "type": "MSc Thesis",
        "name": "Nuclear Structure and Dynamics Group",
        "institute": "Indian Institute of Technology (ISM) Dhanbad",
        "period": "Aug 2024 – Apr 2025",
        "pi": "Prof. Soumya Bagchi",
        "pi_url": "https://www.iitism.ac.in/faculty-details?faculty=sbagchi",
        "group_url": "https://sites.google.com/view/soumya-bagchi/",
    },
]

BLOG_POSTS = [

{
    "id": "iisc-open-day-2026",
    "date": "March 2026",
    "title": "Open Day at IISc",
    "snippet": "Walking through the labs, meeting researchers...",
    "tag": "academia life",
    "content": [
        "March 2026. IISc Bangalore. And the campus is unrecognizable.",
        "Open Day. I had heard about it but nothing quite prepares you for actually being here on this day. The gates are open to everyone — school kids from class one clutching their parents' hands, college students with notebooks, curious adults in their fifties and sixties walking slowly through the departments, eyes wide open. Everyone is welcome. Science is for all and today IISc means it.",
        "The campus which on a normal day is quiet and focused is now buzzing. Every department has something going on. Demonstrations, exhibits, posters, live experiments. The kind of science communication that makes you remember why any of this matters in the first place.",
        "What strikes me most is the crowd. A genuine, mixed, curious crowd. A seven year old asking questions about lasers standing next to a retired professor nodding along. That image alone says everything about what this day is.",
        "For me there is something quietly special about being here as a student, as a researcher, on this side of the gate. Not so long ago I was the outsider looking at IISc from a distance — preparing for exams, giving interviews, hoping to get in. Today I am part of the institution that opened its doors to the world.",
        "It feels like a festival. For IISc members it genuinely is one.",
    ],
    "images": [
        {"file": "openday1.JPG", "caption": "The main building"},
        {"file": "openday2.JPG", "caption": "Inside the physics lab"},
        {"file": "openday3.JPG", "caption": "With fellow researchers"},
        {"file": "openday4.JPG", "caption": "Lab Group"},
    ],
},
{
    "id": "msc-convocation-2025",
    "date": "August 2025",
    "title": "Convocation — the end of one chapter",
    "snippet": "No exams to prepare for, no results to wait for. Just three days with MSc friends, a degree in hand and a new chapter already waiting.",
    "tag": "academia life",
    "content": [
        "August 2025. IIT ISM Dhanbad. The convocation is finally here.",
        "There is a different kind of energy this time. No exam to prepare for, no result to wait for, no interview to crack. For the first time in what feels like a very long time I am just — relaxed. The next chapter is already decided. IISc is waiting. Right now though, this moment belongs to us.",
        "All of us MSc friends together for three days. The kind of days where nothing is particularly planned but everything feels memorable. We wander around campus, eat together, talk about everything and nothing, laugh about the chaos of the past two years. The late nights of thesis work, the exam stress, the uncertainty that slowly turned into clarity.",
        "Three days of just being present with the people who lived this journey alongside me.",
        "Then the convocation day arrives. We walk up, collect our degrees and just like that two years of MSc at IIT ISM Dhanbad are officially done.",
        "I look around at everyone in that moment — same batch, same department, same journey. Some are heading to other institutes, some to industry, some still figuring it out. But today none of that matters. Today we all made it here together.",
        "One chapter closed. The next one is already beginning.",
    ],
    "images": [
        {"file": "convocation1.jpeg", "caption": "MSc Physics_23-25"},
        {"file": "convocation2.jpeg", "caption": "👽"},
        {"file": "convocation3.jpeg", "caption": "Degree"},
    ],
},
{
        "id": "joining-iisc",
        "date": "July 2025",
        "title": "How I ended up at IISc — interviews, self-doubt, and an offer I didn't expect",
        "snippet": "Three interviews, two rejections, and one offer letter that felt completely unreal. Here's my honest story of getting into IISc.",
        "tag": "academia life",
        "content": [
            "After months of preparation, uncertainty, and three interviews across some of India's top research institutions — IIT Bombay, IIT Kanpur, and finally IISc Bangalore — I found myself holding an offer letter I almost didn't believe was real.",
            "The journey wasn't smooth. I interviewed at IIT Bombay and IIT Kanpur before IISc. Each interview taught me something different — about physics, about myself, and about how much I still had to learn.",
            "When my IISc interview happened, I walked out feeling unsure. I had given everything I had — my full 100% — but I wasn't fully satisfied with how I performed. The questions pushed me to my limits and I left the room thinking it probably hadn't gone the way I hoped.",
            "So when the offer letter arrived, it felt unreal. I genuinely was not prepared for that moment. There was no grand celebration planned, no backup speech ready. Just a quiet, overwhelming feeling of disbelief.",
            "If there's one thing I want anyone reading this to take away — especially those of you preparing for PhD interviews right now — it's this: never put yourself in the undeserving category by yourself. That judgment is not yours to make. Show up, give your 100%, and let the process decide. You might just surprise yourself.",
        ],
    },
{
    "id": "interview-month-may-2025",
    "date": "May 2025",
    "title": "May 2025 — the interview month",
    "snippet": "Four applications, three interviews, three offer letters. And one decision that was never really a decision at all.",
    "tag": "academia life",
    "content": [
        "After GATE, NET and BARC the next step is clear — PhD. And for PhD in India the competitive exam score is just the entry ticket. The real game is the interview round. May 2025 becomes that month. Back to back, institute to institute.",
        "I apply to four places. IIT Bombay, IIT Kanpur, IISER Pune and IISc Bangalore. These are not random choices — these are the serious research institutes in India and after the results I have been getting I feel like I have earned the right to aim here.",
        "IISER Pune I have to skip because of academic commitments back at ISM. Three remain. I prepare, I travel, I sit across panels of professors and answer whatever they throw at me.",
        "IIT Bombay. Done. IIT Kanpur. Done. IISc Bangalore. Done. Walked out unsure but gave everything I had.",
        "Then the offer letters start coming. First one. Then another. Then IISc.",
        "All three.",
        "I sit with that for a long moment. A few months ago I was a MSc student juggling thesis work and exam preparation in Dhanbad. Now I have offer letters from three of the finest research institutions in the country sitting in front of me.",
        "The decision doesn't take long. IISc Bangalore. There is no second thought. It is the best research university in India and it is where I want to spend the next years of my life doing serious physics.",
        "I accept the offer. The chapter closes. A bigger one opens.",
    ],
    "images": [],
},
{
    "id": "barc-2025",
    "date": "April 2025",
    "title": "BARC — I just showed up",
    "snippet": "Six days after NET, another exam. No preparation, no pressure. I just appeared. Then the result came and I stared at the screen.",
    "tag": "academia life",
    "content": [
        "Six days after NET I have another exam. BARC. Honestly? I am not serious about it at all. The energy that carried me through GATE and NET has done its job and right now I am running on empty. I register, I show up, I sit in the exam hall. That's about the extent of my preparation and intention.",
        "No strategy, no revision, no pressure. I just appear.",
        "I walk out without giving it a second thought. It's done and I have already moved on mentally.",
        "Then the result comes and I stare at the screen. Cleared. Not just cleared — selected for interview.",
        "Three exams. Three clears. The last one I walked into with almost zero preparation and somehow it still worked. I don't fully understand what is happening but something is clearly going right. Now there's an interview to prepare for.",
    ],
    "images": [],
},
{
    "id": "net-jrf-2024",
    "date": "April 2025",
    "title": "NET JRF — same rank, different exam",
    "snippet": "Fifteen days after GATE, I walked into NET feeling unusually peaceful. Then the result came and I actually laughed — AIR 223. Again.",
    "tag": "academia life",
    "content": [
        "Fifteen days. That's the gap between GATE and NET. Most people would take a breath, rest a little. I do exactly that — not out of laziness but out of a quiet confidence that has settled in after GATE. The preparation I have put in over these months is already there inside me. I don't need to cram again. I just need to show up.",
        "So that's what I do. No extra pressure, no panic revision sessions. I walk into the NET exam hall feeling unusually peaceful for someone sitting a national level exam. The questions feel familiar. The GATE preparation has done its job — the concepts are solid, the problem solving instinct is there.",
        "I walk out feeling okay. Not overconfident, not worried. Just okay.",
        "Then the result comes. I look at my rank and I actually laugh. All India Rank 223. Again. The exact same number. Out of all the possible ranks in the entire country I land on 223 twice in fifteen days. Qualified as Junior Research Fellow.",
        "I don't know what to make of that coincidence. Maybe it means nothing. Maybe it means everything. But sitting here with two national level exams cleared and JRF in hand — I feel like the path ahead is becoming clearer with every result that drops.",
    ],
    "images": [],
},
{
    "id": "gate-2025-result",
    "date": "March 2025",
    "title": "AIR 223 — I wasn't expecting this",
    "snippet": "Two months, two things running parallel — MSc thesis and GATE preparation. Then the result dropped and I just sat with that number for a moment.",
    "tag": "academia life",
    "content": [
        "December 2024. MSc thesis is already consuming most of my time and energy but I know I cannot ignore GATE. The exam is in February 2025 and that gives me roughly two months. I start preparing alongside my thesis work — splitting my days between simulation tools, correlation matrices and GATE problem sets.",
        "It is not easy managing both. Some days the thesis takes everything and GATE preparation gets pushed to late nights. Some days it is the other way around. But I keep going because I know what is at stake. GATE is not just an exam — it is the next door.",
        "February comes and I sit for the exam. Walking out I have that familiar feeling — I gave it what I had but I genuinely don't know what number is coming. I am not expecting anything spectacular. I just hope it is good enough.",
        "Then the result drops. All India Rank 223.",
        "I sit with that number for a moment. 223. I read it again. Still 223. Honestly I don't have a grand reaction — no jumping around, no big celebration. Just a quiet, deep happiness for myself. Something I worked for in the middle of everything else actually came through. That feeling is enough.",
    ],
    "images": [],
},
{
    "id": "first-research-group-2024",
    "date": "August 2024",
    "title": "Walking into my first research group",
    "snippet": "First preference, cgpa counselling, and a group that made me feel like research was exactly where I belonged.",
    "tag": "research",
    "content": [
        "MSc thesis semester is here and everyone is trying to get into their preferred group. The process works through cgpa counselling — you list your preferences and hope the numbers work in your favour. Prof. Soumya Bagchi's Nuclear Dynamics Group is my first preference and I get it. That moment itself feels like a small win.",
        "From the very beginning I have been drawn toward nuclear physics. There is something about it — the scale, the complexity, the fact that you are trying to understand what is happening inside the nucleus itself. So walking into this group doesn't feel like an assignment. It feels like exactly where I want to be.",
        "The group members are the first thing that surprises me. I was not sure what to expect but they are genuinely warm and friendly from day one. No hierarchy, no coldness. Just people who are doing serious work and are happy to have you around. They motivate me, check in on my progress and make me feel like my future in research is something real and worth investing in.",
        "The work itself though — that's a different story initially. The concepts, the simulation tools, the way research actually functions day to day — it takes time to catch up. There are moments where I feel completely lost. But Prof. Bagchi never makes me feel that way. He always gives me time. Sits with me, explains things patiently, never makes me feel like I am behind. That kind of mentorship in the early days of research means everything.",
        "I don't know it yet but this group, this professor, this topic — it is all quietly shaping the kind of researcher I am becoming.",
    ],
    "images": [],
},
{
    "id": "jam-journey-2023",
    "date": "March 2023",
    "title": "The JAM that opened the door",
    "snippet": "Final semester, parallel preparation, and one rank that changed everything. This is how my journey into serious academic physics began.",
    "tag": "academia life",
    "content": [
        "It's my final semester of BSc at Utkal University and honestly the pressure is real. While everyone around me is laser focused on end semester exams, I have been running two things in parallel for months now — regular coursework and JAM preparation.",
        "From day one of my undergraduate life I have been clear about one thing — I want to continue with Masters in Physics and I want to do it at a good institute. In India that path has one gate and it is called JAM. The Joint Admission test for MSc. Clear it and the IITs become real. Miss it and you either spend another year or rethink everything.",
        "Results come out in March 2023. Right in the middle of my final semester. I open the page and see All India Rank 1029. Honestly? I am pretty chill. Not because the number doesn't matter but because the only thing that mattered has just happened — I have cleared it. I have a seat at an IIT. That was always the goal and it is done.",
        "I am ending up at IIT (ISM) Dhanbad. A new city, a new institute, a whole new chapter. I don't know what is coming next but right now in this moment it feels like the door just opened. I am walking through it.",
    ],
    "images": [],
},
]

# ─────────────────────────────────────────
#  ROUTES
# ─────────────────────────────────────────

@app.route("/")
def index():
    return render_template(
        "index.html",
        me=ME,
        research=RESEARCH,
        publications=PUBLICATIONS,
        blog_posts=BLOG_POSTS,
        groups=GROUPS,
        now=datetime.now(),
    )
@app.route("/blog/<post_id>")
def blog_post(post_id):
    post = next((p for p in BLOG_POSTS if p["id"] == post_id), None)
    if post is None:
        return "Post not found", 404
    return render_template("blog_post.html", post=post, me=ME)
@app.route("/about")
def about():
    return render_template("about.html", me=ME)
@app.route("/research/<research_id>")
def research_detail(research_id):
    item = next((r for r in RESEARCH if r["id"] == research_id), None)
    if item is None:
        return "Research not found", 404
    return render_template("research.html", item=item, me=ME)

if __name__ == "__main__":
    app.run(debug=True)
