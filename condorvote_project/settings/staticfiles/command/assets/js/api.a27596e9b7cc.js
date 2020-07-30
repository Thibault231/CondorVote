// API
 $(document).on('click','.add_candidate', function(e){
    e.preventDefault();
    alert('ok ok ok ok ok');
    var desk_id = $('#desk_id').val();

    $.post( "/api/add_candidates/", {desk_id: desk_id}, function(data){
        var resp = $.parseJSON(data);
        if (resp.success){
            $('#message').text(resp.message);
        } else {
            $('#message').text('Error');
        };
    }); 
  });