/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
export default function Hint_Side_Menu({
  _componentProps,
  children,
  _className = "hint_side",
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
        <div className="hint_side-title">
          <h1>Hand</h1>
        </div>
        {/* ONE TILE FOR HAND TO BE USED OTHER TILE FOR HINT */}
        {/* USE THE GENERAL TILES WHEN RECEIVED AND CLOSED OPEN POINTER */}
        <div className="hint_side-wrapper">
          <Hint_Side_Tile _src={_SIDE_LH_} _tag="Left" _id="left" />
          <Hint_Side_Tile _src={_SIDE_RH_} _tag="Right" _id="right" />
        </div>
      </_contextType>
    </>
  );
}
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
const _contextType = "section";
type _props = _defaultProps & _altProps;

type _defaultProps = {
  _componentProps?: React.ComponentPropsWithoutRef<"section"> & {
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
import "./Hint_Side_Menu.scss";
import {
  _SIDE_LH_,
  _SIDE_RH_,
  _CMD_TAG_CLICK_,
  _CMD_TAG_ONE_,
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
import User_interactive_content from "./User_interaction_content";
import Hint_Side_Tile from "../../../UI/components/menu/tiles/Hint_Side_tile";
