<script>
import Index from './components/Index.vue'
import HeaderApp from './components/HeaderApp.vue'
import ChangeColorButton from './components/ChangeColorButton.vue'
export default {
	components: {
		ChangeColorButton,
		Index,
		HeaderApp
	},
}
</script>

<template>
	<div>
		<HeaderApp />
		<div class="flex flex-col items-center justify-center h-screen">
			<Index />
			<ChangeColorButton class="" />
		</div>
	</div>
</template>


