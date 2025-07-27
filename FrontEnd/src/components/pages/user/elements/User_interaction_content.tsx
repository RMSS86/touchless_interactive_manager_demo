/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
import { useState, useEffect } from "react";

export default function User_interactive_content({
  _componentProps,
  children,
  _className = "user_interactive",
  _style,
  _onClick,
  ...rest
}: _props) {
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  const logoNamebase = "_CMD_TAG_";
  const BROADCAST_ADDRESS = "http://localhost:5000/video_feed";

  const [logoIndex, setLogoIndex] = useState(_CMD_TAG_FIVE_);

  // import _socket from "../../remoteIO/remoteIU_cmd";

  //   useEffect(() => {
  //     _socket.on("userCMD_", (CMD_) => {
  //       //console.log(typeof message);
  //       //var _CMD = JSON.parse(CMD_);
  //       cmdSelector(CMD_);
  //       console.log(CMD_);
  //     });
  //   }, [_socket]);

  //   const cmdSelector = (_cmd) => {
  //     if (_cmd === "ZERO_") {
  //       setLogoIndex(_CMD_TAG_ZERO_);
  //     } else if (_cmd === "ONE_") {
  //       setLogoIndex(_CMD_TAG_ONE_);
  //     } else if (_cmd === "TWO_") {
  //       setLogoIndex(_CMD_TAG_TWO_);
  //     } else if (_cmd === "THREE_") {
  //       setLogoIndex(_CMD_TAG_THREE_);
  //     } else if (_cmd === "FOUR_") {
  //       setLogoIndex(_CMD_TAG_FOUR_);
  //     } else if (_cmd === "FIVE_") {
  //       setLogoIndex(_CMD_TAG_FIVE_);
  //     }
  //   };
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

        <div className="display">
          <figure className="display__item">
            <img
              src={Touchless_Interactive_Manager_Logo_Base_TRNSP_C}
              className="brand_logo"
              alt="brandlogo"
            />
            <img
              src={_CMD_MOUSE_MODE_}
              className="command__mode"
              alt="brandlogo"
            />
            <img
              //src={_CMD_TAG_ZERO_}
              src={logoIndex}
              className="command__tag"
              alt="brandlogo"
            />
            <img
              src={BROADCAST_ADDRESS}
              alt="Web--Cam"
              className="gallery__photo"
            />
          </figure>
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
import "./User_interaction_content.scss";
import {
  _CMD_MOUSE_MODE_,
  _CMD_TAG_ZERO_,
  _CMD_TAG_ONE_,
  _CMD_TAG_TWO_,
  _CMD_TAG_THREE_,
  _CMD_TAG_FOUR_,
  _CMD_TAG_FIVE_,
  Touchless_Interactive_Manager_Logo_Base_A,
  Touchless_Interactive_Manager_Logo_Base_TRNSP_C,
  Touchless_Interactive_Manager_Logo_Icon_w_Letters_SM_ICon, //@ts-ignore
} from "../../../../utility/assetsImport";
