import IndexUpperUI from './components/IndexUpperUI'
import Navbar from './components/Navbar'
import FooterComponent from './components/FooterComponent'
function App() {
	return (
		<div className=''>
			<Navbar />
			<IndexUpperUI title='Здесь будет какой то UI' />
			<IndexUpperUI title='Здесь будет отображение товаров' />
			<FooterComponent/>
		</div>
	)
}

export default App
