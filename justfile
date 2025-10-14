set shell := ["zsh", "-lic"]
set dotenv-load := true

FRONTEND := "app/frontend"
BACKEND  := "app/backend"

dev-fe:
  cd {{FRONTEND}} && pnpm dev

dev-be:
  cd {{BACKEND}} && uv run uvicorn main:app --reload
