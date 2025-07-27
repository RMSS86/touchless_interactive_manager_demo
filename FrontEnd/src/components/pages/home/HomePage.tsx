/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
export default function HomePage({
  _componentProps,
  children,
  _className = "homepage",
  _style,
  _onClick,
  ...rest
}: _props) {
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  const _navigator = useNavigate();

  const NavigationHandler = (nav: string) => {
    _navigator(nav);
  };
  //
  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  return (
    <>
      <_contextType
        {...rest}
        className={_className}
        onClick={_onClick}
        style={_style}
      >
        <Landing_section_opener />

        {/* 
      <Landing_section_opener />
      <Landing_section_brand /> 
      <Landing_section_product />
      {/* <LandingSectionsPlans /> 
      <Landing_section_action /> */}
      </_contextType>
    </>
  );
}
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
const _contextType = "section";
type _props = _defaultProps & _altProps;

type _defaultProps = {
  _componentProps?: React.ComponentPropsWithoutRef<"section"> & {
    ///add alternative propierties than the native elements
  };
  children?: React.ReactNode;
  _className?: string;
  _style?: React.CSSProperties;
  _onClick?: () => void;
};

type _altProps = {
  _params?: {
    _param_1: number;
    _param_2: number;
    _param_3: number;
  };
  _onClickParam?: (test: string) => void;
  _paramsRec?: Record<string, number>; ///in case on need to insert parametters mixed
  _setCount?: React.Dispatch<React.SetStateAction<number>>;
};

/////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
/////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////

//@ts-ignore
import { Link, useLoaderData, useNavigate } from "react-router-dom";

// @ts-ignore
import "./HomePage.scss";
import {
  showAlert,
  // @ts-ignore
} from "../../../utility/imports.js";

// import Landing_section_brand from "./sections/Landing_Section_Brand.js";
// import Landing_section_product from "./sections/Landing_section_product.js";
// import Landing_section_action from "./sections/Landing_section_action.js";
import Landing_section_opener from "./sections/Landing_section_opener";
// import LandingSectionsPlans from "./sections/Landing_section_plans.js";
