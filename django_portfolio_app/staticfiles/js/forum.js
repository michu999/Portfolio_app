document.addEventListener('DOMContentLoaded', function () {
    // Handle reply button clicks
    document.querySelectorAll('.reply-btn').forEach(button => {
        button.addEventListener('click', function () {
            const replyForm = this.nextElementSibling;
            replyForm.classList.toggle('hidden');
        });
    });

    // Handle reactions
    document.querySelectorAll('.reaction-btn').forEach(button => {
        button.addEventListener('click', function() {
            const reactionType = this.getAttribute('data-reaction-type');
            const container = this.closest('.reaction-buttons');
            const postId = container.getAttribute('data-post-id');
            const commentId = container.getAttribute('data-comment-id');

            // Store references to count elements
            const likeBtn = container.querySelector('.like-btn');
            const dislikeBtn = container.querySelector('.dislike-btn');
            const likeCount = container.querySelector('.like-count');
            const dislikeCount = container.querySelector('.dislike-count');

            // Debug output
            console.log('Reaction clicked:', {
                reactionType,
                postId,
                commentId,
                currentLikeCount: likeCount.textContent,
                currentDislikeCount: dislikeCount.textContent
            });

            // Prepare form data
            const formData = new FormData();
            formData.append('csrfmiddlewaretoken', document.querySelector('[name=csrfmiddlewaretoken]').value);
            formData.append('reaction_type', reactionType);

            if (postId) {
                formData.append('post_id', postId);
            } else if (commentId) {
                formData.append('comment_id', commentId);
            }

            // Send AJAX request
            fetch('/forum/reaction/toggle/', {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                },
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                console.log('Server response:', data);

                if (data.success) {
                    // Update counts with new values from server
                    likeCount.textContent = data.like_count;
                    dislikeCount.textContent = data.dislike_count;

                    // Update active states
                    likeBtn.classList.remove('active');
                    dislikeBtn.classList.remove('active');

                    if (data.action !== 'removed') {
                        if (data.reaction_type === 'Like') {
                            likeBtn.classList.add('active');
                        } else if (data.reaction_type === 'Dislike') {
                            dislikeBtn.classList.add('active');
                        }
                    }

                    console.log('Updated counts:', {
                        newLikeCount: likeCount.textContent,
                        newDislikeCount: dislikeCount.textContent
                    });
                } else {
                    console.error('Server reported error:', data.error || 'Unknown error');
                    alert('Could not process reaction. Please try again.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while processing your reaction');
            });
        });
    });
});