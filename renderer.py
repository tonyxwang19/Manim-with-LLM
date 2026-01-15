import subprocess
import re
import os
from pathlib import Path

def extract_scene_class_name(code: str) -> str:
    """
    Finds the name of the class that inherits from Scene.
    """
    match = re.search(r"class\s+(\w+)\s*\(.*Scene.*\):", code)
    if match:
        return match.group(1)
    return "MathScene"  # Default fallback

def render_manim_code(code: str, output_file_name: str = "animation") -> str:
    """
    Saves code to a temp file, runs manim, and returns the path to the video.
    """
    # 1. Save code to file
    script_path = "temp_manim_script.py"
    with open(script_path, "w") as f:
        f.write(code)

    # 2. Extract scene name
    scene_name = extract_scene_class_name(code)

    # 3. Run Manim
    # -qL for low quality (faster for prototype), -o for output filename
    # media_dir can be configured, but default is ./media
    cmd = [
        "manim",
        "-ql",  # Low quality for speed
        "--media_dir", "media",
        script_path,
        scene_name
    ]

    print(f"Running command: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        # print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Manim Error Output:")
        print(e.stderr)
        raise RuntimeError(f"Manim failed to render: {e.stderr}")

    # 4. Find the output video
    # Manim structure: media/videos/temp_manim_script/480p15/SceneName.mp4
    # Note: -ql defaults to 480p15
    video_dir = Path("media/videos/temp_manim_script/480p15")
    video_path = video_dir / f"{scene_name}.mp4"

    if video_path.exists():
        return str(video_path)
    else:
        raise FileNotFoundError(f"Could not find rendered video at {video_path}")
