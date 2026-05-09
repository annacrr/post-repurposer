import os
import streamlit as st
import streamlit.components.v1 as components
from dotenv import load_dotenv
from anthropic import Anthropic


USE_API = False


def build_prompt(long_text, tone, selected_platforms):
    platforms_text = ", ".join(selected_platforms)

    prompt = f"""
You are an expert content strategist, social media copywriter, and platform-native editor.

Your task is to repurpose the long-form content below into platform-specific posts.

Selected tone:
{tone}

Selected platforms:
{platforms_text}

Core rules:
- Keep the original message, facts, and main ideas.
- Do not invent facts, numbers, events, names, or claims.
- Adapt the content to each selected platform instead of simply summarizing it.
- Make each post ready to publish.
- Write in a natural, human voice.
- Avoid generic AI-sounding language.
- Avoid making every platform sound the same.
- If the original content is in English, respond in English.
- If the original content is in Portuguese, respond in Portuguese.
- If the original content is in another language, respond in that same language.
- Return only the selected platforms.

Platform instructions:

LINKEDIN

Tone:
Professional, human, thoughtful, and conversational.
It should feel like a real person sharing a reflection, insight, project, lesson, or achievement.
It should not feel like a corporate announcement.

Length:
Medium length.
Usually 4 to 8 short paragraphs.
It can be longer when the story or insight needs context, but it should still be easy to skim.

Structure:
Start with a strong human hook, observation, or context.
Then develop the idea with short paragraphs.
Use line breaks often.
Add emojis when they feel natural and relevant to the topic, but do not overuse them.
Use bullet points when they help organize ideas, examples, lessons, steps, or takeaways, but not in every post.
End with either a soft reflection, a question, a call to continue the conversation, or a clear closing thought.

Avoid:
- Sounding too formal, robotic, salesy, or generically motivational.
- Huge paragraphs.
- Overusing emojis.
- Forced LinkedIn guru language.
- Making every post into a list.
- Phrases that sound like a press release.

INSTAGRAM

Tone:
Short, visual, warm, simple, and skimmable.
It can be poetic, emotional, informative, or lifestyle-focused depending on the topic, but it should never feel heavy.

Length:
Short.
Usually 3 to 6 short blocks.
Each block should be 1 to 2 lines max.

Structure:
Use line breaks between ideas.
Start with a simple hook or emotional sentence.
Then explain the product, idea, moment, or message clearly.
Use relevant emojis that match the topic, mood, or visual identity.
End with a soft closing, CTA, or final sentence that feels natural.

Hashtags:
Use a small number only when useful.
Usually 3 to 8 hashtags max.
Prefer relevant, specific hashtags over generic ones.

Avoid:
- Long captions with dense paragraphs.
- Too many hashtags.
- Random emojis that do not match the topic.
- Sounding too corporate.
- Overexplaining.
- Making it look like LinkedIn.

TWITTER/X

Tone:
Direct, punchy, curious, and attention-grabbing.
It can be informative, dramatic, funny, ironic, or thread-like depending on the goal.

Length:
Short to medium.
For single tweets, keep it sharp and compact.
For longer storytelling posts, use short lines and strong pacing.

Structure:
Start with a strong hook.
Use short sentences.
Create curiosity quickly.
Break lines often.
For stories, build momentum with specific details, numbers, contrast, or surprising turns.
For tips or insights, make the value clear fast.

Avoid:
- Sounding too polished or corporate.
- Long intro context before the point.
- Weak hooks.
- Overexplaining.
- Hashtags unless they are actually useful.
- Making it feel like an Instagram caption or LinkedIn reflection.

Long-form content:
\"\"\"
{long_text}
\"\"\"

Return the response in this format, but only include the selected platforms:

LINKEDIN:
[LinkedIn post]

INSTAGRAM:
[Instagram post]

TWITTER/X:
[Twitter/X post]
"""

    return prompt


def generate_fake_posts():
    linkedin_post = "LinkedIn output"
    instagram_post = "Instagram output"
    twitter_post = "Twitter/X output"

    return {
        "LinkedIn": linkedin_post,
        "Instagram": instagram_post,
        "Twitter/X": twitter_post
    }


def generate_posts_with_claude(prompt):
    load_dotenv()

    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key:
        raise ValueError("API key not found. Add ANTHROPIC_API_KEY to your .env file.")

    client = Anthropic(api_key=api_key)

    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1500,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.content[0].text


