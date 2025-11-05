# Team Charter

## Team Identity

### Project Name
**Hidden Hill**

### Team Name
**Loki Lovers**

### Team Members
- Kenza Moussaoui Rahali
- Omar Sekkat
- Vincent Graf Von Armansperg
- David Schmidt
- Nour Al-Roub
- Skel Yeung

### Repository
https://github.com/Kenza-R/Hidden-hill

---

## 👥 Roles & Responsibilities

> **Note:** While team members are assigned to specific roles below, in practice **the entire team works collaboratively on all aspects of development**. Role titles help organize responsibilities, but we prioritize shared ownership and cross-functional contribution.

### Scrum Master
**Assigned to:** Kenza Moussaoui Rahali

**Purpose:** Facilitates the agile process, removes blockers, ensures team effectiveness

**Responsibilities:**
- Facilitate daily standups
- Manage sprint planning and retrospectives
- Remove blockers and impediments
- Track sprint metrics (velocity, burndown)
- Ensure team follows Definition of Ready/Done
- Facilitate communication between team and stakeholders

**Authority & Limitations:**
- Cannot directly assign work (team self-organizes)
- Can suggest process improvements
- Acts as servant-leader, not dictator

### Product Owner Proxy
**Assigned to:** Nour Al-Roub

**Purpose:** Represents user needs, prioritizes backlog, accepts completed work

**Responsibilities:**
- Maintain and prioritize product backlog
- Define acceptance criteria for user stories
- Answer questions about requirements
- Accept/reject completed work based on acceptance criteria
- Communicate with stakeholders about priorities
- Validate that stories deliver user value

**Authority & Limitations:**
- Cannot make technical decisions (team decides how)
- Can say "no" to scope creep
- Consults with team on feasibility before committing

### Development Team
**Members:**
- Omar Sekkat
- Vincent Graf Von Armansperg
- David Schmidt
- Skel Yeung
- *(Plus Kenza and Nour who also code)*

**Purpose:** Design, build, test, and deploy features

**Responsibilities:**
- Implement user stories to Definition of Done
- Estimate story effort collaboratively
- Review peers' code before merging
- Write tests and documentation
- Raise concerns about feasibility/risk
- Participate in all ceremonies (standups, planning, retros)

**Authority & Limitations:**
- Choose HOW to implement (technical decisions)
- Can push back on unrealistic deadlines
- Cannot unilaterally change priorities

**Collaborative Development:**
All team members contribute to coding, design, testing, and deployment decisions regardless of formal role. The Scrum Master and Product Owner are active developers too—they just have additional coordination responsibilities.

---

## 📅 Communication Plan

### Regular Meetings

| Meeting | Frequency | Duration | Time | Purpose |
|---------|-----------|----------|------|---------|
| Team Sync | Weekly (Monday) | 1 hour | 7:00 PM | Weekly team check-in and coordination |
| Daily Standup | Daily | 5 min | 7:00 PM | Text on group chat about personal advancement |
| Sprint Planning | Week before sprint | 2 hours | 7:00 PM | Plan upcoming sprint |
| Sprint Review & Retrospective | Sprint end | 2 hours | 7:00 PM | Demo work and reflect on process |

### Key Project Milestones & Sprint Schedule

| Date | Event | Purpose |
|------|-------|---------|
| Tuesday, Nov 4 | Sprint Planning 2 | Plan Sprint 2 development |
| Tuesday, Nov 11 | Sprint 2 Review & Retro | Review Sprint 2 work and reflect |
| Tuesday, Nov 11 | Sprint Planning 3 | Plan Sprint 3 MVP development |
| Tuesday, Nov 18 | Sprint 3 Review & Retro | Review Sprint 3 work and reflect |
| Tuesday, Nov 18 | Sprint Planning 4 | Plan Sprint 4 final sprint |
| Tuesday, Dec 2 | Sprint 4 Review & Retro | Review Sprint 4 work and reflect |
| Thursday, Dec 11 | Final Submission | Project delivery |

**Weekly Team Meeting:** Every Monday at 7:00 PM  
**Daily Standup:** Every day at 7:00 PM via group chat (5 min, text-based updates on personal advancement)

### Async Communication

**Primary Channels:**
- **WhatsApp Group:** Loki Lovers team chat for daily updates and quick questions
- **Zoom Meetings:** For all scheduled team meetings (links shared in WhatsApp)
- **GitHub Issues:** Technical discussions and code-related questions

**Response Time Expectations:**
- Urgent issues: Response within 2 hours (during work hours)
- General questions: Response within 24 hours
- Non-urgent: Can wait until next meeting

