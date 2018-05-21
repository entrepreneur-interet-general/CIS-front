
console.log("::: cis-vue-store.js is loaded") ;

// doc VUEX / cf : https://vuex.vuejs.org/en/getting-started.html 
// add to array / cf : https://stackoverflow.com/questions/41830731/push-to-vuex-store-array-not-working-in-vuejs

const store = new Vuex.Store({
	state: {


		// --- VUEX TUTORIAL ---
		count: 0,


		// // --- SEARCH RESULTS ---
		// // data results
		// d_results			: results, 		
		// // togglers
		// d_loading			: true,
		// d_show_project 		: false,
		// d_current_project 	: {},
		// // pagination
		// d_count  			: count_results, 
		// d_count_tot			: count_results_total,
		// d_page_n			: page_n,
		// d_page_max			: page_max,
		// d_count_start 		: count_start, 
		// d_count_stop  		: count_stop, 
		// d_results_per_page	: results_per_page,

		// // -- FILTERS INPUT --
		// f_filters_tags		: CHOICES_FILTERS_TAGS, 		
		// f_categories 		: CATEGORIES_CIS_DICT_FLAT,		// codes for every filters
		// f_normalization		: NORMALIZATION_TAGS_SOURCES_CIS_DICT, 
		// f_checked			: [],
		// f_checked_as_code_tags	: [], 
		// f_checked_as_src_tags 	: [], 
		// // f_is_partners 		: false , 
		// f_filters_partners	: SRC_INFOS, 
		// // f_filters_partners	: CHOICES_FILTERS_PARTNERS["choices"], 
		// // f_filters_partners	: CHOICES_FILTERS_PARTNERS, 
		// f_checked_partners	: [],
		// f_stats				: {},

		// // --- SEARCH INPUT ---
		// // token
		// q_token				: token_openscraper,
		// // free text
		// q_search_string 	: search_string,
		// // tags for query
		// q_search_in_tags	: search_in_tags,
		// // TO DO : spiders ( aka partners )
		// q_search_in_spiders	: search_in_spiders,
		// // TO DO : adresses ( aka locations )
		// q_search_in_adresses : search_in_adresses,
		// // pagination
		// q_results_per_page 	: results_per_page,
		// q_page_n			: page_n,
		// // shuffle & sort
		// q_shuffle_seed		: shuffle_seed,
		// q_sort_by			: sort_by,
		// q_is_results		: false,


		// --- FAVORITES ---
		// fav list 
		usr_fav_items : [],


	},
	mutations: {

		increment: state => state.count++,
		decrement: state => state.count--,

	}
})