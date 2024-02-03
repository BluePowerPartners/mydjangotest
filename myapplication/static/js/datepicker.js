
$(document).ready(function(){
  var disableSpecificDates = ["10-1-2024"];
  var disableSpecificDates = document.getElementById("hiddenValue").value;

  $('#datepicker').datepicker({
      format: 'yyyy-mm-dd',
      multidate: true,
      startDate:'2024-01-01',
      daysOfWeekHighlighted: "0,6",
      endDate:'2024-01-31',
      autoclose: true,
                beforeShowDay: function (date) {
                    dmy = date.getDate() + "-" + (date.getMonth() + 1) + "-" + date.getFullYear();
                    if (disableSpecificDates.indexOf(dmy) != -1) {
                        return false;
                    } else {
                        return { classes: 'Highlighted' };
                    }
                }
  }).on('show', function(e){
      // Adjust the datepicker position
      // Get the dimensions of the input box
      var inputWidth = $('#datepicker').outerWidth();
      var inputHeight = $('#datepicker').outerHeight();

      // Calculate the position to place the datepicker in the middle or to the right
      var topPosition = $('#datepicker').offset().top + inputHeight;
      var leftPosition = $('#datepicker').offset().left + inputWidth / 2; // Change this line for right placement

      $('.datepicker').css({
          'top': topPosition,
          'left': leftPosition
      });
  });
});