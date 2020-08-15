function filterFunction() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  div = document.getElementById("myDropdown");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}



if (!window.x) {
    x = {};
}

x.Selector = {};
x.Selector.getSelected = function() {
    var t = '';
    if (window.getSelection) {
        t = window.getSelection();
    } else if (document.getSelection) {
        t = document.getSelection();
    } else if (document.selection) {
        t = document.selection.createRange().text;
    }
    return t;
}

$(document).ready(function() {
//    $(document).bind("mouseup", function() {
//        var mytext = x.Selector.getSelected();
////        alert(mytext);
//    });
//    var el
    $('.right_click').on('contextmenu', function(e) {
      console.log('in contextmenu')
      var top = e.pageY + 10;
      var left = e.pageX + 10;
//      el = $(this)
      $("#context-menu").css({
        display: "block",
        top: top,
        left: left
      }).addClass("show");
      return false; //blocks default Webbrowser right click menu
    }).on("click", function() {
      $("#context-menu").removeClass("show").hide();
      console.log('hide')
    });

    $("#context-menu a").on("click", function() {
      $("#context-menu").removeClass("show").hide();
      entity = x.Selector.getSelected()
//      el.parent().find('.entity').val(entity.toString())
      text_el = entity.anchorNode.wholeText
      pre_text = text_el.substring(0, entity.anchorOffset)
      mid_text = '<b style="color: #26ab95;">' + text_el.substring(entity.anchorOffset, entity.extentOffset) + '</b>'
      pos_text = text_el.substring(entity.extentOffset, text_el.length)
      console.log(pre_text)
      console.log(mid_text)
      console.log(pos_text)
      entity.focusNode.parentElement.innerHTML = (pre_text+mid_text+pos_text)
    });
});

