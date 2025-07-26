import { MouseEvent } from "react";

export default function handleHover({
  _e,
  _classList,
  _siblingClosest,
  _siblingSelector,
  _imgTargetClass,
  _link,
}: _defaultParams) {
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  // if (_e.target.addEventListener target.classList.contains(_classList)) {
  //   const _link = _e.target;
  //   const _siblings = link
  //     .closest(_siblingClosest)
  //     .querySelectorAll(_siblingSelector);
  //   const _logo = link.closest(_siblingClosest).querySelector(_imgTargetClass);
  //   _siblings.forEach((_element: { style: { opacity: any } }) => {
  //     if (_element !== _link) _element.style.opacity = this;
  //   });
  //   _logo.style.opacity = this;
  // }
}

/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
type _defaultParams = {
  _e: React.MouseEvent<HTMLElement>;
  _classList: string;
  _siblingClosest: string;
  _siblingSelector: string;
  _link: string;
  _imgTargetClass: string;
};
//////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
/////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
