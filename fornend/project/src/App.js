
import {BrowserRouter,Route, Routes} from 'react-router-dom'

import './App.css';
import Header from './components/Header /Header ';
import Footer from './components/Footer/Footer';
import Siginup from './components/forms/Siginup';
import Login from './components/forms/Login';
import Home from './components/body/Home';
import Showproduct from './components/products/Showproduct';
import Mobileverification from './components/forms/Mobileverification';
import {CookiesProvider} from 'react-cookie'
import Cart from './components/cart/Cart';


function App() {
  return (
    <div>
      <CookiesProvider>
    <BrowserRouter>
    <Header/>
    <Routes>
      <Route path='/'  element={<Home/>}/>
      <Route path="/login"  element={<Login/>}/> 
      <Route path='/siginup'  element={<Siginup/>}/>  
      <Route path='/otp' element={<Mobileverification/>}/>
      <Route path='/showproduct/:id' element={<Showproduct/>}/>
      <Route path='/cart'  element={<Cart/>}/>
      </Routes>
    <Footer/>  
    </BrowserRouter>
    </CookiesProvider>
    
    </div>
  );
}

export default App;
