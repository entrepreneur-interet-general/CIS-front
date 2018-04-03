# -*- encoding: utf-8 -*-

from .. import log_cis, pformat

print
log_cis.info(">>> reading settings.app_settings.py ")


### vars for name application / metas
app_metas = {
	"title"			: u"carrefour des innovations sociales", ### dataioio.com | coralcommons.com/io | tadata.io | coraless.io | solidata.io
	"subtitle"		: u"TO DO : tagline",
	"version"		: u"v.0.1 beta",
	"description"	: u"TO DO : long tagline",
	"authors"		: u"Julien Paris",
	"licence"		: u"MIT",
	"metas"			: u"""
		ESS,économie sociale et solidaire,innovation sociale,
		dataviz,data visualisation,data visualization,graph,SIG,France,
		commons,digital commons,
		opensource,open source,open data,creative commons,github,
		JS,javascript,python,flask,HTML,CSS,JSON,bulma
		""",
	"crisp_id"		: {
		u"cis" : "TO DO", 
		},
	"mixpanel_id" 	: {   
		u'production'	: "TO DO ",    ### for production metrics  / mixpanel account : solidata.info
		u'default'		: "TO DO"      ### for development metrics / mixpanel account : jparis.py
		},
	}