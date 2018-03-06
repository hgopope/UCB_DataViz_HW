// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
var $date_timeInput = document.querySelector("#datetime");
var $cityInput = document.querySelector("#city");
var $state1Input = document.querySelector("#state");
var $countryInput = document.querySelector("#country");
var $shapeInput = document.querySelector("#shape");
// var $commentsInput = document.querySelector("#comments");

var $searchBtn = document.querySelector("#search");

// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener("click", handleSearchButtonClick);

// Set filteredAddresses to addressData initially
var filteredAddresses = addressData;

// renderTable renders the filteredAddresses to the tbody
function renderTable() {
  $tbody.innerHTML = "";
  for (var i = 0; i < filteredAddresses.length; i++) {
    // Get get the current address object and its fields
    var address = filteredAddresses[i];
    var fields = Object.keys(address);
    // Create a new row in the tbody, set the index to be i + startingIndex
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < 50; j++) {
      // For every field in the address object, create a new cell at set its inner text to be the current value at the current address's field
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = address[field];
    }
  }
}

function handleSearchButtonClick() {
  // Format the user's search by removing leading and trailing whitespace, lowercase the string
  var filterDate_Time = $date_timeInput.value.trim().toLowerCase();
  var filterCity = $cityInput.value.trim().toLowerCase();
  var filterState1 = $state1Input.value.trim().toLowerCase();
  var filterCountry = $countryInput.value.trim().toLowerCase();
  var filterShape = $shapeInput.value.trim().toLowerCase();
  // var filterComments = $commentsInput.value.trim().toLowerCase();
  
  
  // Set filteredAddresses to an array of all addresses whose "state" matches the filter
  filteredAddresses = addressData.filter(function(address) {
    var addressDate_Time = address.datetime.substring(0, filterDate_Time.length).toLowerCase();
    var addressCity = address.city.substring(0, filterCity.length).toLowerCase();
    var addressState1 = address.state.substring(0, filterState1.length).toLowerCase();
    var addressCountry = address.country.substring(0, filterCountry.length).toLowerCase();
    var addressShape = address.shape.substring(0, filterShape.length).toLowerCase();
    // var addressComments = address.comments.substring(0, filterComments.length).toLowerCase();
    
    
    if (addressDate_Time === filterDate_Time && addressCity === filterCity && addressState1 === filterState1 && addressCountry === filterCountry && addressShape === filterShape) {

      return true;
    }
    return false;
  });
  renderTable();
}

// Render the table for the first time on page load
renderTable();