### Status Updates
- **Standups:** Every weekday morning (async or in-person)
- **Weekly:** Team updates in Friday retro or separate sync
- **Sprint Reports:** At end of each sprint

### Escalation Path
If a blocker can't be resolved:
1. Team member → Scrum Master (remove impediment)
2. Scrum Master → Product Owner Proxy (if priority conflict)
3. Product Owner Proxy → [Stakeholder/Instructor] (if needed)

---

## 🤝 Working Agreements

### Code Review Process

**When:** All code must be reviewed before merging to `main`

**How:**
1. Create a feature branch: `feature/issue-#-short-name` or `fix/issue-#-short-name`
2. Push and open a Pull Request (PR) with description
3. At least **1 reviewer** must approve
4. Status checks must pass (CI/linting/tests)
5. Merge only after approval + checks pass

**Code Review SLA:**
- **Target:** Review within 24 hours
- **Expectation:** Reviews are priority (check PRs first each day)
- **Format:** Constructive feedback, ask questions, suggest improvements
- **Approval:** Reviewer says "Approved" or "Changes Requested"

**Reviews Should Check:**
- [ ] Code follows project style guide
- [ ] Tests written and passing
- [ ] Documentation updated if needed
- [ ] No hardcoded secrets/passwords
- [ ] Performance implications considered
- [ ] Follows Definition of Done

### Branch Naming Convention

**Format:** `[type]/[issue-number]-[short-description]`

**Types:**
- `feature/` - New feature (e.g., `feature/34-user-authentication`)
- `fix/` - Bug fix (e.g., `fix/42-login-timeout`)
- `docs/` - Documentation only (e.g., `docs/api-readme`)
- `refactor/` - Code refactor (e.g., `refactor/database-queries`)
- `test/` - Tests only (e.g., `test/user-model-coverage`)
- `chore/` - Maintenance (e.g., `chore/update-dependencies`)

**Rules:**
- All lowercase
- Use hyphens (no underscores or spaces)
- Keep concise but descriptive
- Link to GitHub issue when possible

### Commit Message Format

**Format:**
```
[TYPE] Brief description (< 50 chars)

- Bullet point explaining the change
- Another detail if needed
- References issue if related: Closes #123
```

**Types:**
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation change
- `style:` Formatting (no code change)
- `refactor:` Code restructure (no behavior change)
- `test:` Test additions/changes
- `chore:` Dependencies, tooling, maintenance

**Examples:**
```
feat: add user login endpoint

- Implement POST /auth/login route
- Add password hashing with bcrypt
- Return JWT token on success
Closes #34
```

```
fix: resolve race condition in cache

- Add mutex lock to prevent concurrent writes
- Refactor cache update logic
- Add test case for concurrent access
```

### Code Style & Standards

**Enforced by:**
- ESLint / Prettier (JavaScript/TypeScript)
- Black / Flake8 (Python)
- [Other tools for your stack]

**Quality Gates:**
- All tests must pass before merge
- Code coverage target: [80%/90%?]
- No hardcoded values or magic numbers
- Documentation for public APIs/functions

### Working Hours & Availability

**Core Hours:** [9 AM - 5 PM timezone/flexible?]

**Expectations:**
- Available for standups during core hours
- Can work async outside core hours
- Notify team if unavailable for more than a day
- Use Slack status to show availability

### Definition of Ready for Backlog Refinement

Before a story enters a sprint, it must meet:
- [ ] User story statement written (As a... I want... so that...)
- [ ] Acceptance criteria defined (Given-When-Then format, minimum 3)
- [ ] Story points estimated by team
- [ ] Priority assigned (High/Medium/Low)
- [ ] Dependencies identified
- [ ] Questions from team answered by PO
- [ ] Mockups/wireframes attached (if needed)
- [ ] Testable and unambiguous

### Definition of Done

A story is done when:
- [ ] Code written and committed to feature branch
- [ ] At least 1 peer code review completed and approved
- [ ] All tests written and passing (unit & integration)
- [ ] Manual testing completed in staging environment
- [ ] No hardcoded values or sensitive data exposed
- [ ] README/documentation updated if needed
- [ ] PR merged to `main` branch
- [ ] Deployed to staging (or ready for release)
- [ ] Product Owner verified acceptance criteria met

---

## 🔄 Role Rotation Schedule

### Scrum Master Rotation

**Why rotate?** Everyone learns the role, no single point of failure, shared ownership

