function submitForm() {
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;

    // Using $.post
    $.post("/submit", {username: username, email: email}, function(response) {
        console.log(response.message);
    });

    // Using $.ajax
    $.ajax({
        type: 'POST',
        url: '/submit',
        data: {username: username, email: email},
        success: function(response) {
            console.log(response.message);
            document.getElementById('result').innerHTML = response.message;
        },
        error: function(error) {
            console.log(error);
        }
    });
}
