# User Manager

FastAPI user service. Auth routes under `/api`, Stripe key from the environment, HTTPS redirect.

## What is in here

- `main.py` — FastAPI app, CORS, SSL
- `app/routers/auth` — register/login
- Stripe via `STRIPE_API_KEY`

## Stack

Python, FastAPI, Stripe
