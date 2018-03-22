window.onload = () => {

    const form = document.getElementById('comment-form');
    if(form)
        form.addEventListener('submit', (event) => {
            event.preventDefault();

            const request = new XMLHttpRequest();

            request.onreadystatechange = function()
            {
                if(request.readyState == 4 && request.status == 200)
                {
                    const response = JSON.parse(request.responseText);
                    const commentsContainer = document.getElementById('comments-container');
                    commentsContainer.innerHTML = response.comments;
                    form.reset()
                } else {
                    //console.log(request);
                }
            }
            request.open("post", form.getAttribute("action"));
            request.setRequestHeader("X-Requested-With",'XMLHttpRequest');
            request.send(new FormData(form));

        });

}