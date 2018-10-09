<template>
	<a class="navbar-item">
        <div class="field">
            <input 	class="is-checkradio is-default is-normal" 
                    type="checkbox" 
                    :id="item.id" 
                    :value="item.id" 
                    change="$emit('change', $event.target.value)"
                    @change="updateChecked"
                    >
            <label :for="item.id">
                {{ item.fullname }}
            </label>
        </div>
    </a>
</template>

<script>
export default {
    props: ["item", "f_checked", "value"],
    /*model: {
        prop: "f_checked",
        event: "change"
    },*/
    methods: {
        updateChecked: function(e) {
            /*var current_value = e.target.value;
            console.log("+++ current_value : ", current_value);

            if (this.f_checked.includes(current_value)) {
                // remove from f_checked if already present
                this.f_checked.splice(this.f_checked.indexOf(current_value), 1);
            } else {
                // add to f_checked if not
                this.f_checked.push(current_value);
            }

            console.log("+++ this.f_checked : ", this.f_checked);*/
        }
    }
};
</script>

<style>
</style>



Vue.component('v-filter-categ-item', {

	delimiters	: custom_delimiters,
	

})