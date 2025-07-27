/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
export default function Landing_section_opener({
  _componentProps,
  children,
  _className = "landing_opener",
  _style,
  _onClick,
  ...rest
}: _props) {
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////

  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  return (
    <>
      <_contextType
        {...rest}
        className={_className}
        onClick={_onClick}
        style={{}}
      >
        {/* {children} */}

        <div className="landing_opener__wrapper">
          <div className="landing_opener__wrapper-left">
            <img
              alt="brand-logo"
              className="landing_opener__wrapper-left_logo"
              src={Touchless_Interactive_Manager_Logo_Base_A}
            />
          </div>
          <div className="landing_opener__wrapper-right">
            <h1 className="landing_opener__wrapper-right_title">
              {HOMEPAGE_DATA[0].text}
            </h1>
            <p className="landing_opener__wrapper-right_about">
              {HOMEPAGE_DATA[1].text}
            </p>
            {/* <p>
              <a href="https://skillicons.dev">
                <img src="https://skillicons.dev/icons?i=py,js,ts,dart,flutter,react,nextjs,mongodb" />
                <img src="https://skillicons.dev/icons?i=firebase,sass,docker,express,flask,tensorflow,opencv" />
              </a>
            </p> */}

            <div className="landing_opener__wrapper-right_foot">
              <img
                alt="brand-logo-two"
                src={Touchless_Interactive_Manager_Logo_Icon_w_Letters_SM_ICon}
                className="landing_opener__wrapper-right_foot-logo"
              />
              <DesignerSign />
            </div>
          </div>
        </div>
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
import "./Landing_section_opener.scss";
import {
  Touchless_Interactive_Manager_Logo_Base_A,
  Touchless_Interactive_Manager_Logo_Icon_w_Letters_SM_ICon, //@ts-ignore
} from "../../../../utility/assetsImport";
import { HOMEPAGE_DATA } from "../../../../utility/data/UI-Data/UIData";
import DesignerSign from "../../../UI/components/particles/DesignerSign";
