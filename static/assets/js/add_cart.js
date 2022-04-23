//console.log('ok1111')
let add_cart,add_cart_id,product_choose,product_id

add_cart = document.querySelectorAll("#add-cart");
add_cart_id = document.querySelectorAll("#add-cart-id");

 

product_choose = []
//product_choose.push(username)
for (let index = 0; index < add_cart.length; ++index) {
    
    add_cart[index].addEventListener('click', e => {
        product_id = add_cart_id[index].innerText
    
        product_choose.push(product_id)
        product_choose = [...new Set(product_choose)]
        //console.log('product_choose',product_choose)
        send_cart = document.getElementsByName("send_cart")[0].value = product_choose
        console.log('send_cart',send_cart)
        //valide_cart(data)
    });
}
/*** 
var valide_cart = (data) => {
    e = data
    $(document).ready(function (e) {
        e_1 = e
        $("#valid-cart").submit(function (event,e_1) {
          event.preventDefault();
          e_2 = e_1
          $.ajax({
            type: "POST",
            url: "/add_cart/",
            data: e_2,
            success: function () {
              $('#message').html("<h2>Cart data send </h2>")
            }
          });
          return false;
        });
      });

}
*/