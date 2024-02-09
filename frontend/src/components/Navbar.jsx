import user_icon from '../images/user_icon.png'
const Navbar = () => {
	return (
		<>
			<nav className='navbar relative max-w-screen-xl mx-auto bg-base-100'>
				<div className='flex-1'>
					<button className='text-xl' type='button'>
						Укажите адрес доставки ↓
					</button>
				</div>
				<div className='absolute left-1/2 transform -translate-x-1/2'>
					<a className='font-bold text-2xl'>Flower shop</a>
				</div>
				<div className='flex-none gap-4'>
					<div className='form-control'>
						<input
							type='text'
							placeholder='Search'
							className='input input-bordered w-36 md:w-72'
						/>
					</div>
					<div className=''>
            <button className='btn btn-active btn-ghost'><img src={user_icon} alt="user-logo" /></button>
					</div>
				</div>
			</nav>
		</>
	)
}

export default Navbar
