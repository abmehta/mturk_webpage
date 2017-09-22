//To place a border around selected image

ims = document.getElementsByTagName("img");
for( i=0 ; i<ims.length ; i++ ){
  ims[i].onclick=function() {
    if (this.className == "clicked") {
      this.className = "";
    } else {
      this.className = "clicked";
    }
  };
}

