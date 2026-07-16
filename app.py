import html as html_lib

import cohere
import streamlit as st

COMPATIBLE_COHERE_MODELS = [
    "command-a-03-2025",
    "command-r-plus-08-2024",
    "command-r-08-2024",
    "command-r7b-12-2024",
]

_CSS = """
<style>
/* ── Page background ───────────────────────────────────────────── */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0a0f1e, #0d2137, #0a1628);
    min-height: 100vh;
}
[data-testid="stHeader"] { background: transparent; }

/* ── Hero banner ───────────────────────────────────────────────── */
.hero {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
}
.hero h1 {
    font-size: 2.6rem;
    font-weight: 800;
    background: linear-gradient(90deg, #39d2c0, #3d8bff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.3rem;
}
.hero p {
    color: #94a3b8;
    font-size: 1.05rem;
    margin-top: 0;
}

/* ── Blog result card ──────────────────────────────────────────── */
.blog-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(57,210,192,0.3);
    border-radius: 14px;
    padding: 1.6rem 1.8rem;
    color: #e2e8f0;
    font-size: 1rem;
    line-height: 1.8;
    white-space: pre-wrap;
    word-break: break-word;
    margin-top: 1rem;
}
.blog-label {
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #39d2c0;
    margin-bottom: 0.4rem;
}

/* ── Buttons ───────────────────────────────────────────────────── */
[data-testid="stDownloadButton"] button,
[data-testid="stButton"] button {
    background: linear-gradient(135deg, #0d9488, #2563eb) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.45rem 1.2rem !important;
    font-weight: 600 !important;
    transition: opacity 0.2s !important;
}
[data-testid="stDownloadButton"] button:hover,
[data-testid="stButton"] button:hover { opacity: 0.85 !important; }

/* ── Sidebar ───────────────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background: rgba(10,15,30,0.92);
    border-right: 1px solid rgba(57,210,192,0.2);
}
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] div { color: #cbd5e1 !important; }
[data-testid="stSidebar"] h2 {
    color: #39d2c0 !important;
    font-size: 1.1rem;
}

/* ── Inputs ────────────────────────────────────────────────────── */
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(57,210,192,0.3) !important;
    border-radius: 8px !important;
    color: #e2e8f0 !important;
}

/* ── Spinner text ──────────────────────────────────────────────── */
[data-testid="stSpinner"] p { color: #39d2c0 !important; }
</style>
"""


def generate_blog_content(api_key, topic, model, length=300):
    co = cohere.ClientV2(api_key)
    response = co.chat(
        model=model,
        messages=[{"role": "user", "content": f"Write a blog post about {topic}."}],
        max_tokens=length,
    )
    return response.message.content[0].text


def main():
    st.set_page_config(
        page_title="Blog Content Generator",
        page_icon="✍️",
        layout="centered",
    )
    st.markdown(_CSS, unsafe_allow_html=True)

    # ── Hero header ────────────────────────────────────────────────
    st.markdown(
        """
        <div class="hero">
            <h1>✍️ Blog Content Generator</h1>
            <p>Powered by the <a href="https://cohere.com" target="_blank"
               style="color:#39d2c0;text-decoration:none;">Cohere AI</a> API —
               craft compelling blog posts in seconds.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Sidebar (settings panel) ───────────────────────────────────
    st.sidebar.header("⚙️ Settings")

    api_key = st.sidebar.text_input(
        "Cohere API Key",
        type="password",
        help="Enter your Cohere API key. Get one at https://cohere.com",
    )
    model = st.sidebar.selectbox(
        "Cohere Model",
        COMPATIBLE_COHERE_MODELS,
        index=0,
        help="Select the Cohere model to use for generation.",
    )
    length = st.sidebar.number_input(
        "Max tokens (approx. length)",
        min_value=100,
        max_value=1000,
        value=300,
        help="Controls the approximate length of the generated blog post.",
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown(
        "[![Cohere](https://img.shields.io/badge/Powered%20by-Cohere-39d2c0?style=flat-square)](https://cohere.com)"
    )
    st.sidebar.markdown(
        "[![GitHub](https://img.shields.io/badge/View%20on-GitHub-181717?logo=github&style=flat-square)](https://github.com/gituserc1140/BlogMobileApp3)"
    )
    st.sidebar.markdown(
        "[![Sponsor me on GitHub](https://img.shields.io/badge/Sponsor%20me%20on-GitHub-EA4AAA?logo=githubsponsors&style=flat-square)](https://github.com/sponsors/gituserc1140)"
    )

    # ── Main content ───────────────────────────────────────────────
    if not api_key:
        st.info("👈 Enter your Cohere API key in the sidebar to get started.", icon=None)
        st.stop()

    topic = st.text_input("📝 Blog topic", placeholder="e.g. The future of renewable energy")

    if st.button("✨ Generate Blog"):
        if not topic:
            st.error("Please enter a blog topic.")
        else:
            with st.spinner("Generating your blog post… ✨"):
                try:
                    st.session_state["blog_content"] = generate_blog_content(api_key, topic, model, length)
                except Exception as e:
                    st.error(f"An error occurred: {e}")

    if "blog_content" in st.session_state:
        st.markdown('<div class="blog-label">📄 Generated Blog Post</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="blog-card">{html_lib.escape(st.session_state["blog_content"])}</div>',
            unsafe_allow_html=True,
        )
        st.download_button(
            label="⬇️ Download as Markdown",
            data=st.session_state["blog_content"],
            file_name="blog.md",
            mime="text/markdown",
        )


if __name__ == "__main__":
    main()