

import streamlit as st
from streamlit.logger import get_logger


LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Traffic Management System",
        page_icon="🚦",
    )

    st.write("# FlowForge: Crafting Seamless Urban Traffic Solutions")

    st.markdown(
        """
        We propose the implementation of a lane priority algorithm to assist traffic junction congestions in urban areas. The deep learning algorithm and API calls operate on parallel threads, while the priority algorithm runs multiple times within each cycle. The cycle time is defined as the total time taken for each lane to receive the green light at least once. Once every lane has received a green light in the current cycle, the cycle is reset, and the priority mask is updated. The priority mask consists of four floating-point values ranging from 0 to 1
    """
    )
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    
    # In each column, display a video player
    video_file_1 = st.sidebar.file_uploader("Upload Video 1", type=["mp4"])
    video_file_2 = st.sidebar.file_uploader("Upload Video 2", type=["mp4"])
    video_file_3 = st.sidebar.file_uploader("Upload Video 3", type=["mp4"])
    video_file_4 = st.sidebar.file_uploader("Upload Video 4", type=["mp4"])

    if video_file_1 is not None:
        col1.video(video_file_1)
    if video_file_2 is not None:
        col2.video(video_file_2)
    if video_file_3 is not None:
        col3.video(video_file_3)
    if video_file_4 is not None:
        col4.video(video_file_4)

    # Initialize play status

    # Play/Pause Button
    if st.button("Play all videos"):

        st.components.v1.html(
            """<script>
            let videos = parent.document.querySelectorAll("video");
            videos.forEach(v => {
                v.play();
            })
            </script>""", 
            width=0, height=0
        )
    if st.button("Pause all videos"):

        st.components.v1.html(
            """<script>
            let videos = parent.document.querySelectorAll("video");
            videos.forEach(v => {
                v.pause();
            })
            </script>""", 
            width=0, height=0
        )
    if video_file_1 is not None:
        send_to_endpoint(video_file_1)
    if video_file_2 is not None:
        send_to_endpoint(video_file_2)
    if video_file_3 is not None:
        send_to_endpoint(video_file_3)
    if video_file_4 is not None:
        send_to_endpoint(video_file_4)

def send_to_endpoint(video_file):
    # Example URL for module endpoint
    endpoint_url = "http://example.com/module_endpoint"
    
    # Send video file to module endpoint
    files = {"file": video_file.getvalue()}
    response = requests.post(endpoint_url, files=files)

    # Display response
    st.write(f"Sending video {video_file.name} to module endpoint...")
    st.write(f"Response: {response.text}")


if __name__ == "__main__":
    run()
