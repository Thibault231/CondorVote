$( document ).ready(function() {
    $(".addingc").click(function() {
        if ($("form").is(":visible")) {
            $(".formc").slideUp(250); 
        } else {
           $(".formc").slideDown(250);
           $(".addingc").css('cursor', 'default');
        }
     });
});

$( document ).ready(function() {
    $(".addingt").click(function() {
         if ($("form").is(":visible")) {
             $(".formt").slideUp(250); 
         } else {
            $(".formt").slideDown(250);
            $(".addingt").css('cursor', 'default');
         }
        
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

$("#form_adding_tickets").submit(function (event) {
    event.preventDefault();
    var donnees = $(this).serialize();
            $.ajax({
                type: 'POST',
                url: $(this).attr('action'),
                data: donnees,

                success: function(data) {
                    var resp = $.parseJSON(data);
                    alert(resp.message);
                },
                error: function(resultat, status, erreur) {
                    alert(resultat + status + erreur);
                }
            });
            return false;
});

$("#form_deleting_tickets").submit(function (event) {
    event.preventDefault();
    var donnees = $(this).serialize();
            $.ajax({
                type: 'POST',
                url: $(this).attr('action'),
                data: donnees,

                success: function(data) {
                    var resp = $.parseJSON(data);
                    alert(resp.message);
                },
                error: function(resultat, status, erreur) {
                    alert(resultat + status + erreur);
                }
            });
            return false;
});

$(".hide_tickets").click(function() {
    if ($("#ul_tickets").hasClass("visible")) {
        $("#ul_tickets").removeClass('visible').addClass('hidden');
    } else if ($("#ul_tickets").hasClass("hidden")) {
        $("#ul_tickets").removeClass('hidden').addClass('visible');
    };
});

$(".about-btn2").click(function() {
    $("#formular_desk").addClass('hidden');
    $("#end_add").addClass('hidden');
});