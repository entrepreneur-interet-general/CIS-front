
const APISearchOrigin = 'http://www.cis-openscraper.com';

/*
Example of project in Mongo:
{
    "titre du projet": [
        "Association OLCQ"
    ],
    "tags": [
        "Mobilité Solidaire"
    ],
    "adresse du projet": [
        "Corse, Bastia",
        "17/12/2014",
        "Parrainé par"
    ],
    "partenaires du projet": [
        "Parrainé par",
        "17/12/2014"
    ],
    "added_at": 1522885074.672806,
    "link_src": "https://www.fondation-vinci.com/fondation/fr/recherche/projets.htm&a=&r=&d=&t=Mobilit%C3%A9%20solidaire&g=&p=&c=&q=",
    "spider_id": "5aaff8aa0a82860b06c94a6e",
    "résumé du projet": [
        "Accompagner les personnes en situation de handicap moteur vers le permis B"
    ],
    "_id": "5ac561d23ba14c4f0972a2f2"
}

Expected output : 

interface CISProjectFront{
    id: CIS_ID (extends String)
    title: string,
    tags: Array<string>,
    image: Array<string>, // URL
    address: string,
    projectPartners: Array<string>,
    url: string
    // spider_id: SpiderId,
    description: string
}

*/
function fromMongoModelToFrontModel(projectInMongo){
    return {
        id: projectInMongo['_id'],
        title: Array.isArray(projectInMongo['titre du projet']) ? projectInMongo['titre du projet'].join(' '): '',
        tags: projectInMongo['tags'],
        image: projectInMongo['image(s) du projet'],
        address: Array.isArray(projectInMongo['adresse du projet']) ? projectInMongo['adresse du projet'].join(' '): '',
        projectPartners: projectInMongo['partenaires du projet'],
        url: projectInMongo['link_src'],
        // spider_id: SpiderId,
        description: Array.isArray(projectInMongo['résumé du projet']) ? projectInMongo['résumé du projet'].join(' '): '',
    }
}


export function getProjects(count=500){
    
}


export function searchProjects(text, tags, page=1, per_page=1000){
    let url = `${APISearchOrigin}/api/data?page_n=${page}&token=test_token&shuffle_seed=1&search_for=${encodeURIComponent(text)}&results_per_page=${per_page}`
    
    if(tags && tags.size >= 1)
        url += `&search_in_tags=${encodeURIComponent([...tags].join(','))}`

    return fetch(url)
    .then(r => r.json())
    .then(({query_results}) => Array.isArray(query_results) ? query_results.map(fromMongoModelToFrontModel) : [])

}