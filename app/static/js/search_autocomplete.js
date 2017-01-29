/**
 * Created by mould_000 on 9/3/2016.
 */


  $(function() {
    $( "#answer" ).autocomplete({
      source: availableTags,
      select: function(event, ui) {
    $("#answer").val(ui.item.value);
      }
    });
  });

   function getSub(){
    var response = document.getElementById('answer').value;
        location = '/r/'+response;
    return false;
       }


/**
  $(function() {
    var availableTags = [
        {% for sub in subreddits %}
            "{{ sub }}",
        {% endfor %}
    ];
    $( "#answer" ).autocomplete({
      source: availableTags,
      select: function(event, ui) {
    $("#answer").val(ui.item.value);
      }
    });
  });

   function getSub(){
    var response = document.getElementById('answer').value;
        location = '/r/'+response;
    return false;
}

**/