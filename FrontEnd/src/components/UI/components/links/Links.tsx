// import React, { useEffect, useRef, useState } from "react";

const ContextType = "li";

/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
export default function Links({
  children,
  _liClassName,
  _style,
  _onClick,
  _href = "",
  _feat,
  _key,
  _navLink,
  _hoverBind,
  ...rest
}: _defaultProps) {
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////

  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  return (
    <ContextType
      {...rest}
      className={_liClassName}
      onClick={_onClick}
      style={_style}
      key={_key}
    >
      <NavLink className={_navLink} to={_href}>
        {_feat}
      </NavLink>
    </ContextType>
  );
}
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
type _defaultProps = {
  children?: React.ReactNode;
  _contextType?: string;
  _liClassName?: string;
  _style?: React.CSSProperties;
  _onClick?: () => void;
  _href?: string;
  _feat: string;
  _navLink?: string;
  _key?: number;
  _hoverBind?: () => void;
};

//////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
/////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
//@ts-ignore
import { NavLink, Link } from "react-router-dom";
