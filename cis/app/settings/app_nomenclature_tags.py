
# -*- encoding: utf-8 -*-

NOMENCLATURE_CIS_DICT = {
	
	"AGR":{"fullname":u"Agriculture","description":u"alimentation, foret"},
	"AME":{"fullname":u"Aménagement","description":u"espaces publics, gestion de l'espace"},
	"AUT":{"fullname":u"Autres","description":u"société civile, Europe, observation, équipements publics"},
	"BIO":{"fullname":u"Biodiversité","description":u"environnement, espaces verts"},
	"CIT":{"fullname":u"Citoyenneté","description":u"citoyenneté, engagement, mobilisation citoyenne"},
	"CLI":{"fullname":u"Climat","description":u"risques naturels"},
	"COH":{"fullname":u"energie","description":u"solidarités, lien social, vivre ensemble, autonomie, isolement"},
	"COM":{"fullname":u"Communication","description":u""},
	"COP":{"fullname":u"Achats","description":u"commande publique, achats durables"},
	"COR":{"fullname":u"Commerce","description":u"commerce équitable"},
	"CUL":{"fullname":u"Culture","description":u"arts, patrimoine"},
	"DEC":{"fullname":u"Déchets","description":u"recyclage, économie circulaire"},
	"EAU":{"fullname":u"Eau","description":u""},
	"ECO":{"fullname":u"Economie","description":u"développement économique, ESS, entreprenariat, monnaie locale, assurance, auto-production "},
	"EDU":{"fullname":u"Education","description":u"orientation, mobilité internationale, enseignement supérieur, éducation populaire"},
	"EMP":{"fullname":u"Emploi","description":u"groupement employeurs"},
	"ENE":{"fullname":u"Energie","description":u""},
	"EVA":{"fullname":u"Evaluation","description":u""},
	"FIN":{"fullname":u"Finances","description":u"finance solidaire, micro crédit, financements européens"},
	"FOR":{"fullname":u"Formation","description":u"apprentissage, enseignement"},
	"GOU":{"fullname":u"Gouvernance","description":u"organisation, élus, RH, RSE"},
	"HAB":{"fullname":u"Habitat","description":u"logement, éco-construction, travaux publics, rénovation"},
	"HAN":{"fullname":u"Handicap","description":u""},
	"INS":{"fullname":u"Insertion","description":u"insertion professionnelle"},
	"JEU":{"fullname":u"Jeunesse","description":u"enfance"},
	"DRO":{"fullname":u"Droits","description":u"justice, accès aux droits, lutte contre discriminations, harcèlement, sécurité, protection, égalité homme femmes, non recours"},
	"LOI":{"fullname":u"Loisirs","description":u"vacances"},
	"MED":{"fullname":u"Médiation","description":u""},
	"MOB":{"fullname":u"Mobilité","description":u"permis de conduire, transports"},
	"NUM":{"fullname":u"Numérique","description":u""},
	"PAR":{"fullname":u"Participation","description":u"démarches participatives, mobilisation locale, participation usagers"},
	"REC":{"fullname":u"Recherche ","description":u""},
	"SAN":{"fullname":u"Santé","description":u""},
	"SEN":{"fullname":u"Seniors","description":u"intergénérationnel"},
	"SER":{"fullname":u"Services","description":u"services à la population, accueil de jour, accompagnement, animation"},
	"SPO":{"fullname":u"Sports","description":u""},
	"TOU":{"fullname":u"Tourisme","description":u""},
	"URB":{"fullname":u"Urbanisme","description":u""},
	"COO":{"fullname":u"Coopération","description":u"coopération, partenariats, réseaux"},
	"MEC":{"fullname":u"Mécénat","description":u"mécénat, mécénat d'entreprises"}
}

NOMENCLATURE_CIS_LIST = [ {"code" : k , "fullname" : v["fullname"], "description" : v["description"] } for k,v in NOMENCLATURE_CIS_DICT.iteritems() ]