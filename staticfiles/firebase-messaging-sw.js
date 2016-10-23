importScripts('https://www.gstatic.com/firebasejs/3.5.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.5.0/firebase-messaging.js');

var config = {
  apiKey: "AIzaSyC4kx_wrJwyfeQPB1FfQDSy7d7RD0IkhUI",
  messagingSenderId: "190598361806"
};
firebase.initializeApp(config);

const messaging = firebase.messaging();
