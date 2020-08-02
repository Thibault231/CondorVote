$("#form_candidate").submit(function (event) {
    event.preventDefault();
    var donnees = $(this).serialize();
            $.ajax({
                type: 'POST',
                url: $(this).attr('action'),
                data: donnees,

                success: function(data) {
                    var resp = $.parseJSON(data);
                    $('#message').text(resp.message);
                    $('#number_cand').empty().text('Votre bureau compte actuellement '+resp.number_candidate+' candidats');
                },
                error: function(resultat, status, erreur) {
                    alert(resultat + status + erreur);
                }
            });
            return false;

});