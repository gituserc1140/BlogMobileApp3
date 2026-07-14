import streamlit as st
import cohere

def generate_blog_content(api_key, topic, length=300):
    co = cohere.Client(api_key)
    response = co.generate(
        model='command',
        prompt=f'Write a blog post about {topic}.',
        max_tokens=length,
        temperature=0.7
    )
    return response.generations[0].text

def main():
    st.title('Blog Content Generator with Cohere API')
    api_key = st.text_input('Enter your Cohere API Key', type='password')
    topic = st.text_input('Enter the blog topic')
    length = st.number_input('Desired length of the blog (words)', min_value=100, max_value=1000, value=300)

    if st.button('Generate Blog'):
        if not api_key or not topic:
            st.error('Please provide both API Key and a topic.')
        else:
            try:
                blog_content = generate_blog_content(api_key, topic, length)
                st.subheader('Generated Blog Content')
                st.write(blog_content)
            except Exception as e:
                st.error(f'An error occurred: {e}')

if __name__ == '__main__':
    main()