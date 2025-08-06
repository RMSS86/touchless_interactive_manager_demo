/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
import { useState, useEffect } from "react";

export default function User_interactive_content({
  _componentProps,
  children,
  _className = "display",
  _style,
  _onClick,
  ...rest
}: _props) {
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  const logoNamebase = "_CMD_TAG_";

  // MAKE A CLASSS
  const BROADCAST_ADDRESS = "http://192.168.0.105:5000/video_feed"; //http://192.168.0.105:5000 ori_> "http://localhost:5000/video_feed"
  const BROADCAST_ADDRESS_LOCAL = "http://localhost:5000/video_feed";

  // TODO: MAKE A CLASSS
  async function checkBroadcaststatus() {
    const _bradcast_response = await fetch(BROADCAST_ADDRESS, {
      method: "GET",
    });
    console.log(
      `API endpoint ${BROADCAST_ADDRESS} is active (Status: ${_bradcast_response.status})`
    );
  }

  useEffect(() => {
    try {
      checkBroadcaststatus();
    } catch (_) {
      console.log(_);
    }
  }, []);

  const [logoIndex, setLogoIndex] = useState(TIM_OFFLINE_);
  //> TODO: MAKE STATES FOR MODE, CMD_TYPE, HANDNESS, VALUE

  // TODO: MAKE A CLASSS
  // import _socket from "../../remoteIO/remoteIU_cmd";

  useEffect(() => {
    _socket.on("userCMD_", (INCOMING_CMD) => {
      //console.log(typeof message);
      // var PARSED_CMD = JSON.parse(CMD_);
      console.log("CMD_TYPE_CMD FROM [ES]", INCOMING_CMD["CMD_TYPE"]);
      console.log("MODE_CMD FROM [ES]", INCOMING_CMD["MODE"]);
      console.log("HANDNESS_CMD FROM [ES]", INCOMING_CMD["HANDNESS"]);
      console.log("VALUE_CMD FROM [ES]", INCOMING_CMD["VALUE"]);
      cmdSelector(INCOMING_CMD["VALUE"]);

      // console.log(CMD_);
    });
  }, [_socket]);

  const cmdSelector = (_cmd: any) => {
    if (_cmd === "0") {
      setLogoIndex(_CMD_TAG_ZERO_);
    } else if (_cmd === "1") {
      setLogoIndex(_CMD_TAG_ONE_);
    } else if (_cmd === "2") {
      setLogoIndex(_CMD_TAG_TWO_);
    } else if (_cmd === "3") {
      setLogoIndex(_CMD_TAG_THREE_);
    } else if (_cmd === "4") {
      setLogoIndex(_CMD_TAG_FOUR_);
    } else if (_cmd === "5") {
      setLogoIndex(_CMD_TAG_FIVE_);
    }
  };
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
            className="gallery__photo "
          />
        </figure>
        <Hint_Side_Menu />
        <CMD_Sub_Menu />
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
  TIM_OFFLINE_,
  _CMD_MOUSE_MODE_,
  _CMD_TAG_ZERO_,
  _CMD_TAG_ONE_,
  _CMD_TAG_TWO_,
  _CMD_TAG_THREE_,
  _CMD_TAG_FOUR_,
  _CMD_TAG_FIVE_,
  Touchless_Interactive_Manager_BG_edit_A,
  Touchless_Interactive_Manager_Logo_Base_A,
  Touchless_Interactive_Manager_Logo_Base_TRNSP_C,
  Touchless_Interactive_Manager_Logo_Icon_w_Letters_SM_ICon, //@ts-ignore
} from "../../../../utility/assetsImport";
import CMD_Sub_Menu from "./CMD_Sub_Menu";
import Hint_Side_Menu from "./Hint_Side_Menu";
import _socket from "../../../../remoteIO/remoteIU_cmd";
