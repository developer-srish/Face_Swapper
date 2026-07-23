# Models
from PIL import Image
from PIL import Image, ImageDraw, ImageFont
import atexit
import numpy as np
from rich.table import Table
from insightface.app import FaceAnalysis
from insightface import model_zoo
import os
from dotenv import load_dotenv
from pyfiglet import Figlet
from rich.console import Console
from rich.progress import Progress
import time
from PIL import Image
console = Console()
def print(text, style="white", delay=0.05):
    for char in text:
        console.print(char, style=style, end="")
        time.sleep(delay)
    console.print()
waterma = os.path.join(
    os.path.dirname(__file__),
    ".watermark",
    "watermark.png")

def verify_watermark():
    try:
        img = Image.open(waterma)

        expected = {
            "Author": "Srish Ghosh",
            "Software": "Face Swapper",
            "Version": "1.1.0",
            "Watermark": "Official"
        }

        for key, value in expected.items():
            if img.info.get(key) != value:
                print(f"[ERROR] Invalid watermark metadata: {key}",style='bright_red')
                return False

        return True

    except Exception as e:
        print(f"[ERROR] Cannot verify watermark: {e}",style='bright_red')
        return False
if not verify_watermark():
    raise RuntimeError("Invalid watermark image!")
start_time = time.perf_counter()

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


load_dotenv()
pas=os.getenv("REMOVE_WATERMARK_PASSWORD")
if pas is None:
    print(
        ".env password missing",
        style="bright_red"
    )
model_path = os.path.join(
    os.path.dirname(__file__),
    "models",
    "inswapper_128.onnx")
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
elif mo == '/admin':
    if not os.path.exists(model_path):
        print('Download it from : https://huggingface.co/LPDoctor/insightface/blob/main/inswapper_128.onnx')
        raise FileNotFoundError(
        "models/inswapper_128.onnx not found."
    )
    print(model_path,style='bright_red')
    print('Version v.1.10',style='bright_magenta')
    print(f'Pass: {pas}',style='bright_green')
    
    
    
    
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
if not os.path.exists(model_path):
    print('Download it from : https://huggingface.co/LPDoctor/insightface/blob/main/inswapper_128.onnx')
    raise FileNotFoundError(
        "models/inswapper_128.onnx not found."
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
if not source_faces:
    raise Exception('No face in source face')
if not target_faces:
    raise Exception('No face in target face')



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
    waterma = os.path.join(
    os.path.dirname(__file__),
    ".watermark",
    "watermark.png")

    img = Image.fromarray(result).convert("RGBA")
    logo = Image.open(waterma).convert("RGBA")

    # ============================
    # Small corner logo
    # ============================
    corner = logo.copy()

    corner_width = int(img.width * 0.40)
    ratio = corner_width / corner.width

    corner = corner.resize(
        (corner_width, int(corner.height * ratio)),
        Image.LANCZOS
    )

    alpha = corner.getchannel("A")
    alpha = alpha.point(lambda p: int(p * 0.90))
    corner.putalpha(alpha)

    margin = 25

    img.paste(
        corner,
        (
            img.width - corner.width - margin,
            img.height - corner.height - margin
        ),
        corner
    )

    # ============================
    # Repeated diagonal logos
    # ============================
    tile = logo.copy()

    tile_width = int(img.width * 0.12)
    ratio = tile_width / tile.width

    tile = tile.resize(
        (tile_width, int(tile.height * ratio)),
        Image.LANCZOS
    )

    tile = tile.rotate(30, expand=True)

    alpha = tile.getchannel("A")
    alpha = alpha.point(lambda p: int(p * 0.30))
    tile.putalpha(alpha)

    spacing = 260

    for y in range(-tile.height, img.height + tile.height, spacing):
        for x in range(-tile.width, img.width + tile.width, spacing):
            img.paste(tile, (x, y), tile)

    # Save image
    img.convert("RGB").save(
    "result.jpg",
    quality=100,
    subsampling=0,
    optimize=True
)
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
end_time = time.perf_counter()

execution_time = end_time - start_time
def show_summary(
        model_name,
        model_mode,
        source_face,
        target_face,
        watermark_enabled,
        output_file,
        execution_time
    ):
        table = Table(
            title="Face Swapper Summary",
            show_header=True,
            header_style="bold cyan",
            border_style="bright_blue"
        )

        table.add_column("Property", style="bright_white", width=22)
        table.add_column("Value", style="bright_green")

        table.add_row("Model", model_name)
        table.add_row("Mode", model_mode)
        table.add_row(
            "Source Gender",
            "Male" if source_face.gender == 1 else "Female"
        )
        table.add_row(
            "Source Age",
            str(source_face.age)
        )
        table.add_row(
            "Target Gender",
            "Male" if target_face.gender == 1 else "Female"
        )
        table.add_row(
            "Target Age",
            str(target_face.age)
        )
        table.add_row(
            "Watermark",
            "Enabled" if watermark_enabled else "Disabled"
        )
        table.add_row(
            "Output File",
            output_file
        )
        table.add_row(
            "Execution Time",
            f"{execution_time:.2f} sec"
        )
        table.add_row(
            "Status",
            "[bold bright_green]✓ Success[/]"
        )

        console.print(table)
    


show_summary(
    "buffalo_l",
    mo,
    source_face,
    target_face,
    act != pas,
    "result.jpg",
    execution_time  
)
