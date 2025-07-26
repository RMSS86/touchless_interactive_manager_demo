// import React, { useEffect, useRef, useState } from "react";

const ContextType = "ul";
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
export default function FooterLinks({
  children,
  _className,

  _footerLinksSrc,
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
      className="footer__nav"
      onClick={_onClick}
      style={_style}
    >
      {FOOTER_DATA.map((e) => _Links(e))}
    </ContextType>
  );
}
/////I/////////////////////////////////////////////////INNER ELEMENTS
/////I///////////////////////////////////////////////////////////////
const _Links = (feat: footerTag) => {
  return (
    <li className="footer__item" key={feat.tag}>
      <a className="footer__link" href={feat.link}>
        {feat.tag}
      </a>
    </li>
  );
};
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
type _defaultProps = {
  children?: React.ReactNode;

  _footerLinksSrc?: string[];
  _className?: string;
  _style?: React.CSSProperties;
  _onClick?: () => void;
};
type footerTag = {
  tag: string;
  link: string;
  _function?: () => {};
};

//////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
/////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////////

//@ts-ignore
import "../Footer.scss";
import { FOOTER_DATA } from "../../../../utility/data/UI-Data/UIData";
