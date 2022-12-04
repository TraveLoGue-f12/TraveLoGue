$(document).ready(function(){
    $.get("/event/json/", function(data) {
        console.log(data)
        for (i=0; i<data.length; i++){
            $("#cards").append(`
            <div class="col-lg-4 col-sm-6">
                <div class="post-item position-relative h-100">
                <div class="post-content d-flex flex-column">
                    <h3 class="post-title">${data[i].fields.title}</h3>
                    <p>${data[i].fields.description}</p>
                    <hr>
                    <a href="event-detail/${data[i].pk}" class="readmore stretched-link"><span>Read more</span><i class="bi bi-arrow-right"></i></a>
                </div>
                </div>
            </div>`)
        }
    });
    
    // let files
    // $('#image').on('change', function (event) {
    //     files = event.target.files
    //     console.log(files)
    // })


    $("#submit_event").click(function(){
        const formData = new FormData()
        // formData.append('image', files[0])
        formData.append('title', $("#title").val())
        formData.append('place', $("#place").val())
        formData.append('date', $("#date").val())
        formData.append('description', $("#description").val())
        formData.append('category', $("#category").val())

        $.ajax({
            url: '/event/add-new/', // point to server-side URL
            dataType: 'json', // what to expect back from server
            cache: false,
            contentType: false,
            processData: false,
            data: formData,
            type: 'post',
            success: function(result){
                // console.log(result)
                $("#cards").append(`
                <div class="col-lg-4 col-sm-6">
                    <div class="post-item position-relative h-100">
                    <div class="post-content d-flex flex-column">
                        <h3 class="post-title">${result.fields.title}</h3>
                        <p>${result.fields.description}</p>
                        <hr>

                        <a href="event-detail/${result.pk}" class="readmore stretched-link"><span>Read more</span><i class="bi bi-arrow-right"></i></a>
                    </div>
                    </div>
                </div>`);
                $("#title").val(''),
                $("#place").val(''),
                $("#date").val(''),
                $("#description").val(''),
                $("#category").val('')

                alert("Event has added")
            },
            error: function (response) {
                $('#msg').html(response.message); // display error response
            }
        });

    });

});
