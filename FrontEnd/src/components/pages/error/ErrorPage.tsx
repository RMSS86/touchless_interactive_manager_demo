// import React, { useEffect, useRef, useState } from "react";

const ContextType = "div";

/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
export default function ErrorPage({
  children,
  _className = "error__layout",
  _errorMsg,
  _style,
  _onClick,
  ...rest
}: _defaultProps) {
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  const _error = useRouteError();
  console.log("error from the ErrorPage ", _error);

  let _errStatus = "Ooops...";
  let _errMsg = "Something went wrong!";
  let _errStsText = "Please try again later.";

  // if (_error.internal) {
  //   _errStatus = _error.status;
  //   _errMsg = _error.data;
  //   _errStsText = _error.statusText;
  // }

  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  return (
    <ContextType
      {...rest}
      className={_className}
      onClick={_onClick}
      style={_style}
    >
      <Header />
      {/* <Sidebar /> */}
      <ErrorPageContents
        _className="outlet"
        _errStatus={_errStatus}
        _errMessage={_errMsg}
        _errStsText={_errStsText}
        // _errLogoMain={ErrorIcon}
      />
      <Footer />
    </ContextType>
  );
}

/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
type _defaultProps = {
  children?: React.ReactNode;
  _errorMsg?: string;
  _className?: string;
  _style?: React.CSSProperties;
  _onClick?: () => void;
};

//////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
/////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
//@ts-ignore
import { useRouteError } from "react-router-dom";
//@ts-ignore
import "./ErrorPage.scss";
import ErrorPageContents from "./elements/ErrorPageContents";
import Footer from "../../UI/footer/Footer";
import Header from "../../UI/header/Header";
import Sidebar from "../../UI/components/side/Sidebar";
