var b = require('bonescript');
b.pinMode('USR0', b.OUTPUT);
b.pinMode('USR1', b.OUTPUT);
b.pinMode('USR2', b.OUTPUT);
b.pinMode('USR3', b.OUTPUT);
b.digitalWrite('USR0', b.LOW);
b.digitalWrite('USR1', b.LOW);
b.digitalWrite('USR2', b.LOW);
b.digitalWrite('USR3', b.LOW);
	
toggleLED = function() {
    console.log('doing nothing');
b.pinMode('USR0', b.OUTPUT);
b.pinMode('USR1', b.OUTPUT);
b.pinMode('USR2', b.OUTPUT);
b.pinMode('USR3', b.OUTPUT);
b.digitalWrite('USR0', b.LOW);
b.digitalWrite('USR1', b.LOW);
b.digitalWrite('USR2', b.LOW);
b.digitalWrite('USR3', b.LOW);
};
setTimeout(toggleLED, 2000);
//setTimeout(restore, 2000);

