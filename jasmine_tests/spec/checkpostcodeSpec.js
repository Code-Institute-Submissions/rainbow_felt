describe("CheckPostcode", function(){

    checkPostcode = new CheckPostcode();

    describe('Check postcode validates correctly', function(){

        it('Should return true for valid postcode', function(){
           checkPostcode.check('ST3 1LW');
           expect(checkPostcode.valid).toBe(true);
        });

        it('Should return true for valid postcode with small letters', function(){
           checkPostcode.check('wr11 1ab');
           expect(checkPostcode.valid).toBe(true);
        });

        it('Should return true for valid postcode with small and capital letters', function(){
           checkPostcode.check('n11 3Rn');
           expect(checkPostcode.valid).toBe(true);
        });

        it('Should return true for valid postcode with no space', function(){
           checkPostcode.check('ST31LW');
           expect(checkPostcode.valid).toBe(true);
        });

        it('Should return false for postcode with too many numbers', function(){
           checkPostcode.check('ST34 41LW');
           expect(checkPostcode.valid).toBe(false);
        });

        it('Should return false for postcode with no numbers', function(){
           checkPostcode.check('ST LW');
           expect(checkPostcode.valid).toBe(false);
        });

        it('Should return false for postcode with too many letters', function(){
           checkPostcode.check('SOT3 1LW');
           expect(checkPostcode.valid).toBe(false);
        });

        it('Should return false for postcode with no letters', function(){
           checkPostcode.check('22002');
           expect(checkPostcode.valid).toBe(false);
        });

        it('Should return false for postcode in the wrong order', function(){
           checkPostcode.check('1LW ST3');
           expect(checkPostcode.valid).toBe(false);
        });

        it('Should return false for postcode with too few letters', function(){
           checkPostcode.check('ST3 1W');
           expect(checkPostcode.valid).toBe(false);
        });

        it('Should return false for postcode with too few numbers', function(){
           checkPostcode.check('ST3 LW');
           expect(checkPostcode.valid).toBe(false);
        });

    });

});