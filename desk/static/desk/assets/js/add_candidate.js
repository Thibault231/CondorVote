$(document).ready(function(){ 
    $('#form_candidate').submit(function(event){
        $.ajax({
            data: $(this).serialize(),
            type: $(this).attr('POST'),
            url: $(this).attr('/candidate/add_candidates'),
            success: function(response) {
                var resp = $.parseJSON(data);
                $('#message').text(resp.message); 
            },
            error: function(e, x, r) { 
                $('#message').text('Erreur1');
            }
        });
        return false;
    });
});