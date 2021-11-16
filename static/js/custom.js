
// JQuery For Multistep Profile Form
$('#tab1').show();
  function Nexttab(n){
    if(n==2){
      $('.progress-bar').css("width","50%");
      $('.step').eq(1).addClass("active");
      $('#tab1').hide();
      $('#tab3').hide();
      $('#tab2').show();
    }
    if(n==3){
      $('.progress-bar').css("width","100%");
      $('.step').eq(2).addClass("active");
      $('#tab1').hide();
      $('#tab3').show();
      $('#tab2').hide();
    }
  }
  function Prevtab(n){
    if(n==1){
      $('.progress-bar').css("width","0%");
      $('.step').eq(1).removeClass("active");
      $('#tab1').show();
      $('#tab3').hide();
      $('#tab2').hide();
    }
    if(n==2){
      $('.progress-bar').css("width","50%");
      $('.step').eq(2).removeClass("active");
      $('#tab1').hide();
      $('#tab3').hide();
      $('#tab2').show();
    }
  }
  function submit_form(){
    $('.progress').hide();
    $('#tab3').hide();
    $('#all-steps').hide();
    $('#text-message').show();
    $('#profile-form').submit();
  }