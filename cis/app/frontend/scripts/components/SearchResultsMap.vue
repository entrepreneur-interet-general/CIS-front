<template>
    <div class="map">
        <div class="count-and-tabs-container">
            <div class="container">
                <CISSearchResultsCountAndTabs :view="VIEW_MAP" :open="!!highlightedProject">
                    <div class="highlighted-project" v-if="highlightedProject" slot="project">
                        <button class="button close" @click="highlightProject(undefined)">
                            <span class="icon is-small">
                                <i class="fas fa-times"></i>
                            </span>
                        </button>

                        <div class="card">
                            <router-link :to="`/project/${highlightedProject.id}`" class="card-image">
                                <img :src="highlightedProject.image" 
                                    :alt="'illustration du projet' + highlightedProject.title">
                            </router-link>
                            
                            <div class="card-content" v-if="highlightedProject.address.trim().length > 1">
                                <!-- 
                                <span class="icon has-text-light">
                                    <i class="fas fa-location-arrow"></i>
                                </span> -->
                                <span class="icon">
                                    <img class="image is-16x16" src="/static/icons/icon_pin.svg">
                                </span>
                                <span class="subtitle is-6">
                                    {{highlightedProject.address.slice(0, 100)}}
                                </span>
                            </div>

                            <router-link :to="`/project/${highlightedProject.id}`" class="card-content">
                                <h1>{{highlightedProject.title}}</h1>
                            </router-link>

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
        :options="{zoomControl: false}"
        :center="center"
        :bounds="bounds"
        @update:center="centerUpdate"
        @update:zoom="zoomUpdate">
            <l-control-zoom position="bottomright"/>
            <l-tile-layer
                :url="url"
                :attribution="attribution"/>
            <v-marker-cluster :options="{showCoverageOnHover: false, iconCreateFunction: iconCreateFunction}">
                <l-marker v-for="p in displayedProjects"
                    :key="p.id"
                    :lat-lng="{lng: geolocByProjectId.get(p.id).longitude, lat: geolocByProjectId.get(p.id).latitude}"
                    @click="highlightProject(p)">
                    
                    <l-icon
                        iconUrl="/static/icons/icon_pin_plein_violet.svg"
                        :iconSize="p === highlightedProject ? [46, 46] : [29, 29]"/>                    

                </l-marker>
            </v-marker-cluster>
        </l-map>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import { L, LMap, LControlZoom, LTileLayer, LMarker, LIcon } from 'vue2-leaflet';
import Vue2LeafletMarkerCluster from 'vue2-leaflet-markercluster'

import CISSearchResultsCountAndTabs from './CISSearchResultsCountAndTabs.vue'

import {VIEW_MAP} from '../constants.js'

const FRANCE_CENTER = [46.2276, 2.2137];



export default {
    name: "CISMap",
    components: {
        LMap,
        LControlZoom,
        LTileLayer,
        LMarker,
        LIcon,
        'v-marker-cluster': Vue2LeafletMarkerCluster,
        CISSearchResultsCountAndTabs
    },
    data() {
        return {
            zoom: 6,
            currentZoom: 6,
            center: FRANCE_CENTER,
            currentCenter: FRANCE_CENTER,

            // url: 'https://{s}.tile.openstreetmap.de/tiles/osmde/{z}/{x}/{y}.png',
            // attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contibutors',
            
            url: 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png',
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
            subdomains: 'abcd',
            maxZoom: 19,

            highlightedProject: undefined,
            VIEW_MAP
        };
    },
    computed: {
        ...mapState({
            projects({search}){ return search.answer.result && search.answer.result.projects },
            displayedProjects(){
                return this.projects && this.projects.filter(p => this.geolocByProjectId.get(p.id))
            },
            bounds(){
                return this.displayedProjects && new L.LatLngBounds(this.displayedProjects.map(p => ({
                    lng: this.geolocByProjectId.get(p.id).longitude, 
                    lat: this.geolocByProjectId.get(p.id).latitude
                })));
            },
            geolocByProjectId({geolocByProjectId}){return geolocByProjectId}
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
            this.highlightedProject = p;
        },
        iconCreateFunction(cluster){
            const markerCount = cluster.getChildCount();

            return new L.DivIcon({
                html: `<span>${markerCount}</span>`, 
                className: 'cis-marker-cluster',
                iconSize: new L.Point(40, 40)
            });
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
    height: calc(100vh - 120px); 
    width: 100%;
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
    top: 1rem;
    width: 100%;
}

.map .count-and-tabs-container .result-count-parent,
.map .count-and-tabs-container .buttons{
    z-index: 2;
}

.map .cis-marker-cluster{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;

    background-color: #80C2BD;
    color: white;

    font-size: 16px;
    font-weight: bold;

    border-radius: 50%;
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