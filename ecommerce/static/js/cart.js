var updateBtns = document.getElementsByClassName('update-cart');
for (i = 0 ; i < updateBtns.length ; i++) {
    updateBtns[i].addEventListener('click', function (){
       var productId = this.dataset.product;
       var action = this.dataset.action;
       if (user === 'AnonymousUser') {

       } else {
           updateOrder(productId, action);
       }
    });
}

function updateOrder(productId, action) {
    var url ='/update_item/';
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({productId, action})
    }).then((response) => {
        return response.json();
    }).then(res => {
        console.log(res);
        location.reload();
    })
}