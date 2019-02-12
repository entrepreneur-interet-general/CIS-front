
// const APISearchOrigin = 'http://www.solidata-preprod.co-demos.com';
// const APISearchOrigin = 'http://www.solidata.co-demos.com';
const APISearchOrigin = 'http://www.cis-openscraper.com';

// feature test for AbortController that works in Safari 12
let abortableFetchSupported = false;

try{
    const ac = new AbortController()
    
    fetch('.', {signal: ac.signal})
    .then(r => r.text())
    .then(result => {
        abortableFetchSupported = false;
    })
    .catch(err => {
        abortableFetchSupported = err.name === 'AbortError'
    })

    ac.abort();
}
catch(e){
    abortableFetchSupported = false;
}



function makeProjectTagToUnifiedTagsMap(){
    const map = new Map();

    for(const [code, projectTags] of Object.entries(NORMALIZATION_TAGS_SOURCES_CIS_DICT)){
        const unifiedTagName = NOMENCLATURE_CIS_DICT[code].fullname;

        for(const tag of projectTags){
            let unifiedTagNames = map.get(tag)
            if(!unifiedTagNames){
                unifiedTagNames = new Set()
            }
            unifiedTagNames.add(unifiedTagName)

            map.set(tag, unifiedTagNames);
        }
    }

    return map;
}


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
    image: string, // URL
    address: string,
    projectPartners: Array<string>,
    website: string,                    // project website
    pageAtSourcer: string,              // project page in sourcer
    projectInSourcerListing: string,    // sourcer searchresult/list page where the project appeared
    spider_id: SpiderId,
    description: string
}

*/
function fromMongoModelToFrontModel(projectInMongo){
    return {
        id: projectInMongo['_id'],
        title: Array.isArray(projectInMongo['titre du projet']) ? projectInMongo['titre du projet'].join(' '): '',
        tags: projectInMongo['tags'] || [],
        image: projectInMongo['image(s) du projet'],
        address: Array.isArray(projectInMongo['adresse du projet']) ? projectInMongo['adresse du projet'].join(' '): '',
        projectPartners: Array.isArray(projectInMongo['partenaires du projet']) ? projectInMongo['partenaires du projet'].join(' '): '',
        website: projectInMongo['website'] && projectInMongo['website'][0],
        pageAtSourcer: projectInMongo['link_data'],
        projectInSourcerListing: projectInMongo['link_src'],
        spiderId: projectInMongo['spider_id'],
        description: Array.isArray(projectInMongo['résumé du projet']) ? projectInMongo['résumé du projet'].join(' '): '',
    }
}


const projectTagToUnifiedTags = makeProjectTagToUnifiedTagsMap();

function uniformizeProject(p){
    const TEXTURE_COUNT = 16;

    if(!p.image){
        // add texture as image
        // so it's a deterministic function, let's use the id to determine which texture is used
        p.image = `/static/illustrations/textures/medium_fiche_${ (parseInt(p.id.substr(p.id.length - 6), 16)%TEXTURE_COUNT) + 1}.png`
    }
    else{
        p.image = p.image[0]
    }

    let projectUnifiedTags = new Set()

    for(const projectTag of p.tags){
        const unifiedTags = projectTagToUnifiedTags.get(projectTag)

        if(unifiedTags){
            for(const t of unifiedTags){
                projectUnifiedTags.add(t);
            }
        }
        else{
            console.warn('No unified tag for project tag', projectTag, p.id, p.title)
        }
    }

    p.tags = [...projectUnifiedTags]

    return p;
}


// This function is awkward
// TODO Create a dedicated server-side end-point to get only the spiders
export function getSpiders(){
    let url = `${APISearchOrigin}/api/infos?only_spiders_list=true`;

    return fetch(url)
    .then(r => r.json())
    .then(({spiders}) => spiders.spiders_dict)
}


// This function is super-inefficient
// TODO Create a server-side end-point to get only one project
export function getProjectById(id){
    let url = `${APISearchOrigin}/api/data?token=pwa&results_per_page=100000`;

    return fetch(url)
    .then(r => r.json())
    .then(({query_results}) => {
        const project = query_results.find(p => p._id === id)

        return project ?
            uniformizeProject(fromMongoModelToFrontModel(project)) : 
            undefined;
    })
}


export function searchProjects(text, tags, spiderIds=[], page=1, per_page=1000){
    text = text.trim();

    const shuffle_seed      = Math.floor((Math.random() * 10000) + 1); ;

    const searchArg         = text.length >= 1 ? '&search_for='+encodeURIComponent(text) : '';
    const spiderArg         = spiderIds.length >= 1 ? '&'+spiderIds.map(id => 'spider_id='+id).join('&') : '';
    const tagsArg           = tags && tags.size >= 1 ? `&search_in_tags=${encodeURIComponent([...tags].join(','))}` : '';

    let url = `${APISearchOrigin}/api/data?page_n=${page}&results_per_page=${per_page}&token=test_token&shuffle_seed=${shuffle_seed}${searchArg}${spiderArg}${tagsArg}`

    // abort fetch if this is supported
    // abort manually when response arrives otherwise
    const ac = abortableFetchSupported ? new AbortController() : undefined
    let searchAborted = false

    return {
        abort(){
            searchAborted = true

            if(ac)
                ac.abort()
        },
        promise: (ac ? fetch(url, {signal: ac.signal} ) : fetch(url))
            .then(r => r.json())
            .then(({query_results, query_log}) => {
                if(searchAborted){
                    const error = new Error('Search aborted')
                    error.name = 'AbortError'
                    throw error
                }
                else{
                    return { 
                        projects: Array.isArray(query_results) ? query_results.map(fromMongoModelToFrontModel).map(uniformizeProject) : [],
                        total: query_log.count_results_tot
                    }
                }
            })
                
    }

}