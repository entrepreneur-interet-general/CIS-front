# -*- encoding: utf-8 -*-


### TO DO : MULTI LANGUAGE FOR ALL CHOICES 

### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### CHOICES ONLY FOR ADMIN
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

CHOICES_AUTH_LEVEL					= [	(u"visitor"			, u"visiteur"),
										(u"user"			, u"utilisateur"),
										(u"staff"			, u"membre du collectif"),
										(u"admin"			, u"administrateur"),
									]

CHOICES_VERIFY_USER_IS_PARTNER 		= [ (u"yes" 	, "user is really a partner"),
										(u"no"		, "user is not a partner"),
										(u"VERIFY"	, "VERIFY if user is really a partner")
									]
CHOICES_VERIFY_USER_IS_PARTNER_LIST = [ i[0] for i in CHOICES_VERIFY_USER_IS_PARTNER ]

### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### CHOICES FOR USERS
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

# CHOICES_DATA_TYPES			= [	(u"data_company"	, u"données sur votre structure"),
# 								(u"data_network"	, u"données sur vos réseaux"  ),
# 								(u"data_activity"	, u"données sur une de vos activités"),
# 								(u"data_people"		, u"données sur une des personnes travaillant dans votre structure"),
# 							]

# CHOICES_NETWORKS			= [	(u"network_up"		, u"structures auxquelles j'adhère"),
# 								(u"network_flat"	, u"structures avec qui je travaille"),
# 								(u"network_down"	, u"structures de mon propre réseau"),
# 							]

CHOICES_PROFILES			= [	(u""				, u" - sélectionnez votre profil de métier-"),

								(u""				, u" - "  ),
								(u"helper"			, u"Accompagnateur.trice"),
								(u"analyst"			, u"Analyste"),
								(u"financer"		, u"Financeur.euse"),
								(u"observer"		, u"Observateur.trice"),
								(u"project_holder"	, u"Porteur.euse de projet"),

								(u""				, u" - "  ),
								# (u""				, u" * * *"),
								(u"citizen"			, u"Citoyen.ne"),
								(u"other"			, u"Autre profil métier"),
							]

CHOICES_STRUCTURE_PROFILE	= [	(u""					, u" - sélectionnez le profil de votre structure -"),

								(u""					, u" - "  ),
								(u"association"			, u"Association"),
								(u"citizen_collective"	, u"Collectif citoyen"),

								(u"public_collective"	, u"Collectivité"),
								(u"cooperative"			, u"Coopérative"),
								(u"entreprise"			, u"Entreprise (sup. ou égal à 10 employés)"),
								(u"entreprise_little"	, u"Entreprise PME (inf. 10 employés)"),
								
								(u"finance"				, u"Etablissement financier"),
								(u"fondation"			, u"Fondation"),
								(u"mutual"				, u"Mutuelle"),
								
								(u"public_state"		, u"Service de l'Etat"),
								(u"public_other"		, u"Structure publique autre"),

								(u""					, u" - "  ),
								# (u""					, u" * * *"),
								(u"none"				, u"Autre"),
						]


