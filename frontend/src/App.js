import React from 'react';
import Camera from './Camera';
import Firstpage from './Firstpage';
import Video from './Video';
import { HashRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path='/' element={<Firstpage />} />
          <Route path='/photo' element={<Camera />} />
          <Route path='/videoprocessing' element={<Video/>} />
        </Routes>
      </Router>
    </>
  )
}

export default App;
