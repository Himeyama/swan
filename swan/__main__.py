from fastapi import Depends, FastAPI
from pydantic import BaseModel
import uvicorn
from swan.port import check_tcp_connectivity, get_random_port
import pandas_datareader.data as web


port: int = get_random_port()
app: FastAPI = FastAPI()

class StockInfo(BaseModel): 
    code: str
    symbol: str
    start_date: str
    end_date: str

@app.get("/api/version")
async def version():
    return "swan"

@app.get("/api/finance")
async def finance(stock: StockInfo = Depends()):        
    #データ取得
    df = web.DataReader(stock.code + stock.symbol, data_source='stooq', start=stock.start_date, end=stock.end_date)
    return df.to_dict()

def main():
    port = 50025
    if check_tcp_connectivity("127.0.0.1", port):
        port = get_random_port()
    try:
        uvicorn.run(app, host="127.0.0.1", port=port)
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()
