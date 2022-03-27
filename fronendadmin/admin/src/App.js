import logo from './logo.svg';
import {BrowserRouter,Route, Routes} from 'react-router-dom'
import './App.css';
import Login from './components/form/Login';
import Userlist from './components/Admincontrol/Userlist';
import Newproduct from './components/product/Newproduct';
import Navbar from './components/adminnavbar/Navbar';
import {CookiesProvider} from 'react-cookie'
import Navigation from './components/verticalNavigation/Navigation';
import Addcategory from './components/category/Addcategory';
import Productlist from './components/product/Productlist';
import Ordermanagement from './order/Ordermanagement';
import Dashbordgraph from './components/Dashbord/Dashbordgraph';


function App() {
  return (
    <div>
      <CookiesProvider>
      <BrowserRouter>
       <Routes>
         <Route path='/' element={<Login/>}></Route>
         <Route exact path='/Listuser' element={<Userlist></Userlist>} />
         <Route path ="/productadd" element={<Newproduct></Newproduct>}/>
         <Route path="/addcategory" element={<Addcategory></Addcategory>}/>
        
         <Route path="/order" element={<Ordermanagement></Ordermanagement>}/>
          <Route path="/dashboard" element={<Dashbordgraph></Dashbordgraph>}/>
         
         
       </Routes>
     </BrowserRouter>
     </CookiesProvider>
    </div>
  );
}

export default App;
