import streamlit as st

from utils.summarizer import generate_summary
from utils.action_items import extract_action_items
from utils.decisions import extract_decisions
from utils.keypoints import extract_key_points
from utils.speaker_identifier import identify_speakers
from utils.pdf_generator import generate_pdf
from utils.audio_to_text import transcribe_audio

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Meeting Minutes Generator",
    layout="wide"
)

st.title("📝 AI-Powered Meeting Minutes Generator")
st.write(
    "Generate structured meeting minutes from **text** or **clear WAV audio**. "
    "For best results, speak slowly with pauses."
)

# ---------------- INPUT SECTION ----------------
input_type = st.radio(
    "Choose input type:",
    ["Text", "Audio (WAV only)"]
)

meeting_text = ""

if input_type == "Text":
    meeting_text = st.text_area(
        "📋 Paste Meeting Transcript",
        height=300,
        placeholder="Paste your meeting text here..."
    )

else:
    audio_file = st.file_uploader(
        "🎤 Upload WAV Audio (slow, clear speech)",
        type=["wav"]
    )

    if audio_file:
        with st.spinner("Converting audio to text..."):
            meeting_text = transcribe_audio(audio_file)

        # ---- SAFETY CHECK ----
        if (
            "Audio not clear enough" in meeting_text
            or "could not understand" in meeting_text.lower()
        ):
            st.error(meeting_text)
            st.stop()

        st.subheader("📝 Transcribed Text")
        st.write(meeting_text)

# ---------------- PROCESSING ----------------
if st.button("🚀 Generate Minutes"):
    if meeting_text.strip() == "":
        st.warning("Please provide meeting input (text or audio).")
    else:
        with st.spinner("Analyzing meeting and generating minutes..."):
            summary = generate_summary(meeting_text)
            key_points = extract_key_points(meeting_text)
            decisions = extract_decisions(meeting_text)
            actions = extract_action_items(meeting_text)
            speakers = identify_speakers(meeting_text)

            pdf_path = generate_pdf(
                summary,
                key_points,
                decisions,
                actions
            )

        # ---------------- OUTPUT ----------------
        st.subheader("📌 Meeting Summary")
        st.write(summary)

        st.subheader("🗂 Key Discussion Points")
        if key_points:
            for p in key_points:
                st.markdown(f"- {p}")
        else:
            st.write("No key points detected.")

        st.subheader("📣 Decisions Made")
        if decisions:
            for d in decisions:
                st.markdown(f"- {d}")
        else:
            st.write("No decisions detected.")

        st.subheader("✅ Action Items")
        if actions:
            for a in actions:
                st.markdown(f"- {a}")
        else:
            st.write("No action items detected.")

        st.subheader("🗣 Speaker-wise Statements")
        if speakers:
            for s in speakers:
                st.markdown(f"**{s['speaker']}**: {s['statement']}")
        else:
            st.write("No speaker names detected.")

        # ---------------- PDF DOWNLOAD ----------------
        with open(pdf_path, "rb") as f:
            st.download_button(
                label="📄 Download Meeting Minutes (PDF)",
                data=f,
                file_name="meeting_minutes.pdf",
                mime="application/pdf"
            )

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "✅ **Features:** Text/WAV Audio Input • NLP Summarization • "
    "Decisions • Action Items • Speaker Identification • PDF Export"
)
