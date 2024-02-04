<template>
	<div class="navbar bg-base-100">
		<div class="flex-1">
			<a class="btn btn-ghost text-xl">Flowers Shop</a>
		</div>
		<button
			class="btn bg- -500 mr-4"
			@click="toggleTheme"
		>
			{{ currentTheme === 'dark' ? 'Light' : 'Dark' }}
		</button>
		<div class="flex-none gap-2">
			<div class="form-control">
				<input
					type="text"
					placeholder="Search"
					class="input input-bordered w-24 md:w-auto"
				/>
			</div>
			<div class="dropdown dropdown-end">
				<div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
					<div class="w-10 rounded-full">
						<img alt="Tailwind CSS Navbar component" src="\unicorn.png" />
					</div>
				</div>
				<ul
					tabindex="0"
					class="mt-3 z-[1] p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-52"
				>
					<li>
						<a class="justify-between"> Profile </a>
					</li>
					<li><a>Settings</a></li>
					<li><a>Logout</a></li>
				</ul>
			</div>
		</div>
	</div>
</template>

<script>
import { onMounted, ref } from 'vue'
import { themeChange } from 'theme-change'

export default {
	setup() {
		const currentTheme = ref('light')
		onMounted(() => {
			themeChange(false)
			currentTheme.value =
				document.documentElement.getAttribute('data-theme') || 'light'
		})
		const toggleTheme = () => {
			if (currentTheme.value === 'dark') {
				document.documentElement.setAttribute('data-theme', 'light')
				currentTheme.value = 'light'
			} else {
				document.documentElement.setAttribute('data-theme', 'dark')
				currentTheme.value = 'dark'
			}
		}
		return { toggleTheme, currentTheme }
	},
}
</script>
