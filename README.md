# lori-claude-skills

![Two Claude skills: cross-project-extraction and retrieval-coach](docs/cover.svg)

Skills I built for Claude to fix problems I kept running into in my own work. Each one started as a workaround I got tired of repeating. They are free to use and change.

A skill is a folder with a `SKILL.md` file that tells Claude how to handle one kind of task. Once installed, Claude picks it up on its own when the situation matches.

## The skills

| Skill | Use it when | What it does |
|---|---|---|
| [cross-project-extraction](cross-project-extraction/) | You solved something in one Claude project and need it in another | Runs the search as a planned trip with three stops, and carries context between projects in a copy-paste block |
| [retrieval-coach](retrieval-coach/) | You're in the right project and your search words keep missing | Asks one question before searching, offers different angles on the idea, then shows you why the winning keyword worked |

The two work as a pair. `cross-project-extraction` gets you to the right project. `retrieval-coach` helps once you're there and can't name what you want.

## How they work

![One trip with three stops, and the retrieval coach flow](docs/how-it-works.svg)

## Install

**Claude app (web, desktop, mobile)**

1. Download this repo and zip the folder of the skill you want, for example `retrieval-coach`. The folder name has to match the skill name.
2. In Claude, go to **Customize > Skills**.
3. Click **+**, then **Create skill**, then **Upload a skill**.
4. Upload the zip.

Code execution has to be on for skills to work. On individual plans it is under **Settings > Capabilities**. On Team and Enterprise plans an owner turns it on for the organization.

**Claude Code**

Copy the skill folder into `~/.claude/skills/`.

Steps follow Anthropic's guide as of October 2026: [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## Before you use them

Each skill folder has its own README with the problem behind it, how it works, what to edit for your setup, and its limits. `cross-project-extraction` has a project map you need to fill in with your own projects.

## License

MIT. See [LICENSE](LICENSE).

Built by [Lorisca Cessia](https://lori-sca.github.io).
