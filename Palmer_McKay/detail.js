console.log(DMP_CONTEXT.get())
$(function(context) {
    return function() {
        // Sets main image by hovering over thumnails
        $(".thumnail-img").mouseover(function(){
          $(".detail-img").attr("src", this.src)
        });


        // Set selected Category menu item to active
        let t = $(".categories:contains("+context.cat_name+")")
        t.children("li,ul").addClass("bolded");
        $("#all").removeClass("bolded");
    }
}(DMP_CONTEXT.get()))
