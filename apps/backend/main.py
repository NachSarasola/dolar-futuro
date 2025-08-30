from fastapi import FastAPI, Query
from packages.shared import Quote, Signal, Sizing, OrderTicket
from .feeds import DemoFeed

app = FastAPI(title="Dolar Futuro API")
feed = DemoFeed()


@app.get("/health")
def health() -> dict:
  return {"status": "ok"}


@app.get("/config")
def config() -> dict:
  return {"mode": "demo"}


@app.get("/quotes", response_model=list[Quote])
def get_quotes(symbols: list[str] = Query(...)):
  return [feed.get_quote(s) for s in symbols]


@app.get("/signals", response_model=list[Signal])
def get_signals():
  return []


@app.get("/sizing", response_model=list[Sizing])
def get_sizing():
  return []


@app.post("/orders/dryrun")
def orders_dryrun(order: OrderTicket) -> dict:
  return {"received": order}


@app.post("/backtest/run")
def backtest_run() -> dict:
  return {"status": "not_implemented"}
