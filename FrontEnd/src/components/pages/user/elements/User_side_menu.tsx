/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
export default function User_side_menu({
  _componentProps,
  children,
  _className = "user_sidebar",
  _style,
  _onClick,
  ...rest
}: _props) {
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////

  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  return (
    <>
      <_contextType
        {...rest}
        className={_className}
        onClick={_onClick}
        style={{}}
      >
        {/* {children} */}
        <ul className="side-nav">
          <img src={SIDE_LOGO} className="side-nav__logo" />

          <li className="side-nav__item side-nav__item--active">
            {/*side-nav__item--active*/}
            <a href="#" className="side-nav__link">
              <img src={HOME_LOGO} className="side-nav__icon" />

              <span>MENU</span>
            </a>
          </li>
          <li className="side-nav__item">
            <a href="#" className="side-nav__link">
              <img src={LOGIN_LOGO} className="side-nav__icon" />

              <span>LOG-IN</span>
            </a>
          </li>
          <li className="side-nav__item">
            <a href="#" className="side-nav__link">
              <img src={OPTIONS_LOGO} className="side-nav__icon" />

              <span>OPTIONS</span>
            </a>
          </li>
          <li className="side-nav__item">
            <a href="#" className="side-nav__link">
              <img src={AUTOMOUSE_LOGO} className="side-nav__icon" />

              <span>AUTO-MOUSE</span>
            </a>
          </li>
          <li className="side-nav__item">
            <a href="#" className="side-nav__link">
              <img src={SLEEP_LOGO} className="side-nav__icon" />

              <span>SLEEP MODE</span>
            </a>
          </li>
          <img src={SIDE_LOGO_BTN} className="side-nav__logo_btn" />
        </ul>

        <div className="legal">
          &copy; 21TIGERS product, designed by Robbie Trevor, All rights
          reserved 2023.
        </div>
      </_contextType>
    </>
  );
}
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
const _contextType = "nav";
type _props = _defaultProps & _altProps;

type _defaultProps = {
  _componentProps?: React.ComponentPropsWithoutRef<"nav"> & {
    ///add alternative propierties than the native elements
  };
  children?: React.ReactNode;
  _className?: string;
  _style?: React.CSSProperties;
  _onClick?: () => void;
};

type _altProps = {
  _params?: {
    _param_1: number;
    _param_2: number;
    _param_3: number;
  };
  _onClickParam?: (test: string) => void;
  _paramsRec?: Record<string, number>; ///in case on need to insert parametters mixed
  _setCount?: React.Dispatch<React.SetStateAction<number>>;
};

/////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
/////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////

//@ts-ignore
import "./User_side_menu.scss";
import {
  HOME_LOGO,
  LOGIN_LOGO,
  LOGOUT_LOGO,
  OPTIONS_LOGO,
  AUTOMOUSE_LOGO,
  SLEEP_LOGO,
  SIDE_LOGO,
  SIDE_LOGO_BTN,
  Touchless_Interactive_Manager_Logo_Base_A,
  Touchless_Interactive_Manager_Logo_Icon_w_Letters_SM_ICon, //@ts-ignore
} from "../../../../utility/assetsImport";
import User_interactive_content from "../elements/User_interaction_content";
