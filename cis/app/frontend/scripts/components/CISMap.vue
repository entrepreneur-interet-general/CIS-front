<template>
    <div class="map">
        <l-map
        :zoom="zoom"
        :center="center"
        @update:center="centerUpdate"
        @update:zoom="zoomUpdate">
            <l-tile-layer
                :url="url"
                :attribution="attribution"/>
            <l-marker v-for="p in projects" 
                :key="p._id"
                :lat-lng="{lon: p.geoloc.longitude, lat: p.geoloc.latitude}">
                <l-popup>
                <div @click="popupClick">
                    <strong>{{(p['titre du projet'] || []).join(' ')}}</strong>
                    <br>{{(p['tags'] || []).join(' ')}}
                </div>
                </l-popup>
            </l-marker>
        </l-map>
    </div>
</template>

<script>
import { mapState } from 'vuex'
import { LMap, LTileLayer, LMarker, LPopup } from "vue2-leaflet";

export default {
    name: "CISMap",
    components: {
        LMap,
        LTileLayer,
        LMarker,
        LPopup
    },
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
    computed: mapState([
        'projects'
    ]),
    methods: {
        zoomUpdate(zoom) {
            this.currentZoom = zoom;
        },
        centerUpdate(center) {
            this.currentCenter = center;
        },
        popupClick() {
            console.log("Popup Click!");
        }
    }
};
</script>

<style>
.map { 
    height: 500px; 
    width: 80%;
    margin-left: 10%;
}
</style>