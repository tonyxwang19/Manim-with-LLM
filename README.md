# Math to Manim Generator MVP

This is a prototype application that uses an LLM (DeepSeek) to generate Manim animations from natural language descriptions.

## Prerequisites

### 1. System Dependencies (macOS)
You need `ffmpeg` and a LaTeX distribution for Manim to work.

```bash
brew install ffmpeg
brew install --cask mactex  # Full installation (large)
# OR
brew install --cask basictex  # Minimal installation
```

If you install BasicTeX, you might need to add it to your path or install specific packages if Manim complains.

### 2. Python Dependencies
Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Setup

1. Create a `.env` file in the root directory (copy from `.env.example`):
   ```bash
   cp .env.example .env
   ```
2. Add your DeepSeek API Key to `.env`:
   ```
   DEEPSEEK_API_KEY=sk-...
   ```
   (Alternatively, you can enter the key in the UI).

## Running the App

Run the Streamlit app:

```bash
streamlit run app.py
```

## Usage

1. Open the URL provided by Streamlit (usually http://localhost:8501).
2. Enter a math topic (e.g., "Visual proof of Pythagorean theorem").
3. Click "Generate Animation".
4. Wait for the code generation and rendering to complete.
5. Watch and download your video!
