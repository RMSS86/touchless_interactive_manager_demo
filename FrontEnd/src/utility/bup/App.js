import React, { useState, Fragment } from "react";
///COmponenets
import TrillioHeader from "./components/UI/Headers/TrillioHeader";
import TrillioSideContent from "./components/UI/Contents/TrillioSideContent";
import TrillioMianContent from "./components/Layout/TrillioMianContent";
///SCSS
import "./styles/sass/_layout/Layout.scss";

//import io from "socket.io-client";
//const _socket = io.connect("http://127.0.0.1:3001");

const App = () => {
  return (
    <div class="container">
      <TrillioHeader />
      <div class="content">
        <TrillioSideContent />
        <TrillioMianContent />
      </div>
    </div>
  );
};

export default App;

// import Header from "./components/Layout/Header";
// import Meals from "./components/Meals/Meals";
// import Cart from "./components/Cart/Cart";
// import Footer from "./components/UI/Footer";
// import CartProvider from "./store/CartProvider";

//inside app funct
// const [cartIsShown, setCartIsShown] = useState(false);

// const showCartHandler = () => {
//   setCartIsShown(true);
//   console.log("received from App!");
// };

// const hideCartHandler = () => {
//   setCartIsShown(false);
// };

//  <CartProvider>
//       {cartIsShown && <Cart onClose={hideCartHandler} />}
//       <Header onShowCart={showCartHandler} />
//       <main>
//         <Meals />
//         {/* <div className="main-image">
//           <img src={mealsImage} alt="food food food" />
//         </div> */}
//       </main>
//       <Footer />
//     </CartProvider>
