import os
from fastapi import FastAPI
from app.routers import auth
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import stripe
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from ssl import SSLContext
import ssl

app = FastAPI()
app.add_middleware(
    HTTPSRedirectMiddleware
)

ssl_context = SSLContext(protocol=ssl.PROTOCOL_TLS_CLIENT)
ssl_context.load_cert_chain("cert.pem", "key.pem")

stripe.api_key = os.environ.get("STRIPE_API_KEY", "")

app.include_router(auth.router, prefix="/api")

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=80,
        reload=True,
        workers=1,
        ssl_keyfile="key.pem",
        ssl_certfile="cert.pem"        
    )
