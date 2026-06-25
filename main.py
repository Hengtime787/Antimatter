#All Aboard

import typer
import subprocess

# List of dependancies not including WIP::::
#bluetoothctl
#brightnessctl - LAPTOP ONLY* * some monitors may support??
#playerctl
#Pipewire/Wireplumber

# Global Apps

app = typer.Typer(no_args_is_help=True, add_completion=False)

theme = typer.Typer(no_args_is_help=True)
app.add_typer(theme, name="theme")

bluetooth = typer.Typer(no_args_is_help=True, help="""
    Control Bluetooth connections
    """)
app.add_typer(bluetooth, name="bluetooth")

brightness = typer.Typer(no_args_is_help=True, help="""
Control panel brightness
""")
app.add_typer(brightness, name="brightness")

audio = typer.Typer(no_args_is_help=True, help="""
Change system audio settings
""")
app.add_typer(audio, name="audio")

player = typer.Typer(no_args_is_help=True, help="""
Manage songs now playing
""")
app.add_typer(player, name="player")

tools = typer.Typer(no_args_is_help=True, help="""
Various productivity utilities
"""
app.add_typer(tools, name="tools")
# BT APPS
power = typer.Typer(no_args_is_help=True)
bluetooth.add_typer(power, name="power")

list = typer.Typer(no_args_is_help=True)
bluetooth.add_typer(list, name="list")
#
#
#
#MAKE VOLUME MODUEL IN FUTURE

@tools.command(no_args_is_help=True)
def calc(num1: float, num2: float, divide: bool = False, add: bool = False, subtract: bool = False, multiply: bool = False):
    """
    Simple calculator
    """
    if add:
        print(num1 + num2)
    elif subtract:
        print(num1 - num2)
    elif divide: 
        print(num1 / num2)
    elif multiply:
        print(num1 * num2)
    else:
        print("Please add flag")


# Brightness

@brightness.command(no_args_is_help=True)
def set(num1: str):
    """
    Set screen brightness in percent
    """
    num2 = num1 + "%"
    subprocess.run(["brightnessctl", "s", num2])
    #NTS: must be set as string or brightnessctl doesnt parse it.
    #nts: percent fixed but pelase add more control to brightnessctl in future.
# Player

@player.command()
def play_pause():

    subprocess.run(["playerctl", "play-pause"])
    subprocess.run(["echo", "Now Playing --"])
    subprocess.run(["playerctl", "metadata", "--format", '{{artist}} — {{title}}'])

@player.command()
def pause():
    subprocess.run(["playerctl", "pause"])

@player.command()
def play():
    subprocess.run(["playerctl", "play"])
    subprocess.run(["echo", "Now Playing --"])
    subprocess.run(["playerctl", "metadata", "--format", '{{artist}} — {{title}}'])

@player.command()
def now_playing():
    subprocess.run(["echo", "Now Playing --"])
    subprocess.run(["playerctl", "metadata", "--format", '{{artist}} — {{title}}'])

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
@bluetooth.command()
def devices():
    subprocess.run(["bluetoothctl", "devices"])

@bluetooth.command()
def controllers():
    subprocess.run(["bluetoothctl", "list"])

#Connect
# To update WIPPPP. MAC Adress neded to cnnect to device. make a splice and output subprocess run.
@bluetooth.command()
def connect(device: str):
   subprocess.run(["bluetoothctl", "connect", device])

# Audio

@audio.command()
def vol_up():
    subprocess.run(["wpctl", "set-volume", "@DEFAULT_AUDIO_SINK@", "5%+"])

@audio.command()
def vol_down():
    subprocess.run(["wpctl", "set-volume", "@DEFAULT_AUDIO_SINK@", "5%-"])

@audio.command()
def mute():
    subprocess.run(["wpctl", "set-mute", "@DEFAULT_AUDIO_SINK@", "toggle"])

@audio.command()
def mic_mute():
    subprocess.run(["wpctl", "set-mute", "@DEFAULT_AUDIO_SOURCE@", "toggle"])

if __name__ == "__main__":
    app()
