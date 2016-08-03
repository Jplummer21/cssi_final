$(document).ready(function(){
  $("input[type='button']".click(function(){
    var userVal = $("input[name='user_type']:checked").val();
})
function submit_clicked(event){
  event.preventDefault();
  $ArtistPage.post(
    '/getartist',
    handle_response
  );

}
