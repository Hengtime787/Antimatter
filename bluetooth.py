#All Aboard

import typer
import subprocess

# Global Apps

app = typer.Typer()

btctl = typer.Typer()
app.add_typer(btctl, name="bluetooth")

#BT APPS
power = typer.Typer()
btctl.add_typer(power, name="power")

#Power

@power.command()
def on():
    subprocess.run(["bluetoothctl", "power", "on"])

@power.command()
def off():
    subprocess.run(["bluetoothctl", "power", "off"])

if __name__ == "__main__":
    app()
