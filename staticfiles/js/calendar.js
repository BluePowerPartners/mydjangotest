$(document).ready(function() {
    var eventshid = document.getElementById("hiddenJson").value;
    console.log(eventshid);
    $('#calendar').fullCalendar({
      header: {
        left: 'prev,next today',
        center: 'title',
        right: 'month,basicWeek,basicDay'
      },
      defaultDate: '2024-02-03',
      navLinks: false, // can click day/week names to navigate views
      editable: false,
      eventLimit: false, // allow "more" link when too many events
      events: [
        {
          title: 'All Day Event',
          start: '2024-02-02'
        },
        {
          title: 'Long Event',
          start: '2024-02-03', color: 'red'
        },
      ]
    });
    
  });