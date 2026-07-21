# Models
from PIL import Image
import atexit
import numpy as np
from insightface.app import FaceAnalysis
from insightface import model_zoo
import os
from pyfiglet import Figlet
from rich.console import Console
from rich.progress import Progress
import time
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
# 1. Start InsightFace
# -----------------------------------
app =FaceAnalysis(name="buffalo_l")
# Module Power is max at 1024,1024 and create deep fake photo We do not suggest to use the max mode
app.prepare(ctx_id=-1, det_size=(640, 640))  # CPU

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

Image.fromarray(result).save("result.jpg")

print("✅ Face swap completed!",style='bright_green')
print("Saved as result.jpg",style='bright_green')
