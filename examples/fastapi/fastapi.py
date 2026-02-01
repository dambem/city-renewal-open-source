from threading import Thread
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from consumer import KafkaConsumerBuilder
import asyncio 
import socketio 
from contextlib import asynccontextmanager

MAIN_LOOP = None

# Initialize FastAPI and SocketIO

def kafka_reader():
    consumer = KafkaConsumerBuilder()
    consumer.build()
    while True:
        try:
            messages = consumer.poll_values()
            if MAIN_LOOP:
                asyncio.run_coroutine_threadsafe(
                    sio.emit("tag_scanned", {"val": messages}),
                    MAIN_LOOP
                )
        except Exception as e:
            print(f"Communication Error: {e}")
            break

@app.get("/health")
async def ping():
    return {"ping": "hello-world"}

@asynccontextmanager
async def lifespan(app: FastAPI):
    global MAIN_LOOP
    MAIN_LOOP = asyncio.get_event_loop()
    serial_thread = Thread(target=kafka_reader, daemon=True)
    serial_thread.start()

    yield
    print('Shutting down...')
    
app = FastAPI(lifespan=lifespan)
sio = socketio.AsyncServer(
    async_mode="asgi",
    cors_allowed_origins="*",
    logger=True,
    engineio_logger=True
)
asgi_app = socketio.ASGIApp(sio, app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Your Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
