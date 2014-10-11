var b = require('bonescript');
b.pinMode("P8_13", b.OUTPUT, 7, 'pullup', 
 'fast', printStatus);
b.getPinMode("P8_13", printPinMux);
function printStatus(x) {
    console.log('value = ' + x.value);
    console.log('err = ' + x.err);
}
function printPinMux(x) {
    console.log('mux = ' + x.mux);
    console.log('pullup = ' + x.pullup);
    console.log('slew = ' + x.slew);
    console.log('options = ' + x.options.join(','));
    console.log('err = ' + x.err);
}
