// import React, { useEffect, useRef, useState } from "react";

const ContextType = "ul";
const ContextId = "";
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
export default function TopNavLinks({
  children,
  _className = "nav__links",
  _id = ContextId,
  _style,
  _onClick,
  _onCompClick,
  _userContext,
  _invokeModal,
  ...rest
}: _defaultProps) {
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  console.log(HEADER_DATA);

  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  return (
    <ContextType
      {...rest}
      id={_id}
      className={_className}
      onClick={_onClick}
      style={_style}
    >
      {/* ///MAKE COMPONENET/// */}

      {HEADER_DATA.map((e) => (
        <Links
          _feat={e.menu}
          _href={e.direct}
          _liClassName="nav__item"
          _navLink="nav__link"
          _onClick={e.action}
          key={e.id}
        />
      ))}
      {_userContext!._active ? (
        <LogOutNav
          _liClass="nav__item"
          _aClass="nav__link"
          _aTag="LogOut"
          _onClick={_invokeModal}
          // _onClick={_logOut}
        />
      ) : (
        <Links
          key={99}
          _feat="Logout" //> Login
          _href="login"
          _liClassName="nav__item"
          _navLink="nav__link"
          _onClick={() => {}}
        />
      )}
    </ContextType>
  );
}

/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
type _defaultProps = {
  children?: React.ReactNode;
  _id?: string;
  _className?: string;
  _style?: React.CSSProperties;
  _userContext: User | null;
  _invokeModal?: () => void;
  _onClick?: () => void;
  _onCompClick?: () => void;
};

//////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
//////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
import { User } from "../../../../models/types/userType";
import { HEADER_DATA } from "../../../../utility/data/UI-Data/UIData";
import Links from "../../components/links/Links";
import LogOutNav from "./LogOutNav";
//@ts-ignore
import "./TopNavLinks.scss";
