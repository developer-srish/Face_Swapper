# 🎭 Realistic Face Swap with InsightFace

<p align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=32&pause=1000&color=FF4D6D&center=true&vCenter=true&width=900&lines=Realistic+Face+Swap;Powered+by+InsightFace;ONNX+Runtime+%2B+Pillow+%2B+NumPy;Made+by+Srish+Ghosh">
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python)
![InsightFace](https://img.shields.io/badge/InsightFace-Face%20Recognition-success?style=for-the-badge)
![ONNX Runtime](https://img.shields.io/badge/ONNX-Runtime-orange?style=for-the-badge)
![Pillow](https://img.shields.io/badge/Pillow-Image%20Processing-blueviolet?style=for-the-badge)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-yellow?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</p>

<p align="center">
<img src="https://media.giphy.com/media/LmNwrBhejkK9EFP504/giphy.gif" width="650">
</p>

---

# 📖 About

Realistic Face Swap is a beginner-friendly Python project that performs **high-quality AI face swapping** using **InsightFace** and **ONNX Runtime**.

The application automatically detects faces in both the source and target images, swaps the selected face, and generates a realistic output image with only a few lines of Python code.

This project is ideal for learning:

- Artificial Intelligence
- Computer Vision
- Face Detection
- Face Recognition
- Deep Learning Models
- Image Processing
- ONNX Runtime
- InsightFace

---

# ✨ Features

✅ High Quality Face Swapping

✅ Automatic Face Detection

✅ AI Face Recognition

✅ Fast CPU Inference

✅ Pillow Image Support

✅ NumPy Processing

✅ ONNX Runtime

✅ Multiple Face Detection Support

✅ Beginner Friendly

✅ Easy to Understand Code

---

# 📂 Project Structure

```text
Face_Swapper/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── models/
│   └── .gitkeep
│
├── testing_pics/
│   ├── source.jpg
│   ├── target.jpg
│   └── .gitkeep
│
└── .gitkeep
```

---

# 📋 Requirements

- Python 3.12+
- pip
- Git
- Windows or Linux

---

# 📥 Install Git

## Windows

Download Git

https://git-scm.com/download/win

Verify installation

```bash
git --version
```

---

## Ubuntu / Debian

```bash
sudo apt update
sudo apt install git
```

---

## Fedora

```bash
sudo dnf install git
```

---

## Arch Linux

```bash
sudo pacman -S git
```

---

## macOS

```bash
brew install git
```

or

```bash
xcode-select --install
```

---

# 📥 Clone Repository

```bash
git clone https://github.com/developer-srish/Realistic-Face-Swap.git
```

```bash
cd Face_Swapper
```

---

# 📦 Install Dependencies

Using requirements.txt

```bash
pip install -r requirements.txt
```

or install manually

```bash
pip install insightface pillow numpy
```

---

# 🤖 Download the Face Swap Model

This project requires the **inswapper_128.onnx** model.

Download it here:

**https://huggingface.co/LPDoctor/insightface/blob/main/inswapper_128.onnx**

After downloading, place the model inside the **models** folder.

```text
Face_Swapper/
│
└── models/
    └── inswapper_128.onnx
```

> ⚠️ **Important**
>
> Download the actual **`.onnx`** file, **not** the webpage.
>
> On Hugging Face, click **Download** (or **Raw**) to save the model.

---

# 📂 Final Folder Structure

```text
Face_Swapper/
│
├── main.py
├── README.md
├── requirements.txt
│
├── testing_pics/
│   ├── source.jpg
│   └── target.jpg
│
└── models/
    └── inswapper_128.onnx
```

---
# ▶️ Running the Project

Run the application:

```bash
python main.py
```

If everything is set up correctly, the program will:

- Load the InsightFace models
- Detect faces
- Swap the face
- Save the final image

You should see:

```text
✅ Face swap completed!
Saved as result.jpg
```

---

# 🖼️ Input Images

Place your images inside the project folder.

## Source Image

The face that will be copied.

```
source.jpg
```

Example:

```
👦 Source Person
```

---

## Target Image

The face that will be replaced.

```
target.jpg
```

Example:

```
👨 Target Person
```

---

# 🖼️ Output

After running the project, a new image will automatically be created.

```
result.jpg
```

Example:

```
🎉 Face Swapped Image
```

---

# ⚙️ How It Works

1. Loads the InsightFace face detector.
2. Loads the **inswapper_128.onnx** model.
3. Detects faces in **source.jpg**.
4. Detects faces in **target.jpg**.
5. Swaps the source face onto the target.
6. Saves the final image as **result.jpg**.

---

# 🛠️ Technologies Used

- 🐍 Python
- 🤖 InsightFace
- ⚡ ONNX Runtime
- 🖼️ Pillow
- 🔢 NumPy
- 🧠 Artificial Intelligence
- 👁️ Computer Vision

---

# 📚 What You'll Learn

- Python Programming
- Computer Vision
- Face Detection
- Face Recognition
- AI Face Swapping
- ONNX Runtime
- NumPy Image Processing
- Pillow Image Handling
- InsightFace Model Usage

---

# ⚠️ Troubleshooting

## ModuleNotFoundError

Install the missing package.

Example:

```bash
pip install numpy
```

or

```bash
pip install pillow
```

---

## Model Not Found

Make sure your folder looks like this:

```text
models/
└── inswapper_128.onnx
```

---

## Failed Download URL

Some versions of InsightFace cannot automatically download the model.

Simply download it manually from:

**https://huggingface.co/LPDoctor/insightface/blob/main/inswapper_128.onnx**

and place it inside:

```text
models/
```

---

## No Face Found

Use images where:

- Face is clearly visible
- Face is not blurry
- Face is facing the camera
- Good lighting is available

---

## CUDAExecutionProvider Warning

If you see:

```text
Specified provider 'CUDAExecutionProvider' is not available
```

Don't worry.

This only means the project is running on your CPU instead of an NVIDIA GPU.

The project will still work correctly.

---

# 📦 requirements.txt

Create a file named:

```
requirements.txt
```

Add:

```text
insightface
numpy
pillow
```

Install all packages using:

```bash
pip install -r requirements.txt
```

---
# ⭐ Show Your Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps support the project and motivates me to create more open-source AI and Python projects.

---

# 🤝 Contributing

Contributions are always welcome!

If you have ideas for improvements or find a bug:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📜 License

This project is licensed under the **MIT License**.

You are free to:

- ✅ Use
- ✅ Modify
- ✅ Share
- ✅ Learn from the code

Please respect the licenses of InsightFace and the ONNX model used in this project.

---

# 🙏 Acknowledgements

Special thanks to the developers of these amazing open-source projects:

- InsightFace
- ONNX Runtime
- Pillow (PIL)
- NumPy
- Python

Without these libraries, this project would not have been possible.

---

# 👨‍💻 Author

<p align="center">

## **Srish Ghosh**

Python Developer • Open Source Enthusiast • Student

GitHub

**https://github.com/developer-srish**

</p>

---

# 🌟 Future Improvements

Planned features include:

- 🎥 Video Face Swapping
- 🎭 Multiple Face Selection
- 🖥️ Graphical User Interface (GUI)
- ⚡ GPU Acceleration (CUDA)
- 📁 Batch Image Processing
- 🧠 Face Enhancement (GFPGAN)
- 📷 Webcam Face Swapping
- 🖼️ Drag-and-Drop Image Support

---

# 💖 Support the Project

If this project helped you:

⭐ Star the repository

🍴 Fork the repository

🐛 Report bugs

💡 Suggest new features

📢 Share it with others

Every contribution and star helps the project grow!

---

<p align="center">

# ⭐ Don't Forget to Star this Repository!

If you enjoyed this project or found it helpful, please consider giving it a ⭐ on GitHub.

It motivates future development and helps more people discover the project.

<img src="https://media.giphy.com/media/QBd2kLB5qDmysEXre9/giphy.gif" width="320">

## Made with ❤️ in Python by **Srish Ghosh**

### Happy Coding! 🚀

</p>
