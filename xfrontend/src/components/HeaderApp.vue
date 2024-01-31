<template>
	<header class="p-3 mb-3">
		<nav class="container">
			<div
				class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start"
			>
				<ul
					class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0"
				>
					<li><a href="#" class="nav-link px-2 link-secondary">Overview</a></li>
					<li>
						<a href="#" class="nav-link px-2 link-body-emphasis">Inventory</a>
					</li>
					<li>
						<a href="#" class="nav-link px-2 link-body-emphasis">Customers</a>
					</li>
					<li>
						<a href="#" class="nav-link px-2 link-body-emphasis">Products</a>
					</li>
				</ul>
				<a
					href="/"
					class="position-absolute top-10 start-50 mb-2 mb-lg-0 link-body-emphasis text-decoration-none me-lg-auto mb"
				>
					<img
						src="https://github.com/mdo.png"
						alt="mdo"
						width="32"
						height="32"
						class="rounded-circle"
					/>
				</a>
				<form class="d-flex col-12 col-lg-3 mb-3 mb-lg-0 me-lg-3" role="search">
					<div class="input-group">
						<button class="btn border" type="submit" id="button-addon2">
							<svg
								class="bi bi-search"
								width="18"
								height="19"
								viewBox="0 0 18 19"
								fill="none"
								xmlns="http://www.w3.org/2000/svg"
								data-v-62cffb68=""
								data-v-72b95054=""
							>
								<circle
									cx="8.80553"
									cy="8.80541"
									r="7.49047"
									stroke="#B8B8B8"
									stroke-width="1.5"
									stroke-linecap="round"
									stroke-linejoin="round"
								></circle>
								<path
									d="M14.0153 14.4043L16.9519 17.3334"
									stroke="#B8B8B8"
									stroke-width="1.5"
									stroke-linecap="round"
									stroke-linejoin="round"
								></path>
							</svg>
						</button>
						<input
							type="search"
							class="form-control form-control:focus"
							placeholder="Найти товары"
							aria-label="Search"
						/>
							<i class="bi bi-x-lg form-control-clear"></i>
					</div>
				</form>

				<div class="dropdown text-end">
					<a
						href="#"
						class="d-block link-body-emphasis text-decoration-none dropdown-toggle"
						data-bs-toggle="dropdown"
						aria-expanded="false"
					>
						<img
							src="https://github.com/mdo.png"
							alt="mdo"
							width="32"
							height="32"
							class="rounded-circle"
						/>
					</a>
					<ul class="dropdown-menu text-small" style="">
						<li><a class="dropdown-item" href="#">New project...</a></li>
						<li><a class="dropdown-item" href="#">Settings</a></li>
						<li><a class="dropdown-item" href="#">Profile</a></li>
						<li><hr class="dropdown-divider" /></li>
						<li><a class="dropdown-item" href="#">Sign out</a></li>
					</ul>
				</div>
			</div>
		</nav>
	</header>
</template>

<style scoped>
.form-control:focus {
	border-color: #ced4da;
	box-shadow: none;
  
}

</style>
