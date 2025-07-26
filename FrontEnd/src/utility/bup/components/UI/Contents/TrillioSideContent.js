import "./TrillioSideContent.scss";
import "../../../styles/sass/_layout/Layout.scss";

import home from "../../../assets/img/icons/Custom_Icons_Badge_Menu_B.png";
import login from "../../../assets/img/icons/Custom_Icons_Badge_login_A.png";
import logout from "../../../assets/img/icons/Custom_Icons_Badge_logout_A.png";
import options from "../../../assets/img/icons/Options_Icon_A.png";
import automouse from "../../../assets/img/icons/Custom_Icons_Badge_sleept_A.png";
import sleep from "../../../assets/img/icons/Custom_Icons_Badge_sleep_B.png";

import sidelogo from "../../../assets/img/branding/Touchless_Interactive_Manager_Letters_plus_logo_C.png";
import sidelogo_btn from "../../../assets/img/branding/Touchless_Interactive_Manager_Logo_Base_A.png";

const TrillioSideContent = (props) => {
  return (
    <nav class="sidebar">
      <ul class="side-nav">
        <img src={sidelogo} class="side-nav__logo" />

        <li class="side-nav__item side-nav__item--active">
          {/*side-nav__item--active*/}
          <a href="#" class="side-nav__link">
            <img src={home} class="side-nav__icon" />

            <span>MENU</span>
          </a>
        </li>
        <li class="side-nav__item">
          <a href="#" class="side-nav__link">
            <img src={login} class="side-nav__icon" />

            <span>LOG-IN</span>
          </a>
        </li>
        <li class="side-nav__item">
          <a href="#" class="side-nav__link">
            <img src={options} class="side-nav__icon" />

            <span>OPTIONS</span>
          </a>
        </li>
        <li class="side-nav__item">
          <a href="#" class="side-nav__link">
            <img src={automouse} class="side-nav__icon" />

            <span>AUTO-MOUSE</span>
          </a>
        </li>
        <li class="side-nav__item">
          <a href="#" class="side-nav__link">
            <img src={sleep} class="side-nav__icon" />

            <span>SLEEP MODE</span>
          </a>
        </li>
        <img src={sidelogo_btn} class="side-nav__logo_btn" />
      </ul>

      <div class="legal">
        &copy; 21TIGERS product, designed by Robbie Trevor, All rights reserved
        2023.
      </div>
    </nav>
  );
};

export default TrillioSideContent;
