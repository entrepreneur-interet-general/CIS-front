
<h1 align=center>  CARREFOUR DES INNOVATIONS SOCIALES </h1>


<h3 align=center> a portal to discover social innovations </h3>






-------

## INSTALLATION WALKTHROUGH 

### _LOCALLY_

1. **clone or [download](https://github.com/entrepreneur-interet-general/CIS-front/archive/master.zip) the repo**
1. **[install MongoDB](https://docs.mongodb.com/manual/installation/) locally** or get the URI of the MongoDB you're using
1. **go to your cis folder**
1. **install the libraries (without [virtual environment](https://pypi.python.org/pypi/virtualenv))**

	> $ pip install -r requirements.txt

1. **update the `app/backend/config_secret_vars_example.py` file** with your mongoDB URI (if you're not using default mongoDB connection)

1. **run app** from `$ ~/../cis`

	> $ python run_cis_front.py

1. **check in your browser** at `localhost:8100`



### _PRODUCTION_

1. **get a server** - check digital ocean, OVH, ...
1. optionnal : get a domain name : check OVH, namecheap, godaddy.... 
1. **follow (most of) these [instructions](https://github.com/entrepreneur-interet-general/tutos-2018/wiki/Admin-Sys)** 
1. pray for all that to work as expected... 



------

## TECHNICAL POINTS

#### Tech stack
- _Language_ : **Python**... because ... uuh ... eeeh ... I like this language too much ? 
- _Backend_  : **[Flask](http://www.tornadoweb.org/en/stable/)**... minimalistic Python framework
- _Frontend_ : **[Bulma](https://bulma.io/)**  (to make it nice) and then **[Vue.js](https://vuejs.org/)** (to make it even nicer and bi-directional)


------

## ROADMAP TO A MVP

#### To do list :

1. set up a basic Flask skeleton
1. make the landing page + integrate a form 
1. create a login page and store users in db
1. connect logged pages to [openscraper](https://github.com/entrepreneur-interet-general/OpenScraper) API + display results
1. create a search engine based on [openscraper](https://github.com/entrepreneur-interet-general/OpenScraper) API 

-------

## CREDITS 

#### OpenScraper's team thanks :

- the [SocialConnect](https://entrepreneur-interet-general.etalab.gouv.fr/defi/2017/09/26/socialconnect/) project, aka "Carrefour des Innovations Sociales"
- the [EIG](https://entrepreneur-interet-general.etalab.gouv.fr/) program by [Etalab](https://www.etalab.gouv.fr/)
- the [CGET](http://www.cget.gouv.fr/)

#### Contacts :

- [Julien Paris](<mailto:julien.paris@cget.gouv.fr>) (aka [JPy](https://twitter.com/jparis_py) on Twitter)
