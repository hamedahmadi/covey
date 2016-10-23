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
        if (currentToken) {
          sendTokenToServer(currentToken);
          updateUIForPushEnabled(currentToken);
        } else {
          // Show permission request.
          console.log('No Instance ID token available. Request permission to generate one.');
          // Show permission UI.
          updateUIForPushPermissionRequired();
          setTokenSentToServer(false);
        }
        console.log(currentToken);
      })
      .catch(function(err) {
        console.log('An error occurred while retrieving token. ', err);
        //showToken('Error retrieving Instance ID token. ', err);
        //setTokenSentToServer(false);
      });
  })
  .catch(function(err) {
    console.log('Unable to get permission to notify. ', err);
  });

// Get Instance ID token. Initially this makes a network call, once retrieved
// subsequent calls to getToken will return from cache.

messaging.onMessage(function(payload) {
  console.log("Message received. ", payload);
});

console.log(messaging);
