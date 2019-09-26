$(document).ready(function () {

    // DEFINICIÓN DE LOS BOTONES PARA LA DATATABLE
    try{
        var custom_buttons = custom_buttons;
    }catch(err){
        var custom_buttons = null;
    }
    var final_buttons;
    if(custom_buttons){
        final_buttons = custom_buttons;
    }else{
        final_buttons = [
            {
                extend: 'copy',
                text: 'Copiar'
            },
            {
                extend: 'csv',
                text: 'CSV'
            },
            {
                extend: 'excel',
                text: 'Excel'
            },
            {
                extend: 'pdf',
                text: 'PDF'
            },

            {
                extend: 'print',
                customize: function (win) {
                    $(win.document.body).addClass('white-bg');
                    $(win.document.body).css('font-size', '10px');

                    $(win.document.body).find('table')
                        .addClass('compact')
                        .css('font-size', 'inherit');
                },
                text: 'Imprimir'
            }
        ]
    }
    $("#datatable-rady").DataTable({
        dom: '<"html5buttons"B>lTfgitp',
        language: {
            "url": "//cdn.datatables.net/plug-ins/1.10.11/i18n/Spanish.json"
        },
        responsive: true,
        bAutoWidth: false,
        pageLength: 10,
        processing: true,
        buttons: final_buttons

    });
});