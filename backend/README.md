**FocusFlow MVP Backend Architecture Overview**

---

### 🔧 SYSTEMS OVERVIEW (MVP)

FocusFlow MVP backend will consist of **4 modular Django apps**, each with clear responsibility:

| App Name         | Responsibility                             |
|------------------|---------------------------------------------|
| `users`          | Handles user registration, login (JWT), and profile access |
| `focus_sessions` | Tracks focus session start/stop logic, session history     |
| `journals`       | Manages journal reflections tied to sessions or written freely |
| `quotes`         | Serves one motivational quote per day to all users         |

---

### 👤 USERS APP

**Purpose:** Allow users to register, log in securely, and access protected features.

**Core Features:**
- JWT-based auth using SimpleJWT
- Custom `User` model with email login
- Authenticated access to all app features

**API Endpoints:**
- `POST /api/users/register/` → Register
- `POST /api/users/login/` → Login
- `GET /api/users/me/` → Profile

**Rules:**
- Email must be unique
- Password must be >= 8 characters
- JWT required on all protected routes

---

### ⏱️ FOCUS SESSIONS APP

**Purpose:** Log focused work blocks (like Pomodoro sessions)

**Model Fields:**
- `user`: FK to User
- `start_time`: DateTime
- `end_time`: DateTime (nullable)
- `is_active`: Bool
- `created_at`: DateTime

**API Endpoints:**
- `POST /api/sessions/start/` → Start session
- `POST /api/sessions/stop/` → Stop session
- `GET /api/sessions/active/` → Get active session
- `GET /api/sessions/history/` → Session history

**Rules:**
- Only one active session per user at a time
- Frontend handles timer countdown; backend logs timestamps

---

### 📓 JOURNALS APP

**Purpose:** Let users reflect after sessions or freely during the day

**Model Fields:**
- `user`: FK to User
- `content`: TextField
- `session`: FK to FocusSession (nullable)
- `created_at`: DateTime
- `updated_at`: DateTime

**API Endpoints:**
- `POST /api/journals/create/` → Create journal
- `GET /api/journals/` → All journals
- `GET /api/journals/<id>/` → Specific journal
- `PUT /api/journals/<id>/` → Update (if not tied to session)
- `DELETE /api/journals/<id>/` → Delete (if not tied to session)

**Rules:**
- Journals tied to sessions are final (no edits or deletes)
- Only the journal owner can access, edit, or delete entries

---

### 🌟 DAILY QUOTES APP

**Purpose:** Provide a daily motivational quote to all users

**Model Fields:**
- `text`: CharField/TextField
- `author`: CharField (nullable)
- `created_at`: DateTime

**Logic:**
- Each day, one quote is chosen using the date as a random seed
- All users see the same quote for the day

**API Endpoint:**
- `GET /api/quotes/today/` → Returns the daily quote

**Rules:**
- Quote rotates daily, not randomly every refresh
- Quotes preloaded into DB manually or via script
