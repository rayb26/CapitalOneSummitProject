/**
Author: Rayhan Biju
Version: October 27, 2021
Description: The file contains functionality to allow the client to
search through a list of values.
**/

/*
The following method has functionality to allow users to type a value
and each keystroke gets searched amongst the list of values.
*/
function search() {
$(document).ready(function(){
  $("#searchInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#myList li").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});
}
$(search);
