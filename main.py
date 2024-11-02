from PIL import ImageGrab # for making screenshots
from wand.image import Image # for image converting
from pynput.mouse import Controller # mouse control
from datetime import datetime # current date for screenshot name
from rich import print # for pretty printing text
import os # for creating folders
import time # for sleeping

mouse = Controller()

global start_mouse_position

def convert_png_to_avif(input_png_path, output_avif_path):
    # Open the PNG image
  with Image(filename=input_png_path) as original:
    with original.convert("avif") as converted:
      converted.save(filename=output_avif_path)
  os.remove(input_png_path)

def make_screenshot(folder_num):
  cur_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
  screenshot = ImageGrab.grab()
  screenshot = screenshot.resize((1280, 720))
  save_path = f".\\screenshots\\{folder_num}\\screenshot-{cur_time}.png"
  screenshot.save(save_path)
  # convert_png_to_avif(f".\\screenshots\\{folder_num}\\screenshot-{cur_time}.png", f".\\screenshots\\{folder_num}\\screenshot-{cur_time}.avif")

def typewriter_effect(text, col: str, delay=0.1):
  for char in text:
    print(f"{col}{char}", end='', flush=True)  # Print without newline and flush output
    time.sleep(delay)  # Wait for the specified delay
  print()  # Move to the next line after finishing

def main():
  try:
    os.system("cls")
    ascii_art = r"""
 _______  _______ _________ _______  _______ _________ _______  _______ 
(  ____ )(  ___  )\__   __/(  ____ \(  ____ \\__   __/(  ___  )(  ____ )
| (    )|| (   ) |   ) (   | (    \/| (    \/   ) (   | (   ) || (    )|
| (____)|| (___) |   | |   | (__    | |         | |   | |   | || (____)|
|     __)|  ___  |   | |   |  __)   | |         | |   | |   | ||     __)
| (\ (   | (   ) |   | |   | (      | |         | |   | |   | || (\ (   
| ) \ \__| )   ( |   | |   | (____/\| (____/\   | |   | (___) || ) \ \__
|/   \__/|/     \|   )_(   (_______/(_______/   )_(   (_______)|/   \__/                                                             
    """ 
    print(ascii_art)

    cur_folder_num = 0

    while True:
      cur_folder_num += 1
      if os.path.exists(f".\\screenshots\\{cur_folder_num}"):
        continue
      else:
        try:
          os.mkdir(f".\\screenshots")
        except:
          pass
        os.mkdir(f".\\screenshots\\{cur_folder_num}")
        break

    print("[blue]Security will be activated in 5 seconds ", end="")
    
    typewriter_effect("1..2..3..4..5", "[bold yellow]", delay=0.38)

    typewriter_effect("Security will be activated", "[bold green]", delay=0.03)
    time.sleep(0.1)

    start_mouse_position = mouse.position
    print(f"Mouse position: {start_mouse_position} ", end="")

    while True:
      try:
        if mouse.position != start_mouse_position:
          print("[bold red]Mouse is moved!")
          make_screenshot(cur_folder_num)
          time.sleep(3)
          start_mouse_position = mouse.position
          print(f"[bold]New[/bold] mouse position: {start_mouse_position} ", end="")
        time.sleep(0.2)
      except KeyboardInterrupt:
        print("[bold red]Stopping", end="")
        typewriter_effect("...", "[bold red]", delay=0.1)
        quit()
  except KeyboardInterrupt:
    print("[bold red]Stopping", end="")
    typewriter_effect("...", "[bold red]", delay=0.1)
    quit()
if __name__ == '__main__':
  main()