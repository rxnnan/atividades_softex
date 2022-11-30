import React from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import {Home} from './componentes/Home';
import {Segunda} from './componentes/Segunda';
import {Menu} from './componentes/Menu';

ReactDOM.render(
  <>
    <BrowserRouter>
    <Menu />
     <Routes>
      <Route path='/' element={<Home nome='Rennan'/>} />
      <Route path='/segunda' element={<Segunda />} />
     </Routes>
    </BrowserRouter>
  </>
, document.getElementById('root'))