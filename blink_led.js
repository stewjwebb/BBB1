var b = require('bonescript');
var led0 = "USR0";
var led1 = "USR1";
var led2 = "USR2";
var led3 = "USR3";
var state = 0;

b.pinMode(led0, 'out');
b.pinMode(led1, 'out');
b.pinMode(led2, 'out');
b.pinMode(led3, 'out');
toggleLED = function() {
    console.log('state %d', state);
    state = state ? 0 : 1;
    //state =  0;
    b.digitalWrite(led0, state);
 //b.digitalWrite(led1, state);
    b.digitalWrite(led2, state);
   //b.digitalWrite(led3, state);
};

console.log("test");

timer = setInterval(toggleLED, 100);

stopTimer = function() {
    clearInterval(timer);
};

setTimeout(stopTimer, 3000);
