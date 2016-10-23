importScripts('https://www.gstatic.com/firebasejs/3.5.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.5.0/firebase-messaging.js');

var config = {
  apiKey: "AIzaSyC4kx_wrJwyfeQPB1FfQDSy7d7RD0IkhUI",
  authDomain: "covey-4b152.firebaseapp.com",
  databaseURL: "https://covey-4b152.firebaseio.com",
  storageBucket: "covey-4b152.appspot.com",
  messagingSenderId: "190598361806"
};
firebase.initializeApp(config);

const messaging = firebase.messaging();
