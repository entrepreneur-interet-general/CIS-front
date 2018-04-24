# -*- encoding: utf-8 -*-

from .. import log_cis, pformat

print
log_cis.info(">>> reading settings.app_settings.py ")


### vars for name application / metas
app_metas = {
	
	"title"			: u"carrefour des innovations sociales", ### dataioio.com | coralcommons.com/io | tadata.io | coraless.io | solidata.io
	"subtitle"		: u"le moteur de recherche des innovations sociales",
	"version"		: u"v.0.1 beta",
	"description"	: u"Le Carrefour des innovations sociales regroupe les innovations sociales recensées et actualisées par des partenaires experts. ",
	"authors"		: u"Julien Paris - jpylab.com",
	"licence"		: u"MIT",

	"refresh_page"	: 1800, # refresh/reload page every n seconds : f.e. 1800 s == every 30 min
	
	"keywords"		: u"""
		ESS,économie sociale et solidaire,innovation sociale,
		dataviz,data visualisation,data visualization,SIG,
		France,
		commons,digital commons,API,OpenScraper,Open Scraper,
		opensource,open source,open data,opendata,MIT licence,github,
		JS,javascript,python,flask,HTML,CSS,JSON,bulma,Vue.js,
		Etalab,CGET,Fonda,
		""",
	
	"crisp_id"		: {
		u"cis" : "TO DO", 
		},
	
	"mixpanel_id" 	: {   
		u'production'	: "TO DO ",    ### for production metrics  / mixpanel account : carrefour
		u'default'		: "TO DO"      ### for development metrics / mixpanel account : jparis.py
		},
}