def parse_ai_output(ai_text):
    outputs = {
        "LinkedIn": "",
        "Instagram": "",
        "Twitter/X": ""
    }

    current_platform = None

    for line in ai_text.splitlines():
        clean_line = line.strip()

        if clean_line.upper().startswith("LINKEDIN:"):
            current_platform = "LinkedIn"
            content = clean_line.replace("LINKEDIN:", "").strip()
            if content:
                outputs[current_platform] += content + "\n"
        elif clean_line.upper().startswith("INSTAGRAM:"):
            current_platform = "Instagram"
            content = clean_line.replace("INSTAGRAM:", "").strip()
            if content:
                outputs[current_platform] += content + "\n"
        elif clean_line.upper().startswith("TWITTER/X:"):
            current_platform = "Twitter/X"
            content = clean_line.replace("TWITTER/X:", "").strip()
            if content:
                outputs[current_platform] += content + "\n"
        elif current_platform:
            outputs[current_platform] += line + "\n"

    return outputs


def generate_posts(long_text, tone, selected_platforms):
    prompt = build_prompt(long_text, tone, selected_platforms)

    if USE_API:
        ai_text = generate_posts_with_claude(prompt)
        outputs = parse_ai_output(ai_text)
    else:
        outputs = generate_fake_posts()

    return outputs


