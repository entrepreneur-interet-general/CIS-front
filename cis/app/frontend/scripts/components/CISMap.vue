<template>
    <div class="map">
        <div class="count-and-tabs-container">
            <div class="container">
                <CISSearchResultsCountAndTabs :view="view" @viewChange="$emit('viewChange', $event)"/>
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
            <l-marker v-for="p in projects" 
                v-if="geolocByProjectId.get(p.id)"
                :key="p.id"
                :lat-lng="{lon: geolocByProjectId.get(p.id).longitude, lat: geolocByProjectId.get(p.id).latitude}">
                <l-popup>
                <div @click="popupClick">
                    <strong>{{p['title']}}</strong>
                    <br>{{(p['tags'] || []).join(' ')}}
                </div>
                </l-popup>
            </l-marker>
        </l-map>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import { LMap, LTileLayer, LMarker, LPopup } from "vue2-leaflet";

import CISSearchResultsCountAndTabs from './CISSearchResultsCountAndTabs.vue'


export default {
    name: "CISMap",
    components: {
        LMap,
        LTileLayer,
        LMarker,
        LPopup,
        CISSearchResultsCountAndTabs
    },
    props: ['view'],
    data() {
        return {
            zoom: 6,
            currentZoom: 6,
            center: [46.2276, 2.2137],
            currentCenter: [46.2276, 2.2137],
            url: "https://{s}.tile.openstreetmap.de/tiles/osmde/{z}/{x}/{y}.png",
            attribution:
                '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contibutors'
        };
    },
    computed: {
        ...mapState([
            'geolocByProjectId'
        ]),
        ...mapState({
            projects: ({search}) => search.answer.result && search.answer.result.projects,            
        })
    },
    methods: {
        zoomUpdate(zoom) {
            this.currentZoom = zoom;
        },
        centerUpdate(center) {
            this.currentCenter = center;
        },
        popupClick() {
            console.log("Popup Click!");
        },
        ...mapActions([
            'findProjectsGeolocs'
        ])
    },
    beforeUpdate(){
        const projectsWithMissingAddress = this.projects.filter(p => !this.geolocByProjectId.has(p.id))

        if(projectsWithMissingAddress.length >= 1)
            this.findProjectsGeolocs(projectsWithMissingAddress)
    },
    mounted(){
        const projectsWithMissingAddress = this.projects.filter(p => !this.geolocByProjectId.has(p.id))

        if(projectsWithMissingAddress.length >= 1)
            this.findProjectsGeolocs(projectsWithMissingAddress)
    }
};
</script>

<style>
.map { 
    height: 500px; 
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
    top: 0;
    width: 100%;
}

.map .count-and-tabs-container .results-count,
.map .count-and-tabs-container .buttons{
    z-index: 2;
}

</style>