// import React, { useEffect, useRef, useState } from "react";

const ContextType = "div";

/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
export default function ErrorPageContents({
  children,
  _className,
  _errStatus,
  _errMessage,
  _errStsText,
  _errLogoMain,
  _style,
  _onClick,
  ...rest
}: _defaultProps) {
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////

  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  return (
    <ContextType
      {...rest}
      className={_className}
      onClick={_onClick}
      style={{
        // background: `url(${BGImg}) no-repeat`,
        backgroundSize: "cover",
        backgroundPosition: "top",
        height: "89vh",
      }}
    >
      <div className="error">
        <div className="error__left">
          {/* <img src={ErrorIcon} alt="error-logo" /> */}
        </div>
        <div className="error__right">
          <h1>{_errStatus}</h1>
          <h2>An Error Occurred!</h2>
          <h3>{_errMessage}</h3>
          <h4>{_errStsText}</h4>
          {/* <img src={LogoLetters_only_white} alt="logo" /> */}
        </div>
      </div>
    </ContextType>
  );
}

/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
type _defaultProps = {
  children?: React.ReactNode;
  _className?: string;
  _errStatus?: string;
  _errMessage?: string;
  _errStsText?: string;
  _errLogoMain?: string;
  _style?: React.CSSProperties;
  _onClick?: () => void;
};

//////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
/////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
//@ts-ignore
import "../ErrorPage.scss"; //@ts-ignore
