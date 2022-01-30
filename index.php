    <?php include 'header.php' ?>
    <div class="main-wrapper">
      <h1 class="title">Your Orders:</h1>
      <div class="order-wrapper">
        <script>
          let xhr = new XMLHttpRequest;
          xhr.open('GET', 'https://sapstore.conuhacks.io/orders/byEmail?email=abbigail.kautzer.764458@test.com', true);
          xhr.onload = function() {
            if (this.status === 200) {
              var orders = JSON.parse(this.responseText);
              for (var i = 0; i < orders.length; i++) {
                var products = "";
                for (var j = 0; j < orders[i]["orderEntries"].length; j++) {
                  products += "<p>" + orders[i]["orderEntries"][j]["productName"]; "</p>";
                  products += "<p>" + orders[i]["orderEntries"][j]["quantity"]; "</p>";
                  products += "<p>$" + orders[i]["orderEntries"][j]["totalEntryPrice"]; "</p>";
                }
                var url = window.location.href;
                var order =
                `<div class="order" onclick="location.href = '`+ url + `order?=` + orders[i]["orderId"] + `';">
                  <div class="order-id">
                    <h3>Order ID:</h3>
                    <p>` + orders[i]["orderId"] + `</p>
                  </div>
                  <div class="prep-time">
                    <h3>Preparation Time:</h3>
                    <p>` + orders[i]["preparationTime"] + `</p>
                  </div>
                  <div class="size">
                    <h3>Parcel Size:</h3>
                    <p>` + orders[i]["parcelSize"] + `</p>
                  </div>
                  <div class="order-entries">
                    <h3>Product</h3>
                    <h3>Quantity</h3>
                    <h3>Price</h3>`
                    + products +
                `</div>`;
                $(".order-wrapper").prepend(order);
              }
            }
          }
          xhr.send();
        </script>
      </div>
    </div>
  </body>
</html>
