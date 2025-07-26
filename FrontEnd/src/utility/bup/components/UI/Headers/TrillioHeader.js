import "./TrillioHeader.scss";
import "../../../styles/sass/_layout/Layout.scss";

import logo from "../../../assets/img/branding/Touchless_Interactive_Manager_Logo_Block_NL_White.png";
import magnify from "../../../assets/img/SVG/magnifying-glass.svg";
import options from "../../../assets/img/icons/Options_Icon_A.png";
import voice from "../../../assets/img/icons/Custom_Icons_Badge_B.png";
import userPhoto from "../../../assets/img/userRob.jpg";

const TrillioHeader = (props) => {
  return (
    <header class="header">
      <form action="#" class="search">
        <input type="text" class="search__input" placeholder="Search Option" />
        <button class="search__button">
          <img src={magnify} class="search__icon" />
        </button>
      </form>
      <img src={logo} alt="TIM logo" class="logo" />
      <nav class="user-nav">
        <div class="user-nav__icon-box">
          <img src={options} class="user-nav__icon" />
          {/*<span class="user-nav__notification">8</span>*/}
        </div>
        <div class="user-nav__icon-box">
          <img src={voice} class="user-nav__icon" />

          {/*<span class="user-nav__notification">14</span>*/}
        </div>
        <div class="user-nav__user">
          <span class="user-nav__user-name">Hi Robbie</span>
          <img src={userPhoto} alt="User photo" class="user-nav__user-photo" />
        </div>
      </nav>
    </header>
  );
};

export default TrillioHeader;