**Rotation:**
- **Sprint 2 Scrum Master:** David Schmidt
- **Sprint 3 Scrum Master:** Omar Sekkat
- **Sprint 4 Scrum Master:** Skel Yeung
- **Pattern:** Rotate each sprint

**Transition:**
- Outgoing Scrum Master briefs incoming SM at end of sprint
- Incoming SM prepares for planning meeting
- 2-3 day overlap if possible for questions

### Other Role Considerations
- **Product Owner Proxy:** Nour Al-Roub (fixed for Sprint 1-3)
- **Scrum Master:** Kenza Moussaoui Rahali (fixed for Sprint 1-3)

---

## ⚖️ Conflict Resolution Process

### Principle
**Assume good intent, resolve quickly, move forward as a team**

### Conflicts About Work
*(e.g., design decision, technical approach, priority disagreement)*

**Level 1: Team Discussion**
- Discuss openly in standup or async in Slack
- Share perspectives and rationale
- Aim for consensus (everyone can live with the decision)

**Level 2: Scrum Master Facilitation**
- If stuck, Scrum Master facilitates decision-making
- May use techniques: pros/cons list, spike vote, timeline
- Document decision and rationale

**Level 3: Product Owner Input**
- If business/priority conflict, PO has final say
- Explain reasoning to team
- Team commits to decision

### Interpersonal Conflicts
*(e.g., personality clash, communication breakdown)*

**Level 1: Direct Conversation**
- Talk 1-on-1 privately and respectfully
- Listen to understand, not to win
- Seek common ground

**Level 2: Scrum Master Mediation**
- If unresolved, Scrum Master facilitates conversation
- Private meeting with both parties
- Focus on behaviors and impact, not blame

**Level 3: Team Lead / Instructor**
- If still unresolved, escalate to team lead or course instructor
- Formal mediation if needed

### Escalation Path
```
Team Discussion / 1-on-1 Conversation
        ↓
   Scrum Master Facilitation
        ↓
  Team Lead / Instructor
```

### Team Values for Resolution
- **Respect:** Different opinions are valid
- **Transparency:** Say what you think, not what you think others want to hear
- **Speed:** Make a decision and move forward (don't linger)
- **Commitment:** Once decided, support the team's direction
- **Accountability:** Take responsibility for your part

---

## 📊 Metrics & Success

### Sprint Metrics We'll Track
- **Velocity:** Story points completed per sprint (helps forecast)
- **Burndown:** Work remaining vs. time (shows sprint health)
- **Cycle Time:** Time from start to done per story
- **Code Quality:** Test coverage, code review feedback
- **Team Health:** Retrospective feedback, morale check-ins

### Review Points
- **Weekly:** Standup pulse checks
- **Sprint End:** Full retrospective on process and product
- **Monthly:** Team health check-in (if multi-month project)

---

## 🎉 Team Norms & Culture

### What We Value
- **Quality over Speed:** Better to ship less, but better
- **Collaboration:** Pair programming, knowledge sharing, helping teammates
- **Learning:** Experimentation, trying new things, sharing learnings
- **Psychological Safety:** It's okay to fail, ask questions, be vulnerable
- **Transparency:** Share progress, blockers, and concerns openly

### Celebration & Recognition
- Celebrate sprint wins (shipped features, resolved bugs)
- Recognize good collaboration and peer help
- Share learnings at retro, not failures
- [Optional: weekly shout-outs, prizes, etc.]

### Remote Work Etiquette (if applicable)
- Keep camera on during meetings (builds connection)
- Mute when not speaking (reduces background noise)
- Test tech 5 minutes before important meetings
- Be present (minimize tab switching during standups)

---

## ✍️ Signature / Agreement

This charter represents our team's commitment to working together effectively. By joining the team, you agree to:
- Participate in all ceremonies (standups, planning, retros)
- Follow the working agreements above
- Give constructive feedback to teammates
- Raise concerns promptly rather than lingering
- Support decisions made by the team

**Date Created:** November 5, 2025

**Team Members (signatures):**
- Kenza Moussaoui Rahali - November 5, 2025
- Omar Sekkat - November 5, 2025
- Vincent Graf Von Armansperg - November 5, 2025
- David Schmidt - November 5, 2025
- Nour Al-Roub - November 5, 2025
- Skel Yeung - November 5, 2025

---

## 📝 Charter Updates

This charter is a living document. We can update it if:
- Something isn't working (bring up in retro)
- External circumstances change
- Team consensus agrees on a change
---

**Last Updated:** November 5, 2025  
**Review Frequency:** End of each sprint (can update if needed)
