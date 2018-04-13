$(document).ready(function(){
    $('#productsform').submit(function( event ) {
        event.preventDefault();
        $.ajax({
            data : {
                searchItem : $('#inputProduct').val()
            },
            type : 'POST',
            url : '/getproducts'
        })
        .done(function(productdata){
            table = $('#listProducts').DataTable( {
                data: productdata,
                columns: [
                    { data: "subscribed" },
                    { data: "name" },
                    { data: "price" },
                    { data : "image",
                        "render": function(data, type, full, meta) {
                        return '<img src="' + data + '" alt="' + data + '">';} 
                    },
                    { data: 'subscribed',
                        "render": function(data, type, full, meta){
                            if(type === 'display' && data == 'Yes'){
                                data = '<button id="sub" class="btn btn-danger">Unsubscribe</button>';
                            } else {
                                data = '<button id="sub" class="btn btn-success">Subscribe</button>';
                            }
                        return data;
                     }
                    }
                ],
            });
            table.destroy();
        })
      });

      //Subscribe to product
    $('#listProducts').on('click', '#sub', function (e) {
        e.preventDefault();
 
        var rowData = table.row( $(this).parents('tr') ).data();
        
        $.ajax({
            data: {
                id: rowData['id'],
                name: rowData['name'],
                price: rowData['price'],
                image: rowData['image'],
                subscribed: rowData['subscribed']
            },
            type: 'POST',
            url: '/subscribe',
            success: function(response) {
                $.ajax({
                    data : {
                        searchItem : $('#inputProduct').val()
                    },
                    type : 'POST',
                    url : '/getproducts'
                }).done(function(productdatanew){
                    table = $('#listProducts').DataTable( {
                        data: productdatanew,
                        columns: [
                            { data: "subscribed" },
                            { data: "name" },
                            { data: "price" },
                            { data : "image",
                                "render": function(data, type, full, meta) {
                                return '<img src="' + data + '" alt="' + data + '">';} 
                            },
                            { data: 'subscribed',
                                "render": function(data, type, full, meta){
                                    if(type === 'display' && data == 'Yes'){
                                        data = '<button id="sub" class="btn btn-danger">Unsubscribe</button>';
                                    } else {
                                        data = '<button id="sub" class="btn btn-success">Subscribe</button>';
                                    }
                                return data;
                             }
                            }
                        ],
                    });
                    table.destroy();
                });
            }
        });
    });
});