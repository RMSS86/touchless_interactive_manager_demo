import React, { useEffect, useRef, useState } from "react";
import { motion } from "framer-motion";

const _contextType = "aside";

/////COMPONENET/////COMPONENET/////COMPONENET/////COMPONENET/////
export default function Sidebar({
  _componentProps,
  children,
  _className='sidebar show',
  _id='sidebar',
  _style,
  _onClick,
  ...rest
}: _props) {
  ///////FUNCTIONS//////////FUNCTIONS///////////FUNCTIONS///////////

  ////////RETURN/////RETURN/////RETURN/////RETURN/////RETURN/////
  return (
    <_contextType
      {...rest}
      className={_className}
      onClick={_onClick}
      style={_style}
      id={_id}
    >
      <div className="sidebar__user">
       <div className="sidebar__user-wrap" 
            style={{
            background: `url(${BG_img_one}) no-repeat`,
            backgroundSize: "cover", 
            backgroundPosition: "center",
          }}>
            
         <img alt="user" className="sidebar__user-photo" src={User} />
         <div className="sidebar__user-tagbg">
            <p className="sidebar__user-tag">Robbie</p>
         </div>
        
       </div>
      </div>

      <ul className="sidebar__options">
            {HEADER_DATA.map((e) => (
        <Links
          _feat={e.menu}
          _href={e.direct}
          _liClassName="sidebar__options-item"
          _navLink="sidebar__options-link"
          _onClick={e.action}
          key={e.id}
        />
      ))}
      </ul>

         <div className="sidebar-footer">
            <img className="sidebar-foot" alt="personal" src={MotherTechLogo} />
            <p className="sidebar-credit" >Robbie Solis-Stevenson</p>
          </div>

      <div className="sidebar__foot">
        <img alt="logo" className="sidebar__foot-logo" src={GeneralLogo} />
          <div className="sidebar__foot-log">
              <a className="sidebar__foot-logout">Log Out</a>
          </div>
         
      </div>
      {children}
    </_contextType>
  );
}

/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE/////TYPE///////
type _props = _defaultProps & _altProps;

type _defaultProps = {
  _componentProps?: React.ComponentPropsWithoutRef<"aside"> & {
    ///add alternative propierties than the native elements
  };
  children?: React.ReactNode;
  _contextType?: string;
  _className?: string;
  _style?: React.CSSProperties;
  _id?: string;
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

// @ts-ignore
import "./Sidebar.scss"; // @ts-ignore
import {GeneralLogo, User} from "../../../../utility/assetsImport.js";
import { HEADER_DATA } from "../../../../utility/data/UI-Data/UIData.js";
import Links from "../links/Links.js";
import {BG_img_one, // @ts-ignore
    Actor_male_image_one,MotherTechLogo} from '../../../../utility/assetsImport.js';

