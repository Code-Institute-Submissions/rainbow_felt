// Declare variables
var googleURL = 'https://maps.googleapis.com/maps/api/geocode/json?address=';
var googleAPIKey = 'AIzaSyBIpj0RtXIJuK4y0Cvd5TWIFhjpxAx9Qgk';

// Add button to form page loads and change css to accommodate
$(document).ready(function(){
    $('#id_postcode')
        .css("width", "50%")
        .parent()
        .append("<button type='button' onclick='lookup()'>Lookup address</button>")
        .css({"display": "flex", "justify-content": "space-between"});
});

// When button clicked lookup address
function lookup() {
    var input = $('#id_postcode').val(); // Get user input
    var requestURL = googleURL + input + '&key=' + googleAPIKey; // Create API request URL
    var postcodeReg = /^[a-z]{1,2}\d\d?\s*\d[a-z]{2}$/i; // Regular expression to validate UK postcode

    // Test if postcode is valid
    if(postcodeReg.test(input)){
        // AJAX request to API
        $.ajax({
            url: requestURL,
            dataType: 'json',
            // If AJAX request successful, check status is OK
            success: function(data){
                if(data.status === "OK"){
                    for(i=0; i < data.results[0].address_components.length; i++){   // Loop to search JSON for wanted fields
                        if(data.results[0].address_components[i].types[0] == "route"){
                            $('#id_street').val(data.results[0].address_components[i].long_name);   // Set street name
                        } else if(data.results[0].address_components[i].types[0] == "postal_town"){
                            $('#id_city').val(data.results[0].address_components[i].long_name); // Set city name
                        }
                    }
                // Fail message if status != OK
                } else {
                    alert('We were unable to lookup your postcode at this time')
                }
            },
            // If AJAX request unsuccessful display error message
            fail: function(data){
                alert('Address lookup was unsuccessful')
            }
        });

    // If postcode not valid display alert message
    } else {
        alert('Please enter a valid UK postcode')
    }

}


