
const APISearchOrigin = 'http://www.cis-openscraper.com';


export function getProjects(count=500){
    
}


export function searchProjects(text, page=1, per_page=40){
    const url = `${APISearchOrigin}/api/data?page_n=${page}&token=test_token&shuffle_seed=1&search_for=${encodeURIComponent(text)}&results_per_page=${per_page}`

    return fetch(url)
    .then(r => r.json())
}