<template>
    <div>
        <header>
            <span>X projets trouvés</span>
        </header>
        <div>
            <CISProjectCard v-for="project in projects" :key="project.id" :project="project"/> 
        </div>
    </div>
</template>

<script>
import {mapState} from 'vuex'
import CISProjectCard from './CISProjectCard.vue'

export default {
    components: {
        CISProjectCard
    },
    
    
    computed: mapState([
        'projects'
    ])
    
}
</script>
