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
