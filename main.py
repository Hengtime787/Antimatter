#All Aboard

import typer
import subprocess

# Global Apps

app = typer.Typer(no_args_is_help=True, add_completion=False)

bluetooth = typer.Typer(no_args_is_help=True)
app.add_typer(bluetooth, name="bluetooth")

#BT APPS
power = typer.Typer(no_args_is_help=True)
bluetooth.add_typer(power, name="power")

list = typer.Typer(no_args_is_help=True)
bluetooth.add_typer(list, name="list")

#connect = typer.Typer(typer.Option(help="Hello"))
#bluetooth.add_typer(connect, name="connect")

#Power

@power.command()
def on():
    subprocess.run(["bluetoothctl", "power", "on"])

@power.command()
def off():
    subprocess.run(["bluetoothctl", "power", "off"])
#List
@list.command()
def devices():
    subprocess.run(["bluetoothctl", "devices"])

@list.command()
def controller():
    subprocess.run(["bluetoothctl", "list"])

#Connect

@bluetooth.command()
def connect(device: str):
    subprocess.run(["bluetoothctl", "connect", device])

if __name__ == "__main__":
    app()
