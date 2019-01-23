<template>
    <div>
        <NavBar :logo="logo" :brand="brand"/>
        <NotFoundError/>
        <Footer/>
    </div>
</template>

<script>
import NavBar from '../NavBar.vue';
import NotFoundError from '../NotFoundError.vue';
import Footer from '../Footer.vue';

export default {
    name: 'NotFoundScreen',
    components: {
        NavBar, NotFoundError, Footer
    },
    props: [
        'logo', 'brand'
    ]
}
</script>

<style>
.list .filter-feedback{
    padding-bottom: 0;
}
</style>