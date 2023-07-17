// Create a client instance
client = new Paho.MQTT.Client("seal.local", 9001, "client_id");
//Example client = new Paho.MQTT.Client("m11.cloudmqtt.com", 32903, "web_" + parseInt(Math.random() * 100, 10));

// set callback handlers
client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;
var options = {
  useSSL: false,
//   userName: "username",
//   password: "password",
  onSuccess:onConnect,
  onFailure:doFail
}

// connect the client
client.connect(options);

// called when the client connects
function onConnect() {
  // Once a connection has been made, make a subscription and send a message.
  console.log("onConnect");
  client.subscribe("aaa");
//   message = new Paho.MQTT.Message("Hello CloudMQTT");
//   message.destinationName = "/cloudmqtt";
//   client.send(message);
}

function send(text) {
  message = new Paho.MQTT.Message(text);
  message.destinationName = "bbb";
  client.send(message);
}

function doFail(e){
  console.log(e);
}

// called when the client loses its connection
function onConnectionLost(responseObject) {
  if (responseObject.errorCode !== 0) {
    console.log("onConnectionLost:"+responseObject.errorMessage);
  }
}

// called when a message arrives
function onMessageArrived(message) {
  document.getElementById("msg").innerHTML = message.payloadString;
}

window.addEventListener("load", function() {
    var bn = document.getElementById("send");
    bn.addEventListener("click", function() {
        send(document.getElementById('text').value);
    });    
});