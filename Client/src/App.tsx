import React from 'react';
import GlobalStyle from './GlobalStyles';
import Home from './Pages/Home';
import 'react-bootstrap';
const App : React.FC = () =>  {
  return (
    <div>
      <GlobalStyle />
      <Home />
    </div>
   
  );
}

export default App;
