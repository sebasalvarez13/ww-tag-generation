function openPage(event, pageName){
    //Declare all variables
    var i, pagecontent, pagelinks;
  
    //Get all elements with class="tabcontent" and hide them
    pagecontent = document.getElementsByClassName("pagecontent");
    for(i = 0; i < pagecontent.length; i++){
        pagecontent[i].style.display = "none";
    }
  
    //Get all elements with class="tablinks" and remove the class "active"
    pagelinks = document.getElementsByClassName("pagelinks");
    for(i = 0; i < pagelinks.length; i++){
        pagelinks[i].className = pagelinks[i].className.replace("active", "");
    }
  
    //Show the current tab and add an "active" class to the button that opened the tab
    document.getElementById(pageName).style.display = "block";
    evt.currentTarget.className += "active";
  }