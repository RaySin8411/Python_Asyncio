| 層次 | 概念 | 實作 |
| -------- | -------- | -------- |
| L1(base) | **協程** | async def、async with、async for、await |
| L2       | **事件迴圈** | asyncio.run() BaseEventLoop|
| L3       | Future | asyncio.Future|
| L4       | Task | asyncio.Task、asyncio.create_Task()|
| L5       | **子行程與執行緒**|run_in_executor()、asyncio.subprocess|
| L6       | **工具** | asyncio.Queue |
| L7       | 網路:傳輸 | BaseTransport |
| L8       | 網路:TCP與UDP | Protocol |
| L9       | **網路:串流** | StreamReader、StreamWriter、asyncio.open_connection()、asyncio.start_server()|