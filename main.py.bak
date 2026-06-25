#All Aboard

import typer
import subprocess

# List of dependancies not including WIP::::
#bluetoothctl
#brightnessctl
#playerctl

# Global Apps

app = typer.Typer(no_args_is_help=True, add_completion=False)

bluetooth = typer.Typer(no_args_is_help=True)
app.add_typer(bluetooth, name="bluetooth")

brightness = typer.Typer(no_args_is_help=True)
app.add_typer(brightness, name="brightness")

player = typer.Typer(no_args_is_help=True)
app.add_typer(player, name="player")

# BT APPS
power = typer.Typer(no_args_is_help=True)
bluetooth.add_typer(power, name="power")

list = typer.Typer(no_args_is_help=True)
bluetooth.add_typer(list, name="list")
#
#
#
#MAKE VOLUME MODUEL IN FUTURE
# Brightness

@brightness.command()
def set(num1: str):
    num2 = num1 + "%"
    subprocess.run(["brightnessctl", "s", num2])
    #NTS: must be set as string or brightnessctl doesnt parse it.
        #nts: percent fixed but pelase add more control to brightnessctl in future.

# Player

@player.command()
def play_pause():
    subprocess.run(["playerctl", "play-pause"])

@player.command()
def pause():
    subprocess.run(["playerctl", "pause"])

@player.command()
def play():
    subprocess.run(["playerctl", "play"])

@player.command()
def stop():
    subprocess.run(["playerctl", "stop"])

@player.command()
def next():
    subprocess.run(["playerctl", "next"])

@player.command()
def previous():
    subprocess.run(["playerctl", "previous"])
# Power

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
# To update WIPPPP. MAC Adress neded to cnnect to device. make a splice and output subprocess run.
@bluetooth.command()
def connect(device: str):
   subprocess.run(["bluetoothctl", "connect", device])

if __name__ == "__main__":
    app()
