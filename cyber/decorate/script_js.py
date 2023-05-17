
js_back_to_up = """
function scrollToTop() {
    window.scrollTo(0, 0);
  }
"""

js_packages_space = """
  var divs = document.getElementsByClassName("packages");
  for (var i = 0; i < divs.length; i++) {
    var ps = divs[i].getElementsByTagName("p");
    for (var j = 0; j < ps.length; j++) {
      var p = ps[j];
      var text = p.textContent;
      text = text.replace(/\\n/g, "<br>");
      p.innerHTML = text;
    }
    }
"""

js_dir = {
    'js_back_to_up': js_back_to_up,
    'js_packages_space': js_packages_space
}
