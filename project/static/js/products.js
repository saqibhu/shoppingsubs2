$(document).ready(function(){
    $('#productsform').submit(function( event ) {
        $.ajax({
            data : {
                searchItem : $('#inputProduct').val()
            },
            type : 'POST',
            url : '/getproducts'
        })
        .done(function(productdata){
            table = $('#listProducts').dataTable({
                destroy: true,
                data: productdata,
                columns: [
                    { data : 'name' }
                ]
            });
        })

        event.preventDefault();
      });
});