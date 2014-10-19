var b = require('bonescript');
b.pinMode('P8_11', b.INPUT);
b.digitalRead('P8_11', printStatus);
function printStatus(x) {
    console.log('x.value = ' + x.value);
    console.log('x.err = ' + x.err);
}
