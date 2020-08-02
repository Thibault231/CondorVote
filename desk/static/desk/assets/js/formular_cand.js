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
    event.preventDefault();
    var donnees = $(this).serialize();
            $.ajax({
                type: 'POST',
                url: $(this).attr('action'),
                data: donnees,

                success: function(data) {
                    var resp = $.parseJSON(data);
                    $("#cand_list").append($("<li style='list-style-type: none;'>").html('<h4><i class="bx bx-face"></i>'+resp.message+'</h4>'));
                },
                error: function(resultat, status, erreur) {
                    alert(resultat + status + erreur);
                }
            });
            return false;
});