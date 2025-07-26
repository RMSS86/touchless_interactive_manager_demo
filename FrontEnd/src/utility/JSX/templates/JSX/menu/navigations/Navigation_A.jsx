import { useState } from "react";
import "./Navigation_A.scss";

import NavHolder from "./navElements/NavigationHolder";
import NavElement from "./navElements/NavElement";
import NavList from "./navElements/NavigationList";

const NAVS = [
  {
    navIndex: "01",
    nav: "About Trax",
    href: "#",
  },
  {
    navIndex: "02",
    nav: "Your Benefits",
    href: "#",
  },
  {
    navIndex: "03",
    nav: "Popular Tours",
    href: "#",
  },
  {
    navIndex: "04",
    nav: "Stories",
    href: "#",
  },
  {
    navIndex: "05",
    nav: "Book Now",
    href: "#",
  },
];
export default function Navigation_A({ _id, ...props }) {
  const [name, setName] = useState();

  return (
    <>
      <NavHolder
        className="navigation"
        _inputType="checkbox"
        _inputId="navi-toggle"
        _inputClass="navigation__checkbox"
        _btnFor="navi-toggle"
        _btnClass="navigation__button"
        _iconClass="navigation__icon"
        _bgClass="navigation__background"
      >
        <NavList
          className="navigation__nav"
          _ulClass="navigation__list"
          _key="nav"
        >
          {NAVS.map((nav) => (
            <NavElement
              _className="navigation__item"
              _aClass="navigation__link"
              _navIndex={nav.navIndex}
              _navTitle={nav.nav}
              _href={nav.href}
              _key={nav.nav}
              onClick={() => console.log(nav.nav)}
            />
          ))}
        </NavList>
      </NavHolder>
    </>
  );
}
