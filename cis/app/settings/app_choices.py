# -*- encoding: utf-8 -*-


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### CHOICES ONLY FOR ADMIN
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

CHOICES_AUTH_LEVEL			= [	(u"visitor"			, u"visiteur"),
								(u"user"			, u"utilisateur"),
								(u"staff"			, u"membre du collectif"),
								(u"admin"			, u"administrateur"),
							]


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### CHOICES FOR USERS
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

CHOICES_DATA_TYPES			= [	(u"data_company"	, u"données sur votre structure"),
								(u"data_network"	, u"données sur vos réseaux"  ),
								(u"data_activity"	, u"données sur une de vos activités"),
								(u"data_people"		, u"données sur une des personnes travaillant dans votre structure"),
							]

CHOICES_NETWORKS			= [	(u"network_up"		, u"structures auxquelles j'adhère"),
								(u"network_flat"	, u"structures avec qui je travaille"),
								(u"network_down"	, u"structures de mon propre réseau"),
							]

CHOICES_PROFILES			= [	(u""				, u" - sélectionnez votre profil de métier-"),

								(u""				, u" - "  ),
								(u"helper"			, u"Accompagnateur.trice"),
								(u"analyst"			, u"Analyste"),
								(u"financer"		, u"Financeur.euse"),
								(u"observer"		, u"Observateur.trice"),
								(u"project_holder"	, u"Porteur.euse de projet"),

								(u""				, u""  ),
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


CHOICES_PARTNERS			= [
								(u"ademe"				, u"ADEME"),
								(u"aeidl"				, u"AEIDL"),
								(u"agence_du_num"		, u"Agence du numérique"),
								(u"animafac"			, u"ANIMAFAC"),
								(u"apie"				, u"APIE"),
								(u"apriles"				, u"APRILES"),
								(u"amrf"				, u"AMRF"),
								(u"avise"				, u"Avise"),
								(u"bleu_blanc_zebre"	, u"Bleu Blanc Zèbre"),
								(u"brie_nov"			, u"Brie'nov"),
								(u"bruded"				, u"BRUDED"),
								(u"cget"				, u"CGET"),
								(u"citego"				, u"Citego"),
								(u"cg_scop"				, u"CG SCOP"),
								(u"coorace"				, u"Coorace"),
								(u"cress_pdl"			, u"CRESS PdL"),
								(u"dgcs"				, u"DGCS"),
								(u"dihal"				, u"DIHAL"),
								(u"drjs_hdf"			, u"DRJCS Hauts-de-France"),
								(u"ec_management_paris"	, u"Ecole de Paris du management"),
								(u"ensssemble"			, u"EnSSsemble"),
								(u"etalab"				, u"Etalab"),
								(u"ff_geiq"				, u"Fédération française des GEIQ"),
								(u"fej"					, u"FEJ"),
								(u"fnce"				, u"FNCE"),
								(u"cognac_jay"			, u"Fondation Cognac-Jay"),
								(u"gen_2_conseil"		, u"Génération 2 conseil"),
								(u"gniac"				, u"GNIAC"),
								(u"fonda"				, u"La Fonda"),
								(u"labo_ess"			, u"Labo de l'ESS"),
								(u"part_colibri"		, u"La Part du Colibri"),
								(u"prima_terra"			, u"Prima Terra"),
								(u"reseau_rural"		, u"Réseau rural"),
								(u"rtes"				, u"RTES"),
								(u"sceaux"				, u"Sceaux"),
								(u"siilab"				, u"SIILAB"),
								(u"sparknews"			, u"SparkNews"),
								(u"synergies"			, u"Synergies"),
								(u"territoria"			, u"Territoria"),
								(u"ticket_4_change"		, u"Ticket for change"),
								(u"unadel"				, u"UNADEL"),
								(u"villes_internet"		, u"Villes internet"),
]
LIST_PARTNERS 				= [ i[0] for i in CHOICES_PARTNERS ]

CHOICES_STRUCTURES			= [ (u""					, u" - sélectionnez votre structure -"),
								(u""					, u" - "  ),
								(u""					, u"*** structures partenaires ***"  ), 
							  ] + CHOICES_PARTNERS + [ 
								(u""					, u" - "  ),
								(u"other"				, u"*** autres structures ***"  ),
								(u"_no_"				, u"sans structure"  ),
								(u"other"				, u"autre (merci de compléter)"),
							]




