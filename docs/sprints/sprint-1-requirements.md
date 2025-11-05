# Sprint 1 Deliverables Checklist

> **Kyle's Note:** Focus on what matters: clear user journeys, a solid product backlog, and thoughtful technical planning. This checklist keeps us honest.

## 📋 Deliverable Tracking

- [ ] **User Research & Problem Definition** (3 pts)
- [ ] **Product Backlog with INVEST Stories** (4 pts)
- [ ] **Story Point Estimates & Prioritization** (included in backlog)
- [ ] **Wireframes/Mockups** (2 pts)
- [ ] **Technical Architecture Plan** (2 pts)
- [ ] **GitHub Project Setup** (2 pts)
- [ ] **Sprint 2 & 3 Planning** (1 pt)
- [ ] **Team Documentation** (1 pt)
- [ ] **Sprint 1 Report** (comprehensive summary)

---

## 1️⃣ User Research & Problem Definition

### User Personas & Journeys

**Instructions:** Create 2-3 user personas representing your target users. Document both:
- Current state: How they solve this problem today (pain points)
- Desired state: How your app will solve it

#### Persona Template
```markdown
### Persona: [Name]
- **Role:** [Job title/role]
- **Goals:** [What they want to achieve]
- **Pain Points:** [What frustrates them today]
- **Tech Comfort:** [Beginner/Intermediate/Advanced]

**Current Journey (As-Is):**
[How they currently solve this problem - list steps]
- Step 1:
- Step 2:
- Step 3:
**Pain Points:** [Specific frustrations at each step]

**Ideal Journey (To-Be):**
[How your app improves this - list steps]
- Step 1:
- Step 2:
- Step 3:
**Improvements:** [How this is better]
```

---

### Problem Validation

**Evidence the problem is real:**
- [ ] User interviews conducted (target: 2-3 people)
- [ ] Personal experience / dogfooding
- [ ] Survey data (optional)
- [ ] Competitor research

**Pain Points Identified:**
1. 
2. 
3. 

**Why existing solutions are insufficient:**
- [Solution 1] doesn't work because...
- [Solution 2] fails because...
- [Gap in market]: ...

---

## 2️⃣ Product Backlog with INVEST User Stories

**Location:** GitHub Project → [Link to your project]

### INVEST Criteria Reminder
- **Independent:** Can be built in any order
- **Negotiable:** Implementation details flexible
- **Valuable:** Clear user value
- **Estimable:** Team can estimate effort
- **Small:** Fits in 1-2 week sprint
- **Testable:** Has clear acceptance criteria

### Required Stories (Minimum 15-20)

Add your user stories to GitHub Issues with this format:

```markdown
**Title:** [Feature name] (< 60 chars)

**User Story:**
As a [role], I want [feature], so that [benefit]

**Acceptance Criteria:**
- Given [context], when [action], then [result]
- Given [context], when [action], then [result]
- Given [context], when [action], then [result]

**Story Points:** [1/2/3/5/8/13]
**Priority:** [High/Medium/Low]
**Labels:** #user-story
**Epic:** [Optional]
```

### Story Backlog Summary
| # | Title | Story Points | Priority | Status |
|---|-------|--------------|----------|--------|
| 1 | [Feature] | ? | ? | - |
| 2 | [Feature] | ? | ? | - |
| ... | ... | ... | ... | ... |

**Total Stories:** ? (Target: 15-20)  
**Total Story Points:** ?  
**MVP Stories:** ? of ?

---

## 3️⃣ Story Point Estimates & Prioritization

### Planning Approach
- **Method:** Planning Poker / Team estimation
- **Fibonacci Scale:** 1, 2, 3, 5, 8, 13, ?
- **Date Estimated:** [When]

### Priority Rationale
Prioritize based on:
1. User value (does it solve a core pain point?)
2. Technical dependencies (what must be built first?)
3. Sprint capacity

**MVP vs Nice-to-Have:**
- **MVP (Must-Have):** Stories needed for core user journey
- **Nice-to-Have:** Valuable but not critical for launch

---

## 4️⃣ Wireframes/Mockups

