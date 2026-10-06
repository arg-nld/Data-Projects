# Tidal ATS

Tidal ATS is a React/Vite recruiting dashboard with an Express API for jobs, applications, candidate pipeline management, interview scheduling, notifications, and Gemini-powered resume parsing/screening.

## Run locally

1. Install dependencies:

```bash
npm install
```

2. Create a `.env` file in the project root (the same folder as `package.json`) from `.env.example` and set a valid Google Gemini API key:

```env
GEMINI_API_KEY=your_google_ai_studio_api_key
GEMINI_MODEL=gemini-3.8-flash
PORT=5000
```

3. Start both the API and frontend:

```bash
npm run dev
```

The Vite frontend uses the Express API through `/api`. Gemini calls stay server-side; never put the Gemini key in `src/`.

## Important for Gemini

The resume parser accepts TXT directly, extracts DOCX text with Mammoth before sending it to Gemini, and sends PDF/image files as multipart uploads to the backend. A valid `GEMINI_API_KEY` is required for AI parsing and candidate screening.

## HR pipeline features

The HR portal includes a persistent Candidate Pipeline tab, drag-and-drop stage changes with confirmation, horizontal auto-pan while dragging near the board edges, and a Recruiting Calendar showing scheduled interviews.

## Demo accounts

The bundled demo data restores the seed passwords when older `db.json` files are missing them.

- HR: `hr@tidalats.com` / `password123`
- Applicant: `jordan.hayes@example.com` / `password123`
