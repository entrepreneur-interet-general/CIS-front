<template>
    <div class="map">
        <div class="count-and-tabs-container">
            <div class="container">
                <CISSearchResultsCountAndTabs :view="view" :open="!!highlightedProject" @viewChange="$emit('viewChange', $event)">
                    <div class="highlighted-project" v-if="highlightedProject" slot="project">
                        <button class="button close" @click="highlightProject(undefined)">X</button>

                        <div class="card">
                            <div class="card-image">
                                <img :src="highlightedProject.image" 
                                    :alt="'illustration du projet' + highlightedProject.title">
                            </div>
                            
                            <div class="card-content" v-if="highlightedProject.address.trim().length > 1">
                                <span class="icon has-text-light">
                                    <i class="fas fa-location-arrow"></i>
                                </span>
                                <span class="subtitle is-6">
                                    {{highlightedProject.address.slice(0, 100)}}
                                </span>
                            </div>

                            <div class="card-content">
                            <h1>{{highlightedProject.title}}</h1>
                            </div>

                            <div class="card-content" 
                                v-if="Array.isArray(highlightedProject.tags) && highlightedProject.tags.length >=1">
                                <span v-for="tag in highlightedProject.tags" class="tag" :key="tag">
                                    {{tag}}
                                </span>
                            </div>
                        </div>
                    </div>
                </CISSearchResultsCountAndTabs>
            </div>
        </div>

        <l-map
        :zoom="zoom"
        :center="center"
        @update:center="centerUpdate"
        @update:zoom="zoomUpdate">
            <l-tile-layer
                :url="url"
                :attribution="attribution"/>
            <v-marker-cluster>
                <l-marker v-for="p in projects" 
                    v-if="geolocByProjectId.get(p.id)"
                    :key="p.id"
                    :lat-lng="{lng: geolocByProjectId.get(p.id).longitude, lat: geolocByProjectId.get(p.id).latitude}"
                    @click="highlightProject(p)">
                    
                    <l-icon
                        iconUrl="https://unpkg.com/leaflet@1.3.4/dist/images/marker-icon.png"
                        :iconSize="p === highlightedProject ? [31, 46] : [19, 29]"/>                    

                </l-marker>
            </v-marker-cluster>
        </l-map>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import { LMap, LTileLayer, LMarker, LIcon } from 'vue2-leaflet';
import Vue2LeafletMarkerCluster from 'vue2-leaflet-markercluster'

import CISSearchResultsCountAndTabs from './CISSearchResultsCountAndTabs.vue'

const FRANCE_CENTER = [46.2276, 2.2137];

export default {
    name: "CISMap",
    components: {
        LMap,
        LTileLayer,
        LMarker,
        LIcon,
        'v-marker-cluster': Vue2LeafletMarkerCluster,
        CISSearchResultsCountAndTabs
    },
    props: ['view'],
    data() {
        return {
            zoom: 6,
            currentZoom: 6,
            center: FRANCE_CENTER,
            currentCenter: FRANCE_CENTER,
            url: 'https://{s}.tile.openstreetmap.de/tiles/osmde/{z}/{x}/{y}.png',
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contibutors',
            
            highlightedProject: undefined
        };
    },
    computed: {
        ...mapState({
            projects: ({search}) => search.answer.result && search.answer.result.projects,
            geolocByProjectId: ({geolocByProjectId}) => geolocByProjectId
        })
    },
    methods: {
        zoomUpdate(zoom) {
            this.currentZoom = zoom;
        },
        centerUpdate(center) {
            this.currentCenter = center;
        },
        highlightProject(p) {
            console.log("Highlight project", p);
            this.highlightedProject = p;
        },
        ...mapActions([
            'findProjectsGeolocs'
        ])
    },
    beforeUpdate(){
        if(this.projects){
            const projectsWithMissingAddress = this.projects.filter(p => !this.geolocByProjectId.has(p.id))

            if(projectsWithMissingAddress.length >= 1)
                this.findProjectsGeolocs(projectsWithMissingAddress)
        }
    },
    mounted(){
        if(this.projects){
            const projectsWithMissingAddress = this.projects.filter(p => !this.geolocByProjectId.has(p.id))

            if(projectsWithMissingAddress.length >= 1)
                this.findProjectsGeolocs(projectsWithMissingAddress)
        }
    }
};
</script>

<style>
.map { 
    height: 500px; 
    width: 100%;

    margin-top: 1em;
}

/*
    Leaflet adds its own z-index to a bunch of elements which makes the map appear on top of 
    other elements with no good reason
    This line allows for the map to be usable without known limit yet while leaving the map below
    other elements
*/
.map .leaflet-container *{
  z-index: 1;
}


.map{
    position: relative;
}
.map .count-and-tabs-container{
    position: absolute;
    top: 0;
    width: 100%;
}

.map .count-and-tabs-container .result-count-parent,
.map .count-and-tabs-container .buttons{
    z-index: 2;
}

.highlighted-project{
    display: flex;
    flex-direction: column;
}

.highlighted-project button.close{
    margin: 0.5em 0;
    background-color: transparent;
    border: 0;

    align-self: flex-end;
}

.highlighted-project .card{
    font-size: 0.9em;
    
    box-shadow: none;
}

.highlighted-project .card .card-content{
    padding: 0.2em 0.5em;   
}

.highlighted-project .card .card-content:first-of-type{
    padding-top: 0.5em;
}
.highlighted-project .card .card-content:last-of-type{
    padding-bottom: 0.5em;
}

.highlighted-project .card .card-content h1{
    font-size: 1.1em;
    font-weight: bold;
}

/* TODO SASS : share this style with search result project card tag style */
.highlighted-project .tag{
    margin-right: 0.5em;
    margin-bottom: 0.5em;
    padding: 0.2em 1em;
    background-color: #767676;
    color: white;
}

</style>