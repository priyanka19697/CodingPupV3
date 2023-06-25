import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import {BrowserRouter, Routes, Route} from 'react-router-dom';
import {Login} from "./component/login";
import {Home} from "./component/Home";
import {Navigation} from './component/navigation';
import {Logout} from './component/logout';
import { CreateBlog } from './component/CreateBlog'
import { BlogDetail } from './component/BlogDetail';
function App() {
   return <BrowserRouter>
   <Navigation></Navigation>
   <Routes>
      <Route path='/' element={<Home/>} />
      <Route path='/login' element={<Login/>}/>
      <Route path='/logout' element={<Logout/>}/>
      <Route path="/blogs/create" element={<CreateBlog/>} />
      <Route path="/blogs/:id" element={<BlogDetail />} />
   </Routes>
   </BrowserRouter>
}

export default App;