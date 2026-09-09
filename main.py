```python
import requests
from bs4 import BeautifulSoup
import moviepy.editor as mpy
from moviepy.config import change_settings


# =========================
# Configuration
# =========================

URL = "https://islamqa.info/ar/answers/152004"

BACKGROUND_VIDEO = "background.mp4"
OUTPUT_VIDEO = "output.mp4"

IMAGEMAGICK_PATH = r"C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe"

change_settings({
    "IMAGEMAGICK_BINARY": IMAGEMAGICK_PATH
})


# =========================
# Extract Question & Answer
# =========================

def extract_content(url):
    response = requests.get(url, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "lxml")

    section = soup.find("div", class_="section")

    if not section:
        raise ValueError("Could not find the main content section.")

    title = section.find("h1", class_="title")
    question = section.find("section", class_="text-justified")
    answer = section.find(
        "section",
        class_="single_fatwa__answer"
    )

    if not title or not question or not answer:
        raise ValueError("Could not find the question or answer.")

    answer_text = answer.find("section", class_="_pa--0")

    if not answer_text:
        raise ValueError("Could not find the answer text.")

    return (
        title.get_text(strip=True),
        question.get_text(strip=True),
        answer_text.get_text(strip=True)
    )


# =========================
# Generate Video
# =========================

def generate_video(title, question, answer):
    question = question.replace("،", "\n")
    answer_parts = answer.split(". ")

    answer_count = len(answer_parts)

    title_clip = mpy.TextClip(
        title,
        font="mirza-bold",
        fontsize=50,
        color="white",
        bg_color="gray10"
    )

    title_clip = (
        title_clip
        .set_position(("center", 0.05), relative=True)
        .set_start(2)
        .set_duration(5)
        .crossfadein(0.5)
        .crossfadeout(0.5)
    )

    question_clip = mpy.TextClip(
        question,
        font="mirza-bold",
        fontsize=35,
        color="black"
    )

    question_clip = (
        question_clip
        .set_position(("center", 0.1), relative=True)
        .set_start(9)
        .set_duration(30)
        .crossfadein(1)
        .crossfadeout(1)
    )

    answer_clips = []

    start_time = 40

    for answer_part in answer_parts:

        answer_clip = mpy.TextClip(
            answer_part,
            font="Urdu Typesetting",
            fontsize=40,
            color="black"
        )

        answer_clip = (
            answer_clip
            .set_position(("center", 0.5), relative=True)
            .set_start(start_time)
            .set_duration(20)
            .crossfadein(1)
            .crossfadeout(1)
        )

        answer_clips.append(answer_clip)
        start_time += 20

    video_duration = answer_count * 20 + 25

    background = mpy.VideoFileClip(BACKGROUND_VIDEO)

    if background.duration < video_duration:
        raise ValueError(
            "The background video is shorter than the generated video."
        )

    background = background.subclip(0, video_duration)

    final_video = mpy.CompositeVideoClip(
        [background, title_clip, question_clip] + answer_clips
    )

    final_video.write_videofile(
        OUTPUT_VIDEO,
        fps=60,
        codec="libx264",
        preset="fast",
        bitrate="5000k",
        audio=False
    )

    background.close()
    final_video.close()


# =========================
# Main
# =========================

def main():
    print("Extracting content...")

    title, question, answer = extract_content(URL)

    print(f"Question: {title}")
    print("Generating video...")

    generate_video(title, question, answer)

    print(f"Video saved as: {OUTPUT_VIDEO}")


if __name__ == "__main__":
    main()
```
