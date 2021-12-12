$(document).ready(function(){
    const apiUrl = "http://localhost:8888/api/v1"
        $.postJSON = function(url, data, callback) {
            return jQuery.ajax({
                'type': 'POST',
                'url': url,
                'contentType': 'application/json',
                'data': JSON.stringify(data, " ", 2),
                'dataType': 'json',
                'success': callback
            });
        };

    function generateTable(){
        $.get(apiUrl+'/users/', function(data){
            let innerHtml = ""
            data.map( (element) => {
                innerHtml +=`<tr>
                <th scope=\"row\">${element.pk}</th>
                <td>${element.name}</td>
                <td>${element.email}</td>
                <td>${element.create_on}</td>
                </tr>`
            })
            $("#table-data").html(innerHtml)
        })
    }
    generateTable()


  $("#add").click(function(){

      const data = {
          email: $("#email").val(),
          name: $("#name").val(),
      }
      $.postJSON(apiUrl+'/users/', data)
          .done(function (data) {
              generateTable()
          })
          .fail(function (data) {
              if (data.responseJSON.detail){
                  let info = ""
                  data.responseJSON.detail.map( (error) => {
                      info += error.msg
                  } )
                  alert(info)
              } else {
              alert(data.responseJSON[0])
              }
          })
  });


  $("#clear").click(function(){
        const email = $("#email").val()
      if (email){
          $.ajax({
            url: apiUrl+`/users/email/${email}`,
            type: 'DELETE',
            success: function (data) {
              generateTable()
          }
        });
      } else {
          alert("Input email")
      }

  });

});