### Key User Flows to Wireframe
1. **[Core User Journey #1]** - Screens: [List]
2. **[Core User Journey #2]** - Screens: [List]
3. **[Core User Journey #3]** - Screens: [List]
4. **[Supporting Flow]** - Screens: [List]
5. **[Supporting Flow]** - Screens: [List]

### Wireframe Assets
- **Tool Used:** [Figma/Balsamiq/Hand-drawn/Other]
- **Fidelity Level:** [Low-fi sketches / High-fi mockups]
- **Link/Location:** [Add link or attach files]

### Screen Inventory
| Screen Name | User Journey | Purpose | Notes |
|-------------|-------------|---------|-------|
| [Screen 1] | [Journey] | [Purpose] | [Interactions] |
| [Screen 2] | [Journey] | [Purpose] | [Interactions] |

---

## 5️⃣ Technical Architecture Plan

### Backend Framework
**Choice:** [Django/Rails/Phoenix/Laravel/Other]

**Rationale:**
- Why this framework?
- Team familiarity?
- Scalability fit?
- Community support?

### Database
**Choice:** [PostgreSQL/MySQL/MongoDB/Other]

**Initial Schema Thoughts:**
```
[List key tables/collections you'll need]
- users
- [entity]
- [entity]
```

### Deployment Platform
**Choice:** [Render/Fly.io/Heroku/Railway/Other]

**Reasoning:**
- Cost considerations
- Scaling needs
- Developer experience

### Third-Party Services
- **Authentication:** [Auth0/Firebase/Devise/None]
- **Email:** [SendGrid/Mailgun/Built-in]
- **Storage:** [S3/Cloudinary/Local]
- **Other:** [List any others]

### Development Workflow
**Branching Strategy:** [e.g., Git Flow, Trunk-Based Development]

**Commit Message Format:** 
```
[TYPE] Short description
- Type: feat|fix|docs|style|refactor|test|chore
- Example: feat: add user authentication
```

**Code Review Process:**
- [ ] Pull requests required
- [ ] Minimum reviewers: [1/2]
- [ ] Required status checks: [CI/tests/linting]
- [ ] Target branch protection: `main`

---

## 6️⃣ GitHub Project Setup

### Project Configuration
- **URL:** [Link to GitHub Project]
- **Type:** Table & Board views
- **Created:** [Date]

### Custom Fields
- [ ] **Story Points** - Number (1, 2, 3, 5, 8, 13, ?)
- [ ] **Status** - Single Select (To Do, In Progress, In Review, Done)
- [ ] **Priority** - Single Select (High, Medium, Low)
- [ ] **Sprint** - Iteration field (1-2 week sprints)

### Views Required
- [ ] **Product Backlog** (Table)
  - Filter: `label:"user story"`
  - Sort: Priority ↓, Story Points
  - Visible: Title, Assignees, Story Points, Priority, Status

- [ ] **Sprint 2 Backlog** (Table)
  - Filter: `label:"user story" iteration:"Sprint 2"`
  - Visible: Title, Assignees, Story Points, Status, Sprint

- [ ] **Sprint 2 Task Board** (Board)
  - Filter: `(label:"task" OR label:"spike") iteration:"Sprint 2"`
  - Group by: Status
  - Columns: To Do → In Progress → In Review → Done

### Labels Configured
- [ ] **user story** (blue) - User-facing feature
- [ ] **task** (green) - Technical work
- [ ] **bug** (red) - Defect
- [ ] **epic** (purple) - Feature grouping
- [ ] **spike** (yellow) - Research/investigation
- [ ] **documentation** (gray) - Docs work

### Issue Templates
- [ ] `.github/ISSUE_TEMPLATE/user-story.md`
- [ ] `.github/ISSUE_TEMPLATE/task.md`
- [ ] `.github/ISSUE_TEMPLATE/bug.md`

---

## 7️⃣ Sprint 2 & 3 Planning

### Sprint 2 Plan

**Document Location:** `/docs/sprints/sprint-2-planning.md` *(create if needed)*

- [ ] **Sprint Goal:** [Specific, measurable goal - e.g., "Get working MVP deployed to staging"]
- [ ] **Selected User Stories:** [List with issue numbers & story points]
- [ ] **Total Committed Story Points:** [Number] (Based on team capacity)
- [ ] **Team Member Assignments:** [Who's working on what?]
- [ ] **Dependencies & Risks:** [What could block us?]

### Sprint 3 Preview
- [ ] **Draft Sprint Goal:** [Tentative goal for Sprint 3]
- [ ] **Candidate User Stories:** [Tentatively selected features]
- [ ] **Notes:** [Any dependencies on Sprint 2 work?]

---

## 8️⃣ Team Documentation

### Created Documents

#### `/docs/team-charter.md`
- [ ] Team name and members listed
- [ ] Roles assigned: Scrum Master, Product Owner proxy, Developers
- [ ] Communication plan defined (Slack/Discord channels, meeting times)
- [ ] Working agreements (code review SLA, branch naming, commit format)
- [ ] Role rotation schedule (e.g., Scrum Master rotates each sprint)
- [ ] Conflict resolution process

#### `/docs/definition-of-ready.md`
- [ ] Criteria for when stories are ready to enter Sprint Planning
- [ ] Examples: "Acceptance criteria defined and testable", "Story points estimated"

#### `/docs/definition-of-done.md`
- [ ] Criteria for when stories are marked "Done"
- [ ] Examples: "Code reviewed", "Tests passing", "Deployed to staging"

---

## 📊 Sprint 1 Report

### Report Location
**File:** `/docs/sprints/sprint-1-review.md` (or GitHub Wiki page)

### Report Contents (2-4 pages)

- [ ] **Executive Summary** (2-3 paragraphs)
  - What you're building and why
  - Target users and core pain point
  - MVP scope

- [ ] **User Research** (1 page)
  - Personas
  - User journeys (current + ideal)
  - Problem validation evidence

- [ ] **Product Vision** (1 paragraph)
  - MVP scope
  - Key features
  - Success metrics

- [ ] **Wireframes** (1 page)
  - Link to/embed mockups
  - Key screens/flows annotated

- [ ] **Technical Architecture** (1 page)
  - Framework, database, deployment decisions with rationale

- [ ] **Product Backlog Summary**
  - Link to GitHub Project
  - Story count & total points
  - Top 5 highest-priority stories

- [ ] **Sprint 2 Plan**
  - Sprint goal
  - Committed stories
  - Team capacity & assignments

- [ ] **Team Organization**
  - Link to team charter
  - Roles & meeting schedule

- [ ] **Process Setup**
  - Link to GitHub Project
  - Definition of Done/Ready
  - Issue templates configured

---

## ✅ Submission Checklist

Before submitting Sprint 1:

- [ ] All 8 deliverables above completed
- [ ] User research documented with 2-3 personas
- [ ] 15-20 INVEST-compliant user stories in GitHub Issues
- [ ] Wireframes/mockups for 3-5 key flows
- [ ] GitHub Project configured with fields, views, labels, templates
- [ ] Team Charter & Definition of Ready/Done created
- [ ] Sprint 2 Planning documented
- [ ] Sprint 1 Report written (2-4 pages)
- [ ] All links verified and working

---

## 🎯 Success Criteria

✨ **What Kyle actually cares about:**

1. **Clear User Journeys** - Can someone read your personas and instantly understand who you're building for and why?
2. **Solid Product Backlog** - Are the stories specific, estimable, and actually testable?
3. **Thoughtful Technical Decisions** - Did you reason through your stack choices, or just pick the default?
4. **Working Process** - Is GitHub Project set up so Sprint 2 can hit the ground running?

---

## 📚 Quick References

- [GitHub Projects Quickstart](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)
- [INVEST in Good Stories](https://www.agilealliance.org/glossary/invest/)
- [User Story Examples](https://www.atlassian.com/agile/user-stories)
- [Wireframing Tools](https://www.figma.com) | [Balsamiq](https://balsamiq.com) | [Excalidraw](https://excalidraw.com)

---

**Last Updated:** November 5, 2025  
**Status:** Ready for Team Completion
