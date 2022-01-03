from typing import Optional
import typer
app = typer.Typer()


@app.command()
def name(name: Optional[str] = "hemil"):
    typer.echo(f"Hello {name}")
@app.command()   
def sum(a,b):
    total = int(a) + int(b)
    typer.echo(f"your sum is:{total}")    


@app.command()
def goodbye(name: str, formal: bool = False, simple: bool = False):
    if formal:
        typer.echo(f"Goodbye {name}!!. Have a good day.")
    elif simple:
        typer.echo(f"{name} is a simple boy")
    else:
        typer.echo(f"Bye {name}!")

if __name__ == "__main__":
    app()