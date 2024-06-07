document.addEventListener('DOMContentLoaded', function() {
    const videoContainer = document.getElementById('video-container');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const message = document.getElementById('message');
    let currentIndex = 0;
    let videos = [];

    // Function to fetch video data from API
    async function fetchVideoData() {
        try {
            const response = await fetch('http://127.0.0.1:8000/api-auth/vd/'); // Replace with actual API URL
            const data = await response.json();
            videos = data;
            if (videos.length === 0) {
                showMessage('No videos available');
            } else {
                displayVideo(currentIndex);
                updateButtons();
            }
        } catch (error) {
            console.error('Error fetching video data:', error);
            showMessage('Error fetching video data');
        }
    }

    // Function to display a specific video
    function displayVideo(index) {
        videoContainer.innerHTML = ''; // Clear current content

        const video = videos[index];

        const card = document.createElement('div');
        card.className = 'card';
        card.style.display = 'block';

        const thumbnail = document.createElement('img');
        thumbnail.src = video.thumbnail; // Replace with actual JSON field
        card.appendChild(thumbnail);

        const title = document.createElement('h3');
        title.textContent = video.title; // Replace with actual JSON field
        card.appendChild(title);

        const description = document.createElement('p');
        description.textContent = video.description; // Replace with actual JSON field
        card.appendChild(description);

        const videoLink = document.createElement('a');
        videoLink.href = video.video_file; // Replace with actual JSON field
        videoLink.textContent = 'Watch Video';
        videoLink.target = '_blank';
        card.appendChild(videoLink);

        const datePosted = document.createElement('p');
        datePosted.className = 'date-posted';
        datePosted.textContent = `Posted on: ${new Date(video.date_posted).toLocaleDateString()}`; // Replace with actual JSON field
        card.appendChild(datePosted);

        videoContainer.appendChild(card);
    }

    // Function to update the state of navigation buttons
    function updateButtons() {
        prevBtn.disabled = currentIndex === 0;
        nextBtn.disabled = currentIndex === videos.length - 1;
    }

    // Function to show a message
    function showMessage(text) {
        message.textContent = text;
        videoContainer.innerHTML = '';
        prevBtn.disabled = true;
        nextBtn.disabled = true;
    }

    // Event listeners for navigation buttons
    prevBtn.addEventListener('click', () => {
        if (currentIndex > 0) {
            currentIndex--;
            displayVideo(currentIndex);
            updateButtons();
        }
    });

    nextBtn.addEventListener('click', () => {
        if (currentIndex < videos.length - 1) {
            currentIndex++;
            displayVideo(currentIndex);
            updateButtons();
        }
    });

    // Fetch and display videos on page load
    fetchVideoData();
});