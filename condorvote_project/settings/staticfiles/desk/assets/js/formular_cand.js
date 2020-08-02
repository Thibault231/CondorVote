$( document ).ready(function() {
    $(".addingc").click(function() {
         $("form").slideDown(250);
         // if form is visible
         if ($("form").is(":visible")) {
             // change .addingc cursor to default
             $(".addingc").css('cursor', 'default');
         }
         $("#email").focus();
     });
});

$("#form_cand").submit(function (event) {
    alert('OK1!')
    event.preventDefault();
    var donnees = $(this).serialize();
    alert('OK!')
            $.ajax({
                type: 'POST',
                url: $(this).attr('action'),
                data: donnees,

                success: function(data) {
                    var resp = $.parseJSON(data);
                    alert(resp.message)
                },
                error: function(resultat, status, erreur) {
                    alert(resultat + status + erreur);
                }
            });
            return false;
});

