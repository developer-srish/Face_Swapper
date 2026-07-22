# Models
from PIL import Image
from PIL import Image, ImageDraw, ImageFont
import atexit
import numpy as np
from insightface.app import FaceAnalysis
from insightface import model_zoo
import os
from dotenv import load_dotenv
from pyfiglet import Figlet
from rich.console import Console
from rich.progress import Progress
import time
load_dotenv()
pas=os.getenv("REMOVE_WATERMARK_PASSWORD")
# Mode set
# -----------------------------------
# 1. Start InsightFace
# -----------------------------------
app =FaceAnalysis(name="buffalo_l")
# Module Power is max at 1024,1024 and create deep fake photo We do not suggest to use the max mode
  # CPU

mo=input('Model power max at /full and medium at /med chose one to proced :  ')
if mo =='/full':
    app.prepare(ctx_id=0, det_size=(1024,1024))
    
elif mo == '/med':
    app.prepare(ctx_id=0, det_size=(640,640))

console = Console()
fig = Figlet(font="starwars")
banner = fig.renderText("Face Swapper")

colors = [
    "red",
    "yellow",
    "green",
    "cyan",
    "blue",
    "magenta",
    "bright_red",
    "bright_green",
    "bright_blue",
]

for i, line in enumerate(banner.splitlines()):
    console.print(f"[bold {colors[i % len(colors)]}]{line}[/]")
with Progress() as progress:
    task = progress.add_task("[cyan]Loading...", total=100)

    while not progress.finished:
        time.sleep(0.05)
        progress.update(task, advance=1)
def print(text, style="white", delay=0.05):
    for char in text:
        console.print(char, style=style, end="")
        time.sleep(delay)
    console.print()
@atexit.register
def exit_handler():
    print("Thanks For using this programme made by Srish Ghosh",style='bright_green')
# -----------------------------------
# Find the model
# -----------------------------------
model_path = os.path.join(
    os.path.dirname(__file__),
    "models",
    "inswapper_128.onnx"
)

# -----------------------------------
# 2. Load the face swap model
# -----------------------------------
swapper = model_zoo.get_model(
    model_path,
    download=False,
    download_zip=False
)

# -----------------------------------
# 3. Open images
# -----------------------------------
source = Image.open("source.jpg").convert("RGB")
target = Image.open("target.jpg").convert("RGB")

# Convert Pillow images to NumPy arrays
source = np.array(source)
target = np.array(target)

# Convert RGB → BGR (InsightFace uses BGR)
source = source[:, :, ::-1]
target = target[:, :, ::-1]

# -----------------------------------
# 4. Detect faces
# -----------------------------------
source_faces = app.get(source)
target_faces = app.get(target)



# Use the first detected face
source_face = source_faces[0]
target_face = target_faces[0]

# -----------------------------------
# 5. Swap faces
# -----------------------------------
result = swapper.get(
    target,
    target_face,
    source_face,
    paste_back=True
)

# -----------------------------------
# 6. Save result
# -----------------------------------
# Convert BGR → RGB for Pillow
result = result[:, :, ::-1]
# Convert NumPy array to Pillow image
act=input('Enter your code to remove watermark if you have else press enter')
if act ==pas:
    Image.fromarray(result).save('result.jpg')
    s_g='Male'if source_faces[0].gender ==1 else 'Female'
    t_g='Male'if target_faces[0].gender ==1 else 'Female'
    s_a=source_face.age
    t_a=target_face.age
    print(f'Source face gender: {s_g}',style='bright_red')
    print(f'Source face estimated age: {s_a}',style='bright_red')
    print(f'Target face gender: {t_g}',style='bright_magenta')
    print(f'Target face estimated age: {t_a}',style='bright_magenta')
    print("✅ Face swap completed!",style='bright_green')

    print("Saved as result.jpg",style='bright_green')
else:

    img = Image.fromarray(result).convert("RGBA")

    # Create transparent overlay
    overlay = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)

    # Load font
    try:
        font = ImageFont.truetype("arial.ttf", 30)
    except:
        font = ImageFont.load_default()

    watermark = "Deepfake"

    # Get text size
    bbox = draw.textbbox((0, 0), watermark, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Bottom-right position
    x = img.width - text_width - 20
    y = img.height - text_height - 20

    # Draw transparent watermark
    draw.text(
        (x, y),
        watermark,
        fill=(255, 255, 255, 80),   # Alpha = 80 (transparent)
        font=font
    )

    # Merge overlay with image
    img = Image.alpha_composite(img, overlay)

    # Save as JPG
    img.convert("RGB").save("result.jpg")
    s_g='Male'if source_faces[0].gender ==1 else 'Female'
    t_g='Male'if target_faces[0].gender ==1 else 'Female'
    s_a=source_face.age
    t_a=target_face.age
    print(f'Source face gender: {s_g}',style='bright_red')
    print(f'Source face estimated age: {s_a}',style='bright_red')
    print(f'Target face gender: {t_g}',style='bright_magenta')
    print(f'Target face estimated age: {t_a}',style='bright_magenta')
    print("✅ Face swap completed!",style='bright_green')

    print("Saved as result.jpg",style='bright_green')
