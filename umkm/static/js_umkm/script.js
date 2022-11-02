
$(document).ready(function () {
    umkmCards();

    $('#halo').click(function () {
            $.post(
                '/local-shops/add_umkm_ajax/',
                {
                    name: $('#name').val(),
                    description: $('#description').val(),
                    link_website: $('#link_website').val(),
                    image : $('#image').val(),

                },
                function (data, status) {
                    if (status == 'success') {
                        $(`#cards`).append(card(data))
                        $('#name').val('')
                        $('#description').val('')
                        $('#link_website').val('')
                        $('#image').val('')
                    }
                },
            )
        })
    
    
    
});


function deleteCard(id) {
        $.ajax({
            url: `/local-shops/delete-ajax/${id}`,
            type: 'DELETE',
            success: function (result) {
                $(`#card-${id}`).remove()
            }
        });
    }

function umkmCards() {
    let stringHTML = "";
    $.ajax({
        url: "json",
        type: "GET",
        dataType: "json",
        success: function(data) {
            
            for (i=0; i<data.length; i++){
                
                stringHTML += ` 
                <div class ="col-12 col-md-6 col-lg-4" id="card-${data[i].pk}">
                    <div class="card shadow p-3 mb-5 bg-white rounded border-0" style="padding-right: 10px;">
                    <img class="w-100" src="${data[i].fields.imageURL}" >
                        <div class="card-body">
                            <h3 class="card-title">${data[i].fields.name}</h5>
                            <br>
                            <a class="card-text " href="shop-detail/${data[i].pk}" target="_blank">Read More</a>
                            
                            
                        
                        </div>
                    </div>
                </div>`;
                $('#cards').html(stringHTML);
            }
        }
    });
}