$( document ).ready( function() {
    const fromHexString = hexString =>
    new Uint8Array(hexString.match(/.{1,2}/g).map(byte => parseInt(byte, 16)));
    
    const toHexString = bytes =>
    bytes.reduce((str, byte) => str + byte.toString(16).padStart(2, '0'), '');
    
    /* Our public key */
    let public_system = "1cccdad29902d2e60462184abef36df5f0d260dca16ef67376a2cfcbc190f117";
    let nonce = nacl.randomBytes(24);
    
    $('#chave').change(function() { 
       
       let fr=new FileReader();
       fr.onload=function(){
           let private = new Uint8Array(fr.result);
           var enc = new TextEncoder();
           let challenge = enc.encode(document.getElementById("challenge").value);
           
           let result = nacl.box(challenge, nonce, fromHexString(public_system), private);
           $("#challenge-answer").val(toHexString(nonce) + toHexString(result));
       }
       fr.readAsArrayBuffer(this.files[0]); 
    });
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

