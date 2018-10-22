<template>
	<div class="navbar-brand" :title="brand">
		<a href="/" class="navbar-item">
			<img id="navbar-logo" :src="logo" :alt="'Logo '+ brand">
		</a>
	</div>
</template>

<script>
export default {
	props: ['logo', 'brand']
}
</script>
