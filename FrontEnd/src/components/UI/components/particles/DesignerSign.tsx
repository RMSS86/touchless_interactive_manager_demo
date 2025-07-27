/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
export default function DesignerSign({
  _componentProps,
  children,
  _className,
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
        <div className="designer-footer">
          <img
            className="designer-foot"
            alt="personal"
            src={Touchless_Interactive_Manager_Logo_Block_NL_White}
          />
          <p className="designer-credit">Robbie Solis-Stevenson</p>
        </div>
      </_contextType>
    </>
  );
}
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
const _contextType = "div";
type _props = _defaultProps & _altProps;

type _defaultProps = {
  _componentProps?: React.ComponentPropsWithoutRef<"div"> & {
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

import { Link, useLoaderData, useNavigate } from "react-router-dom";
import { useQuery } from "@tanstack/react-query"; //@ts-ignore
import { Touchless_Interactive_Manager_Logo_Block_NL_White } from "../../../../utility/assetsImport"; //@ts-ignore
import "./DesignerSign.scss";
