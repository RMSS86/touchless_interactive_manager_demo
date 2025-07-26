import { Fragment, useState } from "react";
import "./Header.scss";

import mealsLogo from "../../assets/21_BTD_Logo_B.png";
import HeaderCartButton from "./headerCartButton";
import BGVideo from "../UI/BG-Video";
import _BGVideo from "../UI/BG-Video";

const features = ["Menu", "Orders", "Locations"];
const order = ["Order Now!"];

const _links = (feat, op) => {
  return (
    <li class="nav__item">
      <a
        class="nav__link"
        href="#section--1"
        onMouseEnter={handleHover.bind(0.5)}
        onMouseOut={handleHover.bind(1)}
      >
        {feat}
      </a>
    </li>
  );
};

const OrderBtn = (props, tag) => {
  const [orderActive, setOrderActive] = useState("false");
  // <HeaderCartButton />
  // <ButtonActive />

  const ActivateBtn = () => {
    setOrderActive("true");
    //console.log("received");
  }; //add this in onClick={} for activebtn

  const OrderNowBtn = (props) => {
    return (
      <Fragment>
        <a
          class="nav__link nav__link--btn btn--show-modal"
          href="#"
          onMouseEnter={handleHover.bind(0.5)}
          onMouseOut={handleHover.bind(1)}
          onClick={ActivateBtn}
        >
          {tag}
        </a>
      </Fragment>
    );
  };

  return (
    <li class="nav__item">
      {/* <ButtonActive /> */}
      {orderActive === "false" ? (
        <OrderNowBtn />
      ) : (
        <HeaderCartButton onCall={props.onShowCart} />
      )}
    </li>
  );
};
//{orderActive === "false" ? tag : <HeaderCartButton />}

const handleHover = function (e) {
  //console.log(e.target.className);
  if (e.target.classList.contains("nav__link")) {
    //console.log(e.target.classList.value, " Included");
    const link = e.target;
    const siblings = link.closest(".nav").querySelectorAll(".nav__link");
    //console.log("siblings ", siblings);
    const logo = link.closest(".nav").querySelector("img");
    //console.log(logo);
    //console.log(this);
    siblings.forEach((el) => {
      if (el !== link) el.style.opacity = this;
    });
    logo.style.opacity = this;
  }
};

const Header = (props) => {
  return (
    <Fragment>
      <header className="header">
        <nav class="nav">
          <img
            src={mealsLogo}
            alt="Food App Logo"
            className="nav__logo"
            id="logo"
            designer="Robbie Trevor"
            data-version-number="3.0"
          ></img>

          <ul className="nav__links">
            {features.map((e) => _links(e))}
            {OrderBtn(props, order[0])}
          </ul>
        </nav>
      </header>
      <div className="main-image">
        {/* <img src={mealsImage} alt="food food food" /> */}
        <BGVideo />
      </div>
    </Fragment>
  ); //On one root Element on JSX ue fragments
};

export default Header;

// const ButtonActive = (props) => {
//   return (
//     <Fragment>
//       {orderActive === "false" ? (
//         <OrderNowBtn />
//       ) : (
//         <ActiveCartBtn onClick={props.onShowCart} />
//       )}
//     </Fragment>
//   );
// };
