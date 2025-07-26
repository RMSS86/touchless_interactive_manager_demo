// import React, { useEffect, useRef, useState } from "react";

const ContextType = "div";
const ContextId = "fragmentpictureheader";
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
export default function HeaderFragment({
  children, 
  _className='fragment',
  _src,
  _id = ContextId,
  _style,
  _onClick, 
  _onCompClick,
  ...rest
}: _defaultProps) { 
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////

  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  return (
    <ContextType 
      {...rest}
      id={_id}
      className={_className}
      onClick={_onClick}
      style={{}}
    >
      {/* {children} */}
      {SUB_HEADER_ITEMS.map((e)=>(
        <div className='fragment__wrapper'>
        <img className='fragment__icon' src={e.icon}></img>
      </div>
      ))}

    </ContextType>
  );
}

/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
type _defaultProps = {
  children?: React.ReactNode;
  _id?: string;
  _className?: string;
  _src?: string;
  _style?: React.CSSProperties;
  _onClick?: () => void;
  _onCompClick?: () => void;
};

//////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////
//////////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS//////IMPORTS/////////

//@ts-ignore
import './HeaderFragment.scss'; //@ts-ignore
import {BG_img_one} from '../../../../utility/assetsImport.js';
import { SUB_HEADER_ITEMS } from '../../../../utility/data/UI-Data/UIData.js';
