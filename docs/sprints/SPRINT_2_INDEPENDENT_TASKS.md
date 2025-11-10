# Sprint 2 Independent Tasks - Parallel Development

## 🎯 Goal
Break down the video generation app into 6 **independent** tasks that can be worked on in parallel by each team member, then integrated at the end of the sprint.

---

## 📦 Task 1: Backend - API Server & Database Schema
**Owner:** [Assign 1 person]  
**Duration:** 1-2 weeks  
**Deliverable:** Working FastAPI server with PostgreSQL database

### What to Build
1. **FastAPI Project Setup**
   - Create new FastAPI project with proper structure
   - Set up project dependencies (requirements.txt or pyproject.toml)
   - Configure CORS, logging, error handling
   - Health check endpoint: `GET /health` → `{"status": "ok"}`

2. **Database Schema**
   - PostgreSQL database with tables:
     - `users` (id, email, created_at)
     - `videos` (id, user_id, pubmed_id, status, created_at, video_url)
     - `jobs` (id, video_id, job_type, status, progress, error_msg, created_at)
   - Use SQLAlchemy ORM for models
   - Create migration scripts

3. **Core API Endpoints (Stubs)**
   - `POST /api/videos/generate` → Accept { "pubmed_id": "..." } → Return { "job_id": "..." }
   - `GET /api/videos/:job_id` → Return job status
   - Store data in database (even if generation doesn't work yet)

### Success Criteria
- ✅ FastAPI server runs locally
- ✅ Can connect to PostgreSQL
- ✅ Create/read video records in database
- ✅ API endpoints return correct JSON structure
- ✅ No external dependencies needed yet (Task 2 handles that)

### Technology
- Framework: FastAPI
- Database: PostgreSQL + SQLAlchemy
- Port: 8000

---

## 📦 Task 2: Job Queue & Video Generation Pipeline
**Owner:** [Assign 1 person]  
**Duration:** 1-2 weeks  
**Deliverable:** Working Celery + Redis setup integrated with professor's code

### What to Build
1. **Redis & Celery Setup**
   - Redis cache running locally
   - Celery worker configured
   - Task: `generate_video_task(pubmed_id)` that wraps professor's CLI

2. **Pipeline Integration**
   - Copy professor's code (main.py, pipeline.py, etc.) into your project
   - Create a function that calls: `python main.py generate-video [PMC_ID] [output_dir]`
   - Task should:
     - Create temp output directory
     - Run professor's pipeline
     - Return video file path
     - Handle errors gracefully

3. **Status Tracking**
   - Task updates database job status: pending → processing → completed/error
   - Store output: video path, error messages, timestamps

4. **Fake Video Generation (for testing)**
   - Create a mock video file (just for testing without needing API keys)
   - Mock function generates dummy MP4 file for testing

### Success Criteria
- ✅ Redis runs locally
- ✅ Celery worker can be started
- ✅ Can queue a task and track status
- ✅ Mock video generation works end-to-end
- ✅ Real generation works with API keys (will test in integration)

### Technology
- Message Queue: Celery
- Cache: Redis
- External: Professor's Python code

### Note
This task can work **independently** because:
- Uses mock videos for testing (no real API keys needed yet)
- Database structure set up by Task 1
- Frontend doesn't depend on this yet

---

## 📦 Task 3: Frontend - React App Setup & UI Components
**Owner:** [Assign 1 person]  
**Duration:** 1-2 weeks  
**Deliverable:** React app with all pages/components built (but not connected to backend yet)

### What to Build
1. **React Project Setup**
   - Create React app with Vite
   - Install dependencies: axios, react-router, tailwindcss
   - Project structure: src/pages/, src/components/, src/api/

2. **Pages**
   - **Homepage:** Landing page with "Get Started" button
   - **Input Page:** Form with PubMed ID input field + submit button
   - **Status Page:** Shows "Processing... 25%", loading spinner, cancel button
   - **Results Page:** Video player, paper metadata, download button
   - **History Page:** List of previous videos

3. **Components** (reusable)
   - `VideoPlayer.jsx` - Uses HTML5 video tag
   - `PaperMetadata.jsx` - Shows title, authors, abstract
   - `StatusProgress.jsx` - Shows progress bar + percentage
   - `InputForm.jsx` - PubMed ID form with validation
   - `ErrorAlert.jsx` - Shows error messages

4. **Styling**
   - Tailwind CSS for all components
   - Responsive design (mobile + desktop)
   - Color scheme: Modern, clean UI

### Success Criteria
- ✅ React app runs on port 3000
- ✅ All pages accessible via routing
- ✅ Components render correctly
- ✅ Form validation works (PubMed ID format check)
- ✅ Responsive on mobile & desktop
- ✅ No backend calls yet (just mock data)

### Technology
- Framework: React with Vite
- CSS: Tailwind CSS
- Routing: React Router
- HTTP: Axios (prepared but not used yet)

### Note
This task can work **independently** because:
- Uses mock data (hardcoded or localStorage)
- Doesn't call backend yet
- UI is purely presentational

---

## 📦 Task 4: Frontend - API Integration Layer
**Owner:** [Assign 1 person]  
**Duration:** 1 week (after Task 1 & 3 exist)  
**Deliverable:** Frontend connected to backend API

### What to Build
1. **API Client**
   - `src/api/client.js` - Axios instance configured
   - Functions:
     - `generateVideo(pubmedId)` → POST /api/videos/generate
     - `getJobStatus(jobId)` → GET /api/videos/:jobId
     - `downloadVideo(jobId)` → GET /api/videos/:jobId/download

2. **State Management**
   - Track current job ID in state
   - Track generation status (pending/processing/completed/error)
   - Handle loading states

3. **Polling Logic**
   - After user submits: poll `getJobStatus()` every 2-3 seconds
   - Update progress display
   - Stop polling when job completes or errors

4. **Error Handling**
   - Display error messages to user
   - Retry logic for failed API calls
   - Network error handling

### Success Criteria
- ✅ Frontend can submit PubMed ID to backend
- ✅ Status updates show in real-time
- ✅ Video displays when ready
- ✅ Error messages appear on failures
- ✅ Polling stops when complete

### Technology
- HTTP Client: Axios
- State Management: React Hooks (useState, useEffect)

### Dependencies
- Requires Task 1 (backend API) to be ready
- Requires Task 3 (UI components) to be ready

---

## 📦 Task 5: DevOps - Environment Setup & Deployment
**Owner:** [Assign 1 person]  
**Duration:** 1-2 weeks  
**Deliverable:** Staging environment with database, Redis, and deployment pipeline

### What to Build
1. **Local Development Environment**
   - Docker Compose file for local setup
   - Includes: FastAPI, PostgreSQL, Redis, React in one command
   - README for developers: "docker-compose up"

2. **Production Database**
   - Create managed PostgreSQL on Render/Railway
   - Run migrations
   - Set up backups

3. **Redis Deployment**
   - Deploy Redis to Render/Railway or similar
   - Configure for Celery workers

4. **GitHub Actions CI/CD**
   - Workflow: On push to main → run tests → deploy to staging
   - Configure environment variables (API keys, database URL)
   - Deploy backend to Render
   - Deploy frontend to Vercel

5. **API Key Management**
   - Set up GitHub Secrets for:
     - GEMINI_API_KEY
     - RUNWAYML_API_KEY
     - DATABASE_URL
     - REDIS_URL

### Success Criteria
- ✅ Docker Compose works: developers can start entire stack locally
- ✅ Production database created and accessible
- ✅ GitHub Actions workflow runs on every push
- ✅ Commits to main auto-deploy to staging
- ✅ Environment variables properly configured

### Technology
- Containerization: Docker & Docker Compose
- Deployment: Render (backend), Vercel (frontend)
- CI/CD: GitHub Actions
- Infrastructure: Managed PostgreSQL, Redis

### Note
This task can work **independently** because:
- Infrastructure doesn't depend on app code
- Can be set up before app is finished
- All other tasks benefit from this work

---

## 📦 Task 6: Testing, Documentation & Integration
**Owner:** [Assign 1 person]  
**Duration:** 1 week (throughout sprint)  
**Deliverable:** Test coverage, API docs, and integration between all tasks

### What to Build
1. **Backend Tests**
   - Unit tests for API endpoints
   - Database model tests
   - Celery task tests (with mocks)
   - Target: 80%+ code coverage
   - Framework: pytest

2. **Frontend Tests**
   - Component tests (render correctly)
   - API client tests (mock HTTP)
   - Form validation tests
   - Framework: Jest + React Testing Library

3. **Integration Tests**
   - End-to-end test: Submit form → check video generation
   - Use mock video generation (no real API keys)
   - Test with all 5 other tasks running together

4. **Documentation**
   - API documentation (FastAPI auto-generates Swagger)
   - Setup guide for developers: "How to run locally"
   - Deployment guide: "How to deploy to staging"
   - README with architecture overview

5. **Integration Work**
   - Help coordinate when all tasks come together
   - Fix any conflicts/mismatches in API contracts
   - End-to-end testing with real backend + frontend

### Success Criteria
- ✅ Tests pass for backend & frontend
- ✅ API documentation complete (accessible at /docs)
- ✅ README has clear setup instructions
- ✅ End-to-end test passes (input → video output)
- ✅ All 5 other tasks integrate without issues

### Technology
- Backend Testing: pytest
- Frontend Testing: Jest + React Testing Library
- API Docs: FastAPI Swagger/OpenAPI
- Integration: Manual testing + automated E2E tests

---

## 🔗 How These Tasks Integrate

```
Task 1 (API Server) ──┐
                      ├──→ Task 4 (Frontend Integration) ──→ Users
Task 2 (Job Queue) ───┤
                      └───→ Task 6 (Testing & Integration)
Task 3 (Frontend UI) ─────→ Task 4 (Frontend Integration) ──→ Users
Task 5 (DevOps) ──────────→ Task 6 (Testing & Integration) ──→ Deployment
```

## 🎯 Integration Timeline

**Week 1 (Nov 11-17):**
- Tasks 1, 2, 3, 5: Work independently
- Each person completes their task at their own pace
- Use mock data/APIs where needed

**Week 2 (Nov 18-24):**
- Task 4: Connect frontend to backend (both exist now)
- Task 6: Write tests, run integration tests
- Debug any mismatches between tasks
- Deploy to staging

**Final (Nov 25-Dec 11):**
- Polish, optimize, fix bugs
- Add real API key integration
- Production deployment

---

## 📊 Task Assignments (Suggestion)

| Task | Description | Suggested Person | Complexity |
|------|-------------|------------------|-----------|
| 1 | Backend API & Database | [Senior Backend] | Medium |
| 2 | Job Queue & Pipeline | [Backend] | High |
| 3 | Frontend UI Components | [Frontend] | Medium |
| 4 | Frontend-Backend Integration | [Frontend] | Medium |
| 5 | DevOps & Deployment | [DevOps/Full-stack] | High |
| 6 | Testing & Integration | [QA/Full-stack] | High |

---

## ✅ Acceptance Criteria (Per Task)

Each task should have a **demo video/screenshot** showing:
- What was built
- How to run it locally
- Any blockers or dependencies

By end of Week 1, each task should be:
- ✅ 80%+ complete
- ✅ Ready to integrate
- ✅ Documented

---

## 🚨 Potential Integration Issues (Expect & Plan For)

1. **API Contract Mismatch**
   - Task 1 (API design) ≠ Task 4 (what frontend expects)
   - **Fix:** Have Task 1 & 4 sync on API spec early

2. **Database Model Mismatch**
   - Task 1 creates different schema than Task 2 expects
   - **Fix:** Collaborate on database design before coding

3. **Environment Variable Issues**
   - Task 5 sets up wrong URLs, keys don't work
   - **Fix:** Coordinate environment setup early

4. **Performance**
   - Job queue takes too long, frontend timeout
   - **Fix:** Use mock videos during development

5. **Deployment Conflicts**
   - Backend & frontend versions don't match
   - **Fix:** Use versioning & environment variables

---

## 🎯 Success Definition

By end of Sprint 2:
- ✅ All 6 tasks complete and integrated
- ✅ User can input PubMed ID in web form
- ✅ Video generates (with mock videos for testing)
- ✅ Results display in browser
- ✅ Deployed to staging environment
- ✅ Tests passing (80%+ coverage)
- ✅ Documentation complete

---

**Created:** November 10, 2025  
**Sprint:** Sprint 2 (Nov 11-24)  
**Team Size:** 6 people  
**Parallelization:** High (all tasks can start simultaneously)
