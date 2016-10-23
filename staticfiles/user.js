// Initialize Firebase
var config = {
  apiKey: "AIzaSyC4kx_wrJwyfeQPB1FfQDSy7d7RD0IkhUI",
  messagingSenderId: "190598361806"
};
firebase.initializeApp(config);

const messaging = firebase.messaging();

messaging.requestPermission()
  .then(function() {
    console.log('Notification permission granted.');

    messaging.getToken()
      .then(function(currentToken) {
        console.log(currentToken);
        document.getElementById('push-notification').textContent = currentToken;
      })
      .catch(function(err) {
        console.log('An error occurred while retrieving token. ', err);
      });
  })
  .catch(function(err) {
    console.log('Unable to get permission to notify. ', err);
  });

messaging.onMessage(function(payload) {
  console.log("Message received. ", payload);
  document.getElementById('push-notification').textContent = payload.notification.title;
});
