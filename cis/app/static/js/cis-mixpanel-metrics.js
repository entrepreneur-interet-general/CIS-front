

//////////////////////////////////////////////////////
// METRICS - GLOBAL

// MP METRICS - LOGO HOME
$("#logo_home").on('click', function() {
	// console.log("send metric - logo_home") ; 
	mixpanel.track("logo_home");
});

// MP METRICS - LOGIN
$("#btn_login").on('click', function() {
	// console.log("send metric - login") ; 
	mixpanel.track("login login");
});

// MP METRICS - LOGIN LANDING
$("#btn_login_landing").on('click', function() {
	// console.log("send metric - login_landing") ; 
	mixpanel.track("login login_landing");
});


// MP METRICS - REGISTER
$("#btn_register").on('click', function() {
	// console.log("send metric - register") ; 
	mixpanel.track("register register");
});

// MP METRICS - REGISTER LANDING
$("#btn_register_landing").on('click', function() {
	// console.log("send metric - register_landing") ; 
	mixpanel.track("register register_landing");
});


// MP METRICS - LOGOUT
$("#btn_logout").on('click', function() {
	// console.log("send metric - logout") ; 
	mixpanel.track("logout");
});

// MP METRICS - MAILTO_NAVBAR
$("#btn_mailto_navbar").on('click', function() {
	// console.log("send metric - mailto_navbar") ; 
	mixpanel.track("mailto navbar");
});

// MP METRICS - MAILTO_FOOTER
$("#btn_mailto_footer").on('click', function() {
	// console.log("send metric - mailto_footer") ; 
	mixpanel.track("mailto footer");
});

// MP METRICS - NEWSLETTER
$("#mc-embedded-subscribe").on('click', function() {
	// console.log("send metric - newsletter") ; 
	mixpanel.track("mailto newsletter");
});

// MP METRICS - CIS_FACEBOOK
$("#btn_cis_facebook").on('click', function() {
	// console.log("send metric - cis_facebook") ; 
	mixpanel.track("cis_facebook");
});

// MP METRICS - CIS_TWITTER
$("#btn_cis_twitter").on('click', function() {
	// console.log("send metric - cis_twitter") ; 
	mixpanel.track("cis_twitter");
});


//////////////////////////////////////////////////////
// METRICS - SEARCH

// MP METRICS - SHUFFLE
$("#btn_shuffle").on('click', function() {
	// console.log("send metric - shuffle") ; 
	mixpanel.track("search shuffle");
});

// MP METRICS - SEARCH INPUT - ENTER
// TO DO 