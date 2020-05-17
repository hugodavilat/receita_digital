$( document ).ready( function() {

    // Botão de dismiss
    $('.del-medicamento').click(function() {
        $(this).closest('.card-body').fadeOut('slow', function() {
            $(this).remove();
        });
    });

    // Autocomplete
    var availableTags = [];
    $('#medicamento').keyup(function() {
        var nome_do_medicamento = $(this).val();

        request = $.ajax({
            url: '/ajax/procurar-medicamento',
            type: 'get',
            data: {
                'nome': nome_do_medicamento
            },
            dataType: 'json',
            success: function(data) {
                availableTags = data.nomes;
                $('#medicamento').autocomplete({
                    source: availableTags
                  });
            }
        });
    });

    // Adicionar medicamento
    $('#add-medicamento').click(function() {
        var div_drugs_list = $("#lista-medicamentos")
        var div_new_drug = $('<div>').attr({class: 'card-body'})
        div_new_drug.append(
            $('<span>').attr({
                class: 'del-medicamento float-right'
            }).html('&times;')
        );
        div_new_drug.append(
            $('<input>').attr({
                class: 'medicamento-adicionado',
                name: 'medicamentos',
                value:  $('#medicamento').val(),
                readonly: true
            })
        );
        div_new_drug.append(
            $('<input>').attr({
                class: 'posologias',
                name: 'posologias',
                placeholder: 'Posologia',
                required: true
            })
        );
        div_drugs_list.append(div_new_drug);
        $('#medicamento').val("");
        $('.del-medicamento').click(function() {
            $(this).closest('.card-body').fadeOut('slow', function() {
                $(this).remove();
            });
        });
    });

});