### TO DO LATER :
### PARTNERS LIST NEED TO BE STORED IN DB LATER WITH MORE DETAILS ABOUT EACH STRUCTURE
### AS : ADDRESS, PROFILE, LOGO, CONTACT, IS_CONTRIBUTOR, SPIDER_ID, HOW MANY SHARED PROJECTS ...
### THIS WILL BE THE PARTNERS DIRECTORY OF THE WEBSITE - 
PARTNERS_DATA			= [
								{ "code" : u"ademe"					, "spider_id" : None ,		"full_name" :"ADEME" },
								{ "code" : u"aeidl"					, "spider_id" : None ,		"full_name" :"AEIDL" },
								{ "code" : u"agence_du_num"			, "spider_id" : None ,		"full_name" :"Agence du numérique" },
								{ "code" : u"animafac"				, "spider_id" : None ,		"full_name" :"ANIMAFAC" },
								{ "code" : u"apie"					, "spider_id" : None ,		"full_name" :"APIE" },
								{ "code" : u"apriles"				, "spider_id" : None ,		"full_name" :"APRILES" },
								{ "code" : u"amrf"					, "spider_id" : None ,		"full_name" :"AMRF" },
								{ "code" : u"avise"					, "spider_id" : None ,		"full_name" :"Avise" },
								{ "code" : u"bleu_blanc_zebre"		, "spider_id" : None ,		"full_name" :"Bleu Blanc Zèbre" },
								{ "code" : u"brie_nov"				, "spider_id" : None ,		"full_name" :"Brie'nov" },
								{ "code" : u"bruded"				, "spider_id" : None ,		"full_name" :"BRUDED" },
								{ "code" : u"cget"					, "spider_id" : None ,		"full_name" :"CGET" },
								{ "code" : u"citego"				, "spider_id" : None ,		"full_name" :"Citego" },
								{ "code" : u"cg_scop"				, "spider_id" : None ,		"full_name" :"CG SCOP" },
								{ "code" : u"coorace"				, "spider_id" : None ,		"full_name" :"Coorace" },
								{ "code" : u"cress_pdl"				, "spider_id" : None ,		"full_name" :"CRESS PdL" },
								{ "code" : u"dgcs"					, "spider_id" : None ,		"full_name" :"DGCS" },
								{ "code" : u"dihal"					, "spider_id" : None ,		"full_name" :"DIHAL" },
								{ "code" : u"drjs_hdf"				, "spider_id" : None ,		"full_name" :"DRJCS Hauts-de-France" },
								{ "code" : u"ec_management_paris"	, "spider_id" : None ,		"full_name" :"Ecole de Paris du management" },
								{ "code" : u"ensssemble"			, "spider_id" : None ,		"full_name" :"EnSSsemble" },
								{ "code" : u"etalab"				, "spider_id" : None ,		"full_name" :"Etalab" },
								{ "code" : u"ff_geiq"				, "spider_id" : None ,		"full_name" :"Fédération française des GEIQ" },
								{ "code" : u"fej"					, "spider_id" : None ,		"full_name" :"FEJ" },
								{ "code" : u"fnce"					, "spider_id" : None ,		"full_name" :"FNCE" },
								{ "code" : u"cognac_jay"			, "spider_id" : None ,		"full_name" :"Fondation Cognac-Jay" },
								{ "code" : u"gen_2_conseil"			, "spider_id" : None ,		"full_name" :"Génération 2 conseil" },
								{ "code" : u"gniac"					, "spider_id" : None ,		"full_name" :"GNIAC" },
								{ "code" : u"fonda"					, "spider_id" : None ,		"full_name" :"La Fonda" },
								{ "code" : u"labo_ess"				, "spider_id" : None ,		"full_name" :"Labo de l'ESS" },
								{ "code" : u"part_colibri"			, "spider_id" : None ,		"full_name" :"La Part du Colibri" },
								{ "code" : u"prima_terra"			, "spider_id" : None ,		"full_name" :"Prima Terra" },
								{ "code" : u"reseau_rural"			, "spider_id" : None ,		"full_name" :"Réseau rural" },
								{ "code" : u"rtes"					, "spider_id" : None ,		"full_name" :"RTES" },
								{ "code" : u"sceaux"				, "spider_id" : None ,		"full_name" :"Sceaux" },
								{ "code" : u"siilab"				, "spider_id" : None ,		"full_name" :"SIILAB" },
								{ "code" : u"sparknews"				, "spider_id" : None ,		"full_name" :"SparkNews" },
								{ "code" : u"synergies"				, "spider_id" : None ,		"full_name" :"Synergies" },
								{ "code" : u"territoria"			, "spider_id" : None ,		"full_name" :"Territoria" },
								{ "code" : u"ticket_4_change"		, "spider_id" : None ,		"full_name" :"Ticket for change" },
								{ "code" : u"unadel"				, "spider_id" : None ,		"full_name" :"UNADEL" },
								{ "code" : u"villes_internet"		, "spider_id" : None ,		"full_name" :"Villes internet" },
]
CHOICES_PARTNERS			= [	( p["code"], 		p["full_name"] )	for p in PARTNERS_DATA ]
CHOICES_SPIDERS				= [	( p["spider_id"], 	p["full_name"] )	for p in PARTNERS_DATA ]
LIST_PARTNERS 				= [ i[0] for i in CHOICES_PARTNERS ]

CHOICES_STRUCTURES			= [ (u""					, u" - sélectionnez votre structure -"),
								(u""					, u" - "  ),
								(u"other"				, u"*** structure non partenaire (merci de compléter) ***"),
								(u"_no_"				, u"*** sans structure ***"  ),
								(u""					, u"*** structure partenaire (merci de choisir dans la liste) ***"  ), 
								(u""					, u" - "  ),
							  ] + CHOICES_PARTNERS + [ 
								(u"other"				, u"*** structure partenaire non citée (merci de compléter) ***"  ),
							]


### TO DO LATER : 
### THOSE TAGS AND RAW TAGS FROM ITEMS WILL BE HOMOGENISED
### BY CUSTOM THIRD PARTY APP 'SOLIDATA', AS A PROXY BETWEEN OPENSCRAPER AND CIS_FRONT)



