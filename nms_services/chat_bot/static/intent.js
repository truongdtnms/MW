window.onload = () => {

    $('#btn-create-intent').click(function (e) {
        data = $('#input-intent').val();
        console.log(data)
        $.ajax({
            type: "post",
            url: "create_intent",
            data: data,
            success: function (response) {
                console.log(response)
            }
        });
    });
}

function create_inent(){
}