// Prototype method

Element.prototype.hasClass = function(a) {
	return new RegExp("(?:^|\\s+)" + a + "(?:\\s+|$)").test(this.className);
};

Element.prototype.addClass = function(a) {
	if (!this.hasClass(a)) {
		this.className = [this.className, a].join(" ");
	}
};

Element.prototype.removeClass = function(b) {
	if (this.hasClass(b)) {
		var a = this.className;
		this.className = a.replace(new RegExp("(?:^|\\s+)" + b + "(?:\\s+|$)", "g"), " ");
	}
};

Element.prototype.toggleClass = function(a) {
	this[this.hasClass(a) ? "removeClass" : "addClass"](a);
};

// Navbar sticky

var nav = document.querySelector('nav');
nav.position = Number(nav.offsetTop);
var header = document.querySelector('.home-header');

document.onscroll = function(e) {
  posScroll = (document.querySelector('body').scrollTop != 0) ? document.querySelector('body').scrollTop : document.querySelector('html').scrollTop;
  if (posScroll>=nav.position) {
    nav.addClass("fixed");
    header.style.marginBottom = nav.offsetHeight + 20;
  }else{
    nav.removeClass("fixed");
    header.style.marginBottom = "";
  }
}
