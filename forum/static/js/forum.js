$(document).ready(function(){
    let cardString = '';

    $.get('/forum/question_json/', function(data){
        if (data.length == 0){
            $("#forumCards").append(`
                <div style="text-align:center">
                    <h2 style="margin-top:0%; padding-bottom:5%; color:grey">No questions yet</h3>
                </div>`)
        } else {
                                            
            for (i=data.length-1; i>=0; i--){
                cardString += `<div id="${data[i].pk}--forum" class="col-md-4 col-lg-4 mb-3">
                                    <div class="forum card d-flex">
                                        <div id="${data[i].pk}--question" class="card-body d-flex flex-column">
                                            <h5 class="card-title">${data[i].fields.title}</h5>
                                            <p class="card-text mb-4">${data[i].fields.question}</p>
                                            <p class="card-text details">${data[i].fields.username} ● ${data[i].fields.date}</p>`

                if (status == 'L'){
                    cardString += `<a href="add_answer/${data[i].pk}", class="btn btn-forum"><span class="glyphicon glyphicon-comment"></span></a>`
                }
                if (user == data[i].fields.username){
                    cardString += `<a href="delete_question/${data[i].pk}", class="btn btn-forum"><span class="glyphicon glyphicon-trash"></span></a>`
                }
                if (data[i].fields.is_answered == false){
                    cardString += `<p class="card-text status p-2 d-flex justify-content-center">Not yet answered</p>`
                }
                else {
                    cardString += `<p class="card-text status pt-2 d-flex justify-content-center">Answers:</p>`
                }
                $.get(`/forum/answer_json/${data[i].pk}`, function(answer){
                    for (j=0; j<answer.length; j++){
                        document.getElementById(`${answer[j].fields.question}--question`).innerHTML += 
                        `<p class="card-text mb-4">${answer[j].fields.answer}</p>
                         <p class="card-text details">${answer[j].fields.username} ● ${answer[j].fields.date}</p>`
                    }
                })
                
                $("#forumCards").append(cardString)
                cardString = ''
            }
        }
    });
    
    
    $('#submit_question').click(function(){
        addQuestion()
        $("#questionForm")[0].reset()
    });
});

function deleteCard(id) {
    $.ajax({
        url: `/forum/delete_question/${id}`,
        type: 'DELETE',
        success: function (result) {
            $(`#${id}--question`).remove()
        }
    });
}

function addQuestion() {
    fetch("/forum/add_question/", {
    method: "POST",
    body: new FormData(document.querySelector("#questionForm"))
    }).then(questionCards)
    return false
}


function questionCards() {
    let cardString = "";
    $.ajax({
        url: "question_json",
        type: "GET",
        dataType: "json",
        success: function(data) {
            var newest = data.length - 1;
            cardString += `<div id="${data[newest].pk}--forum" class="col-md-4 col-lg-4 mb-3">
                                <div class="forum card d-flex">
                                    <div id="${data[newest].pk}--question" class="card-body d-flex flex-column">
                                        <h5 class="card-title">${data[newest].fields.title}</h5>
                                        <p class="card-text mb-4">${data[newest].fields.question}</p>
                                        <p class="card-text details">${data[newest].fields.username} ● ${data[newest].fields.date}</p>`
            if (status == 'L'){
                cardString += `<a href="add_answer/${data[newest].pk}", class="btn btn-forum"><span class="glyphicon glyphicon-comment"></span></a>`
            }  
            if (user == data[newest].fields.username){
                cardString += `<a href="delete_question/${data[newest].pk}", class="btn btn-forum"><span class="glyphicon glyphicon-trash"></span></a>`
            }
            if (data[newest].fields.is_answered == false){
                cardString += `<p class="card-text status p-2 d-flex justify-content-center">Not yet answered</p>`
            }
            else {
                cardString += `<p class="card-text status pt-2 d-flex justify-content-center">Answers:</p>`
            }      

                $.get(`/forum/answer_json/${data[newest].pk}`, function(answer){
                for (j=0; j<answer.length; j++){
                    document.getElementById(`${answer[j].fields.question}--question`).innerHTML +=
                    `<p class="card-text">${answer[j].fields.answer}</p>
                    <p class="card-text">${answer[j].fields.username} ● ${answer[j].fields.date}</p>`
                }
            })
            $('#forumCards').prepend(cardString);
            cardString = "";
        }
    })
}
