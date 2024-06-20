document.addEventListener('DOMContentLoaded', function() {
    const videoContainer = document.getElementById('video-container');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const message = document.getElementById('message');
    let currentIndex = 0;
   
    
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

 
});