st.set_page_config(
    page_title="Post Repurposer",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lora:wght@400;500;600;700&display=swap');

    header[data-testid="stHeader"] {
        display: none;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    html, body, [class*="css"] {
        font-family: 'Lora', Georgia, serif;
    }

    .stApp {
        background-color: #fffdf9;
        color: #111827;
    }

    .block-container {
        max-width: 980px;
        padding-top: 2.4rem;
        padding-bottom: 5rem;
    }

    .brand {
        font-family: 'Lora', Georgia, serif;
        font-size: 22px;
        font-weight: 600;
        color: #13256b;
        letter-spacing: -0.3px;
    }

    .top-spacing {
        margin-bottom: 5.4rem;
    }

    .hero {
        text-align: center;
        margin-bottom: 4.2rem;
    }

    .main-title {
        font-family: 'Lora', Georgia, serif;
        font-size: 54px;
        line-height: 1.12;
        font-weight: 600;
        color: #13256b;
        margin-bottom: 1.2rem;
        letter-spacing: -1.2px;
    }

    .subtitle {
        font-family: 'Lora', Georgia, serif;
        font-size: 16px;
        line-height: 1.65;
        color: #2f3440;
        max-width: 610px;
        margin: 0 auto;
    }

    label, .stTextArea label {
        font-family: 'Lora', Georgia, serif !important;
        color: #111827 !important;
        font-size: 14px !important;
    }

    div[data-testid="stTextArea"] {
        border: none !important;
        box-shadow: none !important;
        outline: none !important;
    }

    div[data-testid="stTextArea"] > div {
        border: none !important;
        box-shadow: none !important;
        outline: none !important;
    }

    div[data-testid="stTextArea"] div {
        border-color: transparent !important;
        box-shadow: none !important;
        outline: none !important;
    }

    div[data-testid="stTextArea"] textarea {
        background-color: #fffefa !important;
        color: #111827 !important;
        border-radius: 24px !important;
        border: 1px solid #ded1c3 !important;
        outline: none !important;
        box-shadow: none !important;
        font-family: 'Lora', Georgia, serif !important;
        font-size: 17px !important;
        line-height: 1.6 !important;
        padding: 20px !important;
    }

    div[data-testid="stTextArea"] textarea:hover {
        border: 1px solid #cdbdad !important;
        outline: none !important;
        box-shadow: none !important;
    }

    div[data-testid="stTextArea"] textarea:focus,
    div[data-testid="stTextArea"] textarea:focus-visible,
    div[data-testid="stTextArea"] textarea:active {
        border: 1px solid #13256b !important;
        outline: none !important;
        box-shadow: none !important;
    }

    div.stButton {
        display: flex;
        justify-content: flex-start;
        margin-top: 1.3rem;
        margin-bottom: 1.8rem;
    }

    div.stButton > button {
        background-color: #13256b;
        color: #fffdf9;
        border: 1px solid #13256b;
        border-radius: 999px;
        padding: 0.78rem 1.9rem;
        font-family: 'Lora', Georgia, serif;
        font-size: 15px;
        font-weight: 600;
    }

    div.stButton > button:hover {
        background-color: #0d1b4c;
        color: #fffdf9;
        border: 1px solid #0d1b4c;
    }

    div[data-testid="stPopover"] button {
        border-radius: 999px;
        border: 1px solid #ded1c3;
        background-color: #fffefa;
        color: #13256b;
        font-family: 'Lora', Georgia, serif;
        font-size: 15px;
        padding: 0.45rem 1rem;
    }

    div[data-testid="stPopover"] button:hover {
        border-color: #13256b;
        color: #13256b;
        background-color: #fffefa;
    }

    div[data-baseweb="select"] > div {
        background-color: #fffefa !important;
        border-radius: 18px !important;
        border: 1px solid #ded1c3 !important;
        font-family: 'Lora', Georgia, serif !important;
        min-height: 52px;
    }

    div[data-baseweb="tag"] {
        border-radius: 999px !important;
        padding: 0.25rem 0.45rem !important;
        font-family: 'Lora', Georgia, serif !important;
        font-size: 15px !important;
        color: #13256b !important;
        background-color: #e9ecff !important;
        border: 1px solid #cfd6ff !important;
    }

    div[data-baseweb="tag"] span {
        color: #13256b !important;
    }

    div[data-baseweb="tag"] svg {
        color: #13256b !important;
    }

    .results-anchor {
        scroll-margin-top: 24px;
    }

    .results-title {
        text-align: center;
        font-family: 'Lora', Georgia, serif;
        font-size: 40px;
        font-weight: 700;
        color: #13256b;
        margin-top: 0.5rem;
        margin-bottom: 2.4rem;
    }

    .platform-section {
        padding: 1.8rem 0 2.3rem 0;
    }

    .platform-divider {
        border-bottom: 1.5px solid #b9aa99;
    }

    .platform-title {
        font-family: 'Lora', Georgia, serif;
        font-size: 26px;
        font-style: italic;
        font-weight: 700;
        margin-bottom: 1rem;
        color: #13256b;
    }

    .output-card {
        background-color: #fffefa;
        border: 1px solid #ded1c3;
        border-radius: 24px;
        padding: 1.5rem 1.7rem;
        font-family: 'Lora', Georgia, serif;
        font-size: 17px;
        line-height: 1.7;
        color: #111827;
        white-space: pre-wrap;
    }

    </style>
    """,
    unsafe_allow_html=True
)


top_left, top_right = st.columns([3, 1])

with top_left:
    st.markdown('<div class="brand">✦ Post Repurposer</div>', unsafe_allow_html=True)

with top_right:
    with st.popover("Settings"):
        tone = st.selectbox(
            "Tone",
            ["Professional", "Casual", "Bold", "Educational", "Warm"]
        )

        selected_platforms = st.multiselect(
            "Platforms",
            ["LinkedIn", "Instagram", "Twitter/X"],
            default=["LinkedIn", "Instagram", "Twitter/X"]
        )

st.markdown('<div class="top-spacing"></div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="hero">
        <div class="main-title">What do you want to repurpose?</div>
        <div class="subtitle">
            Paste a long-form idea and turn it into platform-ready posts with the right tone, structure, and format.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

long_text = st.text_area(
    "Paste your long-form content here:",
    height=260,
    placeholder="Paste a blog post, video script, newsletter, or long caption..."
)

generate_button = st.button("Generate posts")


if generate_button:
    if long_text.strip() == "":
        st.warning("Please paste some content first.")
    elif len(selected_platforms) == 0:
        st.warning("Please select at least one platform in Settings.")
    else:
        try:
            platform_outputs = generate_posts(long_text, tone, selected_platforms)

            st.markdown('<div id="results-anchor" class="results-anchor"></div>', unsafe_allow_html=True)
            st.markdown('<div class="results-title">Results</div>', unsafe_allow_html=True)

            for index, platform in enumerate(selected_platforms):
                divider_class = "platform-divider" if index < len(selected_platforms) - 1 else ""
                output_text = platform_outputs.get(platform, "")

                st.markdown(
                    f"""
                    <div class="platform-section {divider_class}">
                        <div class="platform-title">{platform}</div>
                        <div class="output-card">{output_text}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            components.html(
                """
                <script>
                    const results = window.parent.document.getElementById("results-anchor");
                    if (results) {
                        results.scrollIntoView({ behavior: "smooth", block: "start" });
                    }
                </script>
                """,
                height=0
            )

        except Exception as error:
            st.error("Something went wrong while generating the posts.")
            st.write(error)