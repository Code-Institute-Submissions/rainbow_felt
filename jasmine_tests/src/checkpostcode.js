CheckPostcode = function(){
};

CheckPostcode.prototype.check = function(postcode){
    var postcodeReg = /^[a-z]{1,2}\d\d?\s*\d[a-z]{2}$/i; // Regular expression to validate UK postcode
    this.valid = postcodeReg.test(postcode)
};