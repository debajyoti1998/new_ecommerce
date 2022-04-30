$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

// $('.remove-cart').click(async function() {
//     var id = $(this).attr('pid');
//     console.log(id)
// })






$('.plus-cart').click(async function(){
    try{
        // var myModal = new bootstrap.Modal(document.getElementById('exampleModal'), {keyboard: false})
        var id=$(this).attr("pid");
        var quantity_a = document.getElementById("quantity_"+ id).innerHTML
        var amount_b = document.getElementById("amount").innerHTML
        var totalamount_c = document.getElementById("totalamount").innerHTML
        console.log(id)
        console.log("quantity_"+ id)

        var response = await axios.get(`/pluscart/${id}`)
        //console.log(response)
        
        if(response.status == 200 && response.data && response.data.product_price)  {
            
            document.getElementById("quantity_"+ id).innerHTML = parseInt(quantity_a) +1
            document.getElementById("amount").innerHTML = parseFloat(amount_b)+ parseFloat(response.data.product_price)
            document.getElementById("totalamount").innerHTML = parseFloat(totalamount_c)+ parseFloat(response.data.product_price)
        }
        else{
            myModal.show()
        }
        
    }
    catch( err){
        console.log(err)
        myModal.show()
        // document.getElementById("amount").innerHTML = "-"
        // document.getElementById("totalamount").innerHTML = "-" 
    }
    
    
})




$('.minus-cart').click(async function(){
    try{
        // var myModal = new bootstrap.Modal(document.getElementById('exampleModal'), {keyboard: false})
        var id=$(this).attr("pid");
        var quantity_a = document.getElementById("quantity_"+ id).innerHTML
        var amount_b = document.getElementById("amount").innerHTML
        var totalamount_c = document.getElementById("totalamount").innerHTML
        console.log(quantity_a)
        console.log(amount_b)


        var response = await axios.get(`/minuscart/${id}`)
        //console.log(response)
        
        if(response.status == 200 && response.data && response.data.product_price)  {
            
            document.getElementById("quantity_"+ id).innerHTML = parseInt(quantity_a) -1
            document.getElementById("amount").innerHTML = parseFloat(amount_b)- parseFloat(response.data.product_price)
            document.getElementById("totalamount").innerHTML = parseFloat(totalamount_c)- parseFloat(response.data.product_price)
        }
        // else{
        //     myModal.show()
        // }
        
    }
    catch( err){
        console.log(err)
        // myModal.show()
        // document.getElementById("amount").innerHTML = "-"
        // document.getElementById("totalamount").innerHTML = "-" 
    }
    
    
})



// --------------ajex----------------
// $('.plus-cart').click(function(){
//     var id=$(this).attr("pid").toString();
//     $ajex({
//         type:"GET",
//         url:"/pluscart",
//         data:{
//             prod_id:id
//         },
//         success:function(data){
//             console.log(data)
//             console.log("success")
//         }
//     })
// })
// ----------------end-------------




$('.remove-cart').click( async function() {
    try{
        var id = $(this).attr('pid');
        var response = await axios.get(`/removecart/${id}`)
        var quantity_a = document.getElementById("quantity_"+ id).innerHTML
        var amount_b = document.getElementById("amount").innerHTML
        var totalamount_c = document.getElementById("totalamount").innerHTML

        // var id = '1'
        // var response = await axios.get(`http://fakeapi.jsonparseronline.com/posts/${id}`)


        // var data ={
        //     product_name :"vcgvdgch",
        //     product_rate:"100"
        // }
        // var response = await axios.post(`http://fakeapi.jsonparseronline.com/posts/`,data)
        console.log(response)
       
        if(response.status == 200 && response.data && response.data.product_price)  {
           document.getElementById("amount").innerHTML =  totalamount_c-(quantity_a*response.data.product_price)
           document.getElementById("totalamount").innerHTML = totalamount_c-(quantity_a*response.data.product_price)
        }
        else{
            document.getElementById("amount").innerHTML = "-"
            document.getElementById("totalamount").innerHTML = "-"  
        }
    }
    catch(err){
        console.log(err)
        document.getElementById("amount").innerHTML = "-"
        document.getElementById("totalamount").innerHTML = '-' 
    }
    
})