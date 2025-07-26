// import React, { useEffect, useRef, useState } from "react";

/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
export default function RootLayout({
  children,
  _className,
  _style,
  _onClick, //@ts-ignore
  ...rest
}: _defaultProps) {
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////

  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  return (
    <>
      <Header />
      {/* <Sidebar /> */}
      <main className="outlet">
        <Outlet />
      </main>
      <Footer />
    </>
  );
}

/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
type _defaultProps = {
  children?: React.ReactNode;

  _className?: string;
  _style?: React.CSSProperties;
  _onClick?: () => void;
};

//////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
/////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
import { Outlet } from "react-router"; //@ts-ignore
// import { Header, Footer } from "../../utility/imports.js";
// import Header from "../UI/header/Header";
// import Footer from "../UI/footer/Footer";
// import Sidebar from "../UI/elements/side/Sidebar";
//@ts-ignore
import "./LayOut.scss";
import Footer from "../footer/Footer";
import Header from "../header/Header";
