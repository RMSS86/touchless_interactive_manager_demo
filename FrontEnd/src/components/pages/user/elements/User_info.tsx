/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
import { useState, useEffect } from "react";

export default function User_info({
  _componentProps,
  children,
  _className = "user_info",
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
        <div
          className="user_info-avatar"
          style={{
            background: `url(${User}) no-repeat`,
            backgroundSize: "cover",
            backgroundPosition: "center",
          }}
        >
          <h1 className="user_info-title_top ">{DUMMY_USER_INFO[0]._name}</h1>
          <img
            alt="logo"
            src={Touchless_Interactive_Manager_Logo_Base_A}
            className="user_info-logo"
          />
          <div className="user_info-resume">
            {/* // SCHEDULE MODULE // */}
            <User_scheduleTile _className="user_info-schedule" />

            {/* // EMPLOYEE INFO MODULE // */}
            <User_infoTile
              _className="user_info-info"
              _user_data={DUMMY_USER_INFO[0]}
            />
          </div>
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
import "./User_info.scss";
import {
  User,
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
import User_infoTile from "./User_infoTile";
import { DUMMY_USER_INFO } from "../../../../utility/data/UI-Data/DUMMY_USER_DATA";
import User_scheduleTile from "./User_scheduleTile";
