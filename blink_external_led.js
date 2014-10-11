var b = require('bonescript');
var led = "P8_13";

var state = 0;
b.pinMode(led, 'out');

toggleLED = function() {
    console.log('state %d', state);
    state = state ? 0 : 1;
    //state =  0;
    b.digitalWrite(led, state);
};

console.log("test");

timer = setInterval(toggleLED, 100);

stopTimer = function() {
    clearInterval(timer);
};

setTimeout(stopTimer, 3000);
