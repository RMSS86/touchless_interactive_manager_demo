// import React, { useEffect, useRef, useState } from "react";

const ButtonContainer = "a";

/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
export default function CMD_Menu_Button({
  _children,
  _className = "CMD_btn",
  _isSelected = false,
  _btnText,
  _style,
  _href = "",
  _onClick,
  ...rest
}: _defaultProps) {
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  //   const [isSelected, setIsSelected] = useState(_isSelected);
  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  return (
    <ButtonContainer
      {...rest}
      className={_className}
      onClick={_onClick}
      style={_style}
    >
      {_btnText}
    </ButtonContainer>
  );
}

/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
type _defaultProps = {
  _children?: React.ReactNode;
  _className?: string;
  _btnText?: string;
  _href?: string;
  _isSelected?: boolean;
  _style?: React.CSSProperties;
  _onClick?: () => void;
};

//////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
/////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
//@ts-ignore
import "./CMD_Menu_Button.scss"; //@ts-ignore
import { Link } from "react-router-dom";
