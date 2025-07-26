//import { Fragment, useState } from "react";
import "./Footer.scss";
import logoWhite from "../../assets/21_Bites_Food_Logo_bear_B_white.png";

const footerTags = [
  { tag: "About", link: "https://linkedin.com" },
  { tag: "Orders", link: "#" },
  { tag: "Stores", link: "#" },
  { tag: "Events", link: "#" },
  { tag: "Careers", link: "#" },
  { tag: "Blog", link: "#" },
  { tag: "Contact us", link: "#" },
];

const Links_ = (feat) => {
  return (
    <li class="footer__item">
      <a class="footer__link" href={feat.link}>
        {feat.tag}
      </a>
    </li>
  );
};

const Footer = (props) => {
  return (
    <footer class="footer">
      <ul class="footer__nav">{footerTags.map((e) => Links_(e))}</ul>
      <img src={logoWhite} alt="Logo" class="footer__logo" />
      <p class="footer__copyright">
        &copy; Copyright by
        <a
          class="footer__link twitter-link"
          target="_blank"
          href="https://linkedin.com"
        >
          Robbie Trevor
        </a>
        .
      </p>
    </footer>
  );
};

export default Footer;
