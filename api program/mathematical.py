from fastapi import FastAPI
def root(num1,num2):
    return(f"subtraction is:{int(num1) - int(num2)}")

app = FastAPI()
@app.get("/")
async def sum(num1,num2):
    a=root(num1,num2)
    print(a)
    return (f"{a}\n sum is:{int(num1) + int(num2)}")

#@app.get("/")

