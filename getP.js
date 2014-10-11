var b = require('bonescript');
b.getPlatform(printData);
function printData(x) {
    console.log('name = ' + x.name);
    console.log('version = ' + x.version);
    console.log('serialNumber = ' + x.serialNumber);
    console.log('bonescript = ' + x.bonescript);
}
